import json

import pytest

from tests.conftest import fixture_bytes
from veille.collectors import CollectorError, NotConfigured
from veille.collectors.cisa_kev import parse_kev
from veille.collectors.feedly import collect_feedly, parse_stream
from veille.collectors.iso_opendata import build_items, parse_iso, stage_label, watched_key
from veille.collectors.rss import parse_feed


def test_rss_valide():
    items, warns = parse_feed(fixture_bytes("rss_valide.xml"), "fr")
    assert len(items) == 3 and not warns
    first = items[0]
    assert first["titre"].startswith("Vulnérabilité critique")
    assert first["publie_le"].startswith("2026-10-27")
    assert "alert" not in first["resume_source"] and "<b>" not in first["resume_source"]
    assert "@" not in (first["auteur"] or "")  # minimisation : e-mail supprimé
    assert first["auteur"] == "Jean Test"


def test_atom_valide():
    items, _ = parse_feed(fixture_bytes("atom_valide.xml"))
    assert items[0]["url"] == "https://atom.test/pqc" and items[0]["publie_le"].startswith("2026-10-28")


def test_flux_malforme_conserve_les_elements_lisibles():
    items, warns = parse_feed(fixture_bytes("rss_malforme.xml"))
    assert items and warns


def test_page_html_n_est_pas_un_flux():
    with pytest.raises(CollectorError):
        parse_feed(fixture_bytes("page_html.html"))


def test_max_items():
    items, _ = parse_feed(fixture_bytes("rss_valide.xml"), max_items=1)
    assert len(items) == 1 and items[0]["publie_le"].startswith("2026-10-27")  # le plus récent


def test_kev_fenetre_et_lignes():
    rows, items = parse_kev(fixture_bytes("kev.json"), window_days=36500)
    assert {r["cve_id"] for r in rows} == {"CVE-2099-0001", "CVE-2010-0002"}
    rows, items = parse_kev(fixture_bytes("kev.json"), window_days=30)
    assert len(rows) == 2  # tout le catalogue est mémorisé pour vérifier l'exploitation
    assert all("CVE-2010-0002" not in i["titre"] for i in items)


def test_kev_illisible():
    with pytest.raises(CollectorError):
        parse_kev(b"<html>")


def test_iso_reference_surveillee():
    w = ["ISO/IEC 27001", "ISO/IEC 27035"]
    assert watched_key("ISO/IEC 27001:2022/Amd 1:2024", w) == "ISO/IEC 27001"
    assert watched_key("ISO/IEC FDIS 27001", w) == "ISO/IEC 27001"
    assert watched_key("ISO/IEC 27035-2:2023", w) == "ISO/IEC 27035"
    assert watched_key("ISO/IEC 270011", w) is None
    assert watched_key("ISO 9001:2015", w) is None
    assert "Norme publiée" in stage_label(6060) and "Retirée" in stage_label("9599")


def test_iso_etat_initial_puis_changement():
    watched = ["ISO/IEC 27001", "ISO/IEC 27002"]
    found = parse_iso(fixture_bytes("iso.jsonl"), watched)
    assert len(found["ISO/IEC 27001"]) == 2 and len(found["ISO/IEC 27002"]) == 1
    items, rows = build_items(found, {})
    assert {i["donnees"]["evenement"] for i in items} == {"etat_initial"} and len(items) == 2
    assert any("révision engagée" in i["resume_source"] for i in items)  # 27002 : replacedBy renseigné
    known = {r["reference"]: dict(r) for r in rows}  # copie : état tel qu'enregistré en base
    items2, _ = build_items(found, known)
    assert items2 == []  # rien n'a changé
    found["ISO/IEC 27001"][0]["stade"] = "9092"
    items3, _ = build_items(found, known)
    assert len(items3) == 1 and "stade" in items3[0]["titre"]


def test_feedly_sans_jeton_non_configure(monkeypatch):
    with pytest.raises(NotConfigured):
        collect_feedly(fetcher=None)


def test_feedly_parse_et_jeton_jamais_dans_les_erreurs(monkeypatch):
    import httpx
    from tests.conftest import make_fetcher
    monkeypatch.setenv("FEEDLY_ACCESS_TOKEN", "SECRET-TOKEN-123456")
    monkeypatch.setenv("FEEDLY_STREAM_ID", "user/x/category/global.all")
    seen = {}

    def api(request):
        seen["auth"] = request.headers.get("authorization")
        return httpx.Response(401)

    f = make_fetcher({"/v3/streams/contents": api}, {"cloud.feedly.com"})
    with pytest.raises(CollectorError) as e:
        collect_feedly(f)
    assert seen["auth"] == "Bearer SECRET-TOKEN-123456"
    assert "SECRET-TOKEN" not in str(e.value)
    data = {"items": [{"title": "Article", "alternate": [{"href": "https://a.test/1"}], "published": 1761552000000,
                       "summary": {"content": "<p>Résumé</p>"}, "origin": {"title": "Blog A"}},
                      {"title": "Sans lien", "alternate": [{"href": "javascript:x"}]}]}
    items = parse_stream(data)
    assert len(items) == 1 and items[0]["origine"] == "Feedly — Blog A" and items[0]["resume_source"] == "Résumé"
