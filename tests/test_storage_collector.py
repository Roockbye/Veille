import httpx

from tests.conftest import fixture_bytes, make_fetcher
from veille.collector import collect, is_due, keyword_filter
from veille.normalize import iso, utcnow


def _src(storage, **kw):
    src = {"id": "test-rss", "nom": "Flux de test", "url": "https://feeds.test/rss", "type": "rss", "categorie": "technique",
           "confiance": "elevee", "frequence_minutes": 60, "actif": True, "langue": "fr", "options": {},
           "filtre_mots_cles": [], "technologies": []}
    src.update(kw)
    storage.upsert_source(src)
    return src


def test_deduplication_url_et_contenu(storage):
    _src(storage)
    base = {"source_id": "test-rss", "titre": "Titre", "empreinte": "h1", "collecte_le": iso(utcnow())}
    assert storage.insert_article({**base, "url": "https://a.test/1", "url_canonique": "https://a.test/1"})[1] == "nouveau"
    assert storage.insert_article({**base, "url": "https://a.test/1?utm_source=x", "url_canonique": "https://a.test/1",
                                   "empreinte": "h2"})[1] == "doublon_url"
    assert storage.insert_article({**base, "url": "https://b.test/2", "url_canonique": "https://b.test/2"})[1] == "doublon_contenu"


def test_historique_des_statuts(storage):
    _src(storage)
    aid, _ = storage.insert_article({"source_id": "test-rss", "url": "https://a.test/1", "url_canonique": "https://a.test/1",
                                     "empreinte": "h", "titre": "T", "collecte_le": iso(utcnow())})
    storage.set_article_status(aid, "a_investiguer", "à voir")
    storage.set_article_status(aid, "traite")
    h = storage.query("SELECT ancien, nouveau FROM historique_statuts WHERE article_id = ? ORDER BY id", (aid,))
    assert [(x["ancien"], x["nouveau"]) for x in h] == [("nouveau", "a_investiguer"), ("a_investiguer", "traite")]


def test_verrou_inter_processus(storage):
    assert storage.acquire_lock("collecte", "A", 60)
    assert not storage.acquire_lock("collecte", "B", 60)
    storage.release_lock("collecte", "A")
    assert storage.acquire_lock("collecte", "B", 60)


def test_action_auto_non_ecrasee(storage):
    a = {"constat": "c", "action": "a", "priorite": "Élevée"}
    assert storage.upsert_auto_action("k1", None, a)
    x = storage.list_actions()[0]
    storage.update_action(x["id"], {"statut": "en_cours"})
    assert not storage.upsert_auto_action("k1", None, {**a, "action": "autre"})
    assert storage.list_actions()[0]["statut"] == "en_cours"


def test_collecte_bout_en_bout_et_doublons(storage):
    _src(storage)
    f = make_fetcher({"/rss": (200, fixture_bytes("rss_valide.xml"), {"etag": '"v1"'})}, {"feeds.test"})
    res = collect(storage, fetcher=f, only_due=False)
    assert res["statut"] == "succes" and res["nouveaux"] == 3
    src = storage.get_source("test-rss")
    assert src["statut"] == "ok" and src["etag"] == '"v1"'
    res2 = collect(storage, fetcher=f, only_due=False)
    assert res2["nouveaux"] == 0 and res2["doublons"] == 3
    art = storage.list_articles()[0]
    assert art["publie_le"] != art["collecte_le"]  # dates distinctes conservées


def test_erreur_reseau_conserve_les_donnees(storage):
    _src(storage)
    ok = make_fetcher({"/rss": (200, fixture_bytes("rss_valide.xml"))}, {"feeds.test"})
    collect(storage, fetcher=ok, only_due=False)

    def boom(request):
        raise httpx.ConnectError("injoignable", request=request)

    ko = make_fetcher({"/rss": boom}, {"feeds.test"}, retries=2)
    res = collect(storage, fetcher=ko, only_due=False)
    assert res["statut"] == "echec"
    src = storage.get_source("test-rss")
    assert src["statut"] == "erreur" and src["echecs_consecutifs"] == 1 and "réseau" in src["derniere_erreur"]
    assert storage.scalar("SELECT COUNT(*) FROM articles") == 3  # rien n'est perdu
    assert storage.list_executions(1)[0]["statut"] == "echec"


def test_source_bloquee_est_signalee(storage):
    _src(storage, id="interne", url="https://intranet.test/rss")
    f = make_fetcher({}, {"intranet.test"}, resolver=lambda h: ["192.168.0.10"])
    res = collect(storage, fetcher=f, only_due=False)
    assert storage.get_source("interne")["statut"] == "bloque" and res["sources_erreur"] == 1


def test_filtre_mots_cles_et_frequence(storage):
    items = [{"titre": "NIS2 : nouveaux actes", "resume_source": ""}, {"titre": "Sport", "resume_source": "football"}]
    kept, n = keyword_filter(items, ["nis2"])
    assert len(kept) == 1 and n == 1
    assert is_due({"derniere_verification": None, "frequence_minutes": 60})
    assert not is_due({"derniere_verification": iso(utcnow()), "frequence_minutes": 60})


def test_pipeline_complet_sans_reseau(storage, monkeypatch, profil):
    import veille.pipeline as pl
    _src(storage)
    f = make_fetcher({"/rss": (200, fixture_bytes("rss_valide.xml"))}, {"feeds.test"})
    monkeypatch.setattr(pl, "collect", lambda s, **kw: collect(s, fetcher=f, only_due=False))
    monkeypatch.setattr(pl, "enrich_for", lambda s, ids, settings=None: {})
    monkeypatch.setattr(pl, "current_profile", lambda: profil)
    res = pl.run_pipeline(storage)
    assert res["analyses"] == 3
    rows = {r["titre"][:12]: r for r in storage.list_articles()}
    ad = next(r for t, r in rows.items() if t.startswith("Vulnérabilit"))
    assert {t["nom"] for t in ad["technologies"]} >= {"Active Directory (corp.aerostar.lan)"}
    assert ad["scenarios"] and ad["scenarios"][0]["nom"].startswith("Rançongiciel")
    assert storage.list_actions()  # au moins une action proposée


def test_action_auto_non_modifiee_suit_la_reanalyse(storage):
    storage.upsert_auto_action("k2", None, {"constat": "c", "action": "a", "priorite": "Critique"})
    storage.upsert_auto_action("k2", None, {"constat": "c", "action": "a", "priorite": "Élevée"})
    assert storage.list_actions()[0]["priorite"] == "Élevée"
