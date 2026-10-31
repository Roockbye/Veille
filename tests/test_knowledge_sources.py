import pytest

from tests.conftest import fixture_bytes
from veille.knowledge import applicability_matrix, evaluate_applicability, get_referentiel
from veille.organisation import hypotheses, normalize_profile, validate_profile
from veille.sources import SourceValidationError, allowed_domains, load_catalog, parse_opml, validate_source


def P(**kw):
    return normalize_profile(kw)


def test_nis2_secteur_et_taille():
    nis2 = get_referentiel("nis2")
    assert evaluate_applicability(nis2, P(secteur="sante", taille="moyenne"))["resultat"] == "probable"
    assert evaluate_applicability(nis2, P(secteur="sante", taille="petite"))["resultat"] == "a_qualifier"
    assert evaluate_applicability(nis2, P(secteur="commerce", taille="grande"))["resultat"] == "peu_probable"


def test_informations_manquantes_non_evaluable():
    assert evaluate_applicability(get_referentiel("nis2"), P())["resultat"] == "non_evaluable"


def test_dora_prestataire_indirect():
    r = evaluate_applicability(get_referentiel("dora"), P(secteur="services", roles=["prestataire_tic_secteur_financier"]))
    assert r["resultat"] == "indirect"


def test_norme_volontaire_jamais_obligation():
    r = evaluate_applicability(get_referentiel("iso27001"), P(secteur="services"))
    assert r["nature"] == "norme" and r["resultat"] == "a_qualifier"
    r2 = evaluate_applicability(get_referentiel("iso27001"), P(exigences=[{"id": "iso27001", "nom": "ISO", "statut": "identifiee"}]))
    assert r2["resultat"] == "probable" and "déclaré" in r2["motif"]


def test_matrice_jamais_affirmative():
    for m in applicability_matrix(P(secteur="sante", taille="grande", donnees_traitees=["donnees_sante"])):
        assert m["resultat"] in ("probable", "indirect", "a_qualifier", "peu_probable", "non_evaluable")
        if m["resultat"] == "probable":
            assert "à confirmer" in m["libelle"]


def test_hypotheses_profil_incomplet():
    h = hypotheses(P())
    assert any("Secteur non renseigné" in x for x in h) and any("Inventaire technique vide" in x for x in h)
    assert validate_profile({"nom": ""})


def test_catalogue_initial_valide():
    cat = load_catalog()
    assert len(cat) >= 40
    ids = [s["id"] for s in cat]
    assert len(ids) == len(set(ids))
    for s in cat:
        assert s["justification"], s["id"]
        if s["type"] == "manuel":
            assert not s["actif"] and s.get("alternative")
    cats = {s["categorie"] for s in cat if s["actif"]}
    assert cats == {"technique", "reglementaire", "normative", "technologique"}


@pytest.mark.parametrize("bad", [{"nom": "", "url": "https://a.test"}, {"nom": "x", "url": "javascript:alert(1)"},
                                 {"nom": "x", "url": "https://u:p@a.test"}, {"nom": "x", "url": "https://a.test", "frequence_minutes": 1},
                                 {"nom": "x", "url": "https://a.test", "categorie": "inconnue"}])
def test_validation_source_refuse(bad):
    with pytest.raises(SourceValidationError):
        validate_source(bad)


def test_opml_import_et_securite():
    srcs = parse_opml(fixture_bytes("feeds.opml"))
    assert [s["url"] for s in srcs] == ["https://blog-a.test/feed"]  # javascript: et doublon écartés
    with pytest.raises(SourceValidationError):
        parse_opml('<?xml version="1.0"?><!DOCTYPE x [<!ENTITY e SYSTEM "file:///etc/passwd">]><opml><body/></opml>')


def test_liste_blanche_derivee_des_sources(storage):
    from veille.sources import seed_sources
    seed_sources(storage)
    d = allowed_domains(storage)
    assert "cert.cyber.gouv.fr" in d and "services.nvd.nist.gov" in d and "localhost" not in d


def test_profil_aerostar_fidele_a_la_fiche(profil):
    assert profil["fictive"] and profil["effectif"] == 120 and profil["chiffre_affaires_meur"] == 13.8
    assert profil["taille"] == "moyenne" and profil["maturite_cyber"] == "initiale"
    assert any(e["date"] == "2027-12-31" and "AirCyber Bronze" in e["libelle"] for e in profil["echeances"])
    assert any("180 k€" in c for c in profil["contraintes_securite"]) and any("RTO 24 h" in c for c in profil["contraintes_securite"])
    assert len(profil["scenarios_redoutes"]) == 3 and profil["responsables"]["securite"].startswith("Responsable IT")
    assert not validate_profile(profil)


def test_applicabilite_aerostar(profil):
    get = {m["id"]: m for m in applicability_matrix(profil)}
    assert get["nis2"]["resultat"] == "a_qualifier"          # « à qualifier » comme dans la fiche
    assert get["aircyber"]["resultat"] == "probable" and get["aircyber"]["nature"] == "exigence_contractuelle"
    assert get["en9100"]["resultat"] == "probable" and get["en9100"]["nature"] == "norme"
    assert get["iso27001"]["resultat"] == "a_qualifier" and "cible" in get["iso27001"]["motif"]   # non exigée
    assert get["double_usage"]["resultat"] == "a_qualifier"  # à vérifier projet par projet
    assert get["part_is"]["resultat"] == "indirect"
    assert get["dora"]["resultat"] == "peu_probable" and get["hds"]["resultat"] == "peu_probable"
    assert get["rgpd"]["resultat"] == "probable"


def test_referentiel_bien_forme():
    import yaml
    from veille.config import config_dir
    data = yaml.safe_load((config_dir() / "referentiels.yaml").read_text(encoding="utf-8"))
    for t in data["textes"]:
        for k in ("obligations_possibles", "demarches_applicabilite", "references"):
            assert all(isinstance(x, str) for x in t.get(k) or []), (t["id"], k)  # un « : » non protégé crée un dict
        assert isinstance(t["concernes"], str) and t.get("revise_le")
        for r in t["applicabilite"]["regles"]:
            assert isinstance(r["motif"], str), t["id"]


def test_inventaire_exemple_sans_cle_parasite():
    """Une virgule non protégée dans un nom YAML « {nom: a, b} » crée une clé parasite et tronque le nom."""
    import yaml
    from veille.config import config_dir
    data = yaml.safe_load((config_dir() / "organisation.example.yaml").read_text(encoding="utf-8"))
    allowed = {"nom", "categorie", "versions", "mots_cles", "exclusions", "exposition", "criticite", "gestion", "marque_inconnue"}
    for t in data["technologies"]:
        assert set(t) <= allowed, (t["nom"], set(t) - allowed)
        assert t["nom"].count("(") == t["nom"].count(")"), t["nom"]
