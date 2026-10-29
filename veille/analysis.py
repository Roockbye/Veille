"""Analyse d'un article : fiche structurée, pertinence, priorisation explicable et recommandations.

Principes :
- aucune donnée n'est inventée : CVSS et exploitation active ne sont retenus comme « vérifiés » que
  s'ils proviennent du NVD, de la CISA (KEV) ou de FIRST (EPSS) ; une mention dans l'article est
  signalée comme « déclarée par la source, à confirmer » ;
- chaque point de score est accompagné de sa justification ;
- une recommandation n'est jamais présentée comme une obligation légale.
"""
from __future__ import annotations

import re
from datetime import timedelta

from veille import ANALYZER_VERSION
from veille.classify import CATEGORIES, THEMES, classify, detect_impacts, find_terms, match_inventory, products_cited
from veille.collectors.enrichment import extract_cves
from veille.knowledge import APPLICABILITE, NATURES_JURIDIQUES, STATUTS, detect_referentiels, evaluate_applicability, get_referentiel
from veille.normalize import iso, parse_date, utcnow

PRIORITIES = ["Critique", "Élevée", "Modérée", "Faible", "À qualifier"]
PRIORITY_ORDER = {p: i for i, p in enumerate(["Critique", "Élevée", "À qualifier", "Modérée", "Faible"])}
DEADLINE_DAYS = {"Critique": 2, "Élevée": 7, "Modérée": 30, "Faible": 90, "À qualifier": 7}
URGENCY = {"Critique": "Immédiate (sous 48 h)", "Élevée": "Forte (sous 7 jours)", "Modérée": "Normale (sous 30 jours)",
           "Faible": "Faible (prochaine revue de veille)", "À qualifier": "Qualification requise (sous 7 jours)"}
IMPACT_LABELS = {"confidentialite": "Confidentialité", "integrite": "Intégrité", "disponibilite": "Disponibilité",
                 "conformite": "Conformité"}

EXPLOIT_DECLARED = ["activement exploitée", "activement exploitées", "exploitée activement", "exploitation active",
                    "actively exploited", "exploited in the wild", "under active exploitation", "being exploited",
                    "en cours d'exploitation", "exploitation in the wild", "exploited as a zero-day",
                    "exploited zero-day", "zero-day exploited", "est exploitée", "sont exploitées"]
POC_TERMS = ["preuve de concept", "proof of concept", "proof-of-concept", "PoC", "exploit public",
             "publicly available exploit", "exploit code", "code d'exploitation"]
SEVERITY_TERMS = ["critique", "critical", "sévérité élevée", "high severity", "CVSS 9", "CVSS 10"]
NOISE_FACTOR = -10

FR_MONTHS = {"janvier": 1, "février": 2, "fevrier": 2, "mars": 3, "avril": 4, "mai": 5, "juin": 6, "juillet": 7,
             "août": 8, "aout": 8, "septembre": 9, "octobre": 10, "novembre": 11, "décembre": 12, "decembre": 12}
EN_MONTHS = {m: i for i, m in enumerate(["january", "february", "march", "april", "may", "june", "july", "august",
                                         "september", "october", "november", "december"], 1)}
DATE_PATTERNS = [
    re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b"),
    re.compile(r"\b(\d{1,2})/(\d{1,2})/(\d{4})\b"),
    re.compile(r"\b(\d{1,2})(?:er)?\s+(" + "|".join(FR_MONTHS) + r")\s+(\d{4})\b", re.I),
    re.compile(r"\b(" + "|".join(EN_MONTHS) + r")\s+(\d{1,2}),?\s+(\d{4})\b", re.I),
    re.compile(r"\b(\d{1,2})\s+(" + "|".join(EN_MONTHS) + r")\s+(\d{4})\b", re.I),
]


def extract_dates(text: str) -> list[str]:
    found = []
    for i, rx in enumerate(DATE_PATTERNS):
        for m in rx.finditer(text or ""):
            try:
                if i == 0:
                    y, mo, d = int(m[1]), int(m[2]), int(m[3])
                elif i == 1:
                    d, mo, y = int(m[1]), int(m[2]), int(m[3])
                elif i == 2:
                    d, mo, y = int(m[1]), FR_MONTHS[m[2].lower()], int(m[3])
                elif i == 3:
                    mo, d, y = EN_MONTHS[m[1].lower()], int(m[2]), int(m[3])
                else:
                    d, mo, y = int(m[1]), EN_MONTHS[m[2].lower()], int(m[3])
                if 1990 <= y <= 2100 and 1 <= mo <= 12 and 1 <= d <= 31:
                    s = f"{y:04d}-{mo:02d}-{d:02d}"
                    if s not in found:
                        found.append(s)
            except (KeyError, ValueError):
                continue
    return sorted(found)[:10]


