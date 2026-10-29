from collections import Counter

import pandas as pd
import streamlit as st

from ui import articles_df, esc, get_storage, page_header, profile, render_fiche, selectable_table
from veille.classify import THEMES
from veille.technologies import THEME_GUIDE
from views.flux import filters


def render():
    storage = get_storage()
    page_header("Technologies et innovations", "Tendances émergentes, usages possibles, bénéfices, risques, prérequis et opportunités")
    p = profile()
    watched = set(p.get("themes_veille") or THEMES)
    rows = [r for r in storage.list_articles(categories=["technologie"], limit=5000) if r.get("priorite")]
    count = Counter(t for r in rows for t in r.get("themes") or [])
    st.subheader("Tendances par thème")
    df = pd.DataFrame([{"Thème": THEMES[k][0], "Éléments": count.get(k, 0), "Surveillé par l'organisation": "oui" if k in watched else "non"}
                       for k in THEMES]).sort_values("Éléments", ascending=False)
    st.dataframe(df, hide_index=True, width="stretch")
    theme = st.selectbox("Thème à analyser", list(THEMES), format_func=lambda k: THEMES[k][0])
    g = THEME_GUIDE.get(theme, {})
    c = st.columns(4)
    for col, (k, lab) in zip(c, [("usages", "Usages possibles"), ("benefices", "Bénéfices attendus"),
                                 ("risques", "Risques associés"), ("prerequis", "Conditions de sécurité et prérequis")]):
        col.markdown(f"**{lab}**")
        col.write(g.get(k, "—"))
    st.caption("Grille d'analyse générique (connaissance de l'état de l'art), à confronter aux éléments collectés ci-dessous.")
    sel_rows = [r for r in rows if theme in (r.get("themes") or [])]
    st.subheader(f"Éléments collectés — {THEMES[theme][0]} ({len(sel_rows)})")
    sel = selectable_table(articles_df(sel_rows), "tech_table", height=320)
    if sel:
        render_fiche(storage, storage.get_article_full(sel), "tech")
    st.subheader("Opportunités d'amélioration proposées")
    opps = [a for a in storage.list_actions() if (a.get("risque") or "").startswith("Opportunité")]
    if opps:
        st.dataframe(pd.DataFrame([{"#": a["id"], "Priorité": a["priorite"], "Constat": a["constat"], "Opportunité": a["risque"],
                                    "Action": a["action"], "Statut": a["statut"]} for a in opps]), hide_index=True, width="stretch")
    else:
        st.info("Aucune opportunité générée pour l'instant (thèmes surveillés de priorité modérée ou plus).")
