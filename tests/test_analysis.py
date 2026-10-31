from datetime import timedelta

from veille.analysis import analyze, extract_dates
from veille.classify import classify, find_terms, match_inventory
from veille.normalize import iso, utcnow

NOW = iso(utcnow() - timedelta(days=1))


def art(titre, resume="", **kw):
    a = {"id": 1, "titre": titre, "resume_source": resume, "langue": "en", "publie_le": NOW, "collecte_le": iso(utcnow()),
         "url": "https://src.test/a", "source_id": "src", "source_nom": "Source test", "source_categorie": "technique",
         "source_confiance": "elevee", "source_type": "rss", "sous_categorie": None, "donnees": None}
    a.update(kw)
    return a


def test_acronymes_sensibles_a_la_casse():
    assert find_terms("New AI agents", ["AI"]) == ["AI"]
    assert find_terms("j'ai vu un mail", ["AI"]) == []
    assert find_terms("Plusieurs CVEs publiées", ["CVE"]) == ["CVE"]


def test_correspondance_inventaire_mot_entier():
    techs = [{"nom": "PHP", "mots_cles": ["PHP"], "versions": ["8.2"]}]
    assert match_inventory("Critical PHP 8.2 flaw", techs)[0]["versions_citees"] == ["8.2"]
    assert match_inventory("phpMyAdmin issue", techs) == []


def test_classification_multi_categories():
    c = classify("CNIL : sanction RGPD après une fuite de données", "", {"categorie": "reglementaire"})
    assert "reglementaire" in c["categories"] and "incident" in c["categories"]
    assert classify("Friday squid blogging", "")["categories"] == ["non_pertinent"]


def test_aucun_cvss_invente(profil):
    a = analyze(art("Vulnerability in Dassault Systèmes 3DEXPERIENCE (CVE-2099-1111)", "A flaw allows code execution."), profil, {}, {})
    cve = a["cves"][0]
    assert cve["cvss"] is None and cve["kev"] is False
    assert not any(f["facteur"] == "Gravité technique" and f["verifie"] for f in a["facteurs"])
    assert any("CVSS de CVE-2099-1111 non disponible" in v for v in a["a_verifier"])


def test_exploitation_kev_verifiee_et_critique(profil):
    kev = {"CVE-2099-0001": {"cve_id": "CVE-2099-0001", "fournisseur": "Microsoft", "produit": "Windows Netlogon", "rancongiciel": "Known"}}
    cves = {"CVE-2099-0001": {"cvss_score": 10.0, "cvss_version": "3.1", "severite": "CRITICAL", "cvss_source": "NVD"}}
    a = analyze(art("Windows Server Netlogon elevation of privilege CVE-2099-0001",
                    "Attackers can take over an Active Directory domain controller."), profil, kev, cves)
    assert a["priorite"] == "Critique"
    expl = next(f for f in a["facteurs"] if f["facteur"] == "_exploitation")
    assert expl["verifie"] and "KEV" in expl["justification"]
    assert a["echeance"] and "48 h" in a["urgence"]
    assert any(r["type"] == "Vérification de compromission" for r in a["actions"])
    assert a["scenarios"][0]["nom"].startswith("Rançongiciel")  # scénario redouté d'AéroStar
    assert any(f["facteur"] == "Scénario redouté" for f in a["facteurs"])
    assert a["actions"][0]["responsable"].startswith("Équipe IT interne")  # responsables du profil, pas « RSSI »


def test_equipement_infogere_marque_inconnue(profil):
    kev = {"CVE-2099-7777": {"cve_id": "CVE-2099-7777"}}
    a = analyze(art("SSL VPN appliance flaw CVE-2099-7777", "Unauthenticated remote code execution in a SSL VPN gateway."),
                profil, kev, {"CVE-2099-7777": {"cvss_score": 9.8}})
    assert a["technologies"][0]["gestion"] == "infogerant" and a["technologies"][0]["marque_inconnue"]
    assert a["priorite"] == "Élevée"  # présence non confirmée : jamais « Critique »
    assert "Identifier la marque" in a["actions"][0]["action"]
    assert any("infogérant" in r["action"] and "confirmation écrite" in r["action"] for r in a["actions"])
    assert any("non documentés" in v for v in a["a_verifier"])


def test_service_saas_responsabilite_partagee(profil):
    a = analyze(art("Exchange Online vulnerability CVE-2099-8888", "A flaw in Exchange Online allows spoofing."), profil, {}, {})
    assert any("responsabilité partagée" in r["action"] for r in a["actions"])
    assert not any(r["type"] == "Mise à jour" for r in a["actions"])


def test_exploitation_declaree_non_verifiee(profil):
    a = analyze(art("CATIA flaw actively exploited", "Attackers are actively exploiting 3DEXPERIENCE servers."), profil, {}, {})
    expl = next(f for f in a["facteurs"] if f["facteur"] == "_exploitation")
    assert not expl["verifie"] and "non confirmée" in expl["justification"]
    assert a["priorite"] != "Critique"  # pas de gravité vérifiée


def test_inventaire_vide_a_qualifier():
    p = {"technologies": [], "themes_veille": []}
    a = analyze(art("Vulnerability in Ivanti Connect Secure CVE-2099-2222", "Patch now."), p, {}, {})
    assert a["priorite"] == "À qualifier" and a["pertinence"] == "a_qualifier"


