"""Connecteur RSS / Atom (feedparser), tolérant aux flux mal formés."""
from __future__ import annotations

import re

import feedparser

from veille.collectors import CollectorError
from veille.normalize import clean_title, html_to_text, iso, parse_date, safe_http_url

_EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")


def _author(entry) -> str | None:
    """Nom d'auteur publié (signature) uniquement : les adresses e-mail sont supprimées (minimisation)."""
    name = entry.get("author") or ""
    if not name and entry.get("authors"):
        name = entry["authors"][0].get("name", "")
    name = _EMAIL.sub("", html_to_text(name, 200)).strip(" ()<>,;")
    return name or None


def parse_feed(content: bytes, langue: str | None = None, max_items: int = 60) -> tuple[list[dict], list[str]]:
    warnings: list[str] = []
    parsed = feedparser.parse(content)
    if parsed.bozo and not parsed.entries:
        exc = parsed.get("bozo_exception")
        raise CollectorError(f"Flux illisible ou mal formé : {type(exc).__name__ if exc else 'format inconnu'}")
    if parsed.bozo:
        warnings.append("Flux partiellement mal formé : éléments lisibles conservés.")
    if not parsed.get("version") and not parsed.entries:
        raise CollectorError("La réponse n'est pas un flux RSS/Atom (page HTML ou contenu vide).")

    items = []
    for e in parsed.entries:
        url = safe_http_url(e.get("link") or "") or safe_http_url(e.get("id") or "")
        title = clean_title(e.get("title") or "")
        if not url or not title:
            continue
        raw_summary = e.get("summary") or ""
        if not raw_summary and e.get("content"):
            raw_summary = e["content"][0].get("value", "")
        published = parse_date(e.get("published_parsed") or e.get("updated_parsed"))
        items.append({
            "url": url,
            "titre": title,
            "auteur": _author(e),
            "resume_source": html_to_text(raw_summary, 3000),
            "publie_le": iso(published),
            "langue": langue,
            "origine": None,
            "donnees": {"tags": [t.get("term") for t in e.get("tags", []) if t.get("term")][:15]} if e.get("tags") else None,
        })
    # Les entrées les plus récentes d'abord ; borne le volume des flux très longs (ex. MSRC).
    items.sort(key=lambda i: i["publie_le"] or "", reverse=True)
    return items[:max_items], warnings
