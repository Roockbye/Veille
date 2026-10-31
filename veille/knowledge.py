"""Référentiel des textes et normes (config/referentiels.yaml) et évaluation prudente de l'applicabilité."""
from __future__ import annotations

from functools import lru_cache

from veille.classify import find_terms
from veille.config import config_dir, load_yaml
from veille.organisation import TAILLE_RANG

NATURES_JURIDIQUES = {
    "obligation_legale": "Obligation légale (texte contraignant)",
    "norme": "Norme volontaire",
    "referentiel": "Référentiel de bonnes pratiques",
    "recommandation": "Recommandation (non contraignante)",
    "exigence_contractuelle": "Exigence contractuelle",
}
APPLICABILITE = {
    "probable": "Applicabilité probable — à confirmer",
    "indirect": "Impact indirect probable (clients, contrats)",
    "a_qualifier": "Applicabilité à qualifier",
    "peu_probable": "Applicabilité peu probable en l'état des informations",
    "non_evaluable": "Non évaluable : informations manquantes",
}
STATUTS = {
    "projet": "Projet / proposition",
    "adopte": "Texte adopté",
    "publie": "Publié",
    "applicable": "Applicable",
    "applicable_progressivement": "Application progressive",
    "adopte_transposition_a_verifier": "Adopté (UE) — transposition nationale à vérifier",
    "abroge": "Abrogé",
    "inconnu": "Statut à vérifier",
}


@lru_cache(maxsize=1)
def _load(path_str: str) -> tuple:
    data = load_yaml(config_dir() / "referentiels.yaml")
    return tuple(data.get("textes", []))


def referentiels() -> list[dict]:
    return [dict(t) for t in _load(str(config_dir()))]


def get_referentiel(ref_id: str) -> dict | None:
    return next((t for t in referentiels() if t["id"] == ref_id), None)


def detect_referentiels(text: str) -> list[dict]:
    """Textes et normes cités dans un article (d'après leurs mots-clés)."""
    out = []
    for t in referentiels():
        hits = find_terms(text, t.get("mots_cles", []))
        if hits:
            out.append({"id": t["id"], "nom": t["nom"], "declencheurs": hits[:5]})
    return out


def _cond_ok(cond: dict, p: dict) -> tuple[bool, list[str]]:
    """Toutes les clés de la condition doivent être satisfaites (ET) ; dans une clé, une valeur suffit (OU)."""
    missing = []
    secteurs = {p.get("secteur")} | set(p.get("secteurs_secondaires") or [])
    secteurs.discard(None)
    if "secteurs" in cond:
        if not secteurs:
            missing.append("secteur")
        elif not secteurs & set(cond["secteurs"]):
            return False, missing
    if "taille_min" in cond:
        if not p.get("taille"):
            missing.append("taille")
        elif TAILLE_RANG.get(p["taille"], 0) < TAILLE_RANG[cond["taille_min"]]:
            return False, missing
    if "roles" in cond and not set(p.get("roles") or []) & set(cond["roles"]):
        return False, missing
    if "donnees" in cond:
        if not p.get("donnees_traitees"):
            missing.append("données traitées")
        elif not set(p["donnees_traitees"]) & set(cond["donnees"]):
            return False, missing
    if "exigence" in cond:
        ids = {(e.get("id") or "").lower() for e in p.get("exigences") or [] if e.get("statut") != "cible"}
        if not ids & set(cond["exigence"]):
            return False, missing
    return (not missing), missing


def evaluate_applicability(ref: dict, profile: dict) -> dict:
    """Orientation d'applicabilité justifiée. Ne conclut jamais à une obligation certaine."""
    declared = next((e for e in profile.get("exigences") or [] if (e.get("id") or "").lower() == ref["id"]), None)
    rules = (ref.get("applicabilite") or {}).get("regles") or []
    missing_all: list[str] = []
    result = None
    for rule in rules:
        ok, missing = _cond_ok(rule.get("si") or {}, profile)
        if ok:
            result = {"resultat": rule["resultat"], "motif": rule.get("motif", "")}
            break
        missing_all += missing
    if result is None:
        if missing_all:
            result = {"resultat": "non_evaluable",
                      "motif": "Informations manquantes dans le profil : " + ", ".join(sorted(set(missing_all))) + "."}
        else:
            d = (ref.get("applicabilite") or {}).get("defaut") or {"resultat": "a_qualifier", "motif": ""}
            result = {"resultat": d["resultat"], "motif": d.get("motif", "")}
    if declared and declared.get("statut") == "cible":
        result = {"resultat": "a_qualifier",
                  "motif": "Non exigé : retenu par l'organisation comme référentiel de bonnes pratiques et cible à long terme."
                           + (f" ({declared['commentaire']})" if declared.get("commentaire") else "")}
        declared = None
    if declared:
        statut = "identifiée" if declared.get("statut") == "identifiee" else "à confirmer"
        result["motif"] += f" L'organisation a déclaré cette exigence ({statut})."
        if result["resultat"] in ("peu_probable", "a_qualifier", "non_evaluable") and declared.get("statut") == "identifiee":
            result["resultat"] = "probable"
    result["libelle"] = APPLICABILITE[result["resultat"]]
    result["nature"] = ref.get("nature_juridique")
    result["nature_libelle"] = NATURES_JURIDIQUES.get(ref.get("nature_juridique"), "À qualifier")
    return result


def applicability_matrix(profile: dict) -> list[dict]:
    rows = []
    for ref in referentiels():
        ev = evaluate_applicability(ref, profile)
        rows.append({"id": ref["id"], "nom": ref["nom"], "reference": ref.get("reference"),
                     "type_veille": ref.get("type_veille"), **ev,
                     "statut": STATUTS.get(ref.get("statut"), ref.get("statut")),
                     "note_statut": ref.get("note_statut"), "dates": ref.get("dates") or [],
                     "references": ref.get("references") or [], "revise_le": ref.get("revise_le"),
                     "obligations_possibles": ref.get("obligations_possibles") or [],
                     "demarches_applicabilite": ref.get("demarches_applicabilite") or [],
                     "concernes": ref.get("concernes")})
    return rows
