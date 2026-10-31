from datetime import timedelta

import pandas as pd
import plotly.express as px
import streamlit as st

from ui import PRIO_ICON, PRIORITES, STATUT_SOURCE, esc, get_storage, link, page_header, prio_badge
from veille.classify import CATEGORIES
from veille.normalize import iso, utcnow


def run_collect(storage, only_due: bool) -> None:
    from veille.pipeline import run_pipeline
    bar = st.progress(0.0, text="Préparation de la collecte…")
    res = run_pipeline(storage, trigger="manuel", only_due=only_due,
                       progress=lambda name, i, n: bar.progress(i / max(n, 1), text=f"[{i}/{n}] {name}"))
    bar.empty()
    if res.get("statut") == "deja_en_cours":
        st.warning(res["message"])
        return
    msg = (f"Collecte {res['statut']} : {res['sources_ok']} source(s) OK, {res['sources_erreur']} en erreur, "
           f"{res['nouveaux']} nouveaux éléments, {res['doublons']} doublons écartés, {res.get('actions_creees', 0)} action(s) proposée(s).")
    (st.success if res["statut"] == "succes" else st.warning)(msg)
    for d in res.get("details", []):
        if d["statut"] != "ok":
            st.caption(f"⚠️ {d['source']} : {d['statut']} — {d.get('erreur')}")


