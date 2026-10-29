"""Rendu de chaque page de l'interface (Streamlit AppTest) : premier lancement et base alimentée."""
import pytest

PAGES = ["dashboard", "flux", "vulnerabilites", "reglementaire", "technologies", "plan", "rapports", "sources",
         "configuration", "automatisation"]
ROOT = __import__("pathlib").Path(__file__).resolve().parent.parent


def _run(page: str):
    import streamlit as st
    from streamlit.testing.v1 import AppTest
    st.cache_resource.clear()  # base temporaire propre à chaque test
    code = f"""
import sys
sys.path.insert(0, {str(ROOT / 'app')!r}); sys.path.insert(0, {str(ROOT)!r})
from views import {page}
{page}.render()
"""
    return AppTest.from_string(code, default_timeout=60).run()


@pytest.mark.parametrize("page", PAGES)
def test_page_premier_lancement(page, monkeypatch, tmp_path):
    monkeypatch.setenv("VEILLE_CONFIG_DIR", str(_config_without_profile(tmp_path)))
    at = _run(page)
    assert not at.exception, [e.message for e in at.exception]
    assert at.title


def test_pages_avec_donnees(monkeypatch, tmp_path):
    from tests.conftest import fixture_bytes, make_fetcher
    from veille.collector import collect
    from veille.pipeline import analyze_articles
    from veille.actions import sync_actions
    from veille.storage import Storage
    s = Storage()
    s.init_db()
    s.upsert_source({"id": "t", "nom": "Flux test", "url": "https://feeds.test/rss", "type": "rss", "categorie": "technique",
                     "confiance": "elevee", "frequence_minutes": 60, "actif": True, "langue": "fr", "options": {}, "justification": "test"})
    collect(s, fetcher=make_fetcher({"/rss": (200, fixture_bytes("rss_valide.xml"))}, {"feeds.test"}), only_due=False)
    analyze_articles(s)
    sync_actions(s)
    for page in PAGES:
        at = _run(page)
        assert not at.exception, (page, [e.message for e in at.exception])


def _config_without_profile(tmp_path):
    import shutil
    d = tmp_path / "config"
    shutil.copytree(ROOT / "config", d, ignore=shutil.ignore_patterns("organisation.yaml"))
    return d