def _reg_nature(text: str, url: str) -> tuple[str, str]:
    """(nature de l'évolution, statut détecté) à partir d'indices explicites uniquement."""
    celex = re.search(r"CELEX:?\s*([0-9])(\d{4})([A-Z]{1,2})", f"{url} {text}")
    statut = "À vérifier sur la source officielle"
    if celex:
        sector, kind = celex.group(1), celex.group(3)
        if sector == "5" and kind in ("PC", "DC", "SC", "JC"):
            statut = "Projet (proposition ou document préparatoire de la Commission) — identifiant CELEX"
        elif sector == "3":
            statut = "Texte adopté et publié au Journal officiel de l'UE — identifiant CELEX"
        elif sector == "6":
            statut = "Jurisprudence de la Cour de justice de l'UE — identifiant CELEX"
    checks = [
        (["proposition", "proposal", "projet de loi", "projet de", "draft", "consultation publique",
          "public consultation", "call for evidence", "appel à contributions"], "Projet ou consultation"),
        (["entre en application", "entrée en application", "entry into application", "applicable from",
          "s'applique à compter", "entre en vigueur", "entrée en vigueur", "enters into force", "entry into force"],
         "Entrée en vigueur / en application"),
        (["publié au Journal officiel", "Journal officiel", "Official Journal", "published in the OJ"], "Publication officielle"),
        (["adopté", "adopts", "adopted", "adoption"], "Adoption"),
        (["lignes directrices", "guidelines", "orientations", "FAQ", "questions-réponses", "Q&A"],
         "Lignes directrices / interprétation"),
        (["sanction", "amende", "fine ", "fined", "fines ", "mise en demeure"], "Sanction ou décision d'une autorité"),
        (["recommandation", "recommendation", "référentiel", "guide"], "Recommandation ou référentiel d'une autorité"),
        (["abrogé", "abrogation", "repeal"], "Abrogation"),
    ]
    nature = "Évolution à qualifier"
    for terms, label in checks:
        if find_terms(text, terms):
            nature = label
            break
    if statut.startswith("À vérifier"):
        if nature == "Projet ou consultation":
            statut = "Projet (selon la source) — à confirmer"
        elif nature == "Entrée en vigueur / en application":
            statut = "Applicable ou en voie d'application (selon la source) — à confirmer"
        elif nature == "Publication officielle":
            statut = "Publié (selon la source) — à confirmer"
        elif nature == "Adoption":
            statut = "Adopté (selon la source) — à confirmer"
    return nature, statut


def _norm_type(refs: list[dict], text: str, source: dict) -> str:
    natures = [get_referentiel(r["id"]).get("nature_juridique") for r in refs if get_referentiel(r["id"])]
    for n in ("obligation_legale", "exigence_contractuelle", "norme", "referentiel", "recommandation"):
        if n in natures:
            return n
    if source.get("source_type") == "iso_opendata" or find_terms(text, ["ISO", "IEC", "norme", "FIPS"]):
        return "norme"
    if find_terms(text, ["framework", "référentiel", "CSF", "SLSA", "CIS Controls"]):
        return "referentiel"
    return "recommandation"


