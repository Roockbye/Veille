"""Point d'entrée de l'interface : streamlit run app/streamlit_app.py"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st  # noqa: E402

st.set_page_config(page_title="Veille cybersécurité", page_icon="🛡️", layout="wide")

from ui import CSS, ensure_scheduler, get_storage, profile  # noqa: E402
from views import (automatisation, configuration, dashboard, flux, plan, rapports, reglementaire, sources,  # noqa: E402
                   technologies, vulnerabilites)

st.markdown(CSS, unsafe_allow_html=True)  # CSS statique de l'application (aucun contenu collecté)
storage = get_storage()
ensure_scheduler()

pages = {
    "Veille": [
        st.Page(dashboard.render, title="Tableau de bord", icon="📊", url_path="tableau-de-bord", default=True),
        st.Page(flux.render, title="Flux de veille", icon="📰", url_path="flux"),
        st.Page(vulnerabilites.render, title="Vulnérabilités et menaces", icon="🐞", url_path="vulnerabilites"),
        st.Page(reglementaire.render, title="Réglementation et normes", icon="⚖️", url_path="reglementation"),
        st.Page(technologies.render, title="Technologies et innovations", icon="🚀", url_path="technologies"),
    ],
    "Exploitation": [
        st.Page(plan.render, title="Plan d'action", icon="✅", url_path="plan-action"),
        st.Page(rapports.render, title="Rapports", icon="📄", url_path="rapports"),
    ],
    "Paramétrage": [
        st.Page(sources.render, title="Sources et méthodologie", icon="🗂️", url_path="sources"),
        st.Page(configuration.render, title="Configuration de l'organisation", icon="🏢", url_path="configuration"),
        st.Page(automatisation.render, title="Automatisation et journaux", icon="⚙️", url_path="automatisation"),
    ],
}
nav = st.navigation(pages)
with st.sidebar:
    p = profile()
    st.markdown(f"**{p.get('nom') or 'Organisation non configurée'}**")
    if p.get("fictive"):
        st.caption("Organisation fictive (cas d'étude)")
    last = storage.query("SELECT debut, statut FROM executions WHERE type = 'collecte' ORDER BY id DESC LIMIT 1")
    st.caption(f"Dernière collecte : {last[0]['debut'][:16].replace('T', ' ')} UTC ({last[0]['statut']})" if last else "Aucune collecte effectuée")
    st.caption("Outil de veille et d'aide à la décision — aucune action automatique sur le SI.")
nav.run()
