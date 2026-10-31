import pandas as pd
import streamlit as st

from ui import get_storage, page_header, profile, show_hypotheses
from veille.classify import THEMES
from veille.organisation import (CATEGORIES_TECH, CRITICITES, DONNEES, EXPOSITIONS, FREQUENCES, GESTIONS, MATURITES, ROLES,
                                 ROLES_RESPONSABLES, SECTEURS, TAILLES, has_profile, load_demo_profile, missing_fields,
                                 save_profile)

CRITERES = {"confidentialite": "Confidentialité", "integrite": "Intégrité", "disponibilite": "Disponibilité",
            "tracabilite": "Traçabilité"}


def _lines(text: str) -> list[str]:
    return [l.strip()[:600] for l in (text or "").splitlines() if l.strip()][:50]


def _csv(v) -> list[str]:
    return [x.strip()[:100] for x in str(v or "").split(",") if x.strip()][:30]


def _rows(df: pd.DataFrame, keys: list[str], required: str) -> list[dict]:
    out = []
    for _, r in df.iterrows():
        if str(r.get(required) or "").strip() and str(r.get(required)) != "nan":
            out.append({k: ("" if r.get(k) is None or str(r.get(k)) == "nan" else str(r.get(k)).strip()[:800]) for k in keys})
    return out