def analyze(article: dict, profile: dict, kev: dict[str, dict], cves_data: dict[str, dict]) -> dict:
    title = article["titre"]
    summary = article.get("resume_source") or ""
    text = f"{title}\n{summary}"
    src = {"categorie": article.get("source_categorie"), "sous_categorie": article.get("sous_categorie"),
           "source_type": article.get("source_type"), "type": article.get("source_type")}
    cls = classify(title, summary, src)
    cats = cls["categories"]
    donnees = article.get("donnees") or {}

    cves = extract_cves(text)
    kev_rows = [kev[c] for c in cves if c in kev]
    own_kev = (donnees.get("kev") or {}) if isinstance(donnees, dict) else {}
    # Les champs fournisseur/produit du KEV ne servent qu'aux fiches KEV elles-mêmes : un CVE cité
    # dans un autre avis peut concerner un composant tiers (ex. Chromium embarqué dans un logiciel industriel).
    kev_terms = [f"{own_kev.get('fournisseur') or ''} {own_kev.get('produit') or ''}".strip()] if own_kev else []
    inv = match_inventory(text, profile.get("technologies") or [], kev_terms)
    products = products_cited(text, [own_kev["produit"]] if own_kev.get("produit") else [])
    impacts = detect_impacts(text, cats)
    refs = detect_referentiels(text)
    themes = cls["themes"]
    org_themes = set(profile.get("themes_veille") or THEMES.keys())
    watched_themes = [t for t in themes if t in org_themes]

    # ---------------------------------------------------------------- données vérifiées
    scored = [(c, cves_data[c]) for c in cves if cves_data.get(c, {}).get("cvss_score") is not None]
    best_cvss = max(scored, key=lambda x: x[1]["cvss_score"]) if scored else None
    epss_vals = [(c, cves_data[c]["epss"]) for c in cves if cves_data.get(c, {}).get("epss") is not None]
    best_epss = max(epss_vals, key=lambda x: x[1]) if epss_vals else None
    declared_exploit = find_terms(text, EXPLOIT_DECLARED)
    poc = find_terms(text, POC_TERMS)
    sev_declared = find_terms(text, SEVERITY_TERMS)

    exploitation = {"statut": "aucune_information", "libelle": "Aucune information d'exploitation", "verifie": False}
    if kev_rows:
        exploitation = {"statut": "active_confirmee", "verifie": True,
                        "libelle": "Exploitation active confirmée (catalogue CISA KEV)",
                        "details": [{"cve": k["cve_id"], "ajoute_le": k.get("ajoute_le"),
                                     "rancongiciel": k.get("rancongiciel"), "echeance_cisa": k.get("echeance_cisa")}
                                    for k in kev_rows]}
    elif declared_exploit:
        exploitation = {"statut": "signalee_source", "verifie": False,
                        "libelle": "Exploitation active signalée par la source — non confirmée par le KEV"}
    elif poc:
        exploitation = {"statut": "poc_signale", "verifie": False, "libelle": "Preuve de concept publique signalée par la source"}

    # ---------------------------------------------------------------- pertinence
    applicabilities = []
    for r in refs:
        ref = get_referentiel(r["id"])
        if ref:
            ev = evaluate_applicability(ref, profile)
            applicabilities.append({**r, **ev})
    inventory_empty = not profile.get("technologies")
    # Pour une vulnérabilité, la pertinence se mesure au parc, pas aux thèmes technologiques évoqués
    vuln_centric = cats[0] == "vulnerabilite" and bool(products or cves)
    pert_reasons = []
    if cats == ["non_pertinent"]:
        pertinence = "non_pertinent"
        pert_reasons.append("Aucun indicateur de catégorie de veille détecté (bruit, promotion ou hors périmètre).")
    elif inv:
        pertinence = "forte"
        pert_reasons.append("Technologie(s) du parc citée(s) : " + ", ".join(m["nom"] for m in inv) + ".")
    elif any(a["resultat"] == "probable" for a in applicabilities):
        pertinence = "forte"
        pert_reasons.append("Texte ou référentiel dont l'applicabilité est probable : " +
                            ", ".join(a["nom"] for a in applicabilities if a["resultat"] == "probable") + ".")
    elif any(a["resultat"] == "indirect" for a in applicabilities) or (watched_themes and not vuln_centric):
        pertinence = "moyenne"
        if watched_themes:
            pert_reasons.append("Thème surveillé : " + ", ".join(THEMES[t][0] for t in watched_themes) + ".")
        if any(a["resultat"] == "indirect" for a in applicabilities):
            pert_reasons.append("Impact indirect possible via les clients ou les contrats.")
    elif inventory_empty and (products or cves):
        pertinence = "a_qualifier"
        pert_reasons.append("Inventaire technique non renseigné : présence des produits cités impossible à établir.")
    elif any(a["resultat"] in ("a_qualifier", "non_evaluable") for a in applicabilities):
        pertinence = "a_qualifier"
        pert_reasons.append("Applicabilité du texte à qualifier.")
    elif set(cats) & {"menace", "incident", "bonne_pratique"} and not products:
        pertinence = "moyenne"
        pert_reasons.append("Menace ou pratique générique, potentiellement transposable au SI de l'organisation.")
    else:
        pertinence = "faible"
        if products:
            pert_reasons.append("Produits cités absents de l'inventaire déclaré : " + ", ".join(products[:5]) + ".")
        else:
            pert_reasons.append("Pas de lien établi avec le contexte de l'organisation.")

    # ---------------------------------------------------------------- facteurs de score
    factors: list[dict] = []

    def add(facteur, points, justification, verifie, source=None):
        factors.append({"facteur": facteur, "points": points, "justification": justification,
                        "verifie": verifie, "source": source})

    if best_cvss:
        c, d = best_cvss
        s = d["cvss_score"]
        pts = 30 if s >= 9 else 20 if s >= 7 else 10 if s >= 4 else 3
        add("Gravité technique", pts, f"CVSS {d.get('cvss_version')} {s} ({d.get('severite') or 'n.c.'}) pour {c}.",
            True, d.get("cvss_source"))
    elif sev_declared and ("vulnerabilite" in cats or "menace" in cats):
        add("Gravité technique", 12, f"Gravité « {sev_declared[0]} » indiquée par la source ; aucun score CVSS vérifié.",
            False, article.get("source_nom"))
    if kev_rows:
        add("Exploitation active", 30, "CVE présente(s) dans le catalogue CISA KEV : " +
            ", ".join(k["cve_id"] for k in kev_rows) + ".", True, "CISA KEV")
        if any((k.get("rancongiciel") or "").lower() == "known" for k in kev_rows):
            add("Exploitation active", 5, "Utilisation connue dans des campagnes de rançongiciel (CISA).", True, "CISA KEV")
    elif declared_exploit:
        add("Exploitation active", 18, f"La source signale une exploitation (« {declared_exploit[0]} ») ; "
            "non confirmée par le catalogue KEV.", False, article.get("source_nom"))
    elif poc:
        add("Exploitation active", 8, "Preuve de concept ou code d'exploitation public signalé.", False, article.get("source_nom"))
    if best_epss and best_epss[1] >= 0.1:
        add("Probabilité d'exploitation", 10 if best_epss[1] >= 0.5 else 5,
            f"EPSS {best_epss[1]:.2f} pour {best_epss[0]} (probabilité d'exploitation sous 30 jours).", True, "FIRST EPSS")
    if inv:
        add("Présence dans le parc", 25, "Technologie(s) déclarée(s) dans l'inventaire : " +
            ", ".join(m["nom"] for m in inv) + ".", True, "Inventaire de l'organisation (déclaratif)")
        if any(m["versions_citees"] for m in inv):
            add("Présence dans le parc", 5, "Version(s) du parc citée(s) : " +
                ", ".join(v for m in inv for v in m["versions_citees"]) + ".", True, "Inventaire de l'organisation")
        expo = {m["exposition"] for m in inv}
        if "internet" in expo:
            add("Exposition", 15, "Au moins une technologie concernée est exposée sur Internet.", True, "Inventaire de l'organisation")
        elif "dmz" in expo:
            add("Exposition", 8, "Technologie concernée exposée en DMZ / aux partenaires.", True, "Inventaire de l'organisation")
        crit = max((m["criticite"] for m in inv), key=lambda c: ["faible", "moyenne", "elevee", "critique"].index(c)
                   if c in ("faible", "moyenne", "elevee", "critique") else 1)
        pts = {"critique": 10, "elevee": 6, "moyenne": 3}.get(crit, 0)
        if pts:
            add("Impact sur les activités", pts, f"Criticité métier déclarée de l'actif concerné : {crit}.", True,
                "Inventaire de l'organisation")
    if article.get("source_id") == "certfr-alertes":
        add("Urgence", 10, "Alerte CERT-FR : l'autorité recommande une action rapide.", True, "CERT-FR")
    for a in applicabilities:
        if a["resultat"] == "probable":
            pts = 30 if a["nature"] == "obligation_legale" else 15
            add("Importance réglementaire / normative", pts, f"{a['nom']} : {a['libelle']} ({a['nature_libelle']}). {a['motif']}",
                False, "Référentiel de configuration + profil de l'organisation")
        elif a["resultat"] == "indirect":
            add("Importance réglementaire / normative", 15, f"{a['nom']} : {a['libelle']}. {a['motif']}", False,
                "Référentiel de configuration + profil de l'organisation")
        elif a["resultat"] in ("a_qualifier", "non_evaluable"):
            add("Importance réglementaire / normative", 8, f"{a['nom']} : {a['libelle']}. {a['motif']}", False,
                "Référentiel de configuration + profil de l'organisation")
    if "technologie" in cats and watched_themes:
        add("Thème surveillé", 10, "Thème(s) inscrit(s) au périmètre de veille : " +
            ", ".join(THEMES[t][0] for t in watched_themes) + ".", True, "Profil de l'organisation")
    if pertinence == "moyenne" and set(cats) & {"menace", "incident"} and impacts:
        add("Menace transposable", 8, "Menace ou incident générique avec impact " +
            ", ".join(IMPACT_LABELS[i] for i in impacts) + ".", False, article.get("source_nom"))
    evt = donnees.get("evenement")
    if evt == "changement":
        add("Évolution normative", 20, "Changement de version ou de stade détecté dans les métadonnées officielles de l'ISO.",
            True, "ISO Open Data")
    elif evt == "etat_initial":
        docs = donnees.get("documents") or []
        if any(d.get("remplacee_par") and d.get("stade") == "6060" for d in docs) or any(d.get("stade") == "9092" for d in docs) \
                or any(str(d.get("stade", "")).startswith(("2", "3", "4", "5")) for d in docs):
            add("Évolution normative", 10, "Révision ou nouveau projet enregistré par l'ISO pour cette norme.", True, "ISO Open Data")
    pub_dt = parse_date(article.get("publie_le"))
    age_days = (utcnow() - pub_dt).days if pub_dt and article.get("source_type") != "iso_opendata" else None
    if age_days is not None and age_days > 365:
        add("Ancienneté", -25, f"Information publiée il y a {age_days} jours : vérifier si elle a déjà été traitée.", True, "Date de publication de la source")
    elif age_days is not None and age_days > 90:
        add("Ancienneté", -15, f"Information publiée il y a {age_days} jours : probablement déjà connue.", True, "Date de publication de la source")
    if article.get("source_confiance") == "faible":
        add("Fiabilité de la source", -5, "Source à fiabilité faible : information à recouper.", True, "Catalogue des sources")
    if cls["bruit"]:
        add("Bruit", NOISE_FACTOR, "Contenu promotionnel ou événementiel (" + ", ".join(cls["bruit"]) + ").", True, None)

    score = max(0, sum(f["points"] for f in factors))
    max_cap_reasons = []

    # ---------------------------------------------------------------- niveau de priorité
    verified_severity = bool(kev_rows) or (best_cvss is not None and best_cvss[1]["cvss_score"] >= 9) or \
        article.get("source_id") == "certfr-alertes"
    if pertinence == "non_pertinent":
        priorite = "Faible"
    elif pertinence == "a_qualifier" and score < 50:
        priorite = "À qualifier"
    elif score >= 75 and inv and verified_severity:
        priorite = "Critique"
    elif score >= 50:
        priorite = "Élevée"
        if score >= 75:
            max_cap_reasons.append("Plafonné à « Élevée » : le niveau « Critique » exige une technologie du parc "
                                   "concernée ET une gravité ou une exploitation vérifiée (KEV, CVSS ≥ 9, alerte CERT-FR).")
    elif score >= 25:
        priorite = "Modérée"
    else:
        priorite = "Faible"
    if pertinence == "faible" and priorite in ("Critique", "Élevée"):
        priorite = "Modérée"
        max_cap_reasons.append("Pertinence faible (aucun lien établi avec le parc ou le profil) : niveau plafonné à « Modérée » ; "
                               "vérifier que l'inventaire est complet.")
    if age_days is not None and age_days > 90 and priorite == "Critique":
        priorite = "Élevée"
        max_cap_reasons.append("Information de plus de 90 jours : niveau plafonné à « Élevée ».")
    if age_days is not None and age_days > 365 and priorite in ("Critique", "Élevée"):
        priorite = "Modérée"
        max_cap_reasons.append("Information de plus d'un an : niveau plafonné à « Modérée ».")
    if priorite == "Critique" and set(cats) <= {"reglementaire", "normative"}:
        priorite = "Élevée"
        max_cap_reasons.append("Évolution réglementaire/normative : niveau plafonné à « Élevée ».")

    justification = (f"Score {score} = " + " + ".join(f"{f['points']} ({f['facteur']})" for f in factors)
                     if factors else "Aucun facteur de priorisation détecté.")
    justification += f" Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : {pertinence}."
    if max_cap_reasons:
        justification += " " + " ".join(max_cap_reasons)

    deadline = (utcnow() + timedelta(days=DEADLINE_DAYS[priorite])).date().isoformat()

    # ---------------------------------------------------------------- recommandations
    maturity = profile.get("maturite_cyber") or "reproductible"
    actions = _recommendations(cats, inv, products, kev_rows, declared_exploit, applicabilities, watched_themes,
                               text, maturity, donnees)

    # ---------------------------------------------------------------- confiance et points à vérifier
    conf = {"elevee": 2, "moyenne": 1, "faible": 0}.get(article.get("source_confiance") or "moyenne", 1)
    if best_cvss or kev_rows:
        conf += 1
    if len(summary) < 80:
        conf -= 1
    if cats == ["non_pertinent"]:
        conf -= 0.5
    confiance = "elevee" if conf >= 2.5 else "moyenne" if conf >= 1.5 else "faible"

    to_verify = []
    for c in cves:
        d = cves_data.get(c)
        if not d or d.get("cvss_score") is None:
            st = (d or {}).get("nvd_statut", "non_interroge")
            reason = {"introuvable": "absente du NVD", "erreur": "NVD indisponible lors de l'interrogation",
                      "ok": "pas encore évaluée par le NVD"}.get(st, "NVD non encore interrogé")
            to_verify.append(f"Score CVSS de {c} non disponible ({reason}) : ne pas l'estimer, consulter l'avis éditeur.")
    if declared_exploit and not kev_rows:
        to_verify.append("Exploitation active signalée par la source mais non confirmée par le catalogue CISA KEV.")
    for m in inv:
        if not m["versions_citees"]:
            vp = ", ".join(m["versions_parc"]) or "non renseignées"
            to_verify.append(f"Versions affectées de {m['nom']} à comparer avec les versions du parc ({vp}).")
    missing_products = [p for p in products if not any(p.lower() in " ".join(x["mots"]).lower() for x in inv)]
    if missing_products and not inv and ("vulnerabilite" in cats or "menace" in cats):
        to_verify.append("Présence éventuelle dans le parc à confirmer : " + ", ".join(missing_products[:6]) + ".")
    if article.get("source_confiance") in ("moyenne", "faible"):
        to_verify.append("Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).")
    if "reglementaire" in cats:
        to_verify.append("Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).")
    if len(summary) < 80:
        to_verify.append("Résumé de la source très court : analyse fondée essentiellement sur le titre, consulter l'article.")

    # ---------------------------------------------------------------- fiches spécifiques
    reg = None
    if "reglementaire" in cats:
        nature, statut = _reg_nature(text, article.get("url", ""))
        textes = []
        for a in applicabilities:
            ref = get_referentiel(a["id"]) or {}
            if ref.get("type_veille") != "reglementaire" and ref.get("nature_juridique") != "obligation_legale":
                continue
            textes.append({
                "id": a["id"], "nom": a["nom"], "reference": ref.get("reference"),
                "nature_juridique": NATURES_JURIDIQUES.get(ref.get("nature_juridique")),
                "statut_referentiel": STATUTS.get(ref.get("statut"), "À vérifier"),
                "note_statut": ref.get("note_statut"),
                "dates_referentiel": ref.get("dates") or [], "sources_officielles": ref.get("references") or [],
                "concernes": ref.get("concernes"), "obligations_possibles": ref.get("obligations_possibles") or [],
                "demarches": ref.get("demarches_applicabilite") or [],
                "applicabilite": a["libelle"], "applicabilite_code": a["resultat"], "motif": a["motif"],
            })
        reg = {
            "textes": textes,
            "nature_evolution": nature,
            "statut_detecte": statut,
            "dates_mentionnees": [{"date": d, "source": article.get("url")} for d in extract_dates(text)],
            "impact": ("; ".join(f"{t['nom']} — {t['applicabilite']}" for t in textes)
                       or "Aucun texte du référentiel identifié : impact à qualifier manuellement."),
            "avertissement": "Orientation fondée sur le profil déclaré : l'applicabilité doit être confirmée par le juriste ou le DPO.",
        }
    norm = None
    if "normative" in cats:
        ntype = _norm_type(refs, text, src)
        norm = {
            "type": ntype,
            "type_libelle": NATURES_JURIDIQUES.get(ntype, ntype),
            "referentiels": [{"id": a["id"], "nom": a["nom"], "nature": a["nature_libelle"], "applicabilite": a["libelle"]}
                             for a in applicabilities],
            "evenement": donnees.get("evenement"),
            "changements": donnees.get("changements"),
            "avertissement": ("Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, "
                              "sauf si un texte, un contrat ou une certification visée la rend exigible."
                              if ntype != "obligation_legale" else "Texte contraignant : vérifier le champ d'application."),
        }

    # ---------------------------------------------------------------- résumé en français
    resume, methode = _summary_fr(article, cats, cves, products, inv, exploitation, themes, best_cvss)

    keywords = []
    for c in cats:
        keywords += [k for k in cls["declencheurs"].get(c, []) if not k.startswith(("catégorie", "type de source"))]
    keywords += [r["nom"].split(" — ")[0] for r in refs]
    keywords = list(dict.fromkeys(keywords))[:12]

    return {
        "categories": cats,
        "categorie_principale": cats[0],
        "mots_cles": keywords,
        "technologies": [{"nom": m["nom"], "exposition": m["exposition"], "criticite": m["criticite"],
                          "versions_citees": m["versions_citees"], "versions_parc": m["versions_parc"]} for m in inv],
        "produits_cites": products,
        "cves": [{"id": c, "cvss": (cves_data.get(c) or {}).get("cvss_score"),
                  "cvss_version": (cves_data.get(c) or {}).get("cvss_version"),
                  "severite": (cves_data.get(c) or {}).get("severite"),
                  "cvss_source": (cves_data.get(c) or {}).get("cvss_source"),
                  "epss": (cves_data.get(c) or {}).get("epss"), "kev": c in kev} for c in cves[:30]],
        "impacts": [{"type": k, "libelle": IMPACT_LABELS[k], "indices": v} for k, v in impacts.items()],
        "pertinence": pertinence,
        "pertinence_motifs": pert_reasons,
        "priorite": priorite,
        "score": score,
        "facteurs": factors + [{"facteur": "_exploitation", "points": 0, "justification": exploitation["libelle"],
                                "verifie": exploitation["verifie"], "source": exploitation.get("details")},
                               {"facteur": "_justification", "points": 0, "justification": justification,
                                "verifie": True, "source": None}],
        "actions": actions,
        "echeance": deadline,
        "urgence": URGENCY[priorite],
        "confiance": confiance,
        "a_verifier": to_verify,
        "resume_fr": resume,
        "methode_resume": methode,
        "reglementaire": reg,
        "normatif": norm,
        "version_analyse": ANALYZER_VERSION,
        "analyse_le": iso(utcnow()),
        "themes": themes,
    }


