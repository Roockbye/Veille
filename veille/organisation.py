"""Profil de l'organisation étudiée : vocabulaires, chargement, complétude et hypothèses explicites."""
from __future__ import annotations

from pathlib import Path

from veille.config import config_dir, deep_merge, default_settings, load_yaml, save_yaml

SECTEURS = {
    "energie": "Énergie",
    "transports": "Transports",
    "banque": "Banque",
    "assurance": "Assurance",
    "infrastructures_marches_financiers": "Infrastructures des marchés financiers",
    "sante": "Santé",
    "eau": "Eau potable / eaux usées",
    "infrastructure_numerique": "Infrastructure numérique (cloud, centres de données, DNS, réseaux)",
    "services_tic_b2b": "Gestion des services TIC (infogérance, MSP, MSSP)",
    "administration_publique": "Administration publique (État)",
    "collectivite": "Collectivité territoriale",
    "espace": "Espace",
    "postal": "Services postaux et d'expédition",
    "dechets": "Gestion des déchets",
    "chimie": "Industrie chimique",
    "alimentaire": "Production et distribution alimentaire",
    "fabrication": "Fabrication (dispositifs médicaux, électronique, machines, véhicules...)",
    "fournisseurs_numeriques": "Fournisseurs numériques (places de marché, moteurs de recherche, réseaux sociaux)",
    "recherche": "Recherche",
    "commerce": "Commerce et distribution",
    "education": "Enseignement",
    "services": "Services aux entreprises (conseil, ESN)",
    "industrie_autre": "Autre industrie",
    "association": "Association",
    "autre": "Autre",
}
TAILLES = {
    "micro": "Micro-entreprise (< 10 salariés et CA ≤ 2 M€)",
    "petite": "Petite entreprise (< 50 salariés et CA ≤ 10 M€)",
    "moyenne": "Moyenne entreprise (< 250 salariés et CA ≤ 50 M€)",
    "grande": "Grande entreprise (≥ 250 salariés ou CA > 50 M€)",
}
TAILLE_RANG = {"micro": 0, "petite": 1, "moyenne": 2, "grande": 3}
MATURITES = {
    "initiale": "1 — Initiale (pratiques informelles)",
    "reproductible": "2 — Reproductible (pratiques existantes, peu formalisées)",
    "definie": "3 — Définie (politique et processus documentés)",
    "geree": "4 — Gérée (pilotage par indicateurs)",
    "optimisee": "5 — Optimisée (amélioration continue)",
}
ROLES = {
    "responsable_traitement": "Responsable de traitement (RGPD)",
    "sous_traitant_rgpd": "Sous-traitant au sens du RGPD",
    "prestataire_tic_secteur_financier": "Prestataire TIC d'entités financières",
    "fournisseur_systeme_ia": "Fournisseur / développeur de systèmes d'IA",
    "deployeur_systeme_ia": "Utilisateur professionnel (déployeur) de systèmes d'IA",
    "fabricant_produits_numeriques": "Fabricant de produits comportant des éléments numériques",
    "editeur_logiciel": "Éditeur de logiciels commercialisés",
    "hebergeur_donnees_sante": "Hébergeur de données de santé pour le compte de tiers",
    "accepte_paiements_carte": "Accepte des paiements par carte",
    "operateur_importance_vitale": "Opérateur d'importance vitale (OIV) désigné",
    "prestataire_services_confiance": "Prestataire de services de confiance (eIDAS)",
    "fournisseur_administration": "Fournisseur de l'administration / marchés publics",
}
DONNEES = {
    "donnees_personnelles": "Données personnelles (général)",
    "donnees_clients": "Données clients / usagers",
    "donnees_rh": "Données RH / salariés",
    "donnees_sante": "Données de santé",
    "donnees_bancaires": "Données bancaires / de paiement",
    "donnees_sensibles_rgpd": "Autres données sensibles (art. 9 RGPD)",
    "propriete_intellectuelle": "Propriété intellectuelle / secrets d'affaires",
    "donnees_classifiees": "Informations classifiées ou Diffusion Restreinte",
}
CATEGORIES_TECH = {
    "systeme": "Système d'exploitation serveur", "poste_de_travail": "Poste de travail", "serveur": "Serveur / service",
    "reseau": "Réseau", "securite": "Outil de sécurité", "cloud": "Cloud / conteneurs", "application": "Application",
    "base_de_donnees": "Base de données", "annuaire": "Annuaire / identités", "virtualisation": "Virtualisation",
    "metier": "Solution métier", "autre": "Autre",
}
EXPOSITIONS = {"internet": "Exposé sur Internet", "dmz": "DMZ / partenaires", "interne": "Réseau interne", "inconnue": "Inconnue"}
CRITICITES = {"critique": "Critique", "elevee": "Élevée", "moyenne": "Moyenne", "faible": "Faible"}
FREQUENCES = {"horaire": "Toutes les heures", "quotidienne": "Quotidienne", "hebdomadaire": "Hebdomadaire", "mensuelle": "Mensuelle"}

REQUIRED_FIELDS = {
    "nom": "nom de l'organisation",
    "secteur": "secteur d'activité",
    "taille": "taille",
    "maturite_cyber": "niveau de maturité",
    "activites": "activités principales",
    "donnees_traitees": "données traitées",
    "technologies": "inventaire des technologies",
    "exigences": "exigences réglementaires et contractuelles identifiées",
    "themes_veille": "thèmes technologiques à surveiller",
}


def profile_path() -> Path:
    return config_dir() / "organisation.yaml"


