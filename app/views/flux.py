from datetime import date, timedelta

import streamlit as st

from ui import PRIORITES, STATUTS_ARTICLE, articles_df, get_storage, page_header, render_fiche, selectable_table
from veille.classify import CATEGORIES


def filters(storage, key: str, default_days: int = 30, default_cats=None):
    with st.expander("Filtres", expanded=True):
        c = st.columns([1.3, 1, 1.5, 1.5])
        period = c[0].date_input("Période", (date.today() - timedelta(days=default_days), date.today()), key=f"{key}_p")
        field = c[1].radio("Date utilisée", ["collecte_le", "publie_le"], key=f"{key}_df",
                           format_func={"collecte_le": "Collecte", "publie_le": "Publication"}.get)
        cats = c[2].multiselect("Catégorie", list(CATEGORIES), default=default_cats, format_func=CATEGORIES.get, key=f"{key}_c", placeholder="Toutes")
        prios = c[3].multiselect("Priorité", PRIORITES, key=f"{key}_pr", placeholder="Toutes")
        c = st.columns([1.5, 1.2, 1.2, 1.5])
        sources = storage.list_sources()
        srcs = c[0].multiselect("Source", [s["id"] for s in sources], key=f"{key}_s",
                                format_func={s["id"]: s["nom"] for s in sources}.get, placeholder="Toutes")
        stats = c[1].multiselect("Statut de traitement", list(STATUTS_ARTICLE), format_func=STATUTS_ARTICLE.get, key=f"{key}_st", placeholder="Tous")
        tech = c[2].text_input("Technologie / produit", key=f"{key}_t", max_chars=80)
        search = c[3].text_input("Recherche (titre, résumé, CVE, mot-clé)", key=f"{key}_q", max_chars=120)
    d_from = d_to = None
    if isinstance(period, (list, tuple)) and len(period) == 2:
        d_from, d_to = period[0].isoformat(), period[1].isoformat() + "T23:59:59"
    order = st.radio("Tri", ["priorite", "date"], horizontal=True, key=f"{key}_o",
                     format_func={"priorite": "Par priorité puis date", "date": "Par date (récent d'abord)"}.get)
    st.session_state[f"{key}_order"] = order
    return dict(date_from=d_from, date_to=d_to, date_field=field, categories=cats or None, priorities=prios or None,
                source_ids=srcs or None, statuses=stats or None, technology=tech.strip() or None, search=search.strip() or None)


def sort_rows(rows, key):
    from veille.analysis import PRIORITY_ORDER
    if st.session_state.get(f"{key}_order", "priorite") == "priorite":
        rows.sort(key=lambda r: (r.get("publie_le") or r["collecte_le"]), reverse=True)
        rows.sort(key=lambda r: PRIORITY_ORDER.get(r.get("priorite"), 9))
    return rows


def render():
    storage = get_storage()
    page_header("Flux de veille", "Liste des éléments collectés, analyse et suivi du traitement")
    f = filters(storage, "flux")
    rows = sort_rows([r for r in storage.list_articles(**f) if r.get("priorite")], "flux")
    st.caption(f"{len(rows)} élément(s). Sélectionnez une ligne pour afficher sa fiche d'analyse.")
    df = articles_df(rows)
    sel = selectable_table(df, "flux_table")
    if not df.empty:
        st.download_button("Exporter la sélection filtrée (CSV)", df.to_csv(index=False).encode("utf-8-sig"),
                           "flux_veille.csv", "text/csv")
    if sel:
        st.divider()
        render_fiche(storage, storage.get_article_full(sel), "flux")