def _summary_fr(article, cats, cves, products, inv, exploitation, themes, best_cvss) -> tuple[str, str]:
    summary = article.get("resume_source") or ""
    if (article.get("langue") or "").startswith("fr") and len(summary) >= 40:
        s = summary.replace("\n", " ")
        return (s[:700].rsplit(" ", 1)[0] + " […]" if len(s) > 700 else s), "extrait_source"
    pub = parse_date(article.get("publie_le"))
    parts = [f"{CATEGORIES[cats[0]]} — publication de {article.get('source_nom') or article.get('source_id')}"
             + (f" du {pub.date().isoformat()}" if pub else " (date de publication non fournie)") + "."]
    if cves:
        parts.append(f"CVE citées : {', '.join(cves[:8])}{' …' if len(cves) > 8 else ''}.")
    if best_cvss:
        parts.append(f"Score CVSS le plus élevé (NVD) : {best_cvss[1]['cvss_score']} ({best_cvss[0]}).")
    if products:
        parts.append(f"Produits cités : {', '.join(products[:8])}.")
    if inv:
        parts.append(f"Technologies du parc concernées : {', '.join(m['nom'] for m in inv)}.")
    if exploitation["statut"] != "aucune_information":
        parts.append(exploitation["libelle"] + ".")
    if themes:
        parts.append("Thèmes : " + ", ".join(THEMES[t][0] for t in themes[:3]) + ".")
    if summary:
        ext = summary.replace("\n", " ")
        ext = ext[:350].rsplit(" ", 1)[0] + " […]" if len(ext) > 350 else ext
        parts.append(f"Extrait original ({article.get('langue') or 'langue n.c.'}) : « {ext} »")
    parts.append("(Synthèse automatique par règles, sans traduction : se référer à l'article original.)")
    return " ".join(parts), "synthese_regles"