def test_ancien_article_plafonne(profil):
    kev = {"CVE-2099-0001": {"cve_id": "CVE-2099-0001"}}
    a = analyze(art("Windows Server Active Directory CVE-2099-0001", "privilege escalation", publie_le="2020-01-01T00:00:00+00:00"),
                profil, kev, {"CVE-2099-0001": {"cvss_score": 9.8}})
    assert a["priorite"] in ("Modérée", "Faible") and any(f["facteur"] == "Ancienneté" for f in a["facteurs"])


def test_termes_kev_limites_aux_fiches_kev(profil):
    """Un CVE Chromium (KEV) cité dans un avis industriel ne doit pas rattacher l'avis au navigateur du parc."""
    kev = {"CVE-2023-4863": {"cve_id": "CVE-2023-4863", "fournisseur": "Google", "produit": "Chromium WebP"}}
    a = analyze(art("Mitsubishi Electric GENESIS64 vulnerabilities", "CVE-2023-4863 allows code execution in ICONICS."),
                profil, kev, {})
    assert a["technologies"] == [] and a["priorite"] != "Critique"


def test_recommandation_jamais_obligation(profil):
    a = analyze(art("Nouvelle version du guide d'hygiène informatique de l'ANSSI", "L'ANSSI publie des recommandations.",
                    source_categorie="normative", langue="fr"), profil, {}, {})
    assert a["normatif"]["type"] == "recommandation"
    assert "ne constitue pas une obligation légale" in a["normatif"]["avertissement"]


def test_fiche_reglementaire(profil):
    a = analyze(art("Proposal to amend Directive (EU) 2022/2555 (NIS2)", "The Commission adopted a proposal. Entry into force on 1 January 2027.",
                    source_categorie="reglementaire", url="https://eur-lex.europa.eu/x?uri=CELEX:52026PC0001"), profil, {}, {})
    reg = a["reglementaire"]
    assert reg["statut_detecte"].startswith("Projet")
    assert any(t["id"] == "nis2" for t in reg["textes"])
    assert {"date": "2027-01-01", "source": "https://eur-lex.europa.eu/x?uri=CELEX:52026PC0001"} in reg["dates_mentionnees"]
    assert all("à confirmer" in t["applicabilite"] or "qualifier" in t["applicabilite"].lower() or "probable" in t["applicabilite"]
               for t in reg["textes"])


def test_resume_francais_extrait_ou_synthese(profil):
    fr = analyze(art("Avis", "Une vulnérabilité a été découverte dans nginx. Elle permet une exécution de code.", langue="fr"), profil, {}, {})
    assert fr["methode_resume"] == "extrait_source"
    en = analyze(art("nginx flaw", "A vulnerability in nginx allows code execution."), profil, {}, {})
    assert en["methode_resume"] == "synthese_regles" and "sans traduction" in en["resume_fr"]


def test_extraction_dates():
    assert extract_dates("applicable le 17 janvier 2025 et le 2026-09-11, puis August 2, 2026") == ["2025-01-17", "2026-08-02", "2026-09-11"]


def test_produit_hors_parc_plafonne(profil):
    kev = {"CVE-2015-3306": {"cve_id": "CVE-2015-3306", "fournisseur": "ProFTPD", "produit": "ProFTPD"}}
    a = analyze(art("[KEV] CVE-2015-3306 — ProFTPD", "ProFTPD improper access control.", source_type="cisa_kev",
                    donnees={"kev": kev["CVE-2015-3306"]}), profil, kev, {"CVE-2015-3306": {"cvss_score": 9.8}})
    assert a["pertinence"] == "faible" and a["priorite"] == "Modérée"
    assert any("vérifier si ProFTPD" in r["action"].lower() or "ProFTPD" in r["action"] for r in a["actions"])


def test_theme_ne_rend_pas_pertinente_une_vulnerabilite_hors_parc(profil):
    a = analyze(art("[KEV] CVE-2099-3333 — Siemens SCADA supply chain flaw", "Siemens SCADA software supply chain vulnerability."),
                profil, {"CVE-2099-3333": {"cve_id": "CVE-2099-3333"}}, {"CVE-2099-3333": {"cvss_score": 9.8}})
    assert a["pertinence"] == "faible" and a["priorite"] == "Modérée"


def test_exclusions_inventaire(profil):
    a = analyze(art("Multiples vulnérabilités dans Veeam Backup for Microsoft 365", "Veeam corrige des failles.", langue="fr"), profil, {}, {})
    assert a["technologies"] == []


def test_menace_sur_produit_hors_parc_plafonnee(profil):
    kev = {"CVE-2099-5555": {"cve_id": "CVE-2099-5555"}}
    a = analyze(art("Threat actors exploit PHP flaw CVE-2099-5555 in ransomware campaign", "Attackers deploy ransomware via PHP."),
                profil, kev, {"CVE-2099-5555": {"cvss_score": 9.8, "epss": 0.9}})
    assert a["pertinence"] == "faible" and a["priorite"] == "Modérée"


def test_produit_issu_du_kev_pour_un_nom_de_campagne(profil):
    kev = {"CVE-2099-6666": {"cve_id": "CVE-2099-6666", "fournisseur": "PHP Group", "produit": "PHP"}}
    a = analyze(art("Threat intel identifies PHP2Shell exploitation", "Exploitation of CVE-2099-6666 observed."), profil, kev, {})
    assert "PHP" in a["produits_cites"] and a["technologies"] == [] and a["priorite"] in ("Modérée", "Faible")
