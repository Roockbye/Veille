"""Rendu PDF du rapport avec ReportLab (textes non fiables échappés avant mise en forme)."""
from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle)

from veille.normalize import safe_http_url

FONT_DIRS = [Path("/usr/share/fonts/truetype/dejavu"), Path("/usr/share/fonts/dejavu"), Path("/Library/Fonts"),
             Path("C:/Windows/Fonts")]
NAVY = colors.HexColor("#1F3A5F")
LIGHT = colors.HexColor("#EEF2F7")
PRIO_COLORS = {"Critique": "#B00020", "Élevée": "#E65100", "Modérée": "#B28704", "Faible": "#2E7D32", "À qualifier": "#5E35B1"}

_font_cache: tuple[str, str] | None = None


def _fonts() -> tuple[str, str]:
    """DejaVu (Unicode complet) si disponible, sinon Helvetica avec substitution des caractères non couverts."""
    global _font_cache
    if _font_cache:
        return _font_cache
    for d in FONT_DIRS:
        reg, bold = d / "DejaVuSans.ttf", d / "DejaVuSans-Bold.ttf"
        if reg.exists() and bold.exists():
            try:
                pdfmetrics.registerFont(TTFont("DejaVu", str(reg)))
                pdfmetrics.registerFont(TTFont("DejaVu-Bold", str(bold)))
                _font_cache = ("DejaVu", "DejaVu-Bold")
                return _font_cache
            except Exception:
                continue
    _font_cache = ("Helvetica", "Helvetica-Bold")
    return _font_cache


_FALLBACK = {"≥": ">=", "≤": "<=", "→": "->", "←": "<-", "•": "-", "✓": "v", "’": "'", "≠": "!="}


def _clean(text) -> str:
    s = str(text or "")
    if _fonts()[0] == "Helvetica":
        for k, v in _FALLBACK.items():
            s = s.replace(k, v)
        s = s.encode("cp1252", "replace").decode("cp1252")
    return escape(s).replace("\n", "<br/>")


def _styles():
    reg, bold = _fonts()
    ss = getSampleStyleSheet()
    base = ParagraphStyle("base", parent=ss["Normal"], fontName=reg, fontSize=9, leading=12)
    return {
        "base": base,
        "small": ParagraphStyle("small", parent=base, fontSize=7.5, leading=9.5),
        "h1": ParagraphStyle("h1", parent=base, fontName=bold, fontSize=15, leading=19, textColor=NAVY, spaceBefore=12, spaceAfter=6),
        "h2": ParagraphStyle("h2", parent=base, fontName=bold, fontSize=12, leading=15, textColor=NAVY, spaceBefore=8, spaceAfter=4),
        "h3": ParagraphStyle("h3", parent=base, fontName=bold, fontSize=10, leading=13, spaceBefore=6, spaceAfter=3),
        "note": ParagraphStyle("note", parent=base, backColor=LIGHT, borderPadding=5, leftIndent=4, rightIndent=4,
                               spaceBefore=4, spaceAfter=6, fontSize=8.5),
        "cover_t": ParagraphStyle("ct", parent=base, fontName=bold, fontSize=22, leading=28, textColor=NAVY, alignment=TA_CENTER),
        "cover_s": ParagraphStyle("cs", parent=base, fontSize=13, leading=18, alignment=TA_CENTER),
        "cover_o": ParagraphStyle("co", parent=base, fontName=bold, fontSize=16, leading=22, alignment=TA_CENTER, spaceBefore=20),
        "cover_l": ParagraphStyle("cl", parent=base, fontSize=10, leading=15, alignment=TA_CENTER),
        "demo": ParagraphStyle("demo", parent=base, fontName=bold, fontSize=10, textColor=colors.HexColor("#B00020"),
                               alignment=TA_CENTER, spaceBefore=18),
        "card_t": ParagraphStyle("cardt", parent=base, fontName=bold, fontSize=9.5, leading=12, textColor=NAVY),
        "bold": bold,
    }


def _para(text, style, bold_label=None):
    label = f"<font name='{_fonts()[1]}'>{_clean(bold_label)}</font> " if bold_label else ""
    return Paragraph(label + _clean(text), style)


def _link_para(url, style):
    u = safe_http_url(url or "")
    if not u:
        return Paragraph("", style)
    return Paragraph(f"<link href='{escape(u, {chr(39): '%27'})}' color='blue'>{_clean(u)}</link>", style)