def example_path() -> Path:
    return config_dir() / "organisation.example.yaml"


def has_profile() -> bool:
    return profile_path().exists()


def load_profile() -> dict:
    """Profil réel s'il existe, sinon profil vide (l'interface propose alors la configuration)."""
    data = load_yaml(profile_path())
    return normalize_profile(data)


def load_demo_profile() -> dict:
    return normalize_profile(load_yaml(example_path()))


def normalize_profile(p: dict) -> dict:
    p = dict(p or {})
    for k in ("secteurs_secondaires", "roles", "activites", "donnees_traitees", "technologies",
              "contraintes_securite", "risques_connus", "exigences", "themes_veille"):
        p[k] = list(p.get(k) or [])
    techs = []
    for t in p["technologies"]:
        if isinstance(t, str):
            t = {"nom": t}
        t = dict(t)
        t["nom"] = str(t.get("nom") or "").strip()
        if not t["nom"]:
            continue
        t["mots_cles"] = [str(m) for m in (t.get("mots_cles") or [t["nom"]]) if str(m).strip()]
        t["versions"] = [str(v) for v in (t.get("versions") or [])]
        t.setdefault("categorie", "autre")
        t["exposition"] = t.get("exposition") or "inconnue"
        t["criticite"] = t.get("criticite") or "moyenne"
        techs.append(t)
    p["technologies"] = techs
    exig = []
    for e in p["exigences"]:
        if isinstance(e, str):
            e = {"nom": e}
        exig.append({"id": e.get("id"), "nom": e.get("nom") or e.get("id") or "", "type": e.get("type", "legale"),
                     "statut": e.get("statut", "a_confirmer"), "commentaire": e.get("commentaire", "")})
    p["exigences"] = exig
    return p


def validate_profile(p: dict) -> list[str]:
    errors = []
    if not str(p.get("nom") or "").strip():
        errors.append("Le nom de l'organisation est obligatoire.")
    if p.get("secteur") and p["secteur"] not in SECTEURS:
        errors.append("Secteur inconnu.")
    if p.get("taille") and p["taille"] not in TAILLES:
        errors.append("Taille inconnue.")
    if p.get("maturite_cyber") and p["maturite_cyber"] not in MATURITES:
        errors.append("Niveau de maturité inconnu.")
    for r in p.get("roles", []):
        if r not in ROLES:
            errors.append(f"Rôle inconnu : {r}")
    for d in p.get("donnees_traitees", []):
        if d not in DONNEES:
            errors.append(f"Type de données inconnu : {d}")
    try:
        if p.get("effectif") not in (None, "") and int(p["effectif"]) < 0:
            errors.append("Effectif invalide.")
    except (TypeError, ValueError):
        errors.append("Effectif invalide.")
    return errors


def save_profile(p: dict) -> None:
    p = normalize_profile(p)
    errs = validate_profile(p)
    if errs:
        raise ValueError(" ".join(errs))
    p.pop("hypotheses", None)
    save_yaml(profile_path(), p)


def missing_fields(p: dict) -> list[str]:
    return [label for key, label in REQUIRED_FIELDS.items() if not p.get(key)]


def hypotheses(p: dict) -> list[str]:
    """Hypothèses explicites utilisées tant que le profil est incomplet (affichées dans l'interface et le rapport)."""
    h = []
    if p.get("demonstration"):
        h.append("Profil de DÉMONSTRATION (organisation fictive) : les analyses d'impact illustrent la méthode "
                 "et doivent être refaites avec le profil réel.")
    if not p.get("secteur"):
        h.append("Secteur non renseigné : l'applicabilité des textes sectoriels (NIS 2, DORA...) est « à qualifier ».")
    if not p.get("taille"):
        h.append("Taille non renseignée : les seuils de taille (NIS 2) ne peuvent pas être évalués.")
    if not p.get("technologies"):
        h.append("Inventaire technique vide : la présence d'un produit dans le parc ne peut pas être établie ; "
                 "les vulnérabilités sont classées « À qualifier » plutôt qu'écartées.")
    else:
        if any(t.get("exposition") == "inconnue" for t in p["technologies"]):
            h.append("Exposition inconnue pour certaines technologies : elles sont traitées comme non exposées "
                     "à Internet (hypothèse à confirmer).")
        if any(not t.get("versions") for t in p["technologies"]):
            h.append("Versions non renseignées pour certaines technologies : la correspondance porte sur le produit, "
                     "pas sur la version affectée (vérification manuelle nécessaire).")
    if not p.get("donnees_traitees"):
        h.append("Données traitées non renseignées : traitement de données personnelles supposé (cas général), à confirmer.")
    if not p.get("themes_veille"):
        h.append("Thèmes technologiques non choisis : tous les thèmes sont surveillés par défaut.")
    if not p.get("maturite_cyber"):
        h.append("Maturité non renseignée : niveau 2 « reproductible » supposé pour proportionner les recommandations.")
    return h


# ---------------------------------------------------------------------- paramètres d'exécution
def get_settings(storage=None) -> dict:
    """Paramètres effectifs = config/settings.yaml surchargé par les modifications faites dans l'interface."""
    base = default_settings()
    if storage is None:
        return base
    try:
        return deep_merge(base, storage.get_setting("overrides", {}) or {})
    except Exception:
        return base


def set_setting_override(storage, section: str, key: str, value) -> None:
    ov = storage.get_setting("overrides", {}) or {}
    ov.setdefault(section, {})[key] = value
    storage.set_setting("overrides", ov)
