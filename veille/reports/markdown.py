"""Rendu Markdown du rapport (les textes issus des sources sont échappés)."""
from __future__ import annotations

import re

from veille.normalize import safe_http_url

_MD_SPECIAL = re.compile(r"([\\`*_\[\]<>#|])")


def esc(text) -> str:
    """Échappe le Markdown/HTML d'un texte non fiable (titres et résumés collectés)."""
    return _MD_SPECIAL.sub(r"\\\1", str(text or "")).replace("\n", " ")


def _link(url: str) -> str:
    u = safe_http_url(url or "")
    return f"<{u.replace('>', '%3E').replace(' ', '%20')}>" if u else ""


def render_markdown(doc) -> str:
    out: list[str] = []
    for b in doc.blocks:
        t = b["t"]
        if t == "cover":
            out.append(f"# {esc(b['title'])}\n\n**{esc(b['subtitle'])}**\n\n## {esc(b['org'])}\n")
            out += [f"- {esc(l)}" for l in b["lines"]]
            if b["demo"]:
                out.append("\n> **ORGANISATION FICTIVE (cas d'étude)** — les éléments de veille sont réellement collectés.")
            out.append("\n---\n")
        elif t == "h1":
            out.append(f"\n## {esc(b['text'])}\n")
        elif t == "h2":
            out.append(f"\n### {esc(b['text'])}\n")
        elif t == "h3":
            out.append(f"\n#### {esc(b['text'])}\n")
        elif t == "p":
            out.append((f"**{esc(b['label'])}** " if b.get("label") else "") + esc(b["text"]) + "\n")
        elif t == "note":
            out.append(f"> {esc(b['text'])}\n")
        elif t == "ul":
            out += [f"- " + (f"**{esc(lab)}** : " if lab else "") + esc(txt) for lab, txt in b["items"]]
            out.append("")
        elif t == "table":
            out.append("| " + " | ".join(esc(h) for h in b["head"]) + " |")
            out.append("|" + "|".join("---" for _ in b["head"]) + "|")
            for row in b["rows"]:
                cells = [(" ".join(_link(u) for u in c.split()) if c.startswith(("http://", "https://")) else esc(c))
                         for c in map(str, row)]
                out.append("| " + " | ".join(cells) + " |")
            out.append("")
        elif t == "card":
            out.append(f"\n#### {esc(b['title'])}\n")
            if b.get("url"):
                out.append(f"- **URL** : {_link(b['url'])}")
            out += [f"- **{esc(lab)}** : {esc(txt)}" for lab, txt in b["lines"] if txt]
            out.append("")
        elif t == "pb":
            out.append("\n---\n")
    return "\n".join(out).strip() + "\n"
