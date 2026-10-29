"""Construction du rapport de veille à partir des données réellement collectées sur la période.

Le rapport est d'abord produit sous forme de blocs neutres (titres, paragraphes, listes, tableaux, fiches),
puis rendu en Markdown et en PDF. Aucune section n'est « remplie » artificiellement : en l'absence de
données, la section l'indique explicitement.

Étiquettes utilisées pour distinguer la nature des affirmations :
  [Fait]           information issue d'une source consultable (URL citée)
  [Donnée vérifiée] valeur issue d'une base de référence (NVD, CISA KEV, FIRST EPSS, ISO Open Data)
  [Analyse]        résultat des règles d'analyse de l'outil
  [Hypothèse]      supposition explicite liée à un profil incomplet
  [Recommandation] proposition d'action, à valider
  [À vérifier]     point non confirmé
"""
from __future__ import annotations

from collections import Counter
from datetime import date, datetime, time, timedelta, timezone
from pathlib import Path

from veille import ANALYZER_VERSION, __version__
from veille.analysis import PRIORITY_ORDER
from veille.classify import CATEGORIES, THEMES
from veille.config import reports_dir
from veille.knowledge import applicability_matrix
from veille.organisation import (DONNEES, MATURITES, ROLES, SECTEURS, TAILLES, hypotheses, missing_fields)
from veille.normalize import iso, parse_date, utcnow
from veille.sources import CATEGORIES as SOURCE_CATEGORIES, CONFIANCES, NATURES
from veille.storage import Storage

PERIMETRES = {
    "technique": ("Veille technique et cybersécurité", {"vulnerabilite", "menace", "incident", "bonne_pratique"}),
    "technologique": ("Veille technologique", {"technologie"}),
    "reglementaire": ("Veille réglementaire", {"reglementaire"}),
    "normative": ("Veille normative", {"normative"}),
}
STATUT_SOURCE = {"ok": "Fonctionnelle", "erreur": "En erreur", "bloque": "Bloquée / non collectable",
                 "non_verifie": "Non encore vérifiée", "desactive": "Désactivée"}
ACTION_STATUT = {"a_etudier": "À étudier", "a_valider": "À valider", "planifiee": "Planifiée", "en_cours": "En cours",
                 "terminee": "Terminée", "abandonnee": "Abandonnée"}
EFFORT = {"faible": "Faible", "moyen": "Moyen", "eleve": "Élevé"}
FRESHNESS_DAYS = 30
MAX_ITEMS = {"vuln": 15, "menace": 10, "techno": 12, "reg": 12, "norm": 10, "pratique": 8}


def _d(s: str | None) -> str:
    return (s or "")[:10] or "n.c."


def _prio_key(a: dict) -> tuple:
    return (PRIORITY_ORDER.get(a.get("priorite") or "Faible", 9), -(a.get("score") or 0), a.get("publie_le") or "")


def cluster_topics(items: list[dict]) -> list[tuple[dict, list[dict]]]:
    """Regroupe les éléments traitant du même sujet (CVE communes) : le premier (le plus prioritaire) représente le groupe."""
    groups: list[tuple[dict, list[dict], set]] = []
    for a in items:
        cves = {c["id"] for c in a.get("cves") or []}
        for lead, others, keys in groups:
            if cves and keys & cves:
                others.append(a)
                keys |= cves
                break
        else:
            groups.append((a, [], set(cves)))
    return [(lead, others) for lead, others, _ in groups]


class Doc:
    def __init__(self) -> None:
        self.blocks: list[dict] = []
        self.cited: set[str] = set()

    def h1(self, text): self.blocks.append({"t": "h1", "text": text})
    def h2(self, text): self.blocks.append({"t": "h2", "text": text})
    def h3(self, text): self.blocks.append({"t": "h3", "text": text})
    def p(self, text, label=None): self.blocks.append({"t": "p", "text": text, "label": label})
    def note(self, text): self.blocks.append({"t": "note", "text": text})
    def ul(self, items): self.blocks.append({"t": "ul", "items": [i if isinstance(i, tuple) else (None, i) for i in items]})
    def table(self, head, rows, widths=None): self.blocks.append({"t": "table", "head": head, "rows": rows, "widths": widths})
    def card(self, title, url, lines):
        self.blocks.append({"t": "card", "title": title, "url": url, "lines": lines})
        if url:
            self.cited.add(url)
    def pagebreak(self): self.blocks.append({"t": "pb"})
    def empty(self, what): self.note(f"Aucune donnée pour cette section sur la période : {what}. "
                                     "Rien n'est extrapolé ; voir la section « Limites de la veille ».")


