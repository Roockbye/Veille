"""Normalisation : URL canoniques, empreintes, nettoyage du HTML, dates."""
from __future__ import annotations

import hashlib
import html
import re
import unicodedata
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

TRACKING_PARAMS = {
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "utm_id", "utm_name",
    "gclid", "fbclid", "mc_cid", "mc_eid", "ref", "ref_src", "_hsenc", "_hsmi", "mkt_tok", "cmpid",
    "ncid",
}


def canonical_url(url: str) -> str:
    """URL canonique : schéma/hôte en minuscules, sans fragment ni paramètres de suivi, sans '/' final."""
    url = (url or "").strip()
    if not url:
        return ""
    parts = urlsplit(url)
    scheme = parts.scheme.lower() or "https"
    if scheme == "http":
        scheme = "https"  # même ressource servie en http/https : évite les doublons
    host = (parts.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    port = parts.port
    netloc = host if port in (None, 80, 443) else f"{host}:{port}"
    query = [(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True)
             if k.lower() not in TRACKING_PARAMS and not k.lower().startswith("utm_")]
    query.sort()
    path = re.sub(r"/{2,}", "/", parts.path or "/")
    if len(path) > 1 and path.endswith("/"):
        path = path.rstrip("/")
    return urlunsplit((scheme, netloc, path, urlencode(query), ""))


def _norm_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", text).strip()


def content_hash(title: str, summary: str = "") -> str:
    """Empreinte du contenu (titre + début du résumé normalisés) pour repérer les republications."""
    basis = _norm_text(title) + "|" + _norm_text(summary)[:300]
    return hashlib.sha256(basis.encode()).hexdigest()


class _TextExtractor(HTMLParser):
    SKIP = {"script", "style", "noscript", "iframe", "object", "embed", "svg", "head"}
    BLOCK = {"p", "br", "div", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip += 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip:
            self._skip -= 1
        elif tag in self.BLOCK:
            self.parts.append("\n")

    def handle_data(self, data):
        if not self._skip:
            self.parts.append(data)


def html_to_text(raw: str, max_len: int = 4000) -> str:
    """Convertit un contenu HTML non fiable en texte brut (scripts, styles et balises supprimés)."""
    if not raw:
        return ""
    parser = _TextExtractor()
    try:
        parser.feed(raw)
        parser.close()
        text = "".join(parser.parts)
    except Exception:
        text = re.sub(r"<[^>]+>", " ", raw)
    text = html.unescape(text)
    text = "".join(ch for ch in text if ch == "\n" or ch == "\t" or unicodedata.category(ch)[0] != "C")
    text = re.sub(r"[ \t ]+", " ", text)
    text = re.sub(r"\n\s*\n+", "\n", text).strip()
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + " […]"
    return text


def clean_title(raw: str) -> str:
    return html_to_text(raw, max_len=400).replace("\n", " ").strip()


def utcnow() -> datetime:
    return datetime.now(timezone.utc).replace(microsecond=0)


def iso(dt: datetime | None) -> str | None:
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).replace(microsecond=0).isoformat()


def parse_date(value) -> datetime | None:
    """Accepte struct_time (feedparser), chaîne ISO ou AAAA-MM-JJ."""
    if value is None or value == "":
        return None
    try:
        import time as _t
        if isinstance(value, _t.struct_time):
            return datetime(*value[:6], tzinfo=timezone.utc)
        if isinstance(value, datetime):
            return value if value.tzinfo else value.replace(tzinfo=timezone.utc)
        s = str(value).strip().replace("Z", "+00:00")
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except (ValueError, TypeError):
        return None


def safe_http_url(url: str) -> str:
    """Renvoie l'URL si elle est en http(s), sinon chaîne vide (évite javascript:, data:, file:)."""
    try:
        p = urlsplit((url or "").strip())
    except ValueError:
        return ""
    return url.strip() if p.scheme in ("http", "https") and p.hostname else ""
