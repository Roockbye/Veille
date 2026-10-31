from datetime import date

import pandas as pd
import streamlit as st

from ui import STATUTS_ACTION, articles_df, esc, get_storage, link, page_header, profile, render_fiche, selectable_table, show_hypotheses
from veille.collectors.iso_opendata import stage_label
from veille.knowledge import applicability_matrix
from views.flux import filters, sort_rows


def render():
    storage = get_storage()
    page_header("Réglementation et normes", "Textes et référentiels surveillés, applicabilité à qualifier, évolutions et mise en conformité")
    p = profile()
    show_hypotheses(p)
    tabs = st.tabs(["Textes et applicabilité", "Évolutions réglementaires", "Normes et référentiels", "Écarts et actions de conformité"])
    matrix = applicability_matrix(p)
    with tabs[0]:
        st.warning("L'applicabilité affichée est une **orientation** calculée à partir du profil déclaré, jamais une conclusion "
                   "juridique : elle doit être confirmée par le juriste ou le DPO. Une norme ou une recommandation n'est pas une obligation légale.")
        st.dataframe(pd.DataFrame([{"Texte / référentiel": m["nom"], "Référence": m["reference"], "Nature": m["nature_libelle"],
                                    "Statut (référentiel)": m["statut"], "Applicabilité (orientation)": m["libelle"], "Motif": m["motif"]}
                                   for m in matrix]), hide_index=True, width="stretch")
        today = date.today().isoformat()
        for m in matrix:
            with st.expander(f"{m['nom']} — {m['libelle']}"):
                st.markdown(f"**Nature** : {esc(m['nature_libelle'])} — **référence** : {esc(m['reference'])}")
                if m.get("note_statut"):
                    st.info(m["note_statut"])
                st.markdown(f"**Organisations concernées** : {esc(m['concernes'])}")
                if m["dates"]:
                    st.markdown("**Dates importantes**")
                    for d in m["dates"]:
                        st.markdown(f"- {'🔜' if d['date'] >= today else '✔️'} {d['date']} — {esc(d['libelle'])}")
                if m["obligations_possibles"]:
                    st.markdown("**Obligations possibles (à vérifier)**\n" + "\n".join(f"- {esc(o)}" for o in m["obligations_possibles"]))
                st.markdown("**Démarches pour qualifier l'applicabilité**\n" + "\n".join(f"- {esc(o)}" for o in m["demarches_applicabilite"]))
                st.markdown("**Justificatifs / sources officielles** : " + ", ".join(link(u, u) for u in m["references"]) +
                            f" — fiche révisée le {m['revise_le']} (dates à revérifier sur la source officielle)")
    with tabs[1]:
        f = filters(storage, "reg", default_days=90, default_cats=["reglementaire"])
        rows = sort_rows([r for r in storage.list_articles(**f) if r.get("priorite")], "reg")
        df = articles_df(rows)
        if not df.empty:
            df.insert(4, "Nature de l'évolution", [(r.get("reglementaire") or {}).get("nature_evolution", "—") for r in rows])
            df.insert(5, "Textes", [", ".join(t["nom"].split(" — ")[0] for t in (r.get("reglementaire") or {}).get("textes", [])) or "—" for r in rows])
        sel = selectable_table(df, "reg_table")
        if sel:
            render_fiche(storage, storage.get_article_full(sel), "reg")
    with tabs[2]:
        normes = storage.query("SELECT * FROM normes ORDER BY reference")
        st.markdown("**Versions des normes ISO surveillées** (métadonnées publiques ISO Open Data — le texte des normes, payant, n'est ni consulté ni reproduit)")
        if normes:
            show_all = st.toggle("Afficher aussi les documents retirés ou abandonnés", value=False)
            st.dataframe(pd.DataFrame([{"Référence": n["reference"], "Titre": n["titre"], "Stade": stage_label(n["stade"]),
                                        "Publication": n["date_publication"], "Remplacée par (id ISO)": n["remplacee_par"] or "",
                                        "Comité": n["comite"], "Page officielle": f"https://www.iso.org/standard/{n['iso_id']}.html"}
                                       for n in normes if show_all or not (n["stade"] == "9599" or str(n["stade"]).endswith("98"))]),
                         hide_index=True, width="stretch", column_config={"Page officielle": st.column_config.LinkColumn()})
        else:
            st.info("Aucune donnée ISO : lancez une collecte de la source « ISO Open Data ».")
        f = filters(storage, "norm", default_days=90, default_cats=["normative"])
        rows = [r for r in storage.list_articles(**f) if r.get("priorite")]
        df = articles_df(rows)
        if not df.empty:
            df.insert(4, "Type", [(r.get("normatif") or {}).get("type_libelle", "—") for r in rows])
        sel = selectable_table(df, "norm_table")
        if sel:
            render_fiche(storage, storage.get_article_full(sel), "norm")
    with tabs[3]:
        acts = [a for a in storage.list_actions() if (a.get("risque") or "").startswith(("Risque : non-conformité", "Risque : écart"))
                or "conformité" in (a.get("action") or "").lower()]
        st.markdown(f"**{len(acts)} action(s) de conformité** (gérées dans la page *Plan d'action*).")
        if acts:
            st.dataframe(pd.DataFrame([{"#": a["id"], "Priorité": a["priorite"], "Constat": a["constat"], "Action": a["action"],
                                        "Responsable": a["responsable"], "Échéance": a["echeance"],
                                        "Statut": STATUTS_ACTION.get(a["statut"])} for a in acts]), hide_index=True, width="stretch")
        st.markdown("#### Déclarer un écart de conformité identifié")
        with st.form("ecart"):
            ref = st.selectbox("Texte / référentiel", [m["nom"] for m in matrix])
            constat = st.text_area("Constat (écart observé)", max_chars=2000)
            action = st.text_area("Action de mise en conformité proposée", max_chars=2000)
            c = st.columns(3)
            prio = c[0].selectbox("Priorité", ["Élevée", "Modérée", "Faible", "Critique", "À qualifier"])
            resp = c[1].text_input("Responsable", value="Juriste / DPO, avec le RSSI", max_chars=120)
            ech = c[2].date_input("Échéance")
            preuves = st.text_input("Preuves attendues", value="Analyse d'écarts validée, procédure mise à jour", max_chars=500)
            if st.form_submit_button("Ajouter au plan d'action"):
                if not constat.strip() or not action.strip():
                    st.error("Constat et action sont obligatoires.")
                else:
                    storage.add_manual_action({"constat": f"[{ref}] {constat.strip()}", "risque": f"Risque : non-conformité ({ref}).",
                                               "action": action.strip(), "priorite": prio, "responsable": resp, "echeance": ech.isoformat(),
                                               "effort": "moyen", "preuves": preuves, "benefice": "Conformité démontrable.",
                                               "justification": "Écart identifié par l'analyste."})
                    st.success("Écart ajouté au plan d'action.")