def collect_data(storage: Storage, start: date, end: date, perimetres: list[str] | None = None,
                 profile: dict | None = None, freshness_days: int = FRESHNESS_DAYS) -> dict:
    from veille.pipeline import current_profile
    profile = profile or current_profile()
    perimetres = perimetres or list(PERIMETRES)
    cats_in_scope = set().union(*(PERIMETRES[p][1] for p in perimetres if p in PERIMETRES))
    d_from = iso(datetime.combine(start, time.min, tzinfo=timezone.utc))
    d_to = iso(datetime.combine(end, time.max.replace(microsecond=0), tzinfo=timezone.utc))
    rows = storage.list_articles(date_from=d_from, date_to=d_to, date_field="collecte_le", limit=100000)
    rows = [r for r in rows if r.get("priorite")]  # analysés uniquement
    oldest = datetime.combine(start - timedelta(days=freshness_days), time.min, tzinfo=timezone.utc)
    kept, old, non_pert, user_excluded = [], 0, 0, 0
    for r in rows:
        pub = parse_date(r.get("publie_le"))
        if pub and pub < oldest:
            old += 1
            continue
        if r["statut"] == "non_pertinent":
            user_excluded += 1
            continue
        if r.get("pertinence") == "non_pertinent":
            non_pert += 1
            continue
        if not set(r.get("categories") or []) & cats_in_scope:
            continue
        kept.append(r)
    kept.sort(key=_prio_key)
    actions = storage.list_actions()
    actions = [a for a in actions if a["statut"] not in ("terminee", "abandonnee")
               or (a.get("modifie_le") or "") >= d_from]
    article_ids = {r["id"] for r in kept}
    actions = [a for a in actions if a["article_id"] in article_ids or a["origine"] == "manuel"]
    execs = [e for e in storage.list_executions(1000) if d_from <= e["debut"] <= d_to and e["type"] == "collecte"]
    return {
        "profile": profile, "start": start, "end": end, "perimetres": perimetres, "articles": kept,
        "all_collected": len(rows), "old_excluded": old, "non_pertinent": non_pert, "user_excluded": user_excluded,
        "sources": storage.list_sources(), "actions": actions, "executions": execs,
        "matrix": applicability_matrix(profile), "normes": storage.query("SELECT * FROM normes ORDER BY reference"),
        "freshness_days": freshness_days, "generated": utcnow(),
    }


def _fact_lines(a: dict) -> list[tuple[str, str]]:
    lines = [("Source", f"{a['source_nom']} — publié le {_d(a.get('publie_le'))}, consulté le {_d(a['collecte_le'])}")]
    lines.append(("Catégorie", ", ".join(CATEGORIES.get(c, c) for c in a.get("categories") or [])
                  + (f" — mots-clés : {', '.join(a['mots_cles'][:8])}" if a.get("mots_cles") else "")))
    lines.append(("[Fait] Résumé" if a.get("methode_resume") == "extrait_source" else
                  "[Analyse] Résumé" if (a.get("methode_resume") or "").startswith("synthese") else "[Analyse IA] Résumé",
                  a.get("resume_fr") or "n.c."))
    return lines


def _analysis_lines(a: dict, with_actions: bool = True) -> list[tuple[str, str]]:
    lines = []
    if a.get("technologies"):
        lines.append(("[Analyse] Parc concerné", "; ".join(
            f"{t['nom']} (exposition : {t['exposition']}, criticité : {t['criticite']}, versions du parc : "
            f"{', '.join(t['versions_parc']) or 'n.c.'})" for t in a["technologies"])))
    elif a.get("produits_cites"):
        lines.append(("Produits cités", ", ".join(a["produits_cites"][:8])))
    cves = a.get("cves") or []
    if cves:
        parts = []
        for c in cves[:6]:
            s = c["id"]
            s += f" — CVSS {c['cvss']} ({c.get('severite') or 'n.c.'}, {c.get('cvss_source')})" if c.get("cvss") is not None else " — CVSS non disponible"
            if c.get("epss") is not None:
                s += f", EPSS {c['epss']:.2f}"
            if c.get("kev"):
                s += ", KEV : exploitation active confirmée"
            parts.append(s)
        lines.append(("[Donnée vérifiée] CVE", "; ".join(parts) + (" …" if len(cves) > 6 else "")))
    expl = next((f for f in a.get("facteurs") or [] if f["facteur"] == "_exploitation"), None)
    if expl and (set(a.get("categories") or []) & {"vulnerabilite", "menace", "incident"} or expl["verifie"]):
        lines.append(("Exploitation", expl["justification"] + (" (vérifié)" if expl["verifie"] else "")))
    if a.get("impacts"):
        lines.append(("[Analyse] Impact potentiel", ", ".join(i["libelle"] for i in a["impacts"])))
    lines.append(("[Analyse] Pertinence", f"{a['pertinence']} — " + " ".join(a.get("pertinence_motifs") or [])))
    just = next((f["justification"] for f in a.get("facteurs") or [] if f["facteur"] == "_justification"), "")
    lines.append(("[Analyse] Priorité", f"{a['priorite']} — {just}"))
    if with_actions and a.get("actions"):
        lines.append(("[Recommandation]", " ".join(f"({i}) {r['action']}" for i, r in enumerate(a["actions"], 1))))
        lines.append(("Échéance proposée", f"{a.get('echeance')} — urgence : {a.get('urgence')}"))
    lines.append(("Confiance de l'analyse", a.get("confiance") or "n.c."))
    if a.get("a_verifier"):
        lines.append(("[À vérifier]", " ".join(a["a_verifier"])))
    return lines


