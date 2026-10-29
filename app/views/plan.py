import pandas as pd
import streamlit as st

from ui import PRIORITES, STATUTS_ACTION, get_storage, page_header

EFFORTS = {"faible": "Faible", "moyen": "Moyen", "eleve": "Élevé"}


def render():
    storage = get_storage()
    page_header("Plan d'action", "Recommandations issues de la veille : priorité, responsable, échéance, statut et preuves")
    c = st.columns(3)
    stats = c[0].multiselect("Statut", list(STATUTS_ACTION), default=["a_etudier", "a_valider", "planifiee", "en_cours"], format_func=STATUTS_ACTION.get, placeholder="Tous")
    prios = c[1].multiselect("Priorité", PRIORITES, placeholder="Tous")
    q = c[2].text_input("Recherche", max_chars=100)
    acts = storage.list_actions(statuses=stats or None)
    if prios:
        acts = [a for a in acts if a["priorite"] in prios]
    if q:
        acts = [a for a in acts if q.lower() in f"{a['constat']} {a['action']} {a.get('responsable')}".lower()]
    st.caption(f"{len(acts)} action(s). Colonnes modifiables : statut, responsable, échéance, effort, commentaire.")
    if acts:
        df = pd.DataFrame([{"id": a["id"], "Priorité": a["priorite"], "Constat": a["constat"], "Risque / opportunité": a.get("risque"),
                            "Action proposée": a["action"], "Justification": a.get("justification"), "Responsable": a.get("responsable"),
                            "Échéance": pd.to_datetime(a.get("echeance"), errors="coerce"), "Effort": a.get("effort"),
                            "Bénéfice attendu": a.get("benefice"), "Preuves de réalisation": a.get("preuves"),
                            "Statut": a["statut"], "Commentaire": a.get("commentaire") or "", "Origine": a["origine"]} for a in acts])
        edited = st.data_editor(
            df, hide_index=True, width="stretch", height=520, key="plan_editor",
            disabled=["id", "Priorité", "Constat", "Risque / opportunité", "Action proposée", "Justification", "Bénéfice attendu",
                      "Preuves de réalisation", "Origine"],
            column_config={
                "id": st.column_config.NumberColumn("#", width="small"),
                "Statut": st.column_config.SelectboxColumn(options=list(STATUTS_ACTION), required=True),
                "Effort": st.column_config.SelectboxColumn(options=list(EFFORTS)),
                "Échéance": st.column_config.DateColumn(format="DD/MM/YYYY"),
                "Constat": st.column_config.TextColumn(width="medium"), "Action proposée": st.column_config.TextColumn(width="large"),
            })
        if st.button("💾 Enregistrer les modifications", type="primary"):
            changed = 0
            for _, row in edited.iterrows():
                orig = df[df["id"] == row["id"]].iloc[0]
                fields = {}
                for col, key in [("Statut", "statut"), ("Responsable", "responsable"), ("Effort", "effort"), ("Commentaire", "commentaire")]:
                    if row[col] != orig[col] and not (pd.isna(row[col]) and pd.isna(orig[col])):
                        fields[key] = None if pd.isna(row[col]) else str(row[col])[:2000]
                ech_new = None if pd.isna(row["Échéance"]) else pd.Timestamp(row["Échéance"]).date().isoformat()
                ech_old = None if pd.isna(orig["Échéance"]) else pd.Timestamp(orig["Échéance"]).date().isoformat()
                if ech_new != ech_old:
                    fields["echeance"] = ech_new
                if fields:
                    storage.update_action(int(row["id"]), fields)
                    changed += 1
            st.success(f"{changed} action(s) mise(s) à jour.")
            st.rerun()
        exp = df.copy()
        exp["Statut"] = exp["Statut"].map(STATUTS_ACTION)
        st.download_button("Exporter le plan d'action (CSV)", exp.to_csv(index=False).encode("utf-8-sig"), "plan_action.csv", "text/csv")
    st.divider()
    st.subheader("Ajouter une action manuelle")
    with st.form("add_action"):
        constat = st.text_area("Constat initial *", max_chars=2000)
        risque = st.text_input("Risque ou opportunité", max_chars=500)
        action = st.text_area("Action proposée *", max_chars=2000)
        justif = st.text_input("Justification", max_chars=1000)
        c = st.columns(4)
        prio = c[0].selectbox("Priorité *", PRIORITES)
        resp = c[1].text_input("Responsable", max_chars=120)
        ech = c[2].date_input("Échéance indicative")
        effort = c[3].selectbox("Effort", list(EFFORTS), format_func=EFFORTS.get)
        benef = st.text_input("Bénéfice attendu", max_chars=500)
        preuves = st.text_input("Preuves de réalisation", max_chars=500)
        if st.form_submit_button("Ajouter"):
            try:
                storage.add_manual_action({"constat": constat.strip(), "risque": risque, "action": action.strip(), "justification": justif,
                                           "priorite": prio, "responsable": resp, "echeance": ech.isoformat(), "effort": effort,
                                           "benefice": benef, "preuves": preuves})
                st.success("Action ajoutée.")
            except ValueError as exc:
                st.error(str(exc))