def render():
    storage = get_storage()
    page_header("Tableau de bord", "Vue d'ensemble de la veille technologique, technique, réglementaire et normative")
    c1, c2, c3 = st.columns([1, 1, 3])
    if c1.button("▶️ Collecter les sources dues", type="primary", help="Interroge les sources dont la fréquence est échue"):
        run_collect(storage, True)
    if c2.button("🔄 Tout collecter", help="Interroge toutes les sources actives (plusieurs minutes)"):
        run_collect(storage, False)

    q = storage.query
    total = storage.scalar("SELECT COUNT(*) FROM articles") or 0
    week = storage.scalar("SELECT COUNT(*) FROM articles WHERE collecte_le >= ?", (iso(utcnow() - timedelta(days=7)),)) or 0
    open_alerts = storage.scalar("""SELECT COUNT(*) FROM analyses n JOIN articles a ON a.id = n.article_id
                                    WHERE n.priorite IN ('Critique','Élevée') AND a.statut NOT IN ('traite','non_pertinent')""") or 0
    crit = storage.scalar("""SELECT COUNT(*) FROM analyses n JOIN articles a ON a.id = n.article_id
                             WHERE n.priorite = 'Critique' AND a.statut NOT IN ('traite','non_pertinent')""") or 0
    actions_open = storage.scalar("SELECT COUNT(*) FROM actions WHERE statut NOT IN ('terminee','abandonnee')") or 0
    src = q("SELECT statut, COUNT(*) n FROM sources WHERE actif = 1 GROUP BY statut")
    src_ok = sum(r["n"] for r in src if r["statut"] == "ok")
    src_err = sum(r["n"] for r in src if r["statut"] in ("erreur", "bloque"))
    last = q("SELECT debut, statut FROM executions WHERE type = 'collecte' ORDER BY id DESC LIMIT 1")

    m = st.columns(6)
    m[0].metric("Articles collectés", total, f"+{week} sur 7 jours")
    m[1].metric("Alertes critiques à traiter", crit)
    m[2].metric("Critiques + élevées ouvertes", open_alerts)
    m[3].metric("Actions à traiter", actions_open)
    m[4].metric("Sources fonctionnelles", src_ok, f"-{src_err} en erreur" if src_err else "aucune erreur", delta_color="inverse" if src_err else "off")
    m[5].metric("Dernière collecte", last[0]["debut"][:10] if last else "—", last[0]["statut"] if last else None, delta_color="off")

    from ui import profile
    from veille.knowledge import applicability_matrix
    from veille.reports.builder import upcoming_deadlines
    p = profile()
    ech = upcoming_deadlines(p, applicability_matrix(p), utcnow().date())
    if ech:
        st.subheader("Échéances à venir")
        cols = st.columns(min(len(ech), 4))
        for col, e in zip(cols, ech[:4]):
            col.metric(e["libelle"][:60] + ("…" if len(e["libelle"]) > 60 else ""), e["quand"], e["origine"], delta_color="off",
                       help=e["libelle"])

    if not total:
        st.info("Aucune donnée : lancez une première collecte avec le bouton ci-dessus (quelques minutes).")
        return

    left, right = st.columns(2)
    with left:
        st.subheader("Répartition par catégorie")
        rows = q("SELECT categorie_principale c, COUNT(*) n FROM analyses GROUP BY c ORDER BY n DESC")
        df = pd.DataFrame([{"Catégorie": CATEGORIES.get(r["c"], r["c"]), "Articles": r["n"]} for r in rows])
        st.plotly_chart(px.bar(df, x="Articles", y="Catégorie", orientation="h", height=320).update_layout(
            margin=dict(l=0, r=0, t=10, b=0), yaxis={"categoryorder": "total ascending"}), width="stretch")
    with right:
        st.subheader("Répartition par priorité")
        rows = q("SELECT priorite p, COUNT(*) n FROM analyses GROUP BY p")
        d = {r["p"]: r["n"] for r in rows}
        df = pd.DataFrame([{"Priorité": p, "Articles": d.get(p, 0)} for p in PRIORITES])
        st.plotly_chart(px.bar(df, x="Priorité", y="Articles", color="Priorité", height=320,
                               color_discrete_map={"Critique": "#c62828", "Élevée": "#ef6c00", "Modérée": "#f9a825",
                                                   "Faible": "#2e7d32", "À qualifier": "#5e35b1"}).update_layout(
            margin=dict(l=0, r=0, t=10, b=0), showlegend=False), width="stretch")

    st.subheader("Évolution du volume de veille (90 derniers jours)")
    since = iso(utcnow() - timedelta(days=90))
    pub = q("SELECT substr(publie_le,1,10) d, COUNT(*) n FROM articles WHERE publie_le >= ? GROUP BY d", (since,))
    col = q("SELECT substr(collecte_le,1,10) d, COUNT(*) n FROM articles WHERE collecte_le >= ? GROUP BY d", (since,))
    t1, t2 = st.tabs(["Par date de publication", "Par date de collecte"])
    for tab, data in ((t1, pub), (t2, col)):
        df = pd.DataFrame([{"Date": r["d"], "Articles": r["n"]} for r in data])
        if not df.empty:
            df["Date"] = pd.to_datetime(df["Date"])
            tab.plotly_chart(px.bar(df, x="Date", y="Articles", height=280).update_layout(margin=dict(l=0, r=0, t=10, b=0)),
                             width="stretch")
    if pub or col:
        st.caption("La date de collecte est distincte de la date de publication : le premier chargement d'un flux ramène des éléments plus anciens.")

    a, b = st.columns([3, 2])
    with a:
        st.subheader("Alertes prioritaires à traiter")
        rows = q("""SELECT a.id, a.titre, a.url, s.nom source, n.priorite, n.echeance, a.statut FROM analyses n
                    JOIN articles a ON a.id = n.article_id JOIN sources s ON s.id = a.source_id
                    WHERE n.priorite IN ('Critique','Élevée') AND a.statut NOT IN ('traite','non_pertinent')
                    ORDER BY CASE n.priorite WHEN 'Critique' THEN 0 ELSE 1 END, n.score DESC LIMIT 12""")
        if not rows:
            st.success("Aucune alerte critique ou élevée en attente.")
        for r in rows:
            st.markdown(f"{prio_badge(r['priorite'])} {link(r['titre'], r['url'])} — _{esc(r['source'])}_ — échéance {r['echeance']}")
        if p.get("scenarios_redoutes"):
            st.subheader("Éléments liés aux scénarios redoutés")
            rows_sc = q("""SELECT a.titre, a.url, n.priorite, n.scenarios FROM analyses n JOIN articles a ON a.id = n.article_id
                           WHERE n.scenarios IS NOT NULL AND n.scenarios != '[]' AND n.priorite IN ('Critique','Élevée','Modérée')
                             AND a.statut NOT IN ('traite','non_pertinent')
                           ORDER BY n.score DESC LIMIT 200""")
            for sc in p["scenarios_redoutes"]:
                linked = [r for r in rows_sc if any(x["nom"] == sc["nom"] for x in r["scenarios"] or [])]
                with st.expander(f"{sc['nom']} — {len(linked)} élément(s) ouvert(s)"):
                    for r in linked[:8]:
                        st.markdown(f"{prio_badge(r['priorite'])} {link(r['titre'], r['url'])}")
    with b:
        st.subheader("État des sources")
        rows = q("SELECT statut, COUNT(*) n FROM sources GROUP BY statut")
        st.dataframe(pd.DataFrame([{"État": STATUT_SOURCE.get(r["statut"], r["statut"]), "Sources": r["n"]} for r in rows]),
                     hide_index=True, width="stretch")
        errs = q("SELECT nom, statut, derniere_erreur FROM sources WHERE statut IN ('erreur','bloque')")
        for e in errs:
            st.caption(f"{STATUT_SOURCE.get(e['statut'])} **{esc(e['nom'])}** — {esc((e['derniere_erreur'] or '')[:160])}")
        st.subheader("Actions par statut")
        rows = q("SELECT priorite, COUNT(*) n FROM actions WHERE statut NOT IN ('terminee','abandonnee') GROUP BY priorite")
        st.dataframe(pd.DataFrame([{"Priorité": f"{PRIO_ICON.get(r['priorite'], '')} {r['priorite']}", "Actions ouvertes": r["n"]} for r in rows]),
                     hide_index=True, width="stretch")
