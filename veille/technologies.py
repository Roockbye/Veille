"""Grille d'analyse des thèmes technologiques (usages, bénéfices, risques, prérequis).

Contenu rédigé comme aide à l'analyse (connaissance générale de l'état de l'art), distinct des
informations collectées : il sert de trame pour évaluer chaque opportunité.
"""

THEME_GUIDE = {
    "ia_generative": {
        "usages": "Assistance à l'analyse d'alertes et à la rédaction (rapports, procédures), recherche documentaire interne, aide au développement.",
        "benefices": "Gain de temps des équipes, meilleure exploitation de la documentation.",
        "risques": "Fuite de données vers des services externes, injection de prompt, hallucinations, dépendance fournisseur, obligations AI Act.",
        "prerequis": "Politique d'usage de l'IA, classification des données autorisées, solution contractualisée (hébergement UE), recensement des usages (AI Act art. 4).",
    },
    "ia_cybersecurite": {
        "usages": "Détection d'anomalies (UEBA), tri automatique des alertes, détection d'hameçonnage.",
        "benefices": "Réduction du bruit pour le SOC, détection de comportements inconnus.",
        "risques": "Faux positifs/négatifs, opacité des modèles, attaques adverses sur les modèles.",
        "prerequis": "Journalisation centralisée de qualité, période d'apprentissage, capacité d'analyse humaine des résultats.",
    },
    "soar": {
        "usages": "Automatisation des réponses récurrentes (enrichissement d'IOC, isolement de poste après validation, ouverture de tickets).",
        "benefices": "Temps de réponse réduit, homogénéité des traitements.",
        "risques": "Actions automatiques erronées à fort impact, comptes de service très privilégiés.",
        "prerequis": "Processus de réponse documentés, SIEM opérationnel, validation humaine pour les actions destructrices.",
    },
    "siem_edr_xdr": {
        "usages": "Collecte et corrélation des journaux, détection sur les postes et serveurs, investigation.",
        "benefices": "Détection précoce des intrusions, traçabilité exigée par NIS 2 / ISO 27001.",
        "risques": "Coût, volumes de données, couverture incomplète, fatigue d'alertes.",
        "prerequis": "Inventaire des sources de journaux, rétention définie, équipe ou prestataire de supervision.",
    },
    "zero_trust_iam": {
        "usages": "MFA résistante à l'hameçonnage (FIDO2/passkeys), accès conditionnel, gestion des comptes à privilèges, ZTNA à la place du VPN.",
        "benefices": "Réduction du risque de compromission d'identifiants et de mouvement latéral.",
        "risques": "Complexité de déploiement, verrouillage des utilisateurs, dépendance au fournisseur d'identité.",
        "prerequis": "Annuaire maîtrisé, inventaire des applications et des flux, plan de bris de glace.",
    },
    "cloud_conteneurs": {
        "usages": "Sécurisation des environnements cloud (CSPM/CNAPP), durcissement Kubernetes, analyse des images.",
        "benefices": "Visibilité sur les mauvaises configurations, réduction de la surface d'attaque.",
        "risques": "Mauvaises configurations exposées, secrets dans les images, responsabilité partagée mal comprise.",
        "prerequis": "Inventaire des ressources cloud, politique de configuration de référence, intégration CI/CD.",
    },
    "post_quantique": {
        "usages": "Inventaire cryptographique, échanges hybrides post-quantiques (ML-KEM) sur TLS/VPN, gestion des secrets et des certificats.",
        "benefices": "Protection à long terme des données sensibles (menace « collecter maintenant, déchiffrer plus tard »).",
        "risques": "Incompatibilités, performances, produits non encore conformes ; migration longue.",
        "prerequis": "Inventaire des usages cryptographiques, agilité cryptographique, suivi des recommandations ANSSI/NIST.",
    },
    "devsecops_sbom": {
        "usages": "SBOM des applications, analyse des dépendances (SCA), détection de secrets, analyse statique en CI.",
        "benefices": "Réaction rapide aux vulnérabilités de dépendances, préparation au Cyber Resilience Act.",
        "risques": "Bruit des outils, ralentissement des pipelines, dépendances compromises.",
        "prerequis": "Chaîne CI/CD maîtrisée, politique de correction des dépendances, responsabilités définies.",
    },
    "detection_remediation": {
        "usages": "Ingénierie de détection (règles Sigma), gestion de l'exposition, leurres, durcissement guidé.",
        "benefices": "Détection adaptée aux menaces réelles, priorisation de la remédiation.",
        "risques": "Charge de maintenance des règles, fausse impression de sécurité.",
        "prerequis": "Télémétrie suffisante, connaissance des actifs critiques, processus de revue des détections.",
    },
}
