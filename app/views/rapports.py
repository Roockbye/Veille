from datetime import date, timedelta
from pathlib import Path

import pandas as pd
import streamlit as st

from ui import get_storage, page_header
from veille.config import reports_dir
from veille.reports.builder import PERIMETRES, build_document, collect_data, generate_report
from veille.reports.markdown import render_markdown


def _safe_report_path(p: str | None) -> Path | None:
    """N'autorise le téléchargement que de fichiers situés dans le répertoire des rapports."""
    if not p:
        return None
    path = Path(p).resolve()
    base = reports_dir().resolve()
    return path if path.is_file() and base in path.parents else None


def render():
    storage = get_storage()
    page_header("Rapports", "Génération à la demande du rapport de veille (PDF et Markdown)")
    c = st.columns([1, 1.6, 1.4])
    preset = c[0].radio("Période", ["7 derniers jours", "30 derniers jours", "Mois précédent", "Personnalisée"])
    today = date.today()
    if preset == "7 derniers jours":
        start, end = today - timedelta(days=7), today
    elif preset == "30 derniers jours":
        start, end = today - timedelta(days=30), today
    elif preset == "Mois précédent":
        end = today.replace(day=1) - timedelta(days=1)
        start = end.replace(day=1)
    else:
        rng = c[0].date_input("Dates", (today - timedelta(days=14), today))
        start, end = (rng if isinstance(rng, (list, tuple)) and len(rng) == 2 else (today - timedelta(days=14), today))
    perims = c[1].multiselect("Périmètre", list(PERIMETRES), default=list(PERIMETRES), format_func=lambda k: PERIMETRES[k][0], placeholder="Aucun")
    formats = c[2].multiselect("Formats", ["pdf", "md"], default=["pdf", "md"], format_func={"pdf": "PDF", "md": "Markdown"}.get, placeholder="Aucun")
    c[2].caption(f"Période retenue : {start.strftime('%d/%m/%Y')} → {end.strftime('%d/%m/%Y')} (date de collecte).")
    if not perims:
        st.error("Choisissez au moins un périmètre.")
        return
    b = st.columns(2)
    if b[0].button("👁️ Prévisualiser"):
        with st.spinner("Préparation de la prévisualisation…"):
            data = collect_data(storage, start, end, perims)
            st.session_state["preview"] = render_markdown(build_document(data))
            st.session_state["preview_n"] = len(data["articles"])
    if b[1].button("📄 Générer et exporter", type="primary", disabled=not formats):
        with st.spinner("Génération du rapport…"):
            res = generate_report(storage, start, end, categories=perims, formats=formats, trigger="manuel")
        st.success(f"Rapport généré ({res['nb_articles']} éléments).")
        for key, mime in (("chemin_pdf", "application/pdf"), ("chemin_md", "text/markdown")):
            if res.get(key):
                p = Path(res[key])
                st.download_button(f"Télécharger {p.name}", p.read_bytes(), p.name, mime, key=f"dl_new_{key}")
    if st.session_state.get("preview"):
        st.info(f"Prévisualisation : {st.session_state['preview_n']} éléments dans le périmètre. Le PDF reprend exactement ce contenu.")
        with st.container(height=700, border=True):
            st.markdown(st.session_state["preview"])  # contenu échappé par le moteur Markdown (pas de HTML actif)
    st.divider()
    st.subheader("Rapports générés")
    reps = storage.list_reports()
    if not reps:
        st.caption("Aucun rapport généré.")
    for r in reps[:20]:
        cols = st.columns([3, 1, 1])
        cols[0].markdown(f"**{r['periode_debut']} → {r['periode_fin']}** — généré le {r['genere_le'][:16].replace('T', ' ')} "
                         f"({r['declencheur']}, {r['nb_articles']} éléments)")
        for col, key, mime in ((cols[1], "chemin_pdf", "application/pdf"), (cols[2], "chemin_md", "text/markdown")):
            p = _safe_report_path(r.get(key))
            if p:
                col.download_button(p.suffix[1:].upper(), p.read_bytes(), p.name, mime, key=f"dl_{r['id']}_{key}")
