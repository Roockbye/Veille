import pandas as pd
import streamlit as st

from ui import esc, get_storage, page_header, profile, show_hypotheses
from veille.classify import THEMES
from veille.organisation import (CATEGORIES_TECH, CRITICITES, DONNEES, EXPOSITIONS, FREQUENCES, MATURITES, ROLES, SECTEURS,
                                 TAILLES, has_profile, load_demo_profile, missing_fields, save_profile)


def _lines(text: str) -> list[str]:
    return [l.strip()[:500] for l in (text or "").splitlines() if l.strip()][:50]


def render():
    storage = get_storage()
    page_header("Configuration de l'organisation", "Contexte de l'organisation étudiée : base de l'évaluation de pertinence et d'applicabilité")
    p = profile()
    if not has_profile():
        st.warning("Premier lancement : complétez et enregistrez le profil de votre organisation. Le formulaire est prérempli "
                   "avec le profil de **démonstration fictif**, à remplacer.")
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
        sec2 = c[2].multiselect("Secteurs secondaires", list(SECTEURS), default=p.get("secteurs_secondaires"), format_func=SECTEURS.get, placeholder="Aucun")
        c = st.columns(4)
        tk = [""] + list(TAILLES)
        taille = c[0].selectbox("Taille", tk, index=tk.index(p.get("taille") or ""), format_func=lambda k: TAILLES.get(k, "— non renseignée —"))
        effectif = c[1].number_input("Effectif", 0, 10_000_000, int(p.get("effectif") or 0))
        ca = c[2].number_input("Chiffre d'affaires (M€)", 0.0, 1e7, float(p.get("chiffre_affaires_meur") or 0.0))
        mk = [""] + list(MATURITES)
        mat = c[3].selectbox("Maturité cyber", mk, index=mk.index(p.get("maturite_cyber") or ""), format_func=lambda k: MATURITES.get(k, "— non renseignée —"))
        roles = st.multiselect("Rôles de l'organisation (déterminants pour l'applicabilité)", list(ROLES), default=p.get("roles"), format_func=ROLES.get, placeholder="Aucun")
        donnees = st.multiselect("Données traitées", list(DONNEES), default=p.get("donnees_traitees"), format_func=DONNEES.get, placeholder="Aucun")
        activites = st.text_area("Activités principales (une par ligne)", "\n".join(p.get("activites") or []))
        c = st.columns(2)
        contraintes = c[0].text_area("Contraintes de sécurité (une par ligne)", "\n".join(p.get("contraintes_securite") or []))
        risques = c[1].text_area("Risques connus (une par ligne)", "\n".join(p.get("risques_connus") or []))

        st.subheader("Inventaire des technologies")
        st.caption("Les mots-clés servent à reconnaître la technologie dans les articles (séparés par des virgules). "
                   "Exposition et criticité pondèrent la priorité.")
        tdf = pd.DataFrame([{"nom": t["nom"], "categorie": t.get("categorie", "autre"), "versions": ", ".join(t.get("versions") or []),
                             "mots_cles": ", ".join(t.get("mots_cles") or []), "exposition": t.get("exposition", "inconnue"),
                             "criticite": t.get("criticite", "moyenne")} for t in p.get("technologies") or []]
                           or [{"nom": "", "categorie": "autre", "versions": "", "mots_cles": "", "exposition": "inconnue", "criticite": "moyenne"}])
        techs = st.data_editor(tdf, num_rows="dynamic", width="stretch", key="techs", column_config={
            "nom": st.column_config.TextColumn("Technologie", required=True),
            "categorie": st.column_config.SelectboxColumn("Catégorie", options=list(CATEGORIES_TECH)),
            "versions": "Versions", "mots_cles": "Mots-clés de détection",
            "exposition": st.column_config.SelectboxColumn("Exposition", options=list(EXPOSITIONS)),
            "criticite": st.column_config.SelectboxColumn("Criticité", options=list(CRITICITES))})

        st.subheader("Exigences réglementaires et contractuelles identifiées")
        st.caption("Identifiant : rgpd, nis2, dora, ai_act, cra, eidas2, hds, pci_dss, iso27001, iso27002, iso42001, nist_csf, secnumcloud… "
                   "(permet de relier l'exigence au référentiel).")
        edf = pd.DataFrame(p.get("exigences") or [{"id": "", "nom": "", "type": "legale", "statut": "a_confirmer", "commentaire": ""}])
        exig = st.data_editor(edf, num_rows="dynamic", width="stretch", key="exig", column_config={
            "type": st.column_config.SelectboxColumn(options=["legale", "contractuelle", "normative"]),
            "statut": st.column_config.SelectboxColumn(options=["identifiee", "a_confirmer"])})

        st.subheader("Périmètre de veille")
        themes = st.multiselect("Thèmes technologiques à surveiller", list(THEMES), default=p.get("themes_veille") or list(THEMES),
                                format_func=lambda k: THEMES[k][0], placeholder="Aucun")
        c = st.columns(3)
        fk = list(FREQUENCES)
        fc = c[0].selectbox("Fréquence de collecte souhaitée", fk, index=fk.index(p.get("frequence_collecte") or "quotidienne"), format_func=FREQUENCES.get)
        fr = c[1].selectbox("Fréquence des rapports", ["hebdomadaire", "mensuelle"], index=0 if (p.get("frequence_rapport") or "hebdomadaire") == "hebdomadaire" else 1)
        demo = c[2].checkbox("Profil de démonstration (fictif)", bool(p.get("demonstration")))
        st.caption("La planification effective se règle dans la page « Automatisation et journaux ».")
        if st.form_submit_button("💾 Enregistrer le profil", type="primary"):
            tech_list = []
            for _, r in techs.iterrows():
                if str(r.get("nom") or "").strip():
                    tech_list.append({"nom": str(r["nom"]).strip()[:120], "categorie": r.get("categorie") or "autre",
                                      "versions": [v.strip() for v in str(r.get("versions") or "").split(",") if v.strip()][:20],
                                      "mots_cles": [v.strip() for v in str(r.get("mots_cles") or r["nom"]).split(",") if v.strip()][:20],
                                      "exposition": r.get("exposition") or "inconnue", "criticite": r.get("criticite") or "moyenne"})
            ex_list = [{k: (str(r.get(k)) if r.get(k) is not None else "") for k in ("id", "nom", "type", "statut", "commentaire")}
                       for _, r in exig.iterrows() if str(r.get("nom") or r.get("id") or "").strip()]
            new = {"demonstration": demo, "nom": nom.strip(), "secteur": secteur or None, "secteurs_secondaires": sec2, "roles": roles,
                   "taille": taille or None, "effectif": int(effectif) or None, "chiffre_affaires_meur": ca or None, "pays": "France",
                   "maturite_cyber": mat or None, "activites": _lines(activites), "donnees_traitees": donnees,
                   "technologies": tech_list, "contraintes_securite": _lines(contraintes), "risques_connus": _lines(risques),
                   "exigences": ex_list, "themes_veille": themes, "frequence_collecte": fc, "frequence_rapport": fr}
            try:
                save_profile(new)
                st.success("Profil enregistré dans config/organisation.yaml. Pensez à réanalyser les articles pour appliquer le nouveau contexte.")
            except ValueError as exc:
                st.error(str(exc))
    c = st.columns(2)
    if c[0].button("🔁 Réanalyser tous les articles avec ce profil"):
        from veille.pipeline import reanalyze_all
        with st.spinner("Réanalyse en cours…"):
            n = reanalyze_all(storage)
        st.success(f"{n} articles réanalysés ; plan d'action mis à jour (les actions modifiées par l'utilisateur sont conservées).")
    if c[1].button("↩️ Remplacer le profil par le profil de démonstration"):
        save_profile(load_demo_profile())
        st.rerun()