RESPONSABLES = {
    "vulnerabilite": "Équipe infrastructure / exploitation (pilotage RSSI)",
    "menace": "RSSI / équipe de supervision (SOC)",
    "incident": "RSSI",
    "reglementaire": "Juriste / DPO, avec le RSSI",
    "normative": "RSSI / responsable du SMSI",
    "technologie": "DSI / RSSI (étude d'opportunité)",
    "bonne_pratique": "RSSI / administrateurs systèmes",
    "non_pertinent": "—",
}


def _recommendations(cats, inv, products, kev_rows, declared_exploit, applicabilities, watched_themes, text,
                     maturity, donnees) -> list[dict]:
    """Recommandations proportionnées (aucune action automatique sur le SI)."""
    recs = []
    low_maturity = maturity in ("initiale", "reproductible")
    names = ", ".join(m["nom"] for m in inv)
    if "vulnerabilite" in cats:
        if inv:
            recs.append({"type": "Vérification de l'exposition", "action": f"Vérifier la présence et les versions de {names} concernées par l'avis (inventaire, outil de gestion de parc)."})
            recs.append({"type": "Mise à jour", "action": "Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire)."})
            if any(m["exposition"] in ("internet", "dmz") for m in inv):
                recs.append({"type": "Mesure compensatoire", "action": "En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur."})
            if kev_rows or declared_exploit:
                recs.append({"type": "Vérification de compromission", "action": "Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés."})
        elif products:
            recs.append({"type": "Vérification de l'exposition", "action": f"Vérifier si {', '.join(products[:4])} est utilisé dans le SI (inventaire potentiellement incomplet) ; sinon, classer l'information comme non applicable."})
    if "menace" in cats:
        recs.append({"type": "Contrôle de configuration", "action": "Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits."})
        if find_terms(text, ["hameçonnage", "phishing", "ingénierie sociale", "social engineering", "arnaque", "scam"]):
            recs.append({"type": "Sensibilisation", "action": "Informer les utilisateurs du mode opératoire décrit (message de sensibilisation ciblé)."})
        if find_terms(text, ["rançongiciel", "ransomware", "wiper"]):
            recs.append({"type": "Contrôle de configuration", "action": "Vérifier l'existence de sauvegardes hors ligne et tester une restauration."})
    if "incident" in cats:
        recs.append({"type": "Étude complémentaire", "action": "Analyser le retour d'expérience et vérifier si le scénario est transposable (fournisseurs, technologies, processus)."})
    for a in applicabilities:
        if a["resultat"] in ("probable", "indirect", "a_qualifier", "non_evaluable") and ("reglementaire" in cats or "normative" in cats):
            if a["nature"] == "obligation_legale":
                recs.append({"type": "Analyse de conformité", "action": f"Qualifier l'applicabilité de « {a['nom']} » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences."})
            else:
                recs.append({"type": "Analyse de conformité", "action": f"Évaluer l'impact de l'évolution de « {a['nom']} » ({a['nature_libelle'].lower()}) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels."})
    if "normative" in cats and donnees.get("evenement") == "changement":
        recs.append({"type": "Étude complémentaire", "action": "Consulter la page officielle de la norme pour confirmer l'évolution et planifier, le cas échéant, la transition (documentation, audit)."})
    if "reglementaire" in cats and not applicabilities:
        recs.append({"type": "Étude complémentaire", "action": "Identifier le texte concerné et qualifier son applicabilité (secteur, taille, rôle de l'organisation)."})
    if "technologie" in cats and watched_themes:
        recs.append({"type": "Étude complémentaire", "action": "Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée."})
    if "bonne_pratique" in cats:
        recs.append({"type": "Contrôle de configuration", "action": "Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration."})
    if not recs and cats != ["non_pertinent"]:
        recs.append({"type": "Étude complémentaire", "action": "Prendre connaissance de l'information ; aucune action spécifique identifiée à ce stade."})
    if low_maturity and recs:
        recs.append({"type": "Proportionnalité", "action": "Maturité cyber déclarée faible : privilégier les mesures simples et à fort effet (correctifs, MFA, sauvegardes) avant les projets structurants."})
    for r in recs:
        r["responsable"] = RESPONSABLES.get(cats[0], "RSSI")
    # dédoublonnage en conservant l'ordre
    seen, out = set(), []
    for r in recs:
        if r["action"] not in seen:
            seen.add(r["action"])
            out.append(r)
    return out
