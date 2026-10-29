"""Gestion du catalogue de sources : validation, initialisation, import OPML, export YAML."""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlsplit

from veille.config import config_dir, default_settings, load_yaml, save_yaml
from veille.storage import Storage

TYPES = ["rss", "cisa_kev", "iso_opendata", "feedly", "manuel"]
CATEGORIES = {
    "technique": "Veille technique et cybersécurité",
    "reglementaire": "Veille réglementaire",
    "normative": "Veille normative",
    "technologique": "Veille technologique",
}
CONFIANCES = {"elevee": "Élevée", "moyenne": "Moyenne", "faible": "Faible"}
NATURES = {
    "officielle": "Source officielle (autorité, agence, institution)",
    "editeur": "Éditeur / fournisseur",
    "presse_specialisee": "Presse spécialisée",
    "recherche": "Recherche / laboratoire",
    "communautaire": "Communauté / fondation / agrégateur",
}
OPTION_KEYS = ("max_items", "max_octets", "references_surveillees")
_ID_RE = re.compile(r"^[a-z0-9][a-z0-9\-]{1,63}$")


class SourceValidationError(ValueError):
    pass


def slugify(text: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return (s or "source")[:60]


def validate_source(src: dict) -> dict:
    """Valide et normalise une définition de source (saisie utilisateur ou YAML). Lève SourceValidationError."""
    errors = []
    out = dict(src)
    out["nom"] = str(src.get("nom") or "").strip()[:200]
    if not out["nom"]:
        errors.append("Le nom est obligatoire.")
    out["id"] = str(src.get("id") or slugify(out["nom"])).strip().lower()
    if not _ID_RE.match(out["id"]):
        errors.append("Identifiant invalide (lettres minuscules, chiffres, tirets ; 2 à 64 caractères).")
    url = str(src.get("url") or "").strip()
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname:
        errors.append("L'URL doit commencer par http:// ou https:// et contenir un nom d'hôte.")
    elif parts.username or parts.password:
        errors.append("L'URL ne doit pas contenir d'identifiants.")
    elif len(url) > 2000:
        errors.append("URL trop longue.")
    out["url"] = url
    out["type"] = src.get("type") or "rss"
    if out["type"] not in TYPES:
        errors.append(f"Type invalide : {out['type']}")
    out["categorie"] = src.get("categorie") or "technique"
    if out["categorie"] not in CATEGORIES:
        errors.append(f"Catégorie invalide : {out['categorie']}")
    out["confiance"] = src.get("confiance") or "moyenne"
    if out["confiance"] not in CONFIANCES:
        errors.append(f"Niveau de confiance invalide : {out['confiance']}")
    if out.get("nature") and out["nature"] not in NATURES:
        errors.append(f"Nature invalide : {out['nature']}")
    try:
        freq = int(src.get("frequence_minutes") or 1440)
    except (TypeError, ValueError):
        freq = -1
    if not 15 <= freq <= 43200:
        errors.append("La fréquence doit être comprise entre 15 minutes et 30 jours.")
    out["frequence_minutes"] = freq
    for key in ("filtre_mots_cles", "technologies"):
        val = src.get(key) or []
        if isinstance(val, str):
            val = [v.strip() for v in val.split(",")]
        out[key] = [str(v).strip()[:100] for v in val if str(v).strip()][:100]
    opts = dict(src.get("options") or {})
    for k in OPTION_KEYS:
        if src.get(k) is not None:
            opts[k] = src[k]
    if "max_items" in opts:
        opts["max_items"] = max(1, min(int(opts["max_items"]), 1000))
    if "max_octets" in opts:
        opts["max_octets"] = max(10_000, min(int(opts["max_octets"]), 300_000_000))
    out["options"] = opts
    for key in ("sous_categorie", "organisme", "justification", "alternative", "langue"):
        out[key] = (str(src[key]).strip()[:3000] if src.get(key) else None)
    out["actif"] = bool(src.get("actif", True)) and out["type"] != "manuel"
    if src.get("statut_initial"):
        out["statut"] = src["statut_initial"]
    if errors:
        raise SourceValidationError(" ".join(errors))
    return out


def catalog_path() -> Path:
    return config_dir() / "sources.yaml"


def load_catalog(path: Path | None = None) -> list[dict]:
    data = load_yaml(path or catalog_path())
    return [validate_source(s) for s in data.get("sources", [])]


def seed_sources(storage: Storage, path: Path | None = None, overwrite: bool = False) -> int:
    """Charge le catalogue YAML en base. Les sources existantes ne sont pas écrasées (sauf overwrite)."""
    n = 0
    for src in load_catalog(path):
        if storage.upsert_source(src, overwrite=overwrite):
            n += 1
    return n


def export_catalog(storage: Storage) -> str:
    import yaml
    out = []
    for s in storage.list_sources():
        item = {k: s.get(k) for k in ("id", "nom", "url", "type", "categorie", "sous_categorie", "organisme",
                                      "nature", "confiance", "langue", "frequence_minutes", "justification",
                                      "alternative") if s.get(k) not in (None, "")}
        for k in ("filtre_mots_cles", "technologies"):
            if s.get(k):
                item[k] = s[k]
        item.update(s.get("options") or {})
        item["actif"] = bool(s["actif"])
        out.append(item)
    return yaml.safe_dump({"sources": out}, allow_unicode=True, sort_keys=False, width=120)


def save_catalog_file(storage: Storage, path: Path | None = None) -> Path:
    import yaml
    p = path or catalog_path()
    save_yaml(p, yaml.safe_load(export_catalog(storage)))
    return p


def parse_opml(content: bytes | str, categorie: str = "technique") -> list[dict]:
    """Lit un export OPML (ex. Feedly : Organize > Export OPML) et renvoie des définitions de sources RSS.
    Le XML est analysé sans résolution d'entités externes (ElementTree ne les résout pas)."""
    if isinstance(content, bytes):
        content = content.decode("utf-8", "replace")
    if "<!ENTITY" in content.upper():
        raise SourceValidationError("Fichier OPML refusé : déclarations d'entités XML non autorisées.")
    root = ET.fromstring(content)
    sources, seen = [], set()
    for outline in root.iter("outline"):
        url = outline.get("xmlUrl")
        if not url or url in seen:
            continue
        seen.add(url)
        title = outline.get("title") or outline.get("text") or urlsplit(url).hostname or "Flux importé"
        try:
            sources.append(validate_source({
                "id": "opml-" + slugify(title)[:50], "nom": title, "url": url, "type": "rss",
                "categorie": categorie, "confiance": "moyenne", "nature": "communautaire",
                "frequence_minutes": 720, "sous_categorie": "Import OPML",
                "justification": "Flux importé depuis un fichier OPML (ex. abonnements Feedly). "
                                 "Fiabilité à évaluer avant de s'appuyer sur ses informations.",
                "actif": True,
            }))
        except SourceValidationError:
            continue
    return sources


def allowed_domains(storage: Storage, settings: dict | None = None) -> set[str]:
    """Liste blanche des hôtes interrogeables : hôtes des sources configurées + API d'enrichissement."""
    settings = settings or default_settings()
    hosts = set()
    for s in storage.list_sources():
        h = urlsplit(s["url"]).hostname
        if h:
            hosts.add(h.lower())
    hosts.update(settings.get("collecte", {}).get("domaines_autorises_supplementaires", []) or [])
    return hosts