def build_document(data: dict) -> Doc:
    p = data["profile"]
    arts = data["articles"]
    doc = Doc()
    by_cat = lambda cats: [a for a in arts if set(a.get("categories") or []) & cats]  # noqa: E731
    vulns = [a for a in by_cat({"vulnerabilite"}) if a["priorite"] != "Faible" or any(c.get("kev") for c in a.get("cves") or [])]
    menaces = by_cat({"menace", "incident"})
    techno = [a for a in by_cat({"technologie"}) if a["pertinence"] in ("forte", "moyenne")]
    reg = by_cat({"reglementaire"})
    norm = by_cat({"normative"})
    pratiques = [a for a in by_cat({"bonne_pratique"}) if a["priorite"] != "Faible"]
    prio = Counter(a["priorite"] for a in arts)
    period = f"du {data['start'].strftime('%d/%m/%Y')} au {data['end'].strftime('%d/%m/%Y')}"
    scope_labels = [PERIMETRES[x][0] for x in data["perimetres"] if x in PERIMETRES]
    hyps = hypotheses(p)

    # 1. Page de garde
    doc.blocks.append({"t": "cover", "title": "Rapport de veille technologique, technique, réglementaire et normative",
                       "subtitle": "Sécurité du système d'information",
                       "org": p.get("nom") or "Organisation non renseignée",
                       "lines": [f"Période : {period}",
                                 f"Généré le {data['generated'].strftime('%d/%m/%Y à %H:%M')} (UTC)",
                                 "Périmètre : " + ", ".join(scope_labels),
                                 f"Outil : VeilleCyber {__version__} — moteur d'analyse {ANALYZER_VERSION}",
                                 "Compétence visée : B1.A1.C3"],
                       "demo": bool(p.get("demonstration"))})

    # 2. Résumé exécutif
    doc.h1("1. Résumé exécutif")
    doc.p(f"Sur la période {period}, {data['all_collected']} éléments ont été collectés automatiquement auprès de "
          f"{sum(1 for s in data['sources'] if s['statut'] == 'ok')} sources fonctionnelles. Après exclusion des "
          f"éléments anciens republiés ({data['old_excluded']}), non pertinents ({data['non_pertinent']}) ou écartés par "
          f"l'analyste ({data['user_excluded']}), {len(arts)} éléments entrent dans le périmètre de ce rapport.", "[Fait]")
    doc.table(["Priorité", "Nombre d'éléments"], [[k, str(prio.get(k, 0))] for k in ["Critique", "Élevée", "Modérée", "Faible", "À qualifier"]])
    top = cluster_topics([a for a in arts if a["priorite"] in ("Critique", "Élevée")])[:8]
    if top:
        doc.p("Points d'attention prioritaires (un sujet couvert par plusieurs sources n'est cité qu'une fois) :", "[Analyse]")
        doc.ul([f"[{a['priorite']}] {a['titre']} ({a['source_nom']}, {_d(a.get('publie_le'))})"
                + (f" — confirmé par {len(others)} autre(s) source(s) : {', '.join(sorted({o['source_nom'] for o in others})[:5])}" if others else "")
                + f" — {(a.get('actions') or [{'action': 'à qualifier'}])[0]['action']}" for a, others in top])
    else:
        doc.p("Aucun élément de priorité critique ou élevée n'a été identifié sur la période.", "[Analyse]")
    reg_prob = [m for m in data["matrix"] if m["resultat"] in ("probable", "indirect") and m["nature"] in ("obligation_legale", "exigence_contractuelle")]
    if reg_prob:
        doc.p("Textes dont l'applicabilité est probable ou indirecte (à confirmer) : " +
              ", ".join(m["nom"].split(" — ")[0] for m in reg_prob) + ".", "[Analyse]")
    open_actions = [a for a in data["actions"] if a["statut"] not in ("terminee", "abandonnee")]
    doc.p(f"{len(open_actions)} actions sont proposées ou en cours dans le plan d'action "
          f"({sum(1 for a in open_actions if a['priorite'] == 'Critique')} critiques, "
          f"{sum(1 for a in open_actions if a['priorite'] == 'Élevée')} élevées).", "[Recommandation]")
    if p.get("demonstration"):
        doc.note("Profil de démonstration : l'organisation étudiée est fictive. Les données collectées sont réelles, "
                 "mais l'analyse d'impact illustre la méthode et doit être refaite avec le profil réel.")

    # 3. Objectifs et périmètre
    doc.h1("2. Objectifs et périmètre de la veille")
    doc.p("Objectifs : (1) surveiller les menaces, vulnérabilités et innovations technologiques pertinentes ; "
          "(2) suivre l'évolution des cadres légaux et des normes applicables ; (3) analyser leurs impacts sur "
          "l'organisation ; (4) identifier les obligations à vérifier et les opportunités d'amélioration de la sécurité du SI.")
    doc.h2("Organisation étudiée")
    doc.table(["Élément", "Valeur déclarée"], [
        ["Nom", p.get("nom") or "Non renseigné"],
        ["Secteur", SECTEURS.get(p.get("secteur"), "Non renseigné") +
         (" ; secondaires : " + ", ".join(SECTEURS.get(s, s) for s in p.get("secteurs_secondaires")) if p.get("secteurs_secondaires") else "")],
        ["Taille", (TAILLES.get(p.get("taille"), "Non renseignée")) + (f" — {p['effectif']} salariés" if p.get("effectif") else "")],
        ["Maturité cyber", MATURITES.get(p.get("maturite_cyber"), "Non renseignée")],
        ["Rôles", ", ".join(ROLES.get(r, r) for r in p.get("roles") or []) or "Non renseignés"],
        ["Données traitées", ", ".join(DONNEES.get(d, d) for d in p.get("donnees_traitees") or []) or "Non renseignées"],
        ["Activités", "; ".join(p.get("activites") or []) or "Non renseignées"],
        ["Technologies inventoriées", str(len(p.get("technologies") or []))],
        ["Exigences identifiées", "; ".join(f"{e['nom']} ({e['type']}, {e['statut']})" for e in p.get("exigences") or []) or "Aucune"],
        ["Thèmes technologiques", ", ".join(THEMES[t][0] for t in p.get("themes_veille") or [] if t in THEMES) or "Tous"],
    ], widths=[0.28, 0.72])
    if p.get("contraintes_securite") or p.get("risques_connus"):
        doc.ul([("Contrainte", c) for c in p.get("contraintes_securite") or []] +
               [("Risque connu", r) for r in p.get("risques_connus") or []])
    if hyps:
        doc.h2("Hypothèses de travail")
        doc.ul([("[Hypothèse]", h) for h in hyps])
    miss = missing_fields(p)
    if miss:
        doc.p("Informations à compléter dans le profil : " + ", ".join(miss) + ".", "[À vérifier]")
    doc.p("Périmètre du rapport : " + ", ".join(scope_labels) + ".")

    # 4. Méthodologie
    doc.h1("3. Méthodologie")
    doc.ul([
        ("Collecte", "interrogation automatique de flux RSS/Atom et d'interfaces publiques autorisées (CISA KEV, ISO Open Data, "
                     "API NVD, FIRST EPSS), à une fréquence propre à chaque source, avec respect de robots.txt, requêtes conditionnelles "
                     "et limitation de débit. Dates de publication et de collecte conservées séparément."),
        ("Déduplication", "URL canonique (suppression des paramètres de suivi) puis empreinte du contenu (titre + résumé normalisés)."),
        ("Classification", "règles explicites (mots-clés FR/EN, type et catégorie de la source) en huit catégories ; un article peut relever de plusieurs catégories."),
        ("Enrichissement", "scores CVSS issus du NVD, exploitation active issue du catalogue CISA KEV, probabilité EPSS (FIRST). Aucune valeur n'est estimée."),
        ("Pertinence", "rapprochement avec l'inventaire technique, les thèmes surveillés et l'applicabilité des textes au profil de l'organisation."),
        ("Priorisation", "score additif explicable (gravité, exploitation, présence et exposition dans le parc, criticité, urgence, importance réglementaire, ancienneté) ; "
                         "niveau « Critique » réservé aux technologies du parc avec gravité ou exploitation vérifiée."),
        ("Restitution", "fiche par élément, plan d'action et ce rapport ; chaque information est reliée à son URL d'origine (annexes)."),
        ("Fraîcheur", f"les éléments publiés plus de {data['freshness_days']} jours avant le début de la période sont exclus des résultats ({data['old_excluded']} éléments)."),
    ])
    doc.p(f"Exécutions de collecte sur la période : {len(data['executions'])} "
          f"(dont {sum(1 for e in data['executions'] if e['statut'] == 'succes')} réussies, "
          f"{sum(1 for e in data['executions'] if e['statut'] == 'partiel')} partielles, "
          f"{sum(1 for e in data['executions'] if e['statut'] == 'echec')} en échec).", "[Fait]")

    # 5. Outils
    doc.h1("4. Justification des outils utilisés")
    doc.table(["Outil", "Usage", "Justification"], [
        ["Python 3", "Langage de l'application", "Écosystème mature pour la collecte, l'analyse et la génération de documents."],
        ["feedparser", "Lecture RSS/Atom", "Tolère les flux mal formés ; standard de fait."],
        ["httpx", "Requêtes HTTP", "Délais, flux de réponse et redirections contrôlés (protection SSRF)."],
        ["SQLite", "Stockage", "Base locale sans serveur, transactionnelle, suffisante pour une veille d'organisation."],
        ["Streamlit", "Interface web", "Tableau de bord local en français, rapide à déployer."],
        ["APScheduler", "Planification", "Collecte et rapports périodiques ; service système possible."],
        ["ReportLab", "Export PDF", "Génération PDF sans dépendance externe."],
        ["API NVD, CISA KEV, FIRST EPSS", "Enrichissement", "Sources de référence publiques pour CVSS, exploitation et probabilité."],
        ["IA (facultative)", "Résumés en français", "Désactivée par défaut ; contenus traités comme données non fiables ; n'influence pas la priorité."],
    ], widths=[0.22, 0.22, 0.56])

    # 6. Sources
    doc.h1("5. Catalogue des sources et justification")
    cat_counts = Counter(a["source_id"] for a in arts)
    for key, label in SOURCE_CATEGORIES.items():
        srcs = [s for s in data["sources"] if s["categorie"] == key]
        if not srcs:
            continue
        doc.h2(label)
        doc.table(["Source", "Nature / confiance", "Fréquence", "État", "Éléments retenus", "Justification"],
                  [[s["nom"], f"{NATURES.get(s.get('nature'), s.get('nature') or 'n.c.').split(' (')[0]} / {CONFIANCES.get(s['confiance'])}",
                    f"{s['frequence_minutes'] // 60} h" if s["frequence_minutes"] >= 60 else f"{s['frequence_minutes']} min",
                    STATUT_SOURCE.get(s["statut"], s["statut"]), str(cat_counts.get(s["id"], 0)),
                    (s.get("justification") or "") + (f" Alternative : {s['alternative']}" if s.get("alternative") and s["statut"] in ("bloque", "erreur", "desactive") else "")]
                   for s in srcs], widths=[0.18, 0.14, 0.08, 0.11, 0.08, 0.41])

    # 7. Résultats veille technique
    doc.h1("6. Résultats de la veille technique et cybersécurité")
    if "technique" not in data["perimetres"]:
        doc.note("Hors périmètre de ce rapport.")
    else:
        tech_all = by_cat(PERIMETRES["technique"][1])
        if not tech_all:
            doc.empty("veille technique")
        else:
            c = Counter(cat for a in tech_all for cat in a["categories"] if cat in PERIMETRES["technique"][1])
            doc.table(["Catégorie", "Éléments"], [[CATEGORIES[k], str(v)] for k, v in c.most_common()])
            tc = Counter(t["nom"] for a in tech_all for t in a.get("technologies") or [])
            if tc:
                doc.p("Technologies du parc les plus citées : " + ", ".join(f"{k} ({v})" for k, v in tc.most_common(8)) + ".", "[Analyse]")
            if pratiques:
                doc.h2("Bonnes pratiques et recommandations publiées")
                for a in pratiques[:MAX_ITEMS["pratique"]]:
                    doc.card(a["titre"], a["url"], _fact_lines(a) + _analysis_lines(a))

    # 8. Menaces et vulnérabilités
    doc.h1("7. Menaces et vulnérabilités identifiées")
    if "technique" not in data["perimetres"]:
        doc.note("Hors périmètre de ce rapport.")
    else:
        doc.h2("Vulnérabilités")
        if not vulns:
            doc.empty("vulnérabilités de priorité modérée ou supérieure")
        else:
            for a in vulns[:MAX_ITEMS["vuln"]]:
                doc.card(f"[{a['priorite']}] {a['titre']}", a["url"], _fact_lines(a) + _analysis_lines(a))
            if len(vulns) > MAX_ITEMS["vuln"]:
                doc.p(f"{len(vulns) - MAX_ITEMS['vuln']} autres vulnérabilités sont référencées en annexe.")
        doc.h2("Menaces, campagnes et incidents")
        if not menaces:
            doc.empty("menaces et incidents")
        else:
            for a in menaces[:MAX_ITEMS["menace"]]:
                doc.card(f"[{a['priorite']}] {a['titre']}", a["url"], _fact_lines(a) + _analysis_lines(a))

    # 9. Technologique
    doc.h1("8. Évolutions technologiques pertinentes")
    if "technologique" not in data["perimetres"]:
        doc.note("Hors périmètre de ce rapport.")
    elif not techno:
        doc.empty("évolutions technologiques pertinentes")
    else:
        tcount = Counter(t for a in techno for t in a.get("themes") or [])
        doc.table(["Thème", "Éléments", "Surveillé"], [[THEMES[k][0], str(v), "oui" if k in (p.get("themes_veille") or THEMES) else "non"]
                                                       for k, v in tcount.most_common() if k in THEMES])
        for a in techno[:MAX_ITEMS["techno"]]:
            doc.card(a["titre"], a["url"], _fact_lines(a) + _analysis_lines(a))

    # 10. Réglementaire
    doc.h1("9. Veille réglementaire")
    if "reglementaire" not in data["perimetres"]:
        doc.note("Hors périmètre de ce rapport.")
    else:
        doc.h2("Textes surveillés et orientation d'applicabilité")
        doc.note("Orientation calculée à partir du profil déclaré : elle ne constitue pas un avis juridique et doit être "
                 "confirmée par le juriste ou le DPO. Statuts et dates issus du référentiel de configuration (vérifié le "
                 "indiqué), à revérifier sur les sources officielles.")
        doc.table(["Texte", "Nature", "Statut (référentiel)", "Applicabilité (orientation)", "Motif"],
                  [[m["nom"], m["nature_libelle"], m["statut"] or "n.c.", m["libelle"], m["motif"]]
                   for m in data["matrix"] if m["nature"] in ("obligation_legale",)],
                  widths=[0.22, 0.13, 0.15, 0.17, 0.33])
        doc.h2("Évolutions détectées sur la période")
        if not reg:
            doc.empty("évolutions réglementaires")
        for a in reg[:MAX_ITEMS["reg"]]:
            r = a.get("reglementaire") or {}
            lines = _fact_lines(a)
            if r:
                lines.append(("[Analyse] Nature de l'évolution", r.get("nature_evolution", "")))
                lines.append(("[Analyse] Statut juridique", r.get("statut_detecte", "")))
                if r.get("dates_mentionnees"):
                    lines.append(("[Fait] Dates mentionnées par la source", ", ".join(d["date"] for d in r["dates_mentionnees"])))
                for t in r.get("textes") or []:
                    lines.append((f"Texte concerné : {t['nom']}",
                                  f"{t['reference']} — {t['nature_juridique']} — {t['applicabilite']}. {t['motif']} "
                                  f"Organisations concernées : {t.get('concernes') or 'n.c.'}"))
                    if t.get("obligations_possibles"):
                        lines.append(("Obligations possibles (à vérifier)", "; ".join(t["obligations_possibles"])))
                    if t.get("demarches"):
                        lines.append(("Démarches pour qualifier l'applicabilité", "; ".join(t["demarches"])))
                lines.append(("[Analyse] Impact potentiel", r.get("impact", "")))
            lines += [l for l in _analysis_lines(a) if not l[0].startswith("[Analyse] Impact")]
            doc.card(f"[{a['priorite']}] {a['titre']}", a["url"], lines)

    # 11. Normative
    doc.h1("10. Veille normative")
    if "normative" not in data["perimetres"]:
        doc.note("Hors périmètre de ce rapport.")
    else:
        doc.note("Distinction appliquée : une norme (ISO/IEC) ou un référentiel (NIST CSF) est d'application volontaire, "
                 "une recommandation (ANSSI) n'est pas contraignante ; seuls un texte légal, un contrat ou une "
                 "certification visée les rendent exigibles. Aucune recommandation n'est présentée comme une obligation légale.")
        doc.table(["Référentiel", "Nature", "Applicabilité (orientation)", "Motif"],
                  [[m["nom"], m["nature_libelle"], m["libelle"], m["motif"]] for m in data["matrix"] if m["nature"] != "obligation_legale"],
                  widths=[0.28, 0.17, 0.2, 0.35])
        if data["normes"]:
            from veille.collectors.iso_opendata import stage_label
            doc.h2("État des normes ISO surveillées (métadonnées ISO Open Data)")
            doc.table(["Référence", "Stade", "Publication", "Mise à jour"],
                      [[n["reference"], stage_label(n["stade"]), n.get("date_publication") or "—", _d(n["maj_le"])]
                       for n in data["normes"] if not str(n["stade"]).endswith("98") and n["stade"] != "9599"],
                      widths=[0.35, 0.35, 0.15, 0.15])
        doc.h2("Évolutions détectées sur la période")
        if not norm:
            doc.empty("évolutions normatives")
        for a in norm[:MAX_ITEMS["norm"]]:
            n = a.get("normatif") or {}
            lines = _fact_lines(a)
            if n:
                lines.append(("[Analyse] Type de document", n.get("type_libelle", "")))
                lines.append(("Avertissement", n.get("avertissement", "")))
            lines += _analysis_lines(a)
            doc.card(f"[{a['priorite']}] {a['titre']}", a["url"], lines)

    # 12. Impacts
    doc.h1("11. Analyse des impacts pour l'organisation")
    if not arts:
        doc.empty("impacts")
    else:
        inv = Counter()
        worst = {}
        for a in arts:
            for t in a.get("technologies") or []:
                inv[t["nom"]] += 1
                if PRIORITY_ORDER.get(a["priorite"], 9) < PRIORITY_ORDER.get(worst.get(t["nom"], "Faible"), 9):
                    worst[t["nom"]] = a["priorite"]
        if inv:
            techs = {t["nom"]: t for t in p.get("technologies") or []}
            doc.h2("Actifs du parc concernés")
            doc.table(["Technologie", "Exposition", "Criticité", "Éléments", "Priorité max."],
                      [[k, techs.get(k, {}).get("exposition", "n.c."), techs.get(k, {}).get("criticite", "n.c."), str(v), worst.get(k, "Faible")]
                       for k, v in inv.most_common(15)], widths=[0.34, 0.16, 0.14, 0.14, 0.22])
        cia = Counter(i["libelle"] for a in arts if a["priorite"] in ("Critique", "Élevée", "Modérée") for i in a.get("impacts") or [])
        if cia:
            doc.p("Types d'impact potentiels (éléments de priorité modérée ou plus) : " +
                  ", ".join(f"{k} ({v})" for k, v in cia.most_common()) + ".", "[Analyse]")
        doc.p("Les impacts sont des potentialités déduites du contenu des sources et du profil déclaré ; "
              "l'exposition réelle doit être confirmée par une vérification sur le SI (aucun scan n'est réalisé par l'outil).", "[Hypothèse]")

    # 13. Obligations et échéances
    doc.h1("12. Obligations potentielles à vérifier et échéances")
    today = date.today().isoformat()
    rows = []
    for m in data["matrix"]:
        if m["resultat"] not in ("probable", "indirect", "a_qualifier", "non_evaluable") or m["nature"] not in ("obligation_legale", "exigence_contractuelle"):
            continue
        future = [d for d in m["dates"] if d["date"] >= today]
        past = [d for d in m["dates"] if d["date"] < today]
        rows.append([m["nom"].split(" — ")[0], m["libelle"],
                     "; ".join(m["obligations_possibles"][:4]) or "—",
                     "; ".join(f"{d['date']} : {d['libelle']}" for d in future) or
                     ("En vigueur depuis " + past[-1]["date"] if past else "À vérifier"),
                     (m.get("note_statut") or "") + " Sources : " + ", ".join(m["references"][:2])])
    if rows:
        doc.table(["Texte", "Applicabilité", "Obligations possibles (à vérifier)", "Échéances", "Remarques / sources"],
                  rows, widths=[0.12, 0.16, 0.32, 0.18, 0.22])
        doc.p("Ces obligations sont « possibles » : elles dépendent de la qualification juridique de l'organisation. "
              "Les dates proviennent des textes officiels référencés et doivent être revérifiées.", "[À vérifier]")
    else:
        doc.empty("obligations potentielles")

    # 14. Opportunités
    doc.h1("13. Opportunités d'amélioration")
    opps = [a for a in arts if set(a.get("categories") or []) & {"technologie", "bonne_pratique"} and a["pertinence"] in ("forte", "moyenne")
            and a["priorite"] in ("Critique", "Élevée", "Modérée")]
    if not opps:
        doc.empty("opportunités d'amélioration")
    else:
        doc.ul([(f"[Recommandation] {a['priorite']}",
                 f"{a['titre']} ({a['source_nom']}) — {(a.get('actions') or [{'action': ''}])[0]['action']} "
                 f"Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.")
                for a in opps[:12]])

    # 15. Plan d'action
    doc.h1("14. Plan d'action priorisé")
    acts = sorted(data["actions"], key=lambda a: (PRIORITY_ORDER.get(a["priorite"], 9), a.get("echeance") or ""))
    if not acts:
        doc.empty("actions")
    else:
        doc.table(["#", "Priorité", "Constat / action proposée", "Responsable", "Échéance", "Effort", "Statut"],
                  [[str(a["id"]), a["priorite"],
                    f"{(a.get('article_titre') or a['constat'])[:140]} → {a['action'][:300]}",
                    a.get("responsable") or "—", a.get("echeance") or "—", EFFORT.get(a.get("effort"), "—"),
                    ACTION_STATUT.get(a["statut"], a["statut"])] for a in acts[:40]],
                  widths=[0.04, 0.09, 0.47, 0.14, 0.1, 0.07, 0.09])
        if len(acts) > 40:
            doc.p(f"{len(acts) - 40} actions supplémentaires sont consultables dans l'outil (page Plan d'action).")
        doc.h2("Détail des actions critiques et élevées")
        for a in [x for x in acts if x["priorite"] in ("Critique", "Élevée")][:10]:
            doc.card(f"Action n° {a['id']} — {a['priorite']}", a.get("article_url"), [
                ("Constat", a["constat"]), ("Risque / opportunité", a.get("risque") or ""), ("[Recommandation] Action", a["action"]),
                ("Justification", a.get("justification") or ""), ("Responsable suggéré", a.get("responsable") or ""),
                ("Échéance indicative", a.get("echeance") or ""), ("Effort estimé", EFFORT.get(a.get("effort"), "")),
                ("Bénéfice attendu", a.get("benefice") or ""), ("Preuves de réalisation", a.get("preuves") or ""),
                ("Statut", ACTION_STATUT.get(a["statut"], a["statut"]))])

    # 16. Limites
    doc.h1("15. Limites de la veille et informations restant à confirmer")
    lim = []
    for s in data["sources"]:
        if s["statut"] in ("bloque", "erreur"):
            lim.append(("Source non collectée", f"{s['nom']} — {STATUT_SOURCE.get(s['statut'])} : {s.get('derniere_erreur') or ''} "
                        f"{('Alternative : ' + s['alternative']) if s.get('alternative') else ''}"))
    no_cvss = sum(1 for a in arts for c in a.get("cves") or [] if c.get("cvss") is None)
    if no_cvss:
        lim.append(("CVSS", f"{no_cvss} mentions de CVE sans score CVSS disponible (non estimé ; limite de débit du NVD ou CVE non encore évaluée)."))
    declared = sum(1 for a in arts for f in a.get("facteurs") or [] if f["facteur"] == "_exploitation" and not f["verifie"]
                   and "signalée" in f["justification"])
    if declared:
        lim.append(("Exploitation", f"{declared} éléments signalent une exploitation active non confirmée par le catalogue KEV."))
    rules = sum(1 for a in arts if a.get("methode_resume") == "synthese_regles")
    if rules:
        lim.append(("Résumés", f"{rules} résumés sont des synthèses automatiques par règles de sources en langue étrangère (sans traduction) : consulter l'article original."))
    lim.append(("Classification", "Par règles et mots-clés : des faux positifs ou négatifs sont possibles ; l'analyste peut requalifier chaque élément (statut)."))
    lim.append(("Inventaire", "La pertinence dépend de l'exhaustivité de l'inventaire déclaré ; les versions affectées ne sont pas comparées automatiquement."))
    lim.append(("Réglementaire", "L'applicabilité est une orientation ; les textes français (Légifrance) ne sont pas collectés automatiquement ; statut de transposition NIS 2 à vérifier."))
    lim.append(("Normes", "Les textes des normes ISO ne sont ni consultés ni reproduits (accès payant) : seules les métadonnées publiques sont suivies."))
    if data["old_excluded"]:
        lim.append(("Fraîcheur", f"{data['old_excluded']} éléments anciens republiés dans les flux ont été exclus des résultats."))
    for h in hyps:
        lim.append(("[Hypothèse]", h))
    doc.ul(lim)

    # 17. Conclusion
    doc.h1("16. Conclusion")
    crit = prio.get("Critique", 0) + prio.get("Élevée", 0)
    doc.p(f"La veille de la période a permis d'identifier {crit} éléments de priorité critique ou élevée, "
          f"{len(reg)} évolutions réglementaires et {len(norm)} évolutions normatives, ainsi que {len(techno)} évolutions "
          f"technologiques pertinentes. {len(open_actions)} actions sont proposées ; les actions critiques doivent être "
          "validées et lancées sans délai, les autres intégrées au plan de traitement des risques. La prochaine itération "
          "devra confirmer les points « à vérifier » listés ci-dessus et mettre à jour le profil de l'organisation si "
          "nécessaire.", "[Analyse]")

    # 18. Annexes
    doc.pagebreak()
    doc.h1("17. Annexes — références consultées")
    annex = [a for a in arts if a["priorite"] != "Faible" or a["url"] in doc.cited]
    doc.p("Toutes les informations citées proviennent des URL ci-dessous ; la date de consultation correspond à la date "
          f"de collecte automatique. {len(arts) - len(annex)} éléments de priorité faible non cités sont consultables dans l'outil.")
    doc.table(["#", "Titre", "Source", "Publication", "Consultation", "URL"],
              [[str(i), a["titre"][:120], a["source_nom"], _d(a.get("publie_le")), _d(a["collecte_le"]), a["url"]]
               for i, a in enumerate(annex, 1)], widths=[0.04, 0.3, 0.14, 0.09, 0.09, 0.34])
    doc.h2("Références officielles du référentiel réglementaire et normatif")
    doc.table(["Texte / norme", "Référence", "Sources officielles", "Vérifié le"],
              [[m["nom"], m.get("reference") or "", ", ".join(m["references"]), m.get("verifie_le") or ""] for m in data["matrix"]],
              widths=[0.3, 0.2, 0.38, 0.12])
    return doc


