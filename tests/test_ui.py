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


def test_enregistrement_du_profil_sans_perte(monkeypatch, tmp_path):
    """Enregistrer le formulaire de configuration ne doit rien perdre du profil d'exemple."""
    from veille.organisation import load_demo_profile, load_profile
    monkeypatch.setenv("VEILLE_CONFIG_DIR", str(_config_without_profile(tmp_path)))
    at = _run("configuration")
    submit = next(b for b in at.button if "Enregistrer le profil" in b.label)
    submit.click().run()
    assert not at.exception, [e.message for e in at.exception]
    saved, ref = load_profile(), load_demo_profile()
    for k in ("nom", "secteur", "secteurs_secondaires", "roles", "taille", "effectif", "maturite_cyber", "donnees_traitees",
              "exigences", "themes_veille", "contraintes_securite", "risques_connus"):
        assert saved[k] == ref[k], k
    assert [t["nom"] for t in saved["technologies"]] == [t["nom"] for t in ref["technologies"]]
    m365 = next(t for t in saved["technologies"] if t["nom"].startswith("Microsoft 365"))
    assert "Veeam Backup for Microsoft 365" in m365["exclusions"]
    assert {t["nom"] for t in saved["technologies"] if t.get("marque_inconnue")} == {t["nom"] for t in ref["technologies"] if t.get("marque_inconnue")}
    assert saved["scenarios_redoutes"] == ref["scenarios_redoutes"] and saved["responsables"] == ref["responsables"]
    assert saved["echeances"] == ref["echeances"] and saved["besoins_securite"] == ref["besoins_securite"]