def render():
    storage = get_storage()
    page_header("Configuration de l'organisation", "Contexte de l'organisation étudiée : base de l'évaluation de pertinence et d'applicabilité")
    p = profile()
    if not has_profile():
        st.warning("Aucun profil enregistré : le formulaire est prérempli avec le profil d'exemple (AéroStar, organisation fictive). "
                   "Vérifiez-le puis enregistrez-le.")
    miss = missing_fields(p)
    if miss:
        st.info("Informations manquantes : " + ", ".join(miss) + ". Des hypothèses explicites sont utilisées en attendant.")
    show_hypotheses(p)

    with st.form("profil"):
        st.subheader("Identité et contexte")
        c = st.columns(3)
        nom = c[0].text_input("Nom de l'organisation *", p.get("nom") or "", max_chars=200)
        sk = [""] + list(SECTEURS)
        secteur = c[1].selectbox("Secteur principal", sk, index=sk.index(p.get("secteur") or ""), format_func=lambda k: SECTEURS.get(k, "— non renseigné —"))
        sec2 = c[2].multiselect("Secteurs secondaires / filière", list(SECTEURS), default=p.get("secteurs_secondaires"), format_func=SECTEURS.get, placeholder="Aucun")
        c = st.columns(4)
        tk = [""] + list(TAILLES)
        taille = c[0].selectbox("Taille", tk, index=tk.index(p.get("taille") or ""), format_func=lambda k: TAILLES.get(k, "— non renseignée —"))
        effectif = c[1].number_input("Effectif", 0, 10_000_000, int(p.get("effectif") or 0))
        ca = c[2].number_input("Chiffre d'affaires (M€)", 0.0, 1e7, float(p.get("chiffre_affaires_meur") or 0.0))
        mk = [""] + list(MATURITES)
        mat = c[3].selectbox("Maturité cyber", mk, index=mk.index(p.get("maturite_cyber") or ""), format_func=lambda k: MATURITES.get(k, "— non renseignée —"))
        roles = st.multiselect("Rôles de l'organisation (déterminants pour l'applicabilité)", list(ROLES), default=p.get("roles"), format_func=ROLES.get, placeholder="Aucun")
        donnees = st.multiselect("Données traitées", list(DONNEES), default=p.get("donnees_traitees"), format_func=DONNEES.get, placeholder="Aucune")
        activites = st.text_area("Activités principales (une par ligne)", "\n".join(p.get("activites") or []))
        c = st.columns(2)
        contraintes = c[0].text_area("Contraintes (budget, ressources, métier, calendrier — une par ligne)", "\n".join(p.get("contraintes_securite") or []), height=160)
        risques = c[1].text_area("Constats et risques connus (un par ligne)", "\n".join(p.get("risques_connus") or []), height=160)

        st.subheader("Besoins de sécurité")
        bdf = pd.DataFrame(p.get("besoins_securite") or [{"besoin": "", "critere": "confidentialite", "niveau": ""}])
        besoins = st.data_editor(bdf, num_rows="dynamic", width="stretch", key="besoins", column_config={
            "besoin": st.column_config.TextColumn("Besoin", width="large"),
            "critere": st.column_config.SelectboxColumn("Critère", options=list(CRITERES)),
            "niveau": st.column_config.TextColumn("Exigence cible")})

        st.subheader("Scénarios redoutés")
        st.caption("Les éléments de veille qui contiennent un des mots-clés (séparés par des virgules) sont rattachés au scénario.")
        sdf = pd.DataFrame([{"nom": x["nom"], "description": x.get("description", ""), "mots_cles": ", ".join(x.get("mots_cles") or [])}
                            for x in p.get("scenarios_redoutes") or []] or [{"nom": "", "description": "", "mots_cles": ""}])
        scen = st.data_editor(sdf, num_rows="dynamic", width="stretch", key="scen", column_config={
            "nom": "Scénario", "description": st.column_config.TextColumn("Description", width="large"), "mots_cles": "Mots-clés"})

        st.subheader("Inventaire des technologies")
        st.caption("Mots-clés précis (produit plutôt qu'éditeur) ; « expressions à exclure » évite les homonymes (ex. « Veeam Backup for Microsoft 365»). Exposition et criticité pondèrent la priorité ; « gestion » oriente le "
                   "responsable des actions ; « marque inconnue » signale un modèle non documenté (présence à confirmer).")
        tdf = pd.DataFrame([{"nom": t["nom"], "categorie": t.get("categorie", "autre"), "versions": ", ".join(t.get("versions") or []),
                             "mots_cles": ", ".join(t.get("mots_cles") or []), "exclusions": ", ".join(t.get("exclusions") or []),
                             "exposition": t.get("exposition", "inconnue"),
                             "criticite": t.get("criticite", "moyenne"), "gestion": t.get("gestion", "interne"),
                             "marque_inconnue": bool(t.get("marque_inconnue"))} for t in p.get("technologies") or []]
                           or [{"nom": "", "categorie": "autre", "versions": "", "mots_cles": "", "exclusions": "", "exposition": "inconnue",
                                "criticite": "moyenne", "gestion": "interne", "marque_inconnue": False}])
        techs = st.data_editor(tdf, num_rows="dynamic", width="stretch", key="techs", column_config={
            "nom": st.column_config.TextColumn("Technologie", required=True),
            "categorie": st.column_config.SelectboxColumn("Catégorie", options=list(CATEGORIES_TECH)),
            "versions": "Versions", "mots_cles": "Mots-clés de détection", "exclusions": "Expressions à exclure",
            "exposition": st.column_config.SelectboxColumn("Exposition", options=list(EXPOSITIONS)),
            "criticite": st.column_config.SelectboxColumn("Criticité", options=list(CRITICITES)),
            "gestion": st.column_config.SelectboxColumn("Gestion", options=list(GESTIONS)),
            "marque_inconnue": st.column_config.CheckboxColumn("Marque inconnue")})

        st.subheader("Exigences réglementaires, normatives et contractuelles")
        st.caption("Identifiant reliant l'exigence au référentiel : rgpd, nis2, aircyber, en9100, iso27001, double_usage, part_is… "
                   "Statut : identifiee, a_confirmer, ou cible (référentiel volontaire visé, non exigé).")
        edf = pd.DataFrame(p.get("exigences") or [{"id": "", "nom": "", "type": "legale", "statut": "a_confirmer", "commentaire": ""}])
        exig = st.data_editor(edf, num_rows="dynamic", width="stretch", key="exig", column_config={
            "type": st.column_config.SelectboxColumn(options=["legale", "contractuelle", "normative"]),
            "statut": st.column_config.SelectboxColumn(options=["identifiee", "a_confirmer", "cible"])})

        st.subheader("Échéances et parties prenantes")
        c = st.columns(2)
        ech = c[0].data_editor(pd.DataFrame(p.get("echeances") or [{"date": "", "libelle": "", "origine": ""}]), num_rows="dynamic",
                               width="stretch", key="ech", column_config={"date": st.column_config.TextColumn("Date (AAAA-MM-JJ ou AAAA)"),
                                                                          "libelle": "Échéance", "origine": "Origine"})
        pp = c[1].data_editor(pd.DataFrame(p.get("parties_prenantes") or [{"nom": "", "attentes": ""}]), num_rows="dynamic",
                              width="stretch", key="pp", column_config={"nom": "Partie prenante", "attentes": "Attentes de sécurité"})

        st.subheader("Responsables des actions")
        resp = {}
        cols = st.columns(len(ROLES_RESPONSABLES))
        for col, (k, lab) in zip(cols, ROLES_RESPONSABLES.items()):
            resp[k] = col.text_input(lab, (p.get("responsables") or {}).get(k, ""), max_chars=120, key=f"resp_{k}")

        st.subheader("Périmètre de veille")
        themes = st.multiselect("Thèmes technologiques à surveiller", list(THEMES), default=p.get("themes_veille") or list(THEMES),
                                format_func=lambda k: THEMES[k][0], placeholder="Aucun")
        c = st.columns(3)
        fk = list(FREQUENCES)
        fc = c[0].selectbox("Fréquence de collecte souhaitée", fk, index=fk.index(p.get("frequence_collecte") or "quotidienne"), format_func=FREQUENCES.get)
        fr = c[1].selectbox("Fréquence des rapports", ["hebdomadaire", "mensuelle"], index=0 if (p.get("frequence_rapport") or "hebdomadaire") == "hebdomadaire" else 1)
        fictive = c[2].checkbox("Organisation fictive (cas d'étude)", bool(p.get("fictive")))
        st.caption("La planification effective se règle dans la page « Automatisation et journaux ».")
        if st.form_submit_button("💾 Enregistrer le profil", type="primary"):
            tech_list = []
            for _, r in techs.iterrows():
                if str(r.get("nom") or "").strip() and str(r.get("nom")) != "nan":
                    t = {"nom": str(r["nom"]).strip()[:120], "categorie": r.get("categorie") or "autre", "versions": _csv(r.get("versions")),
                         "mots_cles": _csv(r.get("mots_cles")), "exclusions": _csv(r.get("exclusions")),
                         "exposition": r.get("exposition") or "inconnue",
                         "criticite": r.get("criticite") or "moyenne", "gestion": r.get("gestion") or "interne"}
                    if bool(r.get("marque_inconnue")):
                        t["marque_inconnue"] = True
                    tech_list.append(t)
            scen_list = [{"nom": x["nom"], "description": x["description"], "mots_cles": _csv(x["mots_cles"])}
                         for x in _rows(scen, ["nom", "description", "mots_cles"], "nom")]
            new = {"fictive": fictive, "nom": nom.strip(), "secteur": secteur or None, "secteurs_secondaires": sec2, "roles": roles,
                   "taille": taille or None, "effectif": int(effectif) or None, "chiffre_affaires_meur": ca or None, "pays": "France",
                   "maturite_cyber": mat or None, "activites": _lines(activites), "donnees_traitees": donnees,
                   "technologies": tech_list, "contraintes_securite": _lines(contraintes), "risques_connus": _lines(risques),
                   "scenarios_redoutes": scen_list, "besoins_securite": _rows(besoins, ["besoin", "critere", "niveau"], "besoin"),
                   "echeances": _rows(ech, ["date", "libelle", "origine"], "libelle"),
                   "parties_prenantes": _rows(pp, ["nom", "attentes"], "nom"),
                   "responsables": {k: v.strip() for k, v in resp.items() if v.strip()},
                   "exigences": _rows(exig, ["id", "nom", "type", "statut", "commentaire"], "nom"),
                   "themes_veille": themes, "frequence_collecte": fc, "frequence_rapport": fr}
            try:
                save_profile(new)
                st.success("Profil enregistré dans config/organisation.yaml. Réanalysez les articles pour appliquer le nouveau contexte.")
            except ValueError as exc:
                st.error(str(exc))
    c = st.columns(2)
    if c[0].button("🔁 Réanalyser tous les articles avec ce profil"):
        from veille.pipeline import reanalyze_all
        with st.spinner("Réanalyse en cours…"):
            n = reanalyze_all(storage)
        st.success(f"{n} articles réanalysés ; plan d'action mis à jour (les actions modifiées par l'utilisateur sont conservées).")
    if c[1].button("↩️ Remplacer le profil par le profil d'exemple (AéroStar)"):
        save_profile(load_demo_profile())
        st.rerun()