def generate_report(storage: Storage, start: date, end: date, categories: list[str] | None = None,
                    formats: list[str] | None = None, trigger: str = "manuel", output_dir: str | Path | None = None,
                    profile: dict | None = None) -> dict:
    from veille.reports.markdown import render_markdown
    from veille.reports.pdf import render_pdf
    formats = formats or ["md", "pdf"]
    if start > end:
        raise ValueError("La date de début doit précéder la date de fin.")
    data = collect_data(storage, start, end, categories, profile=profile)
    doc = build_document(data)
    out = Path(output_dir) if output_dir else reports_dir()
    out.mkdir(parents=True, exist_ok=True)
    stem = f"rapport_veille_{start.isoformat()}_{end.isoformat()}_{utcnow().strftime('%Y%m%dT%H%M%S')}"
    result: dict = {"nb_articles": len(data["articles"])}
    if "md" in formats:
        md_path = out / f"{stem}.md"
        md_path.write_text(render_markdown(doc), encoding="utf-8")
        result["chemin_md"] = md_path
    if "pdf" in formats:
        pdf_path = out / f"{stem}.pdf"
        render_pdf(doc, pdf_path)
        result["chemin_pdf"] = pdf_path
    storage.add_report({"periode_debut": start.isoformat(), "periode_fin": end.isoformat(),
                        "perimetre": categories or list(PERIMETRES), "chemin_md": str(result.get("chemin_md") or ""),
                        "chemin_pdf": str(result.get("chemin_pdf") or ""), "declencheur": trigger,
                        "nb_articles": result["nb_articles"]})
    return result