def _links_para(cell: str, style):
    parts = [safe_http_url(u) for u in cell.split()]
    return Paragraph("<br/>".join(f"<link href='{escape(u, {chr(39): '%27'})}' color='blue'>{_clean(u)}</link>" for u in parts if u), style)


def _title_color(title: str) -> str:
    for k, c in PRIO_COLORS.items():
        if title.startswith(f"[{k}]") or f"— {k}" in title:
            return c
    return "#1F3A5F"


def render_pdf(doc, path: Path) -> Path:
    st = _styles()
    width = A4[0] - 3.6 * cm
    story = []
    org_name = ""
    for b in doc.blocks:
        t = b["t"]
        if t == "cover":
            org_name = b["org"]
            story += [Spacer(1, 4.5 * cm), _para(b["title"], st["cover_t"]), Spacer(1, 0.4 * cm),
                      _para(b["subtitle"], st["cover_s"]), _para(b["org"], st["cover_o"]), Spacer(1, 1.2 * cm)]
            story += [_para(l, st["cover_l"]) for l in b["lines"]]
            if b["demo"]:
                story.append(_para("ORGANISATION FICTIVE (cas d'étude) — les éléments de veille "
                                   "présentés ont été réellement collectés.", st["demo"]))
            story.append(PageBreak())
        elif t in ("h1", "h2", "h3"):
            story.append(_para(b["text"], st[t]))
        elif t == "p":
            story.append(_para(b["text"], st["base"], b.get("label")))
            story.append(Spacer(1, 3))
        elif t == "note":
            story.append(_para(b["text"], st["note"]))
        elif t == "ul":
            for lab, txt in b["items"]:
                story.append(Paragraph("• " + (f"<font name='{st['bold']}'>{_clean(lab)} :</font> " if lab else "") + _clean(txt),
                                       ParagraphStyle("li", parent=st["base"], leftIndent=10, firstLineIndent=-8)))
            story.append(Spacer(1, 4))
        elif t == "table":
            n = len(b["head"])
            widths = [w * width for w in b["widths"]] if b.get("widths") else [width / n] * n
            small = st["small"]
            data = [[Paragraph(f"<font name='{st['bold']}' color='white'>{_clean(h)}</font>", small) for h in b["head"]]]
            for row in b["rows"]:
                data.append([_links_para(str(c), small) if str(c).startswith(("http://", "https://")) else _para(c, small) for c in row])
            tbl = Table(data, colWidths=widths, repeatRows=1)
            tbl.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), NAVY), ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#B0BEC5")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
                ("LEFTPADDING", (0, 0), (-1, -1), 3), ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ]))
            story += [tbl, Spacer(1, 6)]
        elif t == "card":
            color = _title_color(b["title"])
            rows = [[Paragraph(f"<font color='{color}'>{_clean(b['title'])}</font>", st["card_t"])]]
            if b.get("url"):
                rows.append([_link_para(b["url"], st["small"])])
            for lab, txt in b["lines"]:
                if txt:
                    rows.append([_para(txt, st["small"], f"{lab} :")])
            tbl = Table(rows, colWidths=[width])
            tbl.setStyle(TableStyle([
                ("BOX", (0, 0), (-1, -1), 0.6, colors.HexColor(color)), ("BACKGROUND", (0, 0), (-1, 0), LIGHT),
                ("LEFTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 1.5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 1.5),
            ]))
            story += [KeepTogether([tbl]) if len(rows) < 14 else tbl, Spacer(1, 6)]
        elif t == "pb":
            story.append(PageBreak())

    reg, _ = _fonts()

    def on_page(canvas, d):
        if d.page == 1:
            return
        canvas.saveState()
        canvas.setFont(reg, 7.5)
        canvas.setFillColor(colors.grey)
        footer = f"Rapport de veille — {org_name}"[:110]
        if reg == "Helvetica":
            footer = footer.encode("cp1252", "replace").decode("cp1252")
        canvas.drawString(1.8 * cm, 1.2 * cm, footer)
        canvas.drawRightString(A4[0] - 1.8 * cm, 1.2 * cm, f"Page {d.page}")
        canvas.restoreState()

    path = Path(path)
    pdf = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.8 * cm, rightMargin=1.8 * cm, topMargin=1.6 * cm,
                            bottomMargin=1.8 * cm, title="Rapport de veille", author="VeilleCyber",
                            subject="Veille technologique, technique, réglementaire et normative")
    pdf.build(story, onFirstPage=on_page, onLaterPages=on_page)
    return path
