"""Suivi des versions des normes via le jeu ISO Open Data (métadonnées publiques uniquement).

Aucun texte normatif n'est récupéré ni reproduit : seules la référence, le titre, l'édition, le stade
d'élaboration, la date de publication et les liens de remplacement sont exploités.
"""
from __future__ import annotations

import json
import re

from veille.normalize import iso, parse_date, utcnow

STANDARD_PAGE = "https://www.iso.org/standard/{id}.html"

STAGE_GROUPS = {
    "00": "Préliminaire", "10": "Proposition", "20": "Préparation (WD)", "30": "Comité (CD)",
    "40": "Enquête (DIS)", "50": "Approbation (FDIS)", "60": "Publication", "90": "Examen systématique",
    "95": "Retrait",
}
STAGE_SPECIFIC = {
    "6000": "Publication en cours", "6060": "Norme publiée", "9020": "Examen systématique en cours",
    "9060": "Examen systématique clos", "9092": "Décision : à réviser", "9093": "Confirmée après examen",
    "9099": "Retrait proposé", "9520": "Retrait en cours", "9599": "Retirée",
}
_REF_RE = re.compile(r"^ISO(?:/IEC)?(?:/IEEE)?\s+(?:[A-Z]+\s+)*(\d+)(?:-(\d+))?")


def stage_label(code) -> str:
    c = str(code or "").zfill(4)
    if c in STAGE_SPECIFIC:
        return f"{c[:2]}.{c[2:]} — {STAGE_SPECIFIC[c]}"
    if c.endswith("98"):
        return f"{c[:2]}.{c[2:]} — Projet abandonné"
    return f"{c[:2]}.{c[2:]} — {STAGE_GROUPS.get(c[:2], 'Stade inconnu')}"


def is_inactive(code) -> bool:
    c = str(code or "").zfill(4)
    return c == "9599" or c.endswith("98")


def watched_key(reference: str, watched: list[str]) -> str | None:
    """Associe une référence ISO (ex. « ISO/IEC FDIS 27002 », « ISO/IEC 27001:2022/Amd 1:2024 ») à la
    norme surveillée correspondante (ex. « ISO/IEC 27002 »)."""
    m = _REF_RE.match(reference or "")
    if not m:
        return None
    num, part = m.group(1), m.group(2)
    for w in watched:
        wm = _REF_RE.match(w)
        if not wm:
            continue
        if wm.group(1) == num and (wm.group(2) is None or wm.group(2) == part):
            return w
    return None


def parse_iso(content: bytes, watched: list[str]) -> dict[str, list[dict]]:
    numbers = {(_REF_RE.match(w).group(1)).encode() for w in watched if _REF_RE.match(w)}
    found: dict[str, list[dict]] = {w: [] for w in watched}
    for line in content.splitlines():
        if b'"reference":"ISO' not in line or not any(n in line for n in numbers):
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        key = watched_key(d.get("reference", ""), watched)
        if not key:
            continue
        title = d.get("title") or {}
        found[key].append({
            "reference": d["reference"],
            "titre": title.get("fr") or title.get("en"),
            "edition": d.get("edition"),
            "stade": str(d.get("currentStage") or ""),
            "date_publication": d.get("publicationDate"),
            "remplace": json.dumps(d.get("replaces")) if d.get("replaces") else None,
            "remplacee_par": json.dumps(d.get("replacedBy")) if d.get("replacedBy") else None,
            "comite": d.get("ownerCommittee"),
            "iso_id": d.get("id"),
        })
    return found


def build_items(found: dict[str, list[dict]], known: dict[str, dict]) -> tuple[list[dict], list[dict]]:
    """Compare l'état courant avec l'état connu (table normes). Renvoie (éléments à créer, lignes à enregistrer)."""
    items, rows = [], []
    today = utcnow().date().isoformat()
    for family, records in found.items():
        family_known = any(watched_key(ref, [family]) for ref in known)
        active = [r for r in records if not is_inactive(r["stade"])]
        if not family_known:
            if not active:
                continue
            lines = []
            for r in sorted(active, key=lambda r: r["date_publication"] or "9999"):
                line = f"• {r['reference']} — {stage_label(r['stade'])}"
                if r["date_publication"]:
                    line += f", publiée le {r['date_publication']}"
                if r["remplacee_par"] and r["stade"] == "6060":
                    line += " ; un document de remplacement est enregistré par l'ISO (révision engagée, à confirmer sur iso.org)"
                if r["stade"] == "9092":
                    line += " ; l'ISO a décidé de réviser ce document"
                lines.append(line)
            main = next((r for r in active if r["stade"] in ("6060", "9093", "9092", "9020", "9060")), active[0])
            items.append({
                "url": STANDARD_PAGE.format(id=main["iso_id"]),
                "url_canonique": f"iso-opendata:{family}:etat-initial",
                "titre": f"{family} — état de référence des versions (ISO Open Data, {today})",
                "auteur": None,
                "resume_source": f"{main['titre'] or ''}\nDocuments actifs recensés dans les métadonnées ISO :\n" + "\n".join(lines),
                "publie_le": None,  # constat d'état : la date de référence est la date de consultation
                "langue": "fr",
                "origine": "ISO Open Data",
                "donnees": {"norme": family, "evenement": "etat_initial", "documents": active},
            })
        else:
            for r in records:
                old = known.get(r["reference"])
                changes = []
                if old is None:
                    if is_inactive(r["stade"]):
                        continue
                    changes.append(f"nouveau document enregistré ({stage_label(r['stade'])})")
                else:
                    if str(old.get("stade")) != r["stade"]:
                        changes.append(f"stade : {stage_label(old.get('stade'))} → {stage_label(r['stade'])}")
                    if (old.get("date_publication") or None) != (r["date_publication"] or None):
                        changes.append(f"date de publication : {old.get('date_publication') or 'aucune'} → {r['date_publication']}")
                    if (old.get("remplacee_par") or None) != (r["remplacee_par"] or None) and r["remplacee_par"]:
                        changes.append("un document de remplacement est désormais enregistré (révision)")
                if changes:
                    items.append({
                        "url": STANDARD_PAGE.format(id=r["iso_id"]),
                        "url_canonique": f"iso-opendata:{r['iso_id']}:{r['stade']}:{r['date_publication'] or ''}:{r['remplacee_par'] or ''}",
                        "titre": f"{r['reference']} — évolution détectée : {changes[0]}",
                        "auteur": None,
                        "resume_source": f"{r['titre'] or ''}\nNorme surveillée : {family}. Évolutions : " + " ; ".join(changes) + ".",
                        "publie_le": None,  # évolution constatée lors de cette consultation
                        "langue": "fr",
                        "origine": "ISO Open Data",
                        "donnees": {"norme": family, "evenement": "changement", "document": r, "changements": changes},
                    })
        rows.extend(records)
    return items, rows
