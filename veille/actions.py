"""Transformation des analyses en actions du plan d'action (aide à la décision, aucune action automatique sur le SI)."""
from __future__ import annotations

from veille.classify import THEMES
from veille.storage import Storage

EFFORT = {"vulnerabilite": "moyen", "menace": "faible", "incident": "faible", "reglementaire": "moyen",
          "normative": "moyen", "technologie": "moyen", "bonne_pratique": "faible"}
PREUVES = {
    "vulnerabilite": "Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, "
                     "résultat de recherche de compromission.",
    "menace": "Règles de détection créées ou vérifiées, compte rendu de test de détection, message de sensibilisation diffusé.",
    "incident": "Note d'analyse du retour d'expérience et décisions associées.",
    "reglementaire": "Note d'applicabilité validée (juriste/DPO), analyse d'écarts, registre des exigences mis à jour.",
    "normative": "Analyse d'impact sur le SMSI / déclaration d'applicabilité, plan de transition validé.",
    "technologie": "Note d'opportunité (bénéfices, risques, prérequis), décision de la direction.",
    "bonne_pratique": "Compte rendu de contrôle de configuration et mesures ajoutées au plan d'amélioration.",
}


def _risk(cat: str, a: dict) -> str:
    techs = ", ".join(t["nom"] for t in a.get("technologies") or []) or "systèmes potentiellement concernés"
    impacts = ", ".join(i["libelle"].lower() for i in a.get("impacts") or []) or "impact à qualifier"
    if cat == "vulnerabilite":
        return f"Risque : compromission de {techs} (atteinte à : {impacts})."
    if cat == "menace":
        return f"Risque : exposition au mode opératoire décrit (atteinte à : {impacts})."
    if cat == "incident":
        return "Risque : reproduction d'un scénario d'incident similaire dans l'organisation."
    if cat == "reglementaire":
        textes = ", ".join(t["nom"].split(" — ")[0] for t in (a.get("reglementaire") or {}).get("textes", [])) or "texte à identifier"
        return f"Risque : non-conformité ({textes}) — sanctions, exigences des clients, responsabilité de la direction."
    if cat == "normative":
        return "Risque : écart avec la version en vigueur du référentiel (certification, exigences contractuelles). Opportunité : amélioration du SMSI."
    if cat == "technologie":
        themes = ", ".join(THEMES[t][0] for t in a.get("themes") or [] if t in THEMES) or "innovation"
        return f"Opportunité d'amélioration : {themes}. Risques associés à évaluer avant adoption."
    return "Opportunité : renforcer les pratiques de sécurité."


def _benefit(cat: str, a: dict) -> str:
    return {
        "vulnerabilite": "Réduction de la surface d'attaque et du risque de compromission des actifs concernés.",
        "menace": "Meilleure capacité de prévention et de détection face à une menace active.",
        "incident": "Capitalisation sur l'expérience d'autres organisations.",
        "reglementaire": "Maîtrise du risque juridique et capacité à démontrer la conformité.",
        "normative": "Alignement du SMSI sur l'état de l'art et maintien des certifications.",
        "technologie": "Gain de sécurité ou d'efficacité, décision d'adoption argumentée.",
        "bonne_pratique": "Durcissement du SI à coût maîtrisé.",
    }.get(cat, "Amélioration de la sécurité du SI.")


def should_create(a: dict) -> bool:
    if a["priorite"] in ("Critique", "Élevée"):
        return True
    cats = set(a.get("categories") or [])
    reg = a.get("reglementaire") or {}
    if a["priorite"] in ("Modérée", "À qualifier") and cats & {"reglementaire", "normative"} \
            and a["pertinence"] in ("forte", "a_qualifier") \
            and not reg.get("nature_evolution", "").startswith("Sanction"):
        return True
    if a["priorite"] == "Modérée" and "technologie" in cats and a["pertinence"] in ("forte", "moyenne"):
        return True
    return False


def build_action(article: dict, a: dict) -> dict:
    cat = a["categorie_principale"]
    recs = a.get("actions") or []
    action_text = recs[0]["action"] if recs else "Qualifier l'information."
    if len(recs) > 1:
        action_text += " Puis : " + " ".join(f"({i}) {r['action']}" for i, r in enumerate(recs[1:], 2))
    justif = next((f["justification"] for f in a.get("facteurs") or [] if f["facteur"] == "_justification"), "")
    date = (article.get("publie_le") or article.get("collecte_le") or "")[:10]
    effort = EFFORT.get(cat, "moyen")
    if cat == "normative" and (a.get("normatif") or {}).get("evenement") == "changement":
        effort = "eleve"
    return {
        "constat": f"{article['titre']} — {article.get('source_nom') or article['source_id']} ({date}). {article['url']}",
        "risque": _risk(cat, a),
        "action": action_text,
        "justification": justif,
        "priorite": a["priorite"],
        "responsable": recs[0]["responsable"] if recs else "RSSI",
        "echeance": a.get("echeance"),
        "effort": effort,
        "benefice": _benefit(cat, a),
        "preuves": PREUVES.get(cat, "Compte rendu de traitement."),
        "statut": "a_etudier" if a["priorite"] != "À qualifier" else "a_valider",
    }


def sync_actions(storage: Storage, article_ids: list[int] | None = None) -> int:
    if article_ids is not None and not article_ids:
        return 0
    rows = storage.query(
        "SELECT n.article_id FROM analyses n" + (f" WHERE n.article_id IN ({','.join('?' * len(article_ids))})" if article_ids else ""),
        article_ids or [])
    created = 0
    for r in rows:
        art = storage.get_article(r["article_id"])
        an = storage.query("SELECT * FROM analyses WHERE article_id = ?", (r["article_id"],))[0]
        key = f"article:{art['id']}:{an['categorie_principale']}"
        if art["statut"] == "non_pertinent" or not should_create(an):
            # retire une action automatique devenue injustifiée, uniquement si personne ne l'a modifiée
            with storage.conn() as c:
                c.execute("DELETE FROM actions WHERE article_id = ? AND origine = 'auto' AND statut IN ('a_etudier', 'a_valider') "
                          "AND modifie_le = cree_le", (art["id"],))
            continue
        if storage.upsert_auto_action(key, art["id"], build_action(art, an)):
            created += 1
    return created
