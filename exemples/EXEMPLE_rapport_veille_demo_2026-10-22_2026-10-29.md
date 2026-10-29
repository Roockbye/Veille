# Rapport de veille technologique, technique, réglementaire et normative

**Sécurité du système d'information**

## NumériSanté Services (organisation fictive de démonstration)

- Période : du 22/10/2026 au 29/10/2026
- Généré le 29/10/2026 à 21:12 (UTC)
- Périmètre : Veille technique et cybersécurité, Veille technologique, Veille réglementaire, Veille normative
- Outil : VeilleCyber 1.0.0 — moteur d'analyse regles-1.0
- Compétence visée : B1.A1.C3

> **DONNÉES DE DÉMONSTRATION** — organisation fictive ; les éléments de veille sont réellement collectés.

---


## 1. Résumé exécutif

**\[Fait\]** Sur la période du 22/10/2026 au 29/10/2026, 1068 éléments ont été collectés automatiquement auprès de 48 sources fonctionnelles. Après exclusion des éléments anciens republiés (392), non pertinents (31) ou écartés par l'analyste (0), 645 éléments entrent dans le périmètre de ce rapport.

| Priorité | Nombre d'éléments |
|---|---|
| Critique | 17 |
| Élevée | 27 |
| Modérée | 296 |
| Faible | 304 |
| À qualifier | 1 |

**\[Analyse\]** Points d'attention prioritaires (un sujet couvert par plusieurs sources n'est cité qu'une fois) :

- \[Critique\] Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant (Palo Alto Networks — Unit 42, 2026-10-14) — Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc).
- \[Critique\] php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619 (Elastic Security Labs, 2026-10-21) — confirmé par 15 autre(s) source(s) : AWS Security Blog, CERT-FR — Alertes de sécurité, CISA — Cybersecurity Advisories, CISA — Known Exploited Vulnerabilities (KEV), Cisco — Security Advisories — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc).
- \[Critique\] Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open (The Hacker News, 2026-10-29) — confirmé par 2 autre(s) source(s) : CISA — Cybersecurity Advisories, CISA — Known Exploited Vulnerabilities (KEV) — Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc).
- \[Critique\] PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw (The Hacker News, 2026-10-26) — Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, PHP concernées par l'avis (inventaire, outil de gestion de parc).
- \[Critique\] \[KEV\] CVE-2025-61624 — Fortinet Multiple Products : Fortinet Multiple Products Path Traversal Vulnerability (CISA — Known Exploited Vulnerabilities (KEV), 2026-10-16) — Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc).
- \[Élevée\] Widespread PHP Flaw May Cause Many Site Outages Today (Krebs on Security, 2026-10-21) — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc).
- \[Élevée\] Chromium: CVE-2026-79260 Improper input validation in Cookies (Microsoft — Security Update Guide, 2026-10-28) — Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc).
- \[Élevée\] USN-8951-1: c-ares vulnerabilities (Ubuntu — Security Notices, 2026-10-21) — Vérifier la présence et les versions de Ubuntu Server concernées par l'avis (inventaire, outil de gestion de parc).

**\[Analyse\]** Textes dont l'applicabilité est probable ou indirecte (à confirmer) : RGPD, NIS 2, AI Act, Certification Hébergeur de Données de Santé (HDS).

**\[Recommandation\]** 74 actions sont proposées ou en cours dans le plan d'action (17 critiques, 27 élevées).

> Profil de démonstration : l'organisation étudiée est fictive. Les données collectées sont réelles, mais l'analyse d'impact illustre la méthode et doit être refaite avec le profil réel.


## 2. Objectifs et périmètre de la veille

Objectifs : (1) surveiller les menaces, vulnérabilités et innovations technologiques pertinentes ; (2) suivre l'évolution des cadres légaux et des normes applicables ; (3) analyser leurs impacts sur l'organisation ; (4) identifier les obligations à vérifier et les opportunités d'amélioration de la sécurité du SI.


### Organisation étudiée

| Élément | Valeur déclarée |
|---|---|
| Nom | NumériSanté Services (organisation fictive de démonstration) |
| Secteur | Gestion des services TIC (infogérance, MSP, MSSP) ; secondaires : Santé |
| Taille | Moyenne entreprise (\< 250 salariés et CA ≤ 50 M€) — 140 salariés |
| Maturité cyber | 3 — Définie (politique et processus documentés) |
| Rôles | Responsable de traitement (RGPD), Sous-traitant au sens du RGPD, Hébergeur de données de santé pour le compte de tiers, Utilisateur professionnel (déployeur) de systèmes d'IA, Fournisseur de l'administration / marchés publics |
| Données traitées | Données personnelles (général), Données de santé, Données RH / salariés, Données clients / usagers |
| Activités | Infogérance et hébergement d'applications métiers pour des établissements de santé privés; Développement et maintenance d'un portail patient (application web); Support utilisateurs et administration de postes de travail pour ses clients |
| Technologies inventoriées | 19 |
| Exigences identifiées | RGPD (legale, identifiee); Certification HDS (legale, identifiee); ISO/IEC 27001 (contractuelle, identifiee); NIS 2 (legale, a\_confirmer) |
| Thèmes technologiques | Intelligence artificielle et IA générative, Machine learning appliqué à la cybersécurité, Automatisation de la sécurité et SOAR, SIEM, EDR, XDR, détection et réponse aux incidents, Zero Trust, IAM, MFA et gestion des identités, Sécurité du cloud, des conteneurs et de la chaîne logicielle, Cryptographie, post-quantique et gestion des secrets, DevSecOps, SBOM et sécurité des dépendances, Nouvelles méthodes de détection, de prévention et de remédiation |

- **Contrainte** : Disponibilité 24/7 exigée par les clients établissements de santé
- **Contrainte** : Hébergement des données de santé en France
- **Contrainte** : Équipe sécurité réduite (1 RSSI, 2 administrateurs formés)
- **Risque connu** : Rançongiciel via l'accès VPN exposé sur Internet
- **Risque connu** : Compromission de comptes par hameçonnage (Microsoft 365)
- **Risque connu** : Vulnérabilités de l'application web portail patient


### Hypothèses de travail

- **\[Hypothèse\]** : Profil de DÉMONSTRATION (organisation fictive) : les analyses d'impact illustrent la méthode et doivent être refaites avec le profil réel.
- **\[Hypothèse\]** : Versions non renseignées pour certaines technologies : la correspondance porte sur le produit, pas sur la version affectée (vérification manuelle nécessaire).

Périmètre du rapport : Veille technique et cybersécurité, Veille technologique, Veille réglementaire, Veille normative.


## 3. Méthodologie

- **Collecte** : interrogation automatique de flux RSS/Atom et d'interfaces publiques autorisées (CISA KEV, ISO Open Data, API NVD, FIRST EPSS), à une fréquence propre à chaque source, avec respect de robots.txt, requêtes conditionnelles et limitation de débit. Dates de publication et de collecte conservées séparément.
- **Déduplication** : URL canonique (suppression des paramètres de suivi) puis empreinte du contenu (titre + résumé normalisés).
- **Classification** : règles explicites (mots-clés FR/EN, type et catégorie de la source) en huit catégories ; un article peut relever de plusieurs catégories.
- **Enrichissement** : scores CVSS issus du NVD, exploitation active issue du catalogue CISA KEV, probabilité EPSS (FIRST). Aucune valeur n'est estimée.
- **Pertinence** : rapprochement avec l'inventaire technique, les thèmes surveillés et l'applicabilité des textes au profil de l'organisation.
- **Priorisation** : score additif explicable (gravité, exploitation, présence et exposition dans le parc, criticité, urgence, importance réglementaire, ancienneté) ; niveau « Critique » réservé aux technologies du parc avec gravité ou exploitation vérifiée.
- **Restitution** : fiche par élément, plan d'action et ce rapport ; chaque information est reliée à son URL d'origine (annexes).
- **Fraîcheur** : les éléments publiés plus de 30 jours avant le début de la période sont exclus des résultats (392 éléments).

**\[Fait\]** Exécutions de collecte sur la période : 1 (dont 1 réussies, 0 partielles, 0 en échec).


## 4. Justification des outils utilisés

| Outil | Usage | Justification |
|---|---|---|
| Python 3 | Langage de l'application | Écosystème mature pour la collecte, l'analyse et la génération de documents. |
| feedparser | Lecture RSS/Atom | Tolère les flux mal formés ; standard de fait. |
| httpx | Requêtes HTTP | Délais, flux de réponse et redirections contrôlés (protection SSRF). |
| SQLite | Stockage | Base locale sans serveur, transactionnelle, suffisante pour une veille d'organisation. |
| Streamlit | Interface web | Tableau de bord local en français, rapide à déployer. |
| APScheduler | Planification | Collecte et rapports périodiques ; service système possible. |
| ReportLab | Export PDF | Génération PDF sans dépendance externe. |
| API NVD, CISA KEV, FIRST EPSS | Enrichissement | Sources de référence publiques pour CVSS, exploitation et probabilité. |
| IA (facultative) | Résumés en français | Désactivée par défaut ; contenus traités comme données non fiables ; n'influence pas la priorité. |


## 5. Catalogue des sources et justification


### Veille technique et cybersécurité

| Source | Nature / confiance | Fréquence | État | Éléments retenus | Justification |
|---|---|---|---|---|---|
| BleepingComputer | Presse spécialisée / Moyenne | 2 h | Fonctionnelle | 9 | Actualité rapide sur les rançongiciels, incidents et vulnérabilités ; à recouper avec une source primaire. |
| CERT-FR — Alertes de sécurité | Source officielle / Élevée | 1 h | Fonctionnelle | 4 | Centre gouvernemental de veille, d'alerte et de réponse aux attaques informatiques (ANSSI). Les alertes signalent des vulnérabilités activement exploitées ou critiques nécessitant une action rapide. |
| CERT-FR — Avis de sécurité | Source officielle / Élevée | 1 h | Fonctionnelle | 40 | Avis décrivant les vulnérabilités publiées par les éditeurs, les produits affectés et les correctifs. Source de référence francophone pour la gestion des correctifs. |
| CERT-FR — Bulletins d'actualité | Source officielle / Élevée | 12 h | Fonctionnelle | 5 | Bulletins hebdomadaires synthétisant les vulnérabilités significatives et les recommandations associées. |
| CERT-FR — Menaces et incidents | Source officielle / Élevée | 12 h | Fonctionnelle | 3 | Rapports de menace (modes opératoires, rançongiciels, campagnes) produits par l'ANSSI. |
| CISA — Actualités | Source officielle / Élevée | 24 h | Fonctionnelle | 4 | Annonces de la CISA (stratégies, guides conjoints, campagnes). |
| CISA — Cybersecurity Advisories | Source officielle / Élevée | 3 h | Fonctionnelle | 30 | Avis techniques (dont systèmes industriels) et alertes conjointes avec les agences partenaires. |
| CISA — Known Exploited Vulnerabilities (KEV) | Source officielle / Élevée | 6 h | Fonctionnelle | 35 | Catalogue officiel des vulnérabilités dont l'exploitation active est confirmée par la CISA. Utilisé pour vérifier le critère « exploitation active » de la priorisation. |
| Cisco Talos Intelligence | Recherche / laboratoire / Moyenne | 12 h | Fonctionnelle | 15 | Recherche sur les menaces et vulnérabilités ; source éditeur. |
| Cisco — Security Advisories | Éditeur / fournisseur / Élevée | 12 h | Fonctionnelle | 44 | Avis de sécurité officiels Cisco (réseau, sécurité, collaboration). |
| Cybermalveillance.gouv.fr — Actualités | Source officielle / Élevée | 12 h | Fonctionnelle | 5 | Alertes sur les campagnes d'hameçonnage et d'escroquerie ; utile pour la sensibilisation des utilisateurs. |
| Debian — Security Advisories (DSA) | Éditeur / fournisseur / Élevée | 12 h | Fonctionnelle | 30 | Bulletins de sécurité officiels de Debian. |
| Feedly — Flux personnels (API officielle) | Communauté / fondation / agrégateur / Moyenne | 6 h | Désactivée | 0 | Source complémentaire facultative : agrège les flux suivis dans le compte Feedly de l'utilisateur. La fiabilité dépend des flux d'origine (indiqués pour chaque article). Alternative : Nécessite un jeton d'accès API officiel (variable FEEDLY\_ACCESS\_TOKEN), disponible selon l'offre Feedly. Sans jeton : exporter ses abonnements en OPML depuis Feedly et les importer dans le catalogue (page Sources) ; l'application les collecte alors directement en RSS. Voir docs/FEEDLY.md. |
| Fortinet — PSIRT Advisories | Éditeur / fournisseur / Élevée | 12 h | Fonctionnelle | 13 | Avis officiels Fortinet ; équipements fréquemment ciblés en périmètre réseau. |
| Krebs on Security | Presse spécialisée / Moyenne | 24 h | Fonctionnelle | 7 | Enquêtes sur la cybercriminalité et les incidents majeurs. |
| Microsoft Security Blog | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 10 | Renseignement sur la menace (Microsoft Threat Intelligence) et nouveautés sécurité. |
| Microsoft — Security Update Guide | Éditeur / fournisseur / Élevée | 12 h | Fonctionnelle | 150 | Source primaire des vulnérabilités et correctifs Microsoft (flux volumineux, limité aux 150 entrées les plus récentes). |
| NCSC (Royaume-Uni) — Publications | Source officielle / Élevée | 24 h | Fonctionnelle | 9 | Agence nationale homologue de l'ANSSI ; guides et recommandations de sécurité. |
| Palo Alto Networks — Unit 42 | Recherche / laboratoire / Moyenne | 12 h | Fonctionnelle | 15 | Analyses de campagnes et de modes opératoires ; source éditeur. |
| SANS Internet Storm Center — Diaries | Recherche / laboratoire / Élevée | 6 h | Fonctionnelle | 3 | Analyses techniques quotidiennes par des incident handlers (observations terrain, détection). |
| Securelist (Kaspersky GReAT) | Recherche / laboratoire / Moyenne | 12 h | Fonctionnelle | 9 | Analyses APT et logiciels malveillants ; à recouper (contexte géopolitique de l'éditeur). |
| SecurityWeek | Presse spécialisée / Moyenne | 6 h | Fonctionnelle | 8 | Actualité vulnérabilités, ICS et réglementation. |
| The DFIR Report | Recherche / laboratoire / Moyenne | 24 h | Fonctionnelle | 0 | Retours d'expérience détaillés d'intrusions réelles (chaînes d'attaque, détections). |
| The Hacker News | Presse spécialisée / Moyenne | 3 h | Fonctionnelle | 44 | Couverture large des menaces et vulnérabilités ; contenu parfois sponsorisé, à recouper. |
| Ubuntu — Security Notices | Éditeur / fournisseur / Élevée | 12 h | Fonctionnelle | 10 | Bulletins de sécurité officiels de la distribution Ubuntu. |
| WeLiveSecurity (ESET) — FR | Recherche / laboratoire / Moyenne | 12 h | Fonctionnelle | 6 | Recherches sur les logiciels malveillants en français ; source éditeur (biais commercial possible). |
| ZATAZ | Presse spécialisée / Moyenne | 6 h | Fonctionnelle | 7 | Actualité francophone sur les fuites de données et la cybercriminalité ; à recouper. |


### Veille réglementaire

| Source | Nature / confiance | Fréquence | État | Éléments retenus | Justification |
|---|---|---|---|---|---|
| Autorité bancaire européenne (EBA) — Actualités (filtrées) | Source officielle / Élevée | 24 h | Fonctionnelle | 1 | Normes techniques et orientations liées à DORA pour le secteur financier. |
| CNIL — Actualités | Source officielle / Élevée | 12 h | Fonctionnelle | 10 | Autorité française de protection des données ; recommandations, sanctions, référentiels RGPD. |
| Commission européenne — AI Act Service Desk | Source officielle / Élevée | 24 h | Fonctionnelle | 0 | Point d'information officiel de la Commission sur la mise en œuvre du règlement IA. |
| Commission européenne — Stratégie numérique (filtrée) | Source officielle / Élevée | 24 h | Fonctionnelle | 2 | Annonces officielles (actes d'exécution, consultations, lignes directrices) sur NIS2, AI Act, CRA, eIDAS. |
| EDPB — Actualités | Source officielle / Élevée | 24 h | Fonctionnelle | 10 | Lignes directrices et décisions contraignantes interprétant le RGPD au niveau européen. |
| EUR-Lex — Actes du Journal officiel série L (filtrés) | Source officielle / Élevée | 24 h | Fonctionnelle | 0 | Actes publiés au JOUE, notamment les règlements d'exécution et délégués précisant NIS2, DORA, AI Act, CRA. |
| EUR-Lex — Législation du Parlement et du Conseil (filtrée) | Source officielle / Élevée | 24 h | Fonctionnelle | 1 | Source officielle des textes législatifs de l'UE (identifiant CELEX, date de publication). Flux généraliste : un filtre par mots-clés ne conserve que les textes liés au numérique et à la sécurité. |
| EUR-Lex — Propositions de la Commission (filtrées) | Source officielle / Élevée | 24 h | Fonctionnelle | 3 | Propositions législatives (statut « projet ») permettant d'anticiper les évolutions réglementaires. |
| Légifrance — Journal officiel (JORF) | Source officielle / Élevée | 168 h | Bloquée / non collectable | 0 | Source officielle des textes législatifs et réglementaires français (transposition NIS2, lois, décrets). Alternative : Les flux RSS publics de Légifrance renvoient une page de vérification anti-robot (HTTP 403, Cloudflare) : aucune collecte automatique n'est tentée. Alternatives : (1) API Légifrance officielle via le portail PISTE (compte et identifiants OAuth requis, piste.gouv.fr) ; (2) consultation manuelle hebdomadaire et saisie dans l'outil ; (3) suivi des textes européens via EUR-Lex. |
| artificialintelligenceact.eu (non officiel) | Communauté / fondation / agrégateur / Moyenne | 24 h | Fonctionnelle | 6 | Site d'analyse NON officiel du règlement IA, utile pour suivre les débats ; toute information doit être confirmée sur EUR-Lex. |


### Veille normative

| Source | Nature / confiance | Fréquence | État | Éléments retenus | Justification |
|---|---|---|---|---|---|
| ANSSI — Guides et publications (cyber.gouv.fr) | Source officielle / Élevée | 168 h | Bloquée / non collectable | 0 | Guides d'hygiène, recommandations de configuration, référentiels (SecNumCloud, PASSI, etc.). Alternative : Le site cyber.gouv.fr est protégé par un dispositif anti-robot (Incapsula) et ne fournit pas de flux RSS exploitable : aucune collecte automatique n'est tentée. Alternatives : les flux CERT-FR (même organisme) sont collectés automatiquement ; consultation manuelle mensuelle de la page des publications et saisie des nouveautés dans l'outil. |
| ISO Open Data — Métadonnées des normes surveillées | Source officielle / Élevée | 168 h | Fonctionnelle | 0 | Jeu de données ouvert publié par l'ISO (métadonnées : référence, titre, édition, stade, date de publication, remplacements). Permet de détecter une nouvelle édition, un amendement ou une révision sans accéder au texte des normes, qui reste payant et n'est jamais reproduit. |
| NIST — Actualités (filtrées sécurité) | Source officielle / Élevée | 24 h | Fonctionnelle | 2 | Actualités officielles du NIST, filtrées sur la sécurité (normes FIPS, SP 800, PQC, IA). |
| NIST — Cybersecurity Insights (blog) | Source officielle / Élevée | 24 h | Fonctionnelle | 4 | Annonces du NIST sur le Cybersecurity Framework, les SP 800, la cryptographie post-quantique et la sécurité de l'IA. |
| OpenSSF — Blog | Communauté / fondation / agrégateur / Moyenne | 24 h | Fonctionnelle | 9 | Référentiels de bonnes pratiques pour la sécurité de la chaîne d'approvisionnement logicielle (SLSA, SBOM). |


### Veille technologique

| Source | Nature / confiance | Fréquence | État | Éléments retenus | Justification |
|---|---|---|---|---|---|
| AWS Security Blog | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 19 | Nouveautés et bonnes pratiques de sécurité AWS (IAM, détection, chiffrement). |
| CNCF — Blog | Communauté / fondation / agrégateur / Moyenne | 24 h | Fonctionnelle | 7 | Tendances cloud natif (sécurité des conteneurs, identité des charges de travail, IA). |
| Cloudflare Blog | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 20 | Retours techniques sur le déploiement post-quantique, le Zero Trust et les attaques DDoS. |
| CrowdStrike Blog | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 10 | Tendances EDR/XDR et sécurité de l'IA ; source éditeur (biais commercial). |
| Elastic Security Labs | Recherche / laboratoire / Moyenne | 24 h | Fonctionnelle | 8 | Recherches sur l'ingénierie de détection et les nouvelles techniques d'attaque. |
| GitHub Blog — Security | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 5 | DevSecOps, sécurité des dépendances, analyse de code, gestion des secrets. |
| Google Online Security Blog | Éditeur / fournisseur / Moyenne | 24 h | Fonctionnelle | 0 | Innovations (post-quantique, sécurité de l'IA, mémoire sûre) publiées par les équipes sécurité de Google. |
| Kubernetes Blog (filtré sécurité) | Communauté / fondation / agrégateur / Élevée | 24 h | Fonctionnelle | 3 | Annonces officielles du projet Kubernetes (fonctionnalités de sécurité, dépréciations). |
| Schneier on Security | Recherche / laboratoire / Moyenne | 24 h | Fonctionnelle | 10 | Analyses d'expert reconnu en cryptographie et en politique de sécurité. |


## 6. Résultats de la veille technique et cybersécurité

| Catégorie | Éléments |
|---|---|
| Vulnérabilité ou correctif | 433 |
| Menace ou campagne d'attaque | 97 |
| Incident ou retour d'expérience | 46 |
| Bonne pratique ou recommandation | 33 |

**\[Analyse\]** Technologies du parc les plus citées : Google Chrome / Microsoft Edge (151), Debian (30), PHP (23), Microsoft Windows Server (13), Microsoft Windows 11 (13), Ubuntu Server (5), Fortinet FortiGate (VPN SSL) (4), VMware ESXi / vCenter (4).


### Bonnes pratiques et recommandations publiées


#### Critical security issue affecting PHP

- **URL** : <https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php>
- **Source** : NCSC (Royaume-Uni) — Publications — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Bonne pratique ou recommandation
- **\[Analyse\] Résumé** : Bonne pratique ou recommandation — publication de NCSC (Royaume-Uni) — Publications du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « Updated: The NCSC is encouraging UK organisations to take immediate action to mitigate a security issue affecting PHP (CVE-2026-109618 and CVE-2026-109619). » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619)

- **URL** : <https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/>
- **Source** : AWS Security Blog — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Bonne pratique ou recommandation — mots-clés : vulnerabilit, CVE, RCE, code execution, guidance, mitigation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de AWS Security Blog du 2026-10-22. CVE citées : CVE-2026-109618, CVE-2026-109619, CVE-2026-115560. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « October 29, 2026: We added guidance for end-of-life PHP versions (8.1 and earlier), including the source backports that the PHP security team published for PHP 7.4, 8.0, and 8.1. October 23, 2026 (update 2): The PHP project disclosed CVE-2026-115560, a separate remote code execution issue that the October 21 releases don’t fix. It affects only \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-115560 — CVSS non disponible
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-115560 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Kicking off Cybersecurity Career Week with NIST!

- **URL** : <https://www.nist.gov/blogs/cybersecurity-insights/kicking-cybersecurity-career-week-nist>
- **Source** : NIST — Cybersecurity Insights (blog) — publié le 2026-10-14, consulté le 2026-10-29
- **Catégorie** : Bonne pratique ou recommandation, Évolution normative — mots-clés : awareness, how to, NIST Cybersecurity Framework 2.0
- **\[Analyse\] Résumé** : Bonne pratique ou recommandation — publication de NIST — Cybersecurity Insights (blog) du 2026-10-14. Extrait original (en) : « Considering a career in cybersecurity? Cybersecurity Career Week (CCW), a campaign led by the NICE Program at NIST from October 19-24, 2026, aims to raise public awareness and help people find their path to \#ChooseCyber. During this week, academia, industry, non-profit organizations, and government agencies host events, share resources, provide \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : a\_qualifier — Applicabilité du texte à qualifier.
- **\[Analyse\] Priorité** : À qualifier — Score 8 = 8 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : a\_qualifier.
- **\[Recommandation\]** : (1) Évaluer l'impact de l'évolution de « NIST Cybersecurity Framework 2.0 » (référentiel de bonnes pratiques) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (2) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-11-05 — urgence : Qualification requise (sous 7 jours)
- **Confiance de l'analyse** : moyenne


#### Siemens Software Center

- **URL** : <https://www.cisa.gov/news-events/ics-advisories/icsa-26-295-03>
- **Source** : CISA — Cybersecurity Advisories — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Bonne pratique ou recommandation — mots-clés : vulnerabilit, CVE, code execution, exploitation, recommend, guide, how to
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Cybersecurity Advisories du 2026-10-22. CVE citées : CVE-2026-110936. Produits cités : Siemens. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « View CSAF Summary The affected application loads dynamic-link libraries (DLLs) from an uncontrolled search path. This could allow an authenticated local attacker to place a specially crafted DLL in a directory that the application searches, leading to arbitrary code execution with the privileges of the affected application. Siemens has released a \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **Produits cités** : Siemens
- **\[Donnée vérifiée\] CVE** : CVE-2026-110936 — CVSS non disponible, EPSS 0.01, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : faible — Produits cités absents de l'inventaire déclaré : Siemens.
- **\[Analyse\] Priorité** : Modérée — Score 42 = 12 (Gravité technique) + 30 (Exploitation active) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : faible.
- **\[Recommandation\]** : (1) Vérifier si Siemens est utilisé dans le SI (inventaire potentiellement incomplet) ; sinon, classer l'information comme non applicable. (2) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-110936 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Présence éventuelle dans le parc à confirmer : Siemens.


#### De la protection des données à la création de valeur en finance : des autorités européennes publient une étude et des bonnes pratiques

- **URL** : <https://www.cnil.fr/fr/protection-donnees-valeur-finance-etude-autorites-europeennes>
- **Source** : CNIL — Actualités — publié le 2026-10-16, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Bonne pratique ou recommandation — mots-clés : CNIL, protection des données, bonnes pratiques, RGPD
- **\[Fait\] Résumé** : La CNIL, l’ICO et la CNPD publient leur étude conjointe « De la protection des données à la création de valeur en finance : évaluation des données, comptabilité, fusions-acquisitions et gouvernance », rassemblant analyses et bonnes pratiques à destination des entreprises et des acteurs financiers.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


## 7. Menaces et vulnérabilités identifiées


### Vulnérabilités


#### \[Critique\] Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant

- **URL** : <https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/>
- **Source** : Palo Alto Networks — Unit 42 — publié le 2026-10-14, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : malware, attackers, CVE, exploited
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Palo Alto Networks — Unit 42 du 2026-10-14. CVE citées : CVE-2024-47575. Score CVSS le plus élevé (NVD) : 9.8 (CVE-2024-47575). Produits cités : FortiGate. Technologies du parc concernées : Fortinet FortiGate (VPN SSL). Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « We investigated an intrusion where attackers exploited CVE-2024-47575 to target 500+ firewalls and deploy PEERSTITCH, a memory-resident ARM64 malware. The post Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant appeared first on Unit 42. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Fortinet FortiGate (VPN SSL) (exposition : internet, criticité : critique, versions du parc : 7.4)
- **\[Donnée vérifiée\] CVE** : CVE-2024-47575 — CVSS 9.8 (CRITICAL, NVD (nvd@nist.gov, Primary)), EPSS 0.95, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Fortinet FortiGate (VPN SSL).
- **\[Analyse\] Priorité** : Critique — Score 120 = 30 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 10 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Versions affectées de Fortinet FortiGate (VPN SSL) à comparer avec les versions du parc (7.4). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619

- **URL** : <https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection>
- **Source** : Elastic Security Labs — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : CVE, flaw, RCE, exploitation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Elastic Security Labs du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP, Elastic. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : SIEM, EDR, XDR, détection et réponse aux incidents. Extrait original (en) : « CVE-2026-109618 and CVE-2026-109619 are critical PHP core RCE flaws that leaked ahead of disclosure. We cover what is verified, why exploitation converges on a web server spawning a shell, and the Elastic detections developed to catch this behavior. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Confidentialité, Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 108 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] Critical RCE vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619)

- **URL** : <https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/>
- **Source** : Securelist (Kaspersky GReAT) — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, RCE
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Securelist (Kaspersky GReAT) du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « We discuss the incident involving the leak of information about vulnerabilities CVE-2026-109618 and CVE-2026-109619. Kaspersky solutions detect the PHP2Shell exploit: we’ll walk you through examples using KEDR, KATA, and KES. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Confidentialité, Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] CISA Adds Two Known Exploited Vulnerabilities to Catalog

- **URL** : <https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog>
- **Source** : CISA — Cybersecurity Advisories — publié le 2026-10-26, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, KEV, exploited, exploitation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Cybersecurity Advisories du 2026-10-26. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog and updated the PHP Alert, Critical Vulnerabilities in PHP Require Immediate Patching:  CVE-2026-109618 – PHP Memory Corruption Vulnerability  CVE-2026-109619 – PHP Stale Internal Request-State Vulnerability  These types of vulnerabilities are a frequent \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Critique\] Vulnerabilities in PHP Affecting Cisco Products: October 2026

- **URL** : <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20PHP%20Affecting%20Cisco%20Products:%20October%202026%26vs_k=1>
- **Source** : Cisco — Security Advisories — publié le 2026-10-28, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, advisory, RCE
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Cisco — Security Advisories du 2026-10-28. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : Cisco, PHP, Splunk. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « On October 21, the PHP Foundation announced the availability of a Critical PHP Security release addressing two critical vulnerabilities:  CVE-2026-109618 - RCE via OOM corruption CVE-2026-109619 - RCE via stale global state For information about these vulnerabilities, see the advisories GHSA-w8hw-w9fx-j79w and GHSA-6wmf-4rv5-p3rp. These \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Critique\] Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29)

- **URL** : <https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/>
- **Source** : Palo Alto Networks — Unit 42 — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : threat brief, vulnerabilit, CVE
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Palo Alto Networks — Unit 42 du 2026-10-29. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « CVE-2026-109618 and CVE-2026-109619 are Critical vulnerabilities in PHP, a scripting language used globally for web servers and CMS systems. The post Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) appeared first on Unit 42. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open

- **URL** : <https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html>
- **Source** : The Hacker News — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, flaw
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de The Hacker News du 2026-10-29. CVE citées : CVE-2026-97229. Produits cités : Linux, GitLab. Technologies du parc concernées : GitLab. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « An attacker tried to exploit a critical GitLab vulnerability on the Alpine Linux project's own GitLab server a week after GitLab released a fix, Alpine Linux said on 28 October. The flaw, CVE-2026-97229 (CVSS score: 10.0), can let an attacker run code on a GitLab server through a crafted regular expression in a CI configuration. Alpine found no \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : GitLab (exposition : internet, criticité : elevee, versions du parc : n.c.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-97229 — CVSS non disponible, EPSS 0.18, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : GitLab.
- **\[Analyse\] Priorité** : Critique — Score 93 = 12 (Gravité technique) + 30 (Exploitation active) + 5 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-97229 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de GitLab à comparer avec les versions du parc (non renseignées). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] CISA Adds Two Known Exploited Vulnerabilities to Catalog

- **URL** : <https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog>
- **Source** : CISA — Cybersecurity Advisories — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, KEV, exploited, exploitation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Cybersecurity Advisories du 2026-10-29. CVE citées : CVE-2026-111357, CVE-2026-97229. Produits cités : Ivanti, GitLab. Technologies du parc concernées : GitLab. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Zero Trust, IAM, MFA et gestion des identités, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « CISA has added two new vulnerabilities to its Known Exploited Vulnerabilities (KEV) Catalog, based on evidence of active exploitation. CVE-2026-111357 Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability CVE-2026-97229 GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound vulnerability These \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : GitLab (exposition : internet, criticité : elevee, versions du parc : n.c.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-111357 — CVSS non disponible, EPSS 0.00; CVE-2026-97229 — CVSS non disponible, EPSS 0.18, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : GitLab.
- **\[Analyse\] Priorité** : Critique — Score 93 = 12 (Gravité technique) + 30 (Exploitation active) + 5 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-111357 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-97229 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de GitLab à comparer avec les versions du parc (non renseignées).


#### \[Critique\] PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw

- **URL** : <https://thehackernews.com/2026/10/php-issues-second-windows-security.html>
- **Source** : The Hacker News — publié le 2026-10-26, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : CVE, flaw, security update, code execution
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de The Hacker News du 2026-10-26. CVE citées : CVE-2026-111497. Produits cités : Windows, PHP, Brotli. Technologies du parc concernées : Microsoft Windows Server, Microsoft Windows 11, PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : DevSecOps, SBOM et sécurité des dépendances. Extrait original (en) : « PHP has rebuilt its official Windows packages for PHP 8.2 through 8.5 to fix CVE-2026-111497, a flaw in the Brotli compression library that the packages include. The flaw can let an attacker corrupt memory and potentially run code. PHP says the flaw can be reached through the cURL extension when the extension decompresses HTTP responses \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Microsoft Windows Server (exposition : interne, criticité : elevee, versions du parc : 2019, 2022); Microsoft Windows 11 (exposition : interne, criticité : moyenne, versions du parc : 23H2, 24H2); PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-111497 — CVSS non disponible, EPSS 0.83, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Microsoft Windows Server, Microsoft Windows 11, PHP.
- **\[Analyse\] Priorité** : Critique — Score 91 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 5 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-111497 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de Microsoft Windows Server à comparer avec les versions du parc (2019, 2022). Versions affectées de Microsoft Windows 11 à comparer avec les versions du parc (23H2, 24H2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619)

- **URL** : <https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/>
- **Source** : AWS Security Blog — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Bonne pratique ou recommandation — mots-clés : vulnerabilit, CVE, RCE, code execution, guidance, mitigation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de AWS Security Blog du 2026-10-22. CVE citées : CVE-2026-109618, CVE-2026-109619, CVE-2026-115560. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « October 29, 2026: We added guidance for end-of-life PHP versions (8.1 and earlier), including the source backports that the PHP security team published for PHP 7.4, 8.0, and 8.1. October 23, 2026 (update 2): The PHP project disclosed CVE-2026-115560, a separate remote code execution issue that the October 21 releases don’t fix. It affects only \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-115560 — CVSS non disponible
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-115560 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] \[KEV\] CVE-2026-109619 — PHP Group PHP : PHP Stale Internal Request-State Vulnerability

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109619>
- **Source** : CISA — Known Exploited Vulnerabilities (KEV) — publié le 2026-10-26, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, code execution, KEV, exploitation, catalogue KEV
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Known Exploited Vulnerabilities (KEV) du 2026-10-26. CVE citées : CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « PHP contains a stale internal request-state vulnerability that allows for unauthenticated remote code execution. Ajoutée au catalogue KEV le 2026-10-26 (exploitation active confirmée par la CISA). Action requise (CISA) : Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Critique\] \[KEV\] CVE-2026-109618 — PHP Group PHP : PHP Memory Corruption Vulnerability

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109618>
- **Source** : CISA — Known Exploited Vulnerabilities (KEV) — publié le 2026-10-26, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, code execution, KEV, exploitation, catalogue KEV
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Known Exploited Vulnerabilities (KEV) du 2026-10-26. CVE citées : CVE-2026-109618. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « PHP contains an out-of-memory corruption vulnerability that allows for unauthenticated remote code execution. Ajoutée au catalogue KEV le 2026-10-26 (exploitation active confirmée par la CISA). Action requise (CISA) : Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Critique\] CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution

- **URL** : <https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html>
- **Source** : The Hacker News — publié le 2026-10-27, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, flaw, patch, code execution, KEV, exploited, exploitation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de The Hacker News du 2026-10-27. CVE citées : CVE-2026-109618. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « The U.S. Cybersecurity and Infrastructure Security Agency (CISA) on Monday confirmed active exploitation of the recently patched PHP2Shell flaws by adding them to its Known Exploited Vulnerabilities (KEV) catalog. The PHP vulnerabilities, both rated 9.2 on the CVSS scoring system, facilitate unauthenticated remote code execution on affected \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] \[KEV\] CVE-2026-46300 — Linux Kernel : Linux Kernel Missing Initialization of a Variable Vulnerability

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-46300>
- **Source** : CISA — Known Exploited Vulnerabilities (KEV) — publié le 2026-10-28, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, KEV, exploitation, catalogue KEV
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Known Exploited Vulnerabilities (KEV) du 2026-10-28. CVE citées : CVE-2026-46300, CVE-2026-109618, CVE-2026-109619. Produits cités : Linux kernel, PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-46300 — CVSS non disponible, EPSS 0.16, KEV : exploitation active confirmée; CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-46300 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Critique\] \[KEV\] CVE-2026-97229 — GitLab Community Edition and Enterprise Edition : GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-97229>
- **Source** : CISA — Known Exploited Vulnerabilities (KEV) — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif — mots-clés : vulnerabilit, CVE, patch, security update, KEV, exploitation, catalogue KEV
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de CISA — Known Exploited Vulnerabilities (KEV) du 2026-10-29. CVE citées : CVE-2026-97229. Produits cités : GitLab, Community Edition and Enterprise Edition. Technologies du parc concernées : GitLab. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, DevSecOps, SBOM et sécurité des dépendances, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation. Ajoutée au catalogue KEV le 2026-10-29 \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : GitLab (exposition : internet, criticité : elevee, versions du parc : n.c.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-97229 — CVSS non disponible, EPSS 0.18, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : GitLab.
- **\[Analyse\] Priorité** : Critique — Score 81 = 30 (Exploitation active) + 5 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : elevee
- **\[À vérifier\]** : Score CVSS de CVE-2026-97229 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de GitLab à comparer avec les versions du parc (non renseignées).

281 autres vulnérabilités sont référencées en annexe.


### Menaces, campagnes et incidents


#### \[Critique\] Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant

- **URL** : <https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/>
- **Source** : Palo Alto Networks — Unit 42 — publié le 2026-10-14, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : malware, attackers, CVE, exploited
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Palo Alto Networks — Unit 42 du 2026-10-14. CVE citées : CVE-2024-47575. Score CVSS le plus élevé (NVD) : 9.8 (CVE-2024-47575). Produits cités : FortiGate. Technologies du parc concernées : Fortinet FortiGate (VPN SSL). Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « We investigated an intrusion where attackers exploited CVE-2024-47575 to target 500+ firewalls and deploy PEERSTITCH, a memory-resident ARM64 malware. The post Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant appeared first on Unit 42. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Fortinet FortiGate (VPN SSL) (exposition : internet, criticité : critique, versions du parc : 7.4)
- **\[Donnée vérifiée\] CVE** : CVE-2024-47575 — CVSS 9.8 (CRITICAL, NVD (nvd@nist.gov, Primary)), EPSS 0.95, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Fortinet FortiGate (VPN SSL).
- **\[Analyse\] Priorité** : Critique — Score 120 = 30 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 10 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Versions affectées de Fortinet FortiGate (VPN SSL) à comparer avec les versions du parc (7.4). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Critique\] Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29)

- **URL** : <https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/>
- **Source** : Palo Alto Networks — Unit 42 — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : threat brief, vulnerabilit, CVE
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Palo Alto Networks — Unit 42 du 2026-10-29. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Extrait original (en) : « CVE-2026-109618 and CVE-2026-109619 are Critical vulnerabilities in PHP, a scripting language used globally for web servers and CMS systems. The post Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) appeared first on Unit 42. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Élevée\] Widespread PHP Flaw May Cause Many Site Outages Today

- **URL** : <https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/>
- **Source** : Krebs on Security — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Incident ou retour d'expérience — mots-clés : vulnerabilit, flaw, exploited, outage
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Krebs on Security du 2026-10-21. Produits cités : PHP. Technologies du parc concernées : PHP. Exploitation active signalée par la source — non confirmée par le KEV. Extrait original (en) : « Expect to see quite a few websites serving "404" or "Page Not Found" errors today: Nearly 70 percent of websites need to update their core software to fix a pair of vulnerabilities that allow an attacker to seize full control over affected servers. Experts say there are working exploits for the flaws, and that these critical bugs are already being \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Exploitation active signalée par la source — non confirmée par le KEV
- **\[Analyse\] Impact potentiel** : Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 76 = 12 (Gravité technique) + 18 (Exploitation active) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte. Plafonné à « Élevée » : le niveau « Critique » exige une technologie du parc concernée ET une gravité ou une exploitation vérifiée (KEV, CVSS ≥ 9, alerte CERT-FR).
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Analyser le retour d'expérience et vérifier si le scénario est transposable (fournisseurs, technologies, processus).
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Exploitation active signalée par la source mais non confirmée par le catalogue CISA KEV. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Élevée\] Two critical RCEs in PHP core

- **URL** : <https://blog.talosintelligence.com/two-critical-rces-in-php-core/>
- **Source** : Cisco Talos Intelligence — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Menace ou campagne d'attaque — mots-clés : vulnerabilit, RCE, code execution
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Cisco Talos Intelligence du 2026-10-21. Produits cités : PHP. Technologies du parc concernées : PHP. Extrait original (en) : « Two critical remote code execution vulnerabilities in PHP core could have implications across its wider ecosystem. Talos has published a blog to explain what we know so far, and details the Snort coverage available, including rules in the Community Ruleset. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 12 (Gravité technique) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Élevée\] Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot

- **URL** : <https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/>
- **Source** : AWS Security Blog — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Menace ou campagne d'attaque, Évolution technologique — mots-clés : vulnerabilit, CVE, exploitation, threat intelligence
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de AWS Security Blog du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Exploitation active confirmée (catalogue CISA KEV). Thèmes : SIEM, EDR, XDR, détection et réponse aux incidents, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « Amazon Threat Intelligence identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure of CVE-2026-109618 and CVE-2026-109619. The exploit attempt originated from an IP address associated with a commercial anonymization network. While the vulnerability was under embargo, the \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Confidentialité
- **\[Analyse\] Pertinence** : moyenne — Menace ou pratique générique, potentiellement transposable au SI de l'organisation.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 10 (Thème surveillé) + 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Élevée\] AlerteCyber : Failles de sécurité critiques dans PHP

- **URL** : <https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/alerte-cyber-failles-de-securite-critiques-dans-php-202610>
- **Source** : Cybermalveillance.gouv.fr — Actualités — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : espionnage, faille, déni de service
- **\[Fait\] Résumé** : Failles de sécurité critiques dans PHP Date de l’alerte : 22/10/2026 Risques Déni de service, espionnage, vol voire destruction de vos données suite à la prise de contrôle à distance des équipements vulnérables. …
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Confidentialité, Disponibilité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 12 (Gravité technique) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Élevée\] Cybermalveillance.gouv.fr lance une AlerteCyber concernant deux failles de sécurité critiques dans PHP

- **URL** : <https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/alertecyber-failles-securite-php>
- **Source** : Cybermalveillance.gouv.fr — Actualités — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Menace ou campagne d'attaque — mots-clés : faille
- **\[Fait\] Résumé** : Cybermalveillance.gouv.fr déclenche ce jour une nouvelle AlerteCyber concernant deux failles de sécurité critiques dans le langage de programmation PHP. Il est primordial de les corriger le plus rapidement possible en mettant à jour les systèmes concernés pour réduire les risques d’une…
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 12 (Gravité technique) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2).


#### \[Élevée\] I had plans for that second

- **URL** : <https://blog.talosintelligence.com/i-had-plans-for-that-second/>
- **Source** : Cisco Talos Intelligence — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Cisco Talos Intelligence du 2026-10-22. Produits cités : PHP. Technologies du parc concernées : PHP. Extrait original (en) : « The Earth is speeding up, the leap second is being abolished, oh, and there's critical vulnerabilities in PHP. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 12 (Gravité technique) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Élevée\] AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise

- **URL** : <https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/>
- **Source** : Microsoft Security Blog — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Menace ou campagne d'attaque — mots-clés : AI, agentic, supply chain, campaign
- **\[Analyse\] Résumé** : Évolution technologique — publication de Microsoft Security Blog du 2026-10-21. Produits cités : Microsoft, ConnectWise. Technologies du parc concernées : Microsoft 365 / Exchange Online. Thèmes : Intelligence artificielle et IA générative, Machine learning appliqué à la cybersécurité, Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments. The post AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise appeared first on Microsoft Security Blog. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Microsoft 365 / Exchange Online (exposition : internet, criticité : elevee, versions du parc : n.c.)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Confidentialité, Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Microsoft 365 / Exchange Online.
- **\[Analyse\] Priorité** : Élevée — Score 56 = 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de Microsoft 365 / Exchange Online à comparer avec les versions du parc (non renseignées). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Modérée\] Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware

- **URL** : <https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/>
- **Source** : BleepingComputer — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Vulnérabilité ou correctif — mots-clés : APT, malware, hackers, CVE, flaw, bypass
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de BleepingComputer du 2026-10-29. CVE citées : CVE-2026-20127. Produits cités : Cisco. Exploitation active confirmée (catalogue CISA KEV). Thèmes : Zero Trust, IAM, MFA et gestion des identités. Extrait original (en) : « A newly identified advanced persistent threat (APT) group tracked as UAT-11473 was observed exploiting CVE-2026-20127, an authentication-bypass flaw in Cisco Catalyst SD-WAN Controllers, to deploy a custom malware framework called KeyDrift. \[...\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **Produits cités** : Cisco
- **\[Donnée vérifiée\] CVE** : CVE-2026-20127 — CVSS non disponible, EPSS 0.89, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Zero Trust, IAM, MFA et gestion des identités.
- **\[Analyse\] Priorité** : Modérée — Score 48 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Vérifier si Cisco est utilisé dans le SI (inventaire potentiellement incomplet) ; sinon, classer l'information comme non applicable. (2) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-20127 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Présence éventuelle dans le parc à confirmer : Cisco. Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


## 8. Évolutions technologiques pertinentes

| Thème | Éléments | Surveillé |
|---|---|---|
| Intelligence artificielle et IA générative | 61 | oui |
| Sécurité du cloud, des conteneurs et de la chaîne logicielle | 44 | oui |
| Zero Trust, IAM, MFA et gestion des identités | 15 | oui |
| SIEM, EDR, XDR, détection et réponse aux incidents | 14 | oui |
| Cryptographie, post-quantique et gestion des secrets | 14 | oui |
| DevSecOps, SBOM et sécurité des dépendances | 10 | oui |
| Nouvelles méthodes de détection, de prévention et de remédiation | 6 | oui |
| Machine learning appliqué à la cybersécurité | 5 | oui |
| Automatisation de la sécurité et SOAR | 4 | oui |


#### php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619

- **URL** : <https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection>
- **Source** : Elastic Security Labs — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : CVE, flaw, RCE, exploitation
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Elastic Security Labs du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Produits cités : PHP, Elastic. Technologies du parc concernées : PHP. Exploitation active confirmée (catalogue CISA KEV). Thèmes : SIEM, EDR, XDR, détection et réponse aux incidents. Extrait original (en) : « CVE-2026-109618 and CVE-2026-109619 are critical PHP core RCE flaws that leaked ahead of disclosure. We cover what is verified, why exploitation converges on a web server spawning a shell, and the Elastic detections developed to catch this behavior. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Confidentialité, Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Critique — Score 108 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-10-31 — urgence : Immédiate (sous 48 h)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits

- **URL** : <https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html>
- **Source** : The Hacker News — publié le 2026-10-28, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : flaw, patch, AI
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de The Hacker News du 2026-10-28. Produits cités : Windows, Safari, Android, Chrome, Linux. Technologies du parc concernées : Microsoft Windows Server, Microsoft Windows 11, Google Chrome / Microsoft Edge. Preuve de concept publique signalée par la source. Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « An unreleased Anthropic AI model found security flaws in Chrome, Safari, Android, Windows, and Linux and chained them into working proof-of-concept exploits, the company said in its latest report. The exploits were built in the lab after the model was prompted, not seen in any real attack, and Anthropic reported every flaw to the vendor first, so \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Microsoft Windows Server (exposition : interne, criticité : elevee, versions du parc : 2019, 2022); Microsoft Windows 11 (exposition : interne, criticité : moyenne, versions du parc : 23H2, 24H2); Google Chrome / Microsoft Edge (exposition : internet, criticité : moyenne, versions du parc : n.c.)
- **Exploitation** : Preuve de concept publique signalée par la source
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Microsoft Windows Server, Microsoft Windows 11, Google Chrome / Microsoft Edge.
- **\[Analyse\] Priorité** : Élevée — Score 64 = 8 (Exploitation active) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de Microsoft Windows Server à comparer avec les versions du parc (2019, 2022). Versions affectées de Microsoft Windows 11 à comparer avec les versions du parc (23H2, 24H2). Versions affectées de Google Chrome / Microsoft Edge à comparer avec les versions du parc (non renseignées). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### New Serious PHP Vulnerabilities Released and Patched

- **URL** : <https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html>
- **Source** : Schneier on Security — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : vulnerabilit, patch, code execution
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Schneier on Security du 2026-10-22. Produits cités : Apache, PHP. Technologies du parc concernées : PHP. Extrait original (en) : « PHP maintainers have released fixes for two critical vulnerabilities: PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical vulnerabilities that can allow unauthenticated remote code execution. All PHP users are strongly encouraged to update immediately.  Who is at risk: all PHP installations serving web requests, including PHP-FPM, Apache with \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 63 = 12 (Gravité technique) + 25 (Présence dans le parc) + 5 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot

- **URL** : <https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/>
- **Source** : AWS Security Blog — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Menace ou campagne d'attaque, Évolution technologique — mots-clés : vulnerabilit, CVE, exploitation, threat intelligence
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de AWS Security Blog du 2026-10-21. CVE citées : CVE-2026-109618, CVE-2026-109619. Exploitation active confirmée (catalogue CISA KEV). Thèmes : SIEM, EDR, XDR, détection et réponse aux incidents, Nouvelles méthodes de détection, de prévention et de remédiation. Extrait original (en) : « Amazon Threat Intelligence identified a PHP2Shell exploitation attempt dating to Oct. 17, 2026, in MadPot telemetry, four days before public disclosure of CVE-2026-109618 and CVE-2026-109619. The exploit attempt originated from an IP address associated with a commercial anonymization network. While the vulnerability was under embargo, the \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-109618 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée; CVE-2026-109619 — CVSS non disponible, EPSS 1.00, KEV : exploitation active confirmée
- **Exploitation** : Exploitation active confirmée (catalogue CISA KEV) (vérifié)
- **\[Analyse\] Impact potentiel** : Confidentialité
- **\[Analyse\] Pertinence** : moyenne — Menace ou pratique générique, potentiellement transposable au SI de l'organisation.
- **\[Analyse\] Priorité** : Élevée — Score 58 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 10 (Thème surveillé) + 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Score CVSS de CVE-2026-109618 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Score CVSS de CVE-2026-109619 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Cloudflare deploys protections against php2shell vulnerability

- **URL** : <https://blog.cloudflare.com/php-vulnerabilities-waf-protection/>
- **Source** : Cloudflare Blog — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Vulnérabilité ou correctif — mots-clés : cloud, vulnerabilit
- **\[Analyse\] Résumé** : Évolution technologique — publication de Cloudflare Blog du 2026-10-21. Produits cités : PHP. Technologies du parc concernées : PHP. Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « Cloudflare has deployed default web application firewall (WAF) protections for newly disclosed PHP vulnerabilities before public disclosure. The rules use request and response signals to stop exploit attempts and prevent exposed data from reaching attackers. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Confidentialité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 56 = 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise

- **URL** : <https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/>
- **Source** : Microsoft Security Blog — publié le 2026-10-21, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Menace ou campagne d'attaque — mots-clés : AI, agentic, supply chain, campaign
- **\[Analyse\] Résumé** : Évolution technologique — publication de Microsoft Security Blog du 2026-10-21. Produits cités : Microsoft, ConnectWise. Technologies du parc concernées : Microsoft 365 / Exchange Online. Thèmes : Intelligence artificielle et IA générative, Machine learning appliqué à la cybersécurité, Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « Storm-0940 used ARTEX agentic AI to accelerate a ConnectWise supply chain compromise, enabling application credential abuse across Microsoft 365 environments. The post AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise appeared first on Microsoft Security Blog. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Microsoft 365 / Exchange Online (exposition : internet, criticité : elevee, versions du parc : n.c.)
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Confidentialité, Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Microsoft 365 / Exchange Online.
- **\[Analyse\] Priorité** : Élevée — Score 56 = 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de Microsoft 365 / Exchange Online à comparer avec les versions du parc (non renseignées). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Introducing the Cloudflare PHP Capture the Flag challenge

- **URL** : <https://blog.cloudflare.com/php-ctf/>
- **Source** : Cloudflare Blog — publié le 2026-10-27, consulté le 2026-10-29
- **Catégorie** : Évolution technologique — mots-clés : cloud, introducing
- **\[Analyse\] Résumé** : Évolution technologique — publication de Cloudflare Blog du 2026-10-27. Produits cités : PHP. Technologies du parc concernées : PHP. Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « We are launching a PHP Capture the Flag challenge integrated with our Bug Bounty program to test our WAF protections. Security researchers are invited to bypass our defenses and capture the flag to help make the Internet safer. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PHP (exposition : internet, criticité : elevee, versions du parc : 8.2)
- **\[Analyse\] Impact potentiel** : Intégrité
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PHP.
- **\[Analyse\] Priorité** : Élevée — Score 56 = 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de PHP à comparer avec les versions du parc (8.2). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Chromium: CVE-2026-79108 UI misrepresentation in Web Authentication (Passkeys & Security Keys)

- **URL** : <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79108>
- **Source** : Microsoft — Security Update Guide — publié le 2026-10-28, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : CVE, passkey, authentication
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Microsoft — Security Update Guide du 2026-10-28. CVE citées : CVE-2026-79108. Produits cités : Chromium. Technologies du parc concernées : Google Chrome / Microsoft Edge. Thèmes : Zero Trust, IAM, MFA et gestion des identités. Extrait original (en) : « Information published. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Google Chrome / Microsoft Edge (exposition : internet, criticité : moyenne, versions du parc : n.c.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-79108 — CVSS non disponible, EPSS 0.00
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Google Chrome / Microsoft Edge.
- **\[Analyse\] Priorité** : Élevée — Score 53 = 25 (Présence dans le parc) + 15 (Exposition) + 3 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Score CVSS de CVE-2026-79108 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de Google Chrome / Microsoft Edge à comparer avec les versions du parc (non renseignées). Résumé de la source très court : analyse fondée essentiellement sur le titre, consulter l'article.


#### Chromium: CVE-2026-79178 Incorrect authorization in Web Authentication (Passkeys & Security Keys)

- **URL** : <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79178>
- **Source** : Microsoft — Security Update Guide — publié le 2026-10-28, consulté le 2026-10-29
- **Catégorie** : Vulnérabilité ou correctif, Évolution technologique — mots-clés : CVE, passkey, authentication
- **\[Analyse\] Résumé** : Vulnérabilité ou correctif — publication de Microsoft — Security Update Guide du 2026-10-28. CVE citées : CVE-2026-79178. Produits cités : Chromium. Technologies du parc concernées : Google Chrome / Microsoft Edge. Thèmes : Zero Trust, IAM, MFA et gestion des identités. Extrait original (en) : « Information published. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Google Chrome / Microsoft Edge (exposition : internet, criticité : moyenne, versions du parc : n.c.)
- **\[Donnée vérifiée\] CVE** : CVE-2026-79178 — CVSS non disponible, EPSS 0.00
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Google Chrome / Microsoft Edge.
- **\[Analyse\] Priorité** : Élevée — Score 53 = 25 (Présence dans le parc) + 15 (Exposition) + 3 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-05 — urgence : Forte (sous 7 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Score CVSS de CVE-2026-79178 non disponible (NVD non encore interrogé) : ne pas l'estimer, consulter l'avis éditeur. Versions affectées de Google Chrome / Microsoft Edge à comparer avec les versions du parc (non renseignées). Résumé de la source très court : analyse fondée essentiellement sur le titre, consulter l'article.


#### First harmonised standard supporting the AI Act published in the Official Journal

- **URL** : <https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal>
- **Source** : Commission européenne — Stratégie numérique (filtrée) — publié le 2026-10-19, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Évolution normative, Évolution technologique — mots-clés : Official Journal, AI Act, legal, ISO, IEC, standard, artificial intelligence, AI
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de Commission européenne — Stratégie numérique (filtrée) du 2026-10-19. Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « First harmonised standard supporting the AI Act published in the Official Journal Anonymous (not verified) Mon, 10/19/2026 - 09:37 The European Commission has published the reference to the first harmonised standard supporting the implementation of the AI Act in the Official Journal of the European Union. The standard, EN 18286:2026 - Artificial \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 48 = 30 (Importance réglementaire / normative) + 8 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Évaluer l'impact de l'évolution de « ISO/IEC 42001 — Système de management de l'IA » (norme volontaire) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (3) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### Deploying, maintaining, and migrating production n8n on EKS

- **URL** : <https://www.cncf.io/blog/2026/10/16/deploying-maintaining-and-migrating-production-n8n-on-eks/>
- **Source** : CNCF — Blog — publié le 2026-10-16, consulté le 2026-10-29
- **Catégorie** : Évolution technologique — mots-clés : container
- **\[Analyse\] Résumé** : Évolution technologique — publication de CNCF — Blog du 2026-10-16. Produits cités : PostgreSQL, Redis. Technologies du parc concernées : PostgreSQL. Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « n8n is easy to try and harder to run under production traffic. A single container with SQLite works great for a quick demo. Production is a different story entirely. You need workers, webhook processors, PostgreSQL, Redis,... » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : PostgreSQL (exposition : interne, criticité : critique, versions du parc : 15)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : PostgreSQL.
- **\[Analyse\] Priorité** : Modérée — Score 45 = 25 (Présence dans le parc) + 10 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de PostgreSQL à comparer avec les versions du parc (15). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### Managing identity source transition for AWS IAM Identity Center

- **URL** : <https://aws.amazon.com/blogs/security/managing-identity-source-transition-for-aws-iam-identity-center/>
- **Source** : AWS Security Blog — publié le 2026-10-20, consulté le 2026-10-29
- **Catégorie** : Évolution technologique — mots-clés : identity, IAM, automation
- **\[Analyse\] Résumé** : Évolution technologique — publication de AWS Security Blog du 2026-10-20. Produits cités : Active Directory. Technologies du parc concernées : Active Directory / Entra ID. Thèmes : Automatisation de la sécurité et SOAR, Zero Trust, IAM, MFA et gestion des identités, Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « October 20, 2026: This post was republished to reflect the new migration capability from Active Directory to an external identity provider (IdP) or the Identity Center directory, now available in IAM Identity Center. September 2, 2026: This post was republished to include Active Directory migration strategies and automation for permission sets. \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Parc concerné** : Active Directory / Entra ID (exposition : interne, criticité : critique, versions du parc : n.c.)
- **\[Analyse\] Pertinence** : forte — Technologie(s) du parc citée(s) : Active Directory / Entra ID.
- **\[Analyse\] Priorité** : Modérée — Score 45 = 25 (Présence dans le parc) + 10 (Impact sur les activités) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Versions affectées de Active Directory / Entra ID à comparer avec les versions du parc (non renseignées). Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


## 9. Veille réglementaire


### Textes surveillés et orientation d'applicabilité

> Orientation calculée à partir du profil déclaré : elle ne constitue pas un avis juridique et doit être confirmée par le juriste ou le DPO. Statuts et dates issus du référentiel de configuration (vérifié le indiqué), à revérifier sur les sources officielles.

| Texte | Nature | Statut (référentiel) | Applicabilité (orientation) | Motif |
|---|---|---|---|---|
| RGPD — Règlement général sur la protection des données | Obligation légale (texte contraignant) | Applicable | Applicabilité probable — à confirmer | L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). |
| NIS 2 — Directive sur la sécurité des réseaux et des systèmes d'information | Obligation légale (texte contraignant) | Adopté (UE) — transposition nationale à vérifier | Applicabilité probable — à confirmer | Le secteur déclaré figure dans les annexes de NIS 2 et la taille atteint le seuil des entités moyennes. L'organisation a déclaré cette exigence (à confirmer). |
| DORA — Résilience opérationnelle numérique du secteur financier | Obligation légale (texte contraignant) | Applicable | Applicabilité peu probable en l'état des informations | Organisation non financière et pas de rôle de prestataire TIC du secteur financier déclaré. |
| AI Act — Règlement européen sur l'intelligence artificielle | Obligation légale (texte contraignant) | Application progressive | Applicabilité probable — à confirmer | L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). |
| CRA — Règlement sur la cyberrésilience | Obligation légale (texte contraignant) | Application progressive | Applicabilité peu probable en l'état des informations | Aucune activité d'édition logicielle ou de fabrication de produits numériques déclarée ; impact indirect via les fournisseurs (SBOM, support). |
| eIDAS 2 — Identité numérique européenne et services de confiance | Obligation légale (texte contraignant) | Application progressive | Applicabilité peu probable en l'état des informations | Pas de rôle de prestataire de services de confiance déclaré ; usage possible de la signature électronique à vérifier. |
| Dispositif OIV (loi de programmation militaire) | Obligation légale (texte contraignant) | Applicable | Applicabilité peu probable en l'état des informations | Aucune désignation OIV déclarée (une désignation fait l'objet d'une notification de l'État). |
| Certification Hébergeur de Données de Santé (HDS) | Obligation légale (texte contraignant) | Applicable | Applicabilité probable — à confirmer | L'organisation déclare héberger des données de santé pour le compte de tiers. L'organisation a déclaré cette exigence (identifiée). |


### Évolutions détectées sur la période


#### \[Modérée\] First harmonised standard supporting the AI Act published in the Official Journal

- **URL** : <https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal>
- **Source** : Commission européenne — Stratégie numérique (filtrée) — publié le 2026-10-19, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Évolution normative, Évolution technologique — mots-clés : Official Journal, AI Act, legal, ISO, IEC, standard, artificial intelligence, AI
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de Commission européenne — Stratégie numérique (filtrée) du 2026-10-19. Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « First harmonised standard supporting the AI Act published in the Official Journal Anonymous (not verified) Mon, 10/19/2026 - 09:37 The European Commission has published the reference to the first harmonised standard supporting the implementation of the AI Act in the Official Journal of the European Union. The standard, EN 18286:2026 - Artificial \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Publication officielle
- **\[Analyse\] Statut juridique** : Publié (selon la source) — à confirmer
- **Texte concerné : AI Act — Règlement européen sur l'intelligence artificielle** : Règlement (UE) 2024/1689 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). Organisations concernées : Fournisseurs, déployeurs, importateurs et distributeurs de systèmes d'IA mis sur le marché ou utilisés dans l'UE.
- **Obligations possibles (à vérifier)** : Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50)
- **Démarches pour qualifier l'applicabilité** : Inventorier les usages d'IA (y compris IA générative en libre-service); Qualifier le rôle (fournisseur ou déployeur) pour chaque système; Vérifier si un usage relève de l'annexe III (haut risque)
- **\[Analyse\] Impact potentiel** : AI Act — Règlement européen sur l'intelligence artificielle — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 48 = 30 (Importance réglementaire / normative) + 8 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Évaluer l'impact de l'évolution de « ISO/IEC 42001 — Système de management de l'IA » (norme volontaire) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (3) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Application du chapitre V de la loi européenne sur l'IA

- **URL** : <https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/?utm_source=rss&utm_medium=rss&utm_campaign=enforcement-of-chapter-v-under-the-eu-ai-act>
- **Source** : artificialintelligenceact.eu (non officiel) — publié le n.c., consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Évolution technologique — mots-clés : loi , AI Act, IA, AI
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de artificialintelligenceact.eu (non officiel) (date de publication non fournie). Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « This page aims to provide an overview of the EU AI Act’s enforcement provisions relating to Chapter V, namely the provisions that impose obligations on providers of general-purpose AI (GPAI) models. It also aims to explore the role that other actors can play in the enforcement of the AI Act. Summary Coming up in this \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Évolution à qualifier
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **Texte concerné : AI Act — Règlement européen sur l'intelligence artificielle** : Règlement (UE) 2024/1689 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). Organisations concernées : Fournisseurs, déployeurs, importateurs et distributeurs de systèmes d'IA mis sur le marché ou utilisés dans l'UE.
- **Obligations possibles (à vérifier)** : Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50)
- **Démarches pour qualifier l'applicabilité** : Inventorier les usages d'IA (y compris IA générative en libre-service); Qualifier le rôle (fournisseur ou déployeur) pour chaque système; Vérifier si un usage relève de l'annexe III (haut risque)
- **\[Analyse\] Impact potentiel** : AI Act — Règlement européen sur l'intelligence artificielle — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 40 = 30 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] La thérapie par IA au regard de la loi européenne sur l'IA

- **URL** : <https://artificialintelligenceact.eu/ai-therapy-under-the-eu-ai-act/?utm_source=rss&utm_medium=rss&utm_campaign=ai-therapy-under-the-eu-ai-act>
- **Source** : artificialintelligenceact.eu (non officiel) — publié le n.c., consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Évolution technologique — mots-clés : loi , AI Act, IA, AI
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de artificialintelligenceact.eu (non officiel) (date de publication non fournie). Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « This page aims to provide an overview of AI systems, and in particular general-purpose AI (GPAI) systems, used for the purpose of therapy or emotional support under the AI Act. It explores the obligations of providers of these AI systems both on the system as well as on the model level. Summary Coming up in \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Évolution à qualifier
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **Texte concerné : AI Act — Règlement européen sur l'intelligence artificielle** : Règlement (UE) 2024/1689 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). Organisations concernées : Fournisseurs, déployeurs, importateurs et distributeurs de systèmes d'IA mis sur le marché ou utilisés dans l'UE.
- **Obligations possibles (à vérifier)** : Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50)
- **Démarches pour qualifier l'applicabilité** : Inventorier les usages d'IA (y compris IA générative en libre-service); Qualifier le rôle (fournisseur ou déployeur) pour chaque système; Vérifier si un usage relève de l'annexe III (haut risque)
- **\[Analyse\] Impact potentiel** : AI Act — Règlement européen sur l'intelligence artificielle — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 40 = 30 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Le Forum consultatif : qu'est-ce que c'est et comment ça marche ?

- **URL** : <https://artificialintelligenceact.eu/the-advisory-forum-what-is-it-and-how-does-it-work/?utm_source=rss&utm_medium=rss&utm_campaign=the-advisory-forum-what-is-it-and-how-does-it-work>
- **Source** : artificialintelligenceact.eu (non officiel) — publié le n.c., consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : AI Act
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de artificialintelligenceact.eu (non officiel) (date de publication non fournie). Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « The Advisory Forum (the Forum) is a general advisory body to the European Commission and the AI Board, established to provide technical expertise, advise them, and to contribute to their tasks under the EU AI Act. It sits within the Act’s broader governance architecture, as one of the two advisory bodies, in addition to the \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Évolution à qualifier
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **Texte concerné : AI Act — Règlement européen sur l'intelligence artificielle** : Règlement (UE) 2024/1689 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). Organisations concernées : Fournisseurs, déployeurs, importateurs et distributeurs de systèmes d'IA mis sur le marché ou utilisés dans l'UE.
- **Obligations possibles (à vérifier)** : Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50)
- **Démarches pour qualifier l'applicabilité** : Inventorier les usages d'IA (y compris IA générative en libre-service); Qualifier le rôle (fournisseur ou déployeur) pour chaque système; Vérifier si un usage relève de l'annexe III (haut risque)
- **\[Analyse\] Impact potentiel** : AI Act — Règlement européen sur l'intelligence artificielle — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Le groupe d'experts scientifiques indépendants : qu'est-ce que c'est et comment fonctionne-t-il ?

- **URL** : <https://artificialintelligenceact.eu/scientific-panel/?utm_source=rss&utm_medium=rss&utm_campaign=scientific-panel>
- **Source** : artificialintelligenceact.eu (non officiel) — publié le n.c., consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : AI Act
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de artificialintelligenceact.eu (non officiel) (date de publication non fournie). Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « The scientific panel of independent experts (the Scientific Panel) is a body established under the EU AI Act to support the enforcement of rules on general-purpose AI (GPAI) models and systems. It sits within the Act’s broader governance architecture as one of the three advisory bodies, alongside the AI Board ( established under Article 65) \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Évolution à qualifier
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **Texte concerné : AI Act — Règlement européen sur l'intelligence artificielle** : Règlement (UE) 2024/1689 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare utiliser des systèmes d'IA dans un cadre professionnel (déployeur). Organisations concernées : Fournisseurs, déployeurs, importateurs et distributeurs de systèmes d'IA mis sur le marché ou utilisés dans l'UE.
- **Obligations possibles (à vérifier)** : Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50)
- **Démarches pour qualifier l'applicabilité** : Inventorier les usages d'IA (y compris IA générative en libre-service); Qualifier le rôle (fournisseur ou déployeur) pour chaque système; Vérifier si un usage relève de l'annexe III (haut risque)
- **\[Analyse\] Impact potentiel** : AI Act — Règlement européen sur l'intelligence artificielle — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] The Irish Data Protection Commission fines Google EUR 403 000 000 following Inquiry into Google’s processing of location data

- **URL** : <https://www.edpb.europa.eu/news/the-irish-data-protection-commission-fines-google-403-000-000-eur-following-inquiry_en>
- **Source** : EDPB — Actualités — publié le 2026-09-23, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : fine , fines , compliance, GDPR, data protection, legal, supervisory authority, RGPD
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-09-23. Extrait original (en) : « Background information Date of final decision: 21 September 2026 National case Legal Reference(s): Article 5 (Principles relating to processing of personal data), Article 6 (Lawfulness of processing), Article 12 (Transparent information, communication and modalities for the exercise of the rights of the data subject) and Article 13 (Information to \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2018-05-25, 2020-02-04, 2026-09-21
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Dutch DPA fines Uber EUR 824 990 000 for unlawful automated decision-making and insufficient information on profiling

- **URL** : <https://www.edpb.europa.eu/news/dutch-dpa-fines-uber-eur-824-990-000-for-unlawful-automated-decision-making-and-insufficient_en>
- **Source** : EDPB — Actualités — publié le 2026-10-08, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : regulation, fine , fines , fined, CNIL, GDPR, data protection, legal
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-08. Extrait original (en) : « Background information Cross-border case Controller: Uber B.V Legal Reference(s): Article 22 (Automated individual decision making, including profiling) and Article 13 (Information to be provided where personal data are collected from the data subject) Decision: Administrative fine Key words: Automated decision making, profiling and online \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Hellenic DPA decision on a data breach involving E.E.T.A.A. S.A. as processor for the Ministry of Social Cohesion and Family Affairs

- **URL** : <https://www.edpb.europa.eu/news/hellenic-dpa-decision-on-a-data-breach-involving-eetaa-sa-as-processor-for-the-ministry-of_en>
- **Source** : EDPB — Actualités — publié le 2026-10-08, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Incident ou retour d'expérience — mots-clés : fine , fines , compliance, GDPR, data protection, legal, supervisory authority, incident
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-08. Extrait original (en) : « Background information Date of final decision: 28/07/2026 National case Controller: Ministry of Social Cohesion and Family Affairs Legal Reference(s): Article 25 (Data protection by design and by default), Article 28 (Processor), Article 32 (Security of processing), Article 33 (Notification of a personal data breach to the supervisory authority) \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2026-07-28
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Analyser le retour d'expérience et vérifier si le scénario est transposable (fournisseurs, technologies, processus). (2) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Swedish DPA fines Miljödata i Karlskrona approximately EUR 160 000 for insufficient technical and organisational measures to ensure information security

- **URL** : <https://www.edpb.europa.eu/news/swedish-dpa-fines-miljodata-i-karlskrona-approximately-eur-160-000-for-insufficient-technical_en>
- **Source** : EDPB — Actualités — publié le 2026-10-08, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Incident ou retour d'expérience — mots-clés : fine , fines , GDPR, data protection, legal, incident, data breach, breach
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-08. Thèmes : Zero Trust, IAM, MFA et gestion des identités. Extrait original (en) : « Background information Date of final decision: 22/09/2026 National case Legal Reference(s): Article 32 (Security of processing) Decision: Administrative fine Key words: Cybersecurity, personal data breaches Summary of the Decision Origin of the case In August 2025, the IT service provider Miljödata was targeted in a cyberattack, during which a \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2026-09-22
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Analyser le retour d'expérience et vérifier si le scénario est transposable (fournisseurs, technologies, processus). (2) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Italian DPA fines BBVA EUR 5 508 000 for failing to respect a customer’s objection to direct marketing

- **URL** : <https://www.edpb.europa.eu/news/italian-dpa-fines-bbva-eur-5-508-000-for-failing-to-respect-a-customers-objection-to-direct_en>
- **Source** : EDPB — Actualités — publié le 2026-10-09, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : fine , fines , compliance, GDPR, data protection, legal, RGPD
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-09. Extrait original (en) : « Background information Date of final decision: 3 July 2026 National case Controller: Banco Bilbao Vizcaya Argentaria, S.A., Italian branch (BBVA) Legal Reference(s): Article 5 (Principles relating to processing of personal data), Article 12 (Transparent information, communication and modalities for the exercise of the rights of the data subject), \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2026-07-03
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Italian DPA fines Emirates EUR 180 000 for infringements concerning passengers’ health data

- **URL** : <https://www.edpb.europa.eu/news/italian-dpa-fines-emirates-eur-180-000-for-infringements-concerning-passengers-health-data_en>
- **Source** : EDPB — Actualités — publié le 2026-10-09, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : fine , fines , compliance, GDPR, data protection, legal, RGPD
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-09. Extrait original (en) : « Background information Date of final decision: 14 May 2026 National case Controller: Emirates Legal Reference(s): Article 5 (Principles relating to processing of personal data), Article 12 (Transparent information, communication and modalities for the exercise of the rights of the data subject) and Article 13 (Information to be provided where \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2026-05-14
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Italian DPA fines security company EUR 39 000 for violations concerning employees’ data

- **URL** : <https://www.edpb.europa.eu/news/italian-dpa-fines-security-company-eur-39-000-for-violations-concerning-employees-data_en>
- **Source** : EDPB — Actualités — publié le 2026-10-09, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire — mots-clés : fine , fines , compliance, GDPR, data protection, legal, RGPD
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de EDPB — Actualités du 2026-10-09. Extrait original (en) : « Background information Date of final decision: 6 August 2026 National case Controller: La Patria S.p.A. Legal Reference(s): Article 12 (Transparent information, communication and modalities for the exercise of the rights of the data subject), Article 13 (Information to be provided where personal data are collected from the data subject) and \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Nature de l'évolution** : Sanction ou décision d'une autorité
- **\[Analyse\] Statut juridique** : À vérifier sur la source officielle
- **\[Fait\] Dates mentionnées par la source** : 2026-08-06
- **Texte concerné : RGPD — Règlement général sur la protection des données** : Règlement (UE) 2016/679 — Obligation légale (texte contraignant) — Applicabilité probable — à confirmer. L'organisation déclare traiter des données à caractère personnel. L'organisation a déclaré cette exigence (identifiée). Organisations concernées : Tout organisme qui traite des données à caractère personnel (responsable de traitement ou sous-traitant) établi dans l'UE ou ciblant des personnes dans l'UE.
- **Obligations possibles (à vérifier)** : Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35); Encadrement contractuel des sous-traitants (art. 28)
- **Démarches pour qualifier l'applicabilité** : Vérifier dans le registre des traitements les données personnelles effectivement traitées; Qualifier le rôle de l'organisation (responsable de traitement, sous-traitant, responsable conjoint); Consulter le DPO sur l'impact de l'évolution détectée
- **\[Analyse\] Impact potentiel** : RGPD — Règlement général sur la protection des données — Applicabilité probable — à confirmer
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : RGPD — Règlement général sur la protection des données.
- **\[Analyse\] Priorité** : Modérée — Score 30 = 30 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « RGPD — Règlement général sur la protection des données » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


## 10. Veille normative

> Distinction appliquée : une norme (ISO/IEC) ou un référentiel (NIST CSF) est d'application volontaire, une recommandation (ANSSI) n'est pas contraignante ; seuls un texte légal, un contrat ou une certification visée les rendent exigibles. Aucune recommandation n'est présentée comme une obligation légale.

| Référentiel | Nature | Applicabilité (orientation) | Motif |
|---|---|---|---|
| PCI DSS — Sécurité des données de cartes de paiement | Exigence contractuelle | Applicabilité peu probable en l'état des informations | Aucune acceptation de paiement par carte déclarée. |
| ISO/IEC 27001 — Systèmes de management de la sécurité de l'information | Norme volontaire | Applicabilité probable — à confirmer | L'organisation a déclaré ISO/IEC 27001 dans ses exigences (certification ou exigence contractuelle). L'organisation a déclaré cette exigence (identifiée). |
| ISO/IEC 27002 — Mesures de sécurité de l'information | Norme volontaire | Applicabilité probable — à confirmer | Référentiel de mesures associé à une exigence déclarée par l'organisation. |
| ISO/IEC 42001 — Système de management de l'IA | Norme volontaire | Applicabilité à qualifier | Usages d'IA déclarés ; norme volontaire pouvant structurer la conformité AI Act. |
| NIST Cybersecurity Framework 2.0 | Référentiel de bonnes pratiques | Applicabilité à qualifier | Référentiel de bonnes pratiques volontaire. |
| Guide d'hygiène informatique de l'ANSSI et recommandations ANSSI | Recommandation (non contraignante) | Applicabilité à qualifier | Recommandations applicables à toute organisation, sans caractère obligatoire. |
| SecNumCloud — Référentiel de qualification des prestataires cloud | Référentiel de bonnes pratiques | Applicabilité à qualifier | Prestataire numérique travaillant pour l'administration : exigence possible dans les marchés publics. |


### État des normes ISO surveillées (métadonnées ISO Open Data)

| Référence | Stade | Publication | Mise à jour |
|---|---|---|---|
| ISO 22301:2019 | 90.92 — Décision : à réviser | 2019-10-30 | 2026-10-29 |
| ISO 22301:2019/Amd 1:2024 | 60.60 — Norme publiée | 2024-02-23 | 2026-10-29 |
| ISO/IEC 27001:2022 | 60.60 — Norme publiée | 2022-10-25 | 2026-10-29 |
| ISO/IEC 27001:2022/Amd 1:2024 | 60.60 — Norme publiée | 2024-02-23 | 2026-10-29 |
| ISO/IEC 27002:2022 | 60.60 — Norme publiée | 2022-02-15 | 2026-10-29 |
| ISO/IEC 27005:2022 | 60.60 — Norme publiée | 2022-10-25 | 2026-10-29 |
| ISO/IEC 27017:2026 | 60.60 — Norme publiée | 2026-07-27 | 2026-10-29 |
| ISO/IEC 27018:2025 | 60.60 — Norme publiée | 2025-08-26 | 2026-10-29 |
| ISO/IEC 27035-1:2023 | 60.60 — Norme publiée | 2023-02-13 | 2026-10-29 |
| ISO/IEC 27035-2:2023 | 60.60 — Norme publiée | 2023-02-13 | 2026-10-29 |
| ISO/IEC 27035-3:2020 | 90.60 — Examen systématique clos | 2020-09-16 | 2026-10-29 |
| ISO/IEC 27035-4:2024 | 60.60 — Norme publiée | 2024-12-02 | 2026-10-29 |
| ISO/IEC 27701:2025 | 60.60 — Norme publiée | 2025-10-14 | 2026-10-29 |
| ISO/IEC 42001:2023 | 60.60 — Norme publiée | 2023-12-18 | 2026-10-29 |


### Évolutions détectées sur la période


#### \[À qualifier\] Kicking off Cybersecurity Career Week with NIST!

- **URL** : <https://www.nist.gov/blogs/cybersecurity-insights/kicking-cybersecurity-career-week-nist>
- **Source** : NIST — Cybersecurity Insights (blog) — publié le 2026-10-14, consulté le 2026-10-29
- **Catégorie** : Bonne pratique ou recommandation, Évolution normative — mots-clés : awareness, how to, NIST Cybersecurity Framework 2.0
- **\[Analyse\] Résumé** : Bonne pratique ou recommandation — publication de NIST — Cybersecurity Insights (blog) du 2026-10-14. Extrait original (en) : « Considering a career in cybersecurity? Cybersecurity Career Week (CCW), a campaign led by the NICE Program at NIST from October 19-24, 2026, aims to raise public awareness and help people find their path to \#ChooseCyber. During this week, academia, industry, non-profit organizations, and government agencies host events, share resources, provide \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Référentiel de bonnes pratiques
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : a\_qualifier — Applicabilité du texte à qualifier.
- **\[Analyse\] Priorité** : À qualifier — Score 8 = 8 (Importance réglementaire / normative) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : a\_qualifier.
- **\[Recommandation\]** : (1) Évaluer l'impact de l'évolution de « NIST Cybersecurity Framework 2.0 » (référentiel de bonnes pratiques) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (2) Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Échéance proposée** : 2026-11-05 — urgence : Qualification requise (sous 7 jours)
- **Confiance de l'analyse** : moyenne


#### \[Modérée\] First harmonised standard supporting the AI Act published in the Official Journal

- **URL** : <https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal>
- **Source** : Commission européenne — Stratégie numérique (filtrée) — publié le 2026-10-19, consulté le 2026-10-29
- **Catégorie** : Évolution réglementaire, Évolution normative, Évolution technologique — mots-clés : Official Journal, AI Act, legal, ISO, IEC, standard, artificial intelligence, AI
- **\[Analyse\] Résumé** : Évolution réglementaire — publication de Commission européenne — Stratégie numérique (filtrée) du 2026-10-19. Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « First harmonised standard supporting the AI Act published in the Official Journal Anonymous (not verified) Mon, 10/19/2026 - 09:37 The European Commission has published the reference to the first harmonised standard supporting the implementation of the AI Act in the Official Journal of the European Union. The standard, EN 18286:2026 - Artificial \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Obligation légale (texte contraignant)
- **Avertissement** : Texte contraignant : vérifier le champ d'application.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : AI Act — Règlement européen sur l'intelligence artificielle.
- **\[Analyse\] Priorité** : Modérée — Score 48 = 30 (Importance réglementaire / normative) + 8 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. (2) Évaluer l'impact de l'évolution de « ISO/IEC 42001 — Système de management de l'IA » (norme volontaire) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (3) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : moyenne
- **\[À vérifier\]** : Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Modérée\] Localizing compliance at scale: achieving South Korea’s ISMS certification

- **URL** : <https://blog.cloudflare.com/k-isms/>
- **Source** : Cloudflare Blog — publié le 2026-10-22, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Évolution réglementaire, Évolution normative — mots-clés : cloud, compliance, certification, ISO/IEC 27001
- **\[Analyse\] Résumé** : Évolution technologique — publication de Cloudflare Blog du 2026-10-22. Produits cités : Edge. Thèmes : Sécurité du cloud, des conteneurs et de la chaîne logicielle, Cryptographie, post-quantique et gestion des secrets. Extrait original (en) : « Cloudflare has achieved South Korea's ISMS certification following an audit across 80 controls. Learn how we localized user consent flows, adapted social sign-up paths at the edge, and validated our global security program. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Norme volontaire
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **Produits cités** : Edge
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : forte — Texte ou référentiel dont l'applicabilité est probable : ISO/IEC 27001 — Systèmes de management de la sécurité de l'information.
- **\[Analyse\] Priorité** : Modérée — Score 25 = 15 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **\[Recommandation\]** : (1) Évaluer l'impact de l'évolution de « ISO/IEC 27001 — Systèmes de management de la sécurité de l'information » (norme volontaire) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2026-11-28 — urgence : Normale (sous 30 jours)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Faible\] NIST Report Provides Guidelines for Transition to Post-Quantum Cryptography Standards

- **URL** : <https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-transition-post-quantum-cryptography>
- **Source** : NIST — Actualités (filtrées sécurité) — publié le 2026-10-27, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Évolution normative — mots-clés : post-quantum, quantum, cryptograph, standard, NIST Cybersecurity Framework 2.0
- **\[Analyse\] Résumé** : Évolution technologique — publication de NIST — Actualités (filtrées sécurité) du 2026-10-27. Thèmes : Cryptographie, post-quantique et gestion des secrets. Extrait original (en) : « This report describes the timelines and migration activities for federal agencies, and it can serve as a key resource for technology providers and organizations that are developing their quantum-readiness road maps. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Référentiel de bonnes pratiques
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Cryptographie, post-quantique et gestion des secrets.
- **\[Analyse\] Priorité** : Faible — Score 18 = 8 (Importance réglementaire / normative) + 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Évaluer l'impact de l'évolution de « NIST Cybersecurity Framework 2.0 » (référentiel de bonnes pratiques) sur le SMSI, la déclaration d'applicabilité et les engagements contractuels. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : moyenne


#### \[Faible\] NIK C2: The new AI-enabled command-and-control framework

- **URL** : <https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/>
- **Source** : Cisco Talos Intelligence — publié le 2026-10-29, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Évolution technologique, Évolution normative — mots-clés : C2, AI, framework
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de Cisco Talos Intelligence du 2026-10-29. Produits cités : Cisco. Thèmes : Intelligence artificielle et IA générative. Extrait original (en) : « Cisco Talos observed a new AI-integrated command-and-control (C2) framework in the wild called “NIK C2.” » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Référentiel de bonnes pratiques
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **Produits cités** : Cisco
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Intelligence artificielle et IA générative.
- **\[Analyse\] Priorité** : Faible — Score 18 = 10 (Thème surveillé) + 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Présence éventuelle dans le parc à confirmer : Cisco. Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Faible\] AWS Continuum sets a new standard in autonomous code security

- **URL** : <https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/>
- **Source** : AWS Security Blog — publié le 2026-10-05, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Évolution normative — mots-clés : AI, standard
- **\[Analyse\] Résumé** : Évolution technologique — publication de AWS Security Blog du 2026-10-05. Produits cités : Teams. Thèmes : Intelligence artificielle et IA générative, Sécurité du cloud, des conteneurs et de la chaîne logicielle. Extrait original (en) : « As AI models become more capable, they uncover more security vulnerabilities and identify increasingly sophisticated paths to exploit them, raising the bar for how quickly defenders must respond. Security teams now face more potential vulnerabilities than their existing processes were designed to handle — each requiring investigation, \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Recommandation (non contraignante)
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **Produits cités** : Teams
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Intelligence artificielle et IA générative, Sécurité du cloud, des conteneurs et de la chaîne logicielle.
- **\[Analyse\] Priorité** : Faible — Score 10 = 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


#### \[Faible\] Introducing Privateer: AI-Assisted Security & Compliance Evaluation Framework Joins the OpenSSF Sandbox

- **URL** : <https://openssf.org/blog/2026/10/13/introducing-privateer-ai-assisted-security-compliance-evaluation-framework-joins-the-openssf-sandbox/>
- **Source** : OpenSSF — Blog — publié le 2026-10-13, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Évolution normative, Évolution réglementaire — mots-clés : AI, introducing, framework, compliance
- **\[Analyse\] Résumé** : Évolution technologique — publication de OpenSSF — Blog du 2026-10-13. Thèmes : Intelligence artificielle et IA générative, Machine learning appliqué à la cybersécurité. Extrait original (en) : « Discover Privateer, a new plugin-based, AI-assisted security and compliance evaluation framework that has officially joined the OpenSSF Sandbox under the ORBIT Working Group. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Référentiel de bonnes pratiques
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Intelligence artificielle et IA générative, Machine learning appliqué à la cybersécurité.
- **\[Analyse\] Priorité** : Faible — Score 10 = 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Identifier le texte concerné et qualifier son applicabilité (secteur, taille, rôle de l'organisation). (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité). Statut juridique, dates et champ d'application à confirmer sur le texte officiel (EUR-Lex, Légifrance).


#### \[Faible\] Design Tenets for Agent Identity Management Systems

- **URL** : <https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems>
- **Source** : NIST — Cybersecurity Insights (blog) — publié le 2026-10-27, consulté le 2026-10-29
- **Catégorie** : Évolution technologique, Évolution normative — mots-clés : agentic, authentication, identity, IAM, public comment
- **\[Analyse\] Résumé** : Évolution technologique — publication de NIST — Cybersecurity Insights (blog) du 2026-10-27. Thèmes : Intelligence artificielle et IA générative, Zero Trust, IAM, MFA et gestion des identités. Extrait original (en) : « This is blog \#2 in our series on agentic identity, authentication and authorization. Our other post can be found via Post \#1. In our last blog post, we highlighted the essential nature of having fundamentally sound identity and access management (IAM) capabilities as a precursor to implementing agents at scale. We started to form the core of what \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Recommandation (non contraignante)
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : Intelligence artificielle et IA générative, Zero Trust, IAM, MFA et gestion des identités.
- **\[Analyse\] Priorité** : Faible — Score 10 = 10 (Thème surveillé) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : moyenne


#### \[Faible\] Securing Water and Wastewater Operational Technology Environments

- **URL** : <https://www.nist.gov/blogs/cybersecurity-insights/securing-water-and-wastewater-operational-technology-environments>
- **Source** : NIST — Cybersecurity Insights (blog) — publié le 2026-10-01, consulté le 2026-10-29
- **Catégorie** : Incident ou retour d'expérience, Évolution normative — mots-clés : incident, cyberattack
- **\[Analyse\] Résumé** : Incident ou retour d'expérience — publication de NIST — Cybersecurity Insights (blog) du 2026-10-01. Extrait original (en) : « Recent cyberattacks on the U.S. water and wastewater systems (WWS) sector are highlighting the escalating threat to our nation’s critical infrastructure and the practical challenges of securing it. These incidents underscore an important challenge: the connectivity that utilities depend upon must be designed and operated with security as a core \[…\] » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Recommandation (non contraignante)
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Menace ou pratique générique, potentiellement transposable au SI de l'organisation.
- **\[Analyse\] Priorité** : Faible — Score 8 = 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Analyser le retour d'expérience et vérifier si le scénario est transposable (fournisseurs, technologies, processus).
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : moyenne


#### \[Faible\] Case Study: GitHub Expands Malware Advisories Across Eight Ecosystems with OpenSSF

- **URL** : <https://openssf.org/blog/2026/10/16/case-study-github-expands-malware-advisories-across-eight-ecosystems-with-openssf/>
- **Source** : OpenSSF — Blog — publié le 2026-10-16, consulté le 2026-10-29
- **Catégorie** : Menace ou campagne d'attaque, Évolution normative — mots-clés : malware
- **\[Analyse\] Résumé** : Menace ou campagne d'attaque — publication de OpenSSF — Blog du 2026-10-16. Produits cités : GitHub. Thèmes : DevSecOps, SBOM et sécurité des dépendances. Extrait original (en) : « Learn how GitHub integrated OpenSSF's malicious-package data into its Advisory Database to expand Dependabot malware alerts across eight ecosystems. » (Synthèse automatique par règles, sans traduction : se référer à l'article original.)
- **\[Analyse\] Type de document** : Recommandation (non contraignante)
- **Avertissement** : Une norme, un référentiel ou une recommandation ne constitue pas une obligation légale, sauf si un texte, un contrat ou une certification visée la rend exigible.
- **Produits cités** : GitHub
- **Exploitation** : Aucune information d'exploitation
- **\[Analyse\] Impact potentiel** : Conformité
- **\[Analyse\] Pertinence** : moyenne — Thème surveillé : DevSecOps, SBOM et sécurité des dépendances.
- **\[Analyse\] Priorité** : Faible — Score 8 = 8 (Menace transposable) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : moyenne.
- **\[Recommandation\]** : (1) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Échéance proposée** : 2027-01-27 — urgence : Faible (prochaine revue de veille)
- **Confiance de l'analyse** : faible
- **\[À vérifier\]** : Présence éventuelle dans le parc à confirmer : GitHub. Source secondaire : recouper avec une source primaire (éditeur, CERT-FR, autorité).


## 11. Analyse des impacts pour l'organisation


### Actifs du parc concernés

| Technologie | Exposition | Criticité | Éléments | Priorité max. |
|---|---|---|---|---|
| Google Chrome / Microsoft Edge | internet | moyenne | 151 | Élevée |
| Debian | interne | moyenne | 30 | Modérée |
| PHP | internet | elevee | 24 | Critique |
| Microsoft Windows Server | interne | elevee | 14 | Critique |
| Microsoft Windows 11 | interne | moyenne | 14 | Critique |
| Kubernetes | interne | elevee | 8 | Modérée |
| Ubuntu Server | dmz | elevee | 5 | Élevée |
| Fortinet FortiGate (VPN SSL) | internet | critique | 4 | Critique |
| VMware ESXi / vCenter | interne | critique | 4 | Élevée |
| Microsoft 365 / Exchange Online | internet | elevee | 4 | Élevée |
| GitLab | internet | elevee | 3 | Critique |
| Veeam Backup & Replication | interne | critique | 3 | Élevée |
| Nginx | internet | elevee | 2 | Élevée |
| PostgreSQL | interne | critique | 2 | Modérée |
| Active Directory / Entra ID | interne | critique | 2 | Modérée |

**\[Analyse\]** Types d'impact potentiels (éléments de priorité modérée ou plus) : Intégrité (82), Disponibilité (57), Confidentialité (49), Conformité (23).

**\[Hypothèse\]** Les impacts sont des potentialités déduites du contenu des sources et du profil déclaré ; l'exposition réelle doit être confirmée par une vérification sur le SI (aucun scan n'est réalisé par l'outil).


## 12. Obligations potentielles à vérifier et échéances

| Texte | Applicabilité | Obligations possibles (à vérifier) | Échéances | Remarques / sources |
|---|---|---|---|---|
| RGPD | Applicabilité probable — à confirmer | Tenue du registre des traitements (art. 30); Sécurité des traitements adaptée au risque (art. 32); Notification des violations de données à la CNIL sous 72 h (art. 33) et aux personnes si risque élevé (art. 34); Analyse d'impact (AIPD) pour les traitements à risque élevé (art. 35) | En vigueur depuis 2018-05-25 |  Sources : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679 |
| NIS 2 | Applicabilité probable — à confirmer | Enregistrement auprès de l'autorité nationale (ANSSI); Mesures de gestion des risques cyber (art. 21) approuvées par les organes de direction (art. 20); Notification des incidents importants : alerte précoce 24 h, notification 72 h, rapport final 1 mois (art. 23); Sécurité de la chaîne d'approvisionnement | En vigueur depuis 2024-10-18 | En France, la transposition passe par la loi relative à la résilience des infrastructures critiques et au renforcement de la cybersécurité et ses décrets d'application : le statut de publication et les dates d'entrée en vigueur nationales sont à vérifier sur Légifrance et sur le site de l'ANSSI. Sources : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022L2555, https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2690 |
| AI Act | Applicabilité probable — à confirmer | Recenser les systèmes d'IA utilisés ou développés et les classer par niveau de risque; Maîtrise de l'IA (formation) du personnel concerné (art. 4); Obligations des déployeurs de systèmes à haut risque (art. 26); Obligations de transparence (art. 50) | 2027-08-02 : Systèmes à haut risque intégrés à des produits réglementés (annexe I) | Le calendrier d'application de certaines obligations (notamment haut risque) a fait l'objet de propositions de modification par la Commission (« omnibus numérique », 2025). Les dates ci-dessus sont celles du texte initial : le calendrier en vigueur doit être vérifié sur EUR-Lex. Sources : https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689, https://ai-act-service-desk.ec.europa.eu/ |
| Certification Hébergeur de Données de Santé (HDS) | Applicabilité probable — à confirmer | Certification HDS de l'hébergeur (référentiel s'appuyant notamment sur ISO/IEC 27001) | À vérifier |  Sources : https://esante.gouv.fr/produits-services/hds |

**\[À vérifier\]** Ces obligations sont « possibles » : elles dépendent de la qualification juridique de l'organisation. Les dates proviennent des textes officiels référencés et doivent être revérifiées.


## 13. Opportunités d'amélioration

- **\[Recommandation\] Critique** : php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619 (Elastic Security Labs) — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Critique** : Critical security issue affecting PHP (NCSC (Royaume-Uni) — Publications) — Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration. Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Critique** : Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619) (AWS Security Blog) — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits (The Hacker News) — Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : New Serious PHP Vulnerabilities Released and Patched (Schneier on Security) — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot (AWS Security Blog) — Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Cloudflare deploys protections against php2shell vulnerability (Cloudflare Blog) — Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise (Microsoft Security Blog) — Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Introducing the Cloudflare PHP Capture the Flag challenge (Cloudflare Blog) — Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée. Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Chromium: CVE-2026-79108 UI misrepresentation in Web Authentication (Passkeys & Security Keys) (Microsoft — Security Update Guide) — Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Élevée** : Chromium: CVE-2026-79178 Incorrect authorization in Web Authentication (Passkeys & Security Keys) (Microsoft — Security Update Guide) — Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.
- **\[Recommandation\] Modérée** : First harmonised standard supporting the AI Act published in the Official Journal (Commission européenne — Stratégie numérique (filtrée)) — Qualifier l'applicabilité de « AI Act — Règlement européen sur l'intelligence artificielle » avec le juriste/DPO puis, si applicable, réaliser une analyse d'écarts et mettre à jour le registre des exigences. Bénéfice attendu : amélioration de la sécurité ou de l'efficacité ; risques et prérequis à évaluer.


## 14. Plan d'action priorisé

| \# | Priorité | Constat / action proposée | Responsable | Échéance | Effort | Statut |
|---|---|---|---|---|---|---|
| 101 | Critique | CISA Adds Two Known Exploited Vulnerabilities to Catalog → Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 104 | Critique | CISA Adds Two Known Exploited Vulnerabilities to Catalog → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 107 | Critique | \[KEV\] CVE-2026-97229 — GitLab Community Edition and Enterprise Edition : GitLab Community Edition and Enterprise Edition Integer Overflow or → Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 109 | Critique | \[KEV\] CVE-2026-46300 — Linux Kernel : Linux Kernel Missing Initialization of a Variable Vulnerability → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 110 | Critique | \[KEV\] CVE-2026-109618 — PHP Group PHP : PHP Memory Corruption Vulnerability → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 111 | Critique | \[KEV\] CVE-2026-109619 — PHP Group PHP : PHP Stale Internal Request-State Vulnerability → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 112 | Critique | \[KEV\] CVE-2025-61624 — Fortinet Multiple Products : Fortinet Multiple Products Path Traversal Vulnerability → Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 126 | Critique | Vulnerabilities in PHP Affecting Cisco Products: October 2026 → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 161 | Critique | Critical security issue affecting PHP → Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration. | RSSI / administrateurs systèmes | 2026-10-31 | Faible | À étudier |
| 162 | Critique | Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | RSSI / équipe de supervision (SOC) | 2026-10-31 | Faible | À étudier |
| 163 | Critique | Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant → Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire  | RSSI / équipe de supervision (SOC) | 2026-10-31 | Faible | À étudier |
| 166 | Critique | Critical RCE vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619) → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 169 | Critique | Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open → Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 176 | Critique | CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 177 | Critique | PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw → Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 181 | Critique | Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619) → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 193 | Critique | php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619 → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-10-31 | Moyen | À étudier |
| 75 | Élevée | InfraTrust report warns of exploited flaws in critical network infrastructure → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 76 | Élevée | \[Màj\] Multiples vulnérabilités dans PHP (21 octobre 2026) → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 99 | Élevée | Multiples vulnérabilités dans Veeam Backup for Microsoft 365 (29 octobre 2026) → Vérifier la présence et les versions de Microsoft 365 / Exchange Online, Veeam Backup & Replication concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En a | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 102 | Élevée | CISA Adds Two Known Exploited Vulnerabilities to Catalog → Vérifier la présence et les versions de VMware ESXi / vCenter concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) Rechercher des traces d'exploitation dans  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 106 | Élevée | Siemens RUGGEDCOM CROSSBOW Station Access Controller → Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11 concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 108 | Élevée | \[KEV\] CVE-2026-41709 — Broadcom VMware ESX : Broadcom VMWare ESX Insufficient Logging Vulnerability → Vérifier la présence et les versions de VMware ESXi / vCenter concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) Rechercher des traces d'exploitation dans  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 113 | Élevée | \[KEV\] CVE-2026-96951 — Microsoft Windows : Microsoft Windows Command Injection Vulnerability → Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11 concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) Rechercher des tr | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 122 | Élevée | I had plans for that second → Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. | RSSI / équipe de supervision (SOC) | 2026-11-05 | Faible | À étudier |
| 123 | Élevée | Two critical RCEs in PHP core → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 130 | Élevée | Cisco IOS XE Software Security Hardening Release: August 2026 → Vérifier la présence et les versions de Cisco Catalyst (commutation) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) Rechercher des traces d'exploitatio | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 131 | Élevée | Cybermalveillance.gouv.fr lance une AlerteCyber concernant deux failles de sécurité critiques dans PHP → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 132 | Élevée | AlerteCyber : Failles de sécurité critiques dans PHP → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | RSSI / équipe de supervision (SOC) | 2026-11-05 | Faible | À étudier |
| 136 | Élevée | Double free in signal handler → Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 137 | Élevée | GUI Denial of Service → Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 155 | Élevée | Widespread PHP Flaw May Cause Many Site Outages Today → Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage de | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 156 | Élevée | AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise → Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits. Puis : (2) Étude d'opportunité : évaluer bénéfices, risques et prérequis de sécurité pour l'organisation avant toute expérimentation encadrée. | DSI / RSSI (étude d'opportunité) | 2026-11-05 | Moyen | À étudier |
| 158 | Élevée | Chromium: CVE-2026-79178 Incorrect authorization in Web Authentication (Passkeys & Security Keys) → Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduir | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 159 | Élevée | Chromium: CVE-2026-79260 Improper input validation in Cookies → Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduir | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 160 | Élevée | Chromium: CVE-2026-79108 UI misrepresentation in Web Authentication (Passkeys & Security Keys) → Vérifier la présence et les versions de Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduir | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 171 | Élevée | China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility → Vérifier la présence et les versions de VMware ESXi / vCenter concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) Rechercher des traces d'exploitation dans  | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 173 | Élevée | Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits → Vérifier la présence et les versions de Microsoft Windows Server, Microsoft Windows 11, Google Chrome / Microsoft Edge concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement pri | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 179 | Élevée | USN-8955-1: nginx vulnerabilities → Vérifier la présence et les versions de Ubuntu Server, Nginx concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposi | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |
| 180 | Élevée | USN-8951-1: c-ares vulnerabilities → Vérifier la présence et les versions de Ubuntu Server concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (f | Équipe infrastructure / exploitation (pilotage RSSI) | 2026-11-05 | Moyen | À étudier |

34 actions supplémentaires sont consultables dans l'outil (page Plan d'action).


### Détail des actions critiques et élevées


#### Action n° 101 — Critique

- **URL** : <https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog>
- **Constat** : CISA Adds Two Known Exploited Vulnerabilities to Catalog — CISA — Cybersecurity Advisories (2026-10-29). https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog
- **Risque / opportunité** : Risque : compromission de GitLab (atteinte à : impact à qualifier).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 93 = 12 (Gravité technique) + 30 (Exploitation active) + 5 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 104 — Critique

- **URL** : <https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog>
- **Constat** : CISA Adds Two Known Exploited Vulnerabilities to Catalog — CISA — Cybersecurity Advisories (2026-10-26). https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog
- **Risque / opportunité** : Risque : compromission de PHP (atteinte à : impact à qualifier).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 107 — Critique

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-97229>
- **Constat** : \[KEV\] CVE-2026-97229 — GitLab Community Edition and Enterprise Edition : GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability — CISA — Known Exploited Vulnerabilities (KEV) (2026-10-29). https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search\_api\_fulltext=CVE-2026-97229
- **Risque / opportunité** : Risque : compromission de GitLab (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de GitLab concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 81 = 30 (Exploitation active) + 5 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 109 — Critique

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-46300>
- **Constat** : \[KEV\] CVE-2026-46300 — Linux Kernel : Linux Kernel Missing Initialization of a Variable Vulnerability — CISA — Known Exploited Vulnerabilities (KEV) (2026-10-28). https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search\_api\_fulltext=CVE-2026-46300
- **Risque / opportunité** : Risque : compromission de PHP (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 110 — Critique

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109618>
- **Constat** : \[KEV\] CVE-2026-109618 — PHP Group PHP : PHP Memory Corruption Vulnerability — CISA — Known Exploited Vulnerabilities (KEV) (2026-10-26). https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search\_api\_fulltext=CVE-2026-109618
- **Risque / opportunité** : Risque : compromission de PHP (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 111 — Critique

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109619>
- **Constat** : \[KEV\] CVE-2026-109619 — PHP Group PHP : PHP Stale Internal Request-State Vulnerability — CISA — Known Exploited Vulnerabilities (KEV) (2026-10-26). https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search\_api\_fulltext=CVE-2026-109619
- **Risque / opportunité** : Risque : compromission de PHP (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 112 — Critique

- **URL** : <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2025-61624>
- **Constat** : \[KEV\] CVE-2025-61624 — Fortinet Multiple Products : Fortinet Multiple Products Path Traversal Vulnerability — CISA — Known Exploited Vulnerabilities (KEV) (2026-10-16). https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search\_api\_fulltext=CVE-2025-61624
- **Risque / opportunité** : Risque : compromission de Fortinet FortiGate (VPN SSL) (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de Fortinet FortiGate (VPN SSL) concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 80 = 30 (Exploitation active) + 25 (Présence dans le parc) + 15 (Exposition) + 10 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 126 — Critique

- **URL** : <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20PHP%20Affecting%20Cisco%20Products:%20October%202026%26vs_k=1>
- **Constat** : Vulnerabilities in PHP Affecting Cisco Products: October 2026 — Cisco — Security Advisories (2026-10-28). https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq?vs\_f=Cisco%20Security%20Advisory%26vs\_cat=Security%20Intelligence%26vs\_type=RSS%26vs\_p=Vulnerabilities%20in%20PHP%20Affecting%20Cisco%20Products:%20October%202026%26vs\_k=1
- **Risque / opportunité** : Risque : compromission de PHP (atteinte à : intégrité, disponibilité).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés.
- **Justification** : Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : Équipe infrastructure / exploitation (pilotage RSSI)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Moyen
- **Bénéfice attendu** : Réduction de la surface d'attaque et du risque de compromission des actifs concernés.
- **Preuves de réalisation** : Inventaire des versions avant/après, ticket de changement, rapport de déploiement du correctif, résultat de recherche de compromission.
- **Statut** : À étudier


#### Action n° 161 — Critique

- **URL** : <https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php>
- **Constat** : Critical security issue affecting PHP — NCSC (Royaume-Uni) — Publications (2026-10-21). https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php
- **Risque / opportunité** : Opportunité : renforcer les pratiques de sécurité.
- **\[Recommandation\] Action** : Comparer les recommandations avec la configuration et les pratiques actuelles ; intégrer les mesures pertinentes au plan d'amélioration.
- **Justification** : Score 86 = 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : RSSI / administrateurs systèmes
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Faible
- **Bénéfice attendu** : Durcissement du SI à coût maîtrisé.
- **Preuves de réalisation** : Compte rendu de contrôle de configuration et mesures ajoutées au plan d'amélioration.
- **Statut** : À étudier


#### Action n° 162 — Critique

- **URL** : <https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/>
- **Constat** : Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) — Palo Alto Networks — Unit 42 (2026-10-29). https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/
- **Risque / opportunité** : Risque : exposition au mode opératoire décrit (atteinte à : impact à qualifier).
- **\[Recommandation\] Action** : Vérifier la présence et les versions de PHP concernées par l'avis (inventaire, outil de gestion de parc). Puis : (2) Appliquer le correctif de l'éditeur selon la procédure de gestion des correctifs (test, puis déploiement prioritaire). (3) En attendant le correctif, réduire l'exposition (filtrage des accès, désactivation de la fonctionnalité vulnérable) selon les recommandations de l'éditeur. (4) Rechercher des traces d'exploitation dans les journaux (SIEM/EDR) depuis la date de divulgation et appliquer les indicateurs publiés. (5) Vérifier la couverture de détection (règles SIEM/EDR) des techniques et indicateurs décrits.
- **Justification** : Score 98 = 12 (Gravité technique) + 30 (Exploitation active) + 10 (Probabilité d'exploitation) + 25 (Présence dans le parc) + 15 (Exposition) + 6 (Impact sur les activités) Seuils : Critique ≥ 75 (avec conditions), Élevée ≥ 50, Modérée ≥ 25. Pertinence : forte.
- **Responsable suggéré** : RSSI / équipe de supervision (SOC)
- **Échéance indicative** : 2026-10-31
- **Effort estimé** : Faible
- **Bénéfice attendu** : Meilleure capacité de prévention et de détection face à une menace active.
- **Preuves de réalisation** : Règles de détection créées ou vérifiées, compte rendu de test de détection, message de sensibilisation diffusé.
- **Statut** : À étudier


## 15. Limites de la veille et informations restant à confirmer

- **Source non collectée** : ANSSI — Guides et publications (cyber.gouv.fr) — Bloquée / non collectable :  Alternative : Le site cyber.gouv.fr est protégé par un dispositif anti-robot (Incapsula) et ne fournit pas de flux RSS exploitable : aucune collecte automatique n'est tentée. Alternatives : les flux CERT-FR (même organisme) sont collectés automatiquement ; consultation manuelle mensuelle de la page des publications et saisie des nouveautés dans l'outil.
- **Source non collectée** : Légifrance — Journal officiel (JORF) — Bloquée / non collectable :  Alternative : Les flux RSS publics de Légifrance renvoient une page de vérification anti-robot (HTTP 403, Cloudflare) : aucune collecte automatique n'est tentée. Alternatives : (1) API Légifrance officielle via le portail PISTE (compte et identifiants OAuth requis, piste.gouv.fr) ; (2) consultation manuelle hebdomadaire et saisie dans l'outil ; (3) suivi des textes européens via EUR-Lex.
- **CVSS** : 469 mentions de CVE sans score CVSS disponible (non estimé ; limite de débit du NVD ou CVE non encore évaluée).
- **Exploitation** : 16 éléments signalent une exploitation active non confirmée par le catalogue KEV.
- **Résumés** : 564 résumés sont des synthèses automatiques par règles de sources en langue étrangère (sans traduction) : consulter l'article original.
- **Classification** : Par règles et mots-clés : des faux positifs ou négatifs sont possibles ; l'analyste peut requalifier chaque élément (statut).
- **Inventaire** : La pertinence dépend de l'exhaustivité de l'inventaire déclaré ; les versions affectées ne sont pas comparées automatiquement.
- **Réglementaire** : L'applicabilité est une orientation ; les textes français (Légifrance) ne sont pas collectés automatiquement ; statut de transposition NIS 2 à vérifier.
- **Normes** : Les textes des normes ISO ne sont ni consultés ni reproduits (accès payant) : seules les métadonnées publiques sont suivies.
- **Fraîcheur** : 392 éléments anciens republiés dans les flux ont été exclus des résultats.
- **\[Hypothèse\]** : Profil de DÉMONSTRATION (organisation fictive) : les analyses d'impact illustrent la méthode et doivent être refaites avec le profil réel.
- **\[Hypothèse\]** : Versions non renseignées pour certaines technologies : la correspondance porte sur le produit, pas sur la version affectée (vérification manuelle nécessaire).


## 16. Conclusion

**\[Analyse\]** La veille de la période a permis d'identifier 44 éléments de priorité critique ou élevée, 38 évolutions réglementaires et 16 évolutions normatives, ainsi que 113 évolutions technologiques pertinentes. 74 actions sont proposées ; les actions critiques doivent être validées et lancées sans délai, les autres intégrées au plan de traitement des risques. La prochaine itération devra confirmer les points « à vérifier » listés ci-dessus et mettre à jour le profil de l'organisation si nécessaire.


---


## 17. Annexes — références consultées

Toutes les informations citées proviennent des URL ci-dessous ; la date de consultation correspond à la date de collecte automatique. 297 éléments de priorité faible non cités sont consultables dans l'outil.

| \# | Titre | Source | Publication | Consultation | URL |
|---|---|---|---|---|---|
| 1 | Unit 42 Uncovers PEERSTITCH, a Stealthy FortiGate Implant | Palo Alto Networks — Unit 42 | 2026-10-14 | 2026-10-29 | <https://unit42.paloaltonetworks.com/fortimanager-cve-2024-47575-peerstitch-malware/> |
| 2 | php2shell: Assessing Elastic detection coverage relevant to CVE-2026-109618 and CVE-2026-109619 | Elastic Security Labs | 2026-10-21 | 2026-10-29 | <https://www.elastic.co/security-labs/threat-command/php2shell-php-rce-detection> |
| 3 | Critical RCE vulnerabilities in PHP (CVE-2026-109618, CVE-2026-109619) | Securelist (Kaspersky GReAT) | 2026-10-21 | 2026-10-29 | <https://securelist.com/tr/php2shell-critical-vulnerabilities-in-php/121596/> |
| 4 | CISA Adds Two Known Exploited Vulnerabilities to Catalog | CISA — Cybersecurity Advisories | 2026-10-26 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/26/cisa-adds-two-known-exploited-vulnerabilities-catalog> |
| 5 | Vulnerabilities in PHP Affecting Cisco Products: October 2026 | Cisco — Security Advisories | 2026-10-28 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-php-october26-Jj384Daq?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20PHP%20Affecting%20Cisco%20Products:%20October%202026%26vs_k=1> |
| 6 | Threat Brief: Critical Vulnerabilities in PHP: CVE-2026-109618, CVE-2026-109619 (Updated October 29) | Palo Alto Networks — Unit 42 | 2026-10-29 | 2026-10-29 | <https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/> |
| 7 | Attacker Tried to Exploit Alpine Linux’s GitLab via CVSS 10.0 Flaw Its Ruby Left Open | The Hacker News | 2026-10-29 | 2026-10-29 | <https://thehackernews.com/2026/10/attacker-tried-to-exploit-alpine-linuxs.html> |
| 8 | CISA Adds Two Known Exploited Vulnerabilities to Catalog | CISA — Cybersecurity Advisories | 2026-10-29 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/29/cisa-adds-two-known-exploited-vulnerabilities-catalog> |
| 9 | PHP Issues Second Windows Security Update in Five Days to Fix Brotli Code Execution Flaw | The Hacker News | 2026-10-26 | 2026-10-29 | <https://thehackernews.com/2026/10/php-issues-second-windows-security.html> |
| 10 | Critical security issue affecting PHP | NCSC (Royaume-Uni) — Publications | 2026-10-21 | 2026-10-29 | <https://www.ncsc.gov.uk/news/critical-security-issue-affecting-php> |
| 11 | Using AWS WAF to apply mitigations for PHP2Shell RCE vulnerabilities (CVE-2026-109618 and CVE-2026-109619) | AWS Security Blog | 2026-10-22 | 2026-10-29 | <https://aws.amazon.com/blogs/security/using-aws-waf-to-apply-mitigations-for-php2shell-rce-vulnerabilities-cve-2026-109618-and-cve-2026-109619/> |
| 12 | \[KEV\] CVE-2026-109619 — PHP Group PHP : PHP Stale Internal Request-State Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-26 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109619> |
| 13 | \[KEV\] CVE-2026-109618 — PHP Group PHP : PHP Memory Corruption Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-26 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-109618> |
| 14 | CISA Confirms Active Exploitation of Two PHP2Shell Flaws Enabling Remote Code Execution | The Hacker News | 2026-10-27 | 2026-10-29 | <https://thehackernews.com/2026/10/cisa-confirms-active-exploitation-of.html> |
| 15 | \[KEV\] CVE-2026-46300 — Linux Kernel : Linux Kernel Missing Initialization of a Variable Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-28 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-46300> |
| 16 | \[KEV\] CVE-2026-97229 — GitLab Community Edition and Enterprise Edition : GitLab Community Edition and Enterprise Edition | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-29 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-97229> |
| 17 | \[KEV\] CVE-2025-61624 — Fortinet Multiple Products : Fortinet Multiple Products Path Traversal Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-16 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2025-61624> |
| 18 | Widespread PHP Flaw May Cause Many Site Outages Today | Krebs on Security | 2026-10-21 | 2026-10-29 | <https://krebsonsecurity.com/2026/10/widespread-php-flaw-may-cause-many-site-outages-today/> |
| 19 | Chromium: CVE-2026-79260 Improper input validation in Cookies | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79260> |
| 20 | CISA Adds Two Known Exploited Vulnerabilities to Catalog | CISA — Cybersecurity Advisories | 2026-10-28 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/28/cisa-adds-two-known-exploited-vulnerabilities-catalog> |
| 21 | \[KEV\] CVE-2026-41709 — Broadcom VMware ESX : Broadcom VMWare ESX Insufficient Logging Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-28 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-41709> |
| 22 | China-Linked Hackers Exploited VMware ESX Zero-Day to Reduce Audit Trail Visibility | The Hacker News | 2026-10-29 | 2026-10-29 | <https://thehackernews.com/2026/10/china-linked-hackers-exploited-vmware.html> |
| 23 | USN-8951-1: c-ares vulnerabilities | Ubuntu — Security Notices | 2026-10-21 | 2026-10-29 | <https://ubuntu.com/security/notices/USN-8951-1> |
| 24 | Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits | The Hacker News | 2026-10-28 | 2026-10-29 | <https://thehackernews.com/2026/10/anthropics-unreleased-ai-model-chains.html> |
| 25 | New Serious PHP Vulnerabilities Released and Patched | Schneier on Security | 2026-10-22 | 2026-10-29 | <https://www.schneier.com/blog/archives/2026/10/new-serious-php-vulnerabilities-released-and-patched.html> |
| 26 | Cisco IOS XE Software Security Hardening Release: August 2026 | Cisco — Security Advisories | 2026-10-02 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-iosxe-V8NMuMZJ?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20IOS%20XE%20Software%20Security%20Hardening%20Release:%20August%202026%26vs_k=1> |
| 27 | \[KEV\] CVE-2026-96951 — Microsoft Windows : Microsoft Windows Command Injection Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-13 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-96951> |
| 28 | Two critical RCEs in PHP core | Cisco Talos Intelligence | 2026-10-21 | 2026-10-29 | <https://blog.talosintelligence.com/two-critical-rces-in-php-core/> |
| 29 | Amazon Threat Intelligence identifies PHP2Shell exploitation prior to public disclosure in MadPot | AWS Security Blog | 2026-10-21 | 2026-10-29 | <https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/> |
| 30 | AlerteCyber : Failles de sécurité critiques dans PHP | Cybermalveillance.gouv.fr — Actualités | 2026-10-22 | 2026-10-29 | <https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/alerte-cyber-failles-de-securite-critiques-dans-php-202610> |
| 31 | Cybermalveillance.gouv.fr lance une AlerteCyber concernant deux failles de sécurité critiques dans PHP | Cybermalveillance.gouv.fr — Actualités | 2026-10-22 | 2026-10-29 | <https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/alertecyber-failles-securite-php> |
| 32 | I had plans for that second | Cisco Talos Intelligence | 2026-10-22 | 2026-10-29 | <https://blog.talosintelligence.com/i-had-plans-for-that-second/> |
| 33 | InfraTrust report warns of exploited flaws in critical network infrastructure | BleepingComputer | 2026-10-28 | 2026-10-29 | <https://www.bleepingcomputer.com/news/security/infratrust-report-warns-of-exploited-flaws-in-critical-network-infrastructure/> |
| 34 | \[Màj\] Multiples vulnérabilités dans PHP (21 octobre 2026) | CERT-FR — Alertes de sécurité | 2026-10-21 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-014/> |
| 35 | Cloudflare deploys protections against php2shell vulnerability | Cloudflare Blog | 2026-10-21 | 2026-10-29 | <https://blog.cloudflare.com/php-vulnerabilities-waf-protection/> |
| 36 | AI-driven, large-scale nation-state campaign using ARTEX enables supply chain compromise | Microsoft Security Blog | 2026-10-21 | 2026-10-29 | <https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/> |
| 37 | Introducing the Cloudflare PHP Capture the Flag challenge | Cloudflare Blog | 2026-10-27 | 2026-10-29 | <https://blog.cloudflare.com/php-ctf/> |
| 38 | Siemens RUGGEDCOM CROSSBOW Station Access Controller | CISA — Cybersecurity Advisories | 2026-10-22 | 2026-10-29 | <https://www.cisa.gov/news-events/ics-advisories/icsa-26-295-15> |
| 39 | Chromium: CVE-2026-79108 UI misrepresentation in Web Authentication (Passkeys & Security Keys) | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79108> |
| 40 | Chromium: CVE-2026-79178 Incorrect authorization in Web Authentication (Passkeys & Security Keys) | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79178> |
| 41 | USN-8955-1: nginx vulnerabilities | Ubuntu — Security Notices | 2026-10-26 | 2026-10-29 | <https://ubuntu.com/security/notices/USN-8955-1> |
| 42 | GUI Denial of Service | Fortinet — PSIRT Advisories | 2026-10-13 | 2026-10-29 | <https://fortiguard.fortinet.com/psirt/FG-IR-26-181> |
| 43 | Double free in signal handler | Fortinet — PSIRT Advisories | 2026-10-13 | 2026-10-29 | <https://fortiguard.fortinet.com/psirt/FG-IR-26-182> |
| 44 | Multiples vulnérabilités dans Veeam Backup for Microsoft 365 (29 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-29 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1411/> |
| 45 | Kicking off Cybersecurity Career Week with NIST! | NIST — Cybersecurity Insights (blog) | 2026-10-14 | 2026-10-29 | <https://www.nist.gov/blogs/cybersecurity-insights/kicking-cybersecurity-career-week-nist> |
| 46 | \[KEV\] CVE-2015-3306 — ProFTPD ProFTPD : ProFTPD Improper Access Control Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-08 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2015-3306> |
| 47 | \[KEV\] CVE-2021-3199 — ONLYOFFICE Docs : ONLYOFFICE Docs Server Path Traversal Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-08 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2021-3199> |
| 48 | \[KEV\] CVE-2023-22894 — Strapi Strapi : Strapi Cleartext Storage of Sensitive Information Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-08 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2023-22894> |
| 49 | \[KEV\] CVE-2016-3081 — Apache Struts : Apache Struts Command Injection Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-08 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2016-3081> |
| 50 | \[KEV\] CVE-2015-5477 — ISC BIND :  ISC BIND Data Processing Errors Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-08 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2015-5477> |
| 51 | Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS, GENESIS64, ICONICS Suite, Hyper Historian | CISA — Cybersecurity Advisories | 2026-10-27 | 2026-10-29 | <https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-02> |
| 52 | ShinyHunters-Exploited Oracle PeopleSoft Zero-Day Turns Out to Be Three Chained Flaws | The Hacker News | 2026-10-28 | 2026-10-29 | <https://thehackernews.com/2026/10/shinyhunters-exploited-oracle.html> |
| 53 | Cisco Catalyst SD-WAN Controller Authentication Bypass Vulnerability | Cisco — Security Advisories | 2026-10-28 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-rpa-EHchtZk?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Catalyst%20SD-WAN%20Controller%20Authentication%20Bypass%20Vulnerability%26vs_k=1> |
| 54 | Vulnerabilities in Node.js Affecting Cisco Products: October 2026 | Cisco — Security Advisories | 2026-10-29 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-oct2026-node-js-Jj3SQ19u?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Vulnerabilities%20in%20Node.js%20Affecting%20Cisco%20Products:%20October%202026%26vs_k=1> |
| 55 | Vulnérabilité dans Ivanti Connect Secure (ICS) (14 octobre 2026) | CERT-FR — Alertes de sécurité | 2026-10-14 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-013/> |
| 56 | First harmonised standard supporting the AI Act published in the Official Journal | Commission européenne — Stratégie numérique (filtrée) | 2026-10-19 | 2026-10-29 | <https://digital-strategy.ec.europa.eu/en/library/first-harmonised-standard-supporting-ai-act-published-official-journal> |
| 57 | Hackers exploit Cisco SD-WAN flaw to deploy custom KeyDrift malware | BleepingComputer | 2026-10-29 | 2026-10-29 | <https://www.bleepingcomputer.com/news/security/hackers-exploit-cisco-sd-wan-flaw-to-deploy-custom-keydrift-malware/> |
| 58 | Cisco Catalyst SD-WAN Manager API Authentication Bypass Vulnerability | Cisco — Security Advisories | 2026-10-02 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sdwan-webauth-xr8beuuU?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Catalyst%20SD-WAN%20Manager%20API%20Authentication%20Bypass%20Vulnerability%26vs_k=1> |
| 59 | Adobe, Veeam, Juniper Networks Patch Critical Vulnerabilities | SecurityWeek | 2026-10-29 | 2026-10-29 | <https://www.securityweek.com/adobe-veeam-juniper-networks-patch-critical-vulnerabilities/> |
| 60 | Agents are your newest insiders. Security must move at their speed. | Microsoft Security Blog | 2026-10-19 | 2026-10-29 | <https://www.microsoft.com/en-us/security/blog/2026/10/19/agents-are-your-newest-insiders-security-must-move-at-their-speed/> |
| 61 | DSA-6575-1 nginx - security update | Debian — Security Advisories (DSA) | 2026-10-21 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00490.html> |
| 62 | Attackers Use Microsoft Teams IT Support Scams to Deploy Malware and Ransomware | The Hacker News | 2026-10-26 | 2026-10-29 | <https://thehackernews.com/2026/10/attackers-use-microsoft-teams-it.html> |
| 63 | DSA-6589-1 php-mongodb - security update | Debian — Security Advisories (DSA) | 2026-10-27 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00508.html> |
| 64 | A quiet week in infosec \<.\< | Cisco Talos Intelligence | 2026-10-29 | 2026-10-29 | <https://blog.talosintelligence.com/a-quiet-week-in-infosec/> |
| 65 | Multiples vulnérabilités dans Citrix NetScaler ADC et Gateway (28 septembre 2026) | CERT-FR — Alertes de sécurité | 2026-09-28 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/alerte/CERTFR-2026-ALE-011/> |
| 66 | Deploying, maintaining, and migrating production n8n on EKS | CNCF — Blog | 2026-10-16 | 2026-10-29 | <https://www.cncf.io/blog/2026/10/16/deploying-maintaining-and-migrating-production-n8n-on-eks/> |
| 67 | Managing identity source transition for AWS IAM Identity Center | AWS Security Blog | 2026-10-20 | 2026-10-29 | <https://aws.amazon.com/blogs/security/managing-identity-source-transition-for-aws-iam-identity-center/> |
| 68 | Active Exploitation of May 2026 PAN-OS CVE-2026-0257 (Updated October 20) | Palo Alto Networks — Unit 42 | 2026-10-20 | 2026-10-29 | <https://unit42.paloaltonetworks.com/active-exploitation-of-pan-os-cve-2026-0257/> |
| 69 | Microsoft urges Entra ID admins to migrate users to passkeys | BleepingComputer | 2026-10-28 | 2026-10-29 | <https://www.bleepingcomputer.com/news/microsoft/microsoft-reminds-entra-id-admins-to-migrate-users-to-passkeys/> |
| 70 | USN-8890-2: libsoup vulnerabilities | Ubuntu — Security Notices | 2026-10-21 | 2026-10-29 | <https://ubuntu.com/security/notices/USN-8890-2> |
| 71 | DSA-6577-1 chromium - security update | Debian — Security Advisories (DSA) | 2026-10-22 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00493.html> |
| 72 | Siemens PSS(R)SINCAL | CISA — Cybersecurity Advisories | 2026-10-22 | 2026-10-29 | <https://www.cisa.gov/news-events/ics-advisories/icsa-26-295-06> |
| 73 | Multiples vulnérabilités dans Microsoft Edge (27 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-27 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1395/> |
| 74 | DSA-6592-1 chromium - security update | Debian — Security Advisories (DSA) | 2026-10-28 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00511.html> |
| 75 | Multiples vulnérabilités dans Microsoft Edge (28 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-28 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1405/> |
| 76 | Multiples vulnérabilités dans Google Chrome (28 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-28 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1398/> |
| 77 | Chromium: CVE-2026-79211 Incorrect authorization in USB | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79211> |
| 78 | Chromium: CVE-2026-79097 Use after free in V8 | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79097> |
| 79 | Chromium: CVE-2026-79002 Incorrect authorization in SiteIsolation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79002> |
| 80 | Chromium: CVE-2026-79212 Missing authorization in Passwords | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79212> |
| 81 | Chromium: CVE-2026-79098 UI misrepresentation in PermissionElement | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79098> |
| 82 | Chromium: CVE-2026-79003 Incorrect authorization in Device | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79003> |
| 83 | Chromium: CVE-2026-79099 Missing authorization in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79099> |
| 84 | Chromium: CVE-2026-79214 Improper input validation in Preload | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79214> |
| 85 | Chromium: CVE-2026-79004 Out of bounds read in Media | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79004> |
| 86 | Chromium: CVE-2026-79215 Integer overflow in WebGL | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79215> |
| 87 | Chromium: CVE-2026-79103 Incorrect reference resolution in Speech | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79103> |
| 88 | Chromium: CVE-2026-79005 Incorrect authorization in StorageAccessAPI | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79005> |
| 89 | Chromium: CVE-2026-79216 Buffer overflow in Blink | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79216> |
| 90 | Chromium: CVE-2026-79006 Protection mechanism failure in HttpsUpgrades | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79006> |
| 91 | Chromium: CVE-2026-79104 Missing authorization in Sensor | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79104> |
| 92 | Chromium: CVE-2026-79007 Uninitialized resource in GPU | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79007> |
| 93 | Chromium: CVE-2026-79218 Incorrect authorization in Sandbox | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79218> |
| 94 | Chromium: CVE-2026-79106 Improper input validation in Input | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79106> |
| 95 | Chromium: CVE-2026-79009 UI misrepresentation in UI | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79009> |
| 96 | Chromium: CVE-2026-79219 Use after free in Bluetooth | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79219> |
| 97 | Chromium: CVE-2026-79107 Incorrect authorization in TabGroups | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79107> |
| 98 | Chromium: CVE-2026-79010 Operation on a resource after expiration or release in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79010> |
| 99 | Chromium: CVE-2026-79220 Information leak in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79220> |
| 100 | Chromium: CVE-2026-79011 UI misrepresentation in Browser | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79011> |
| 101 | Chromium: CVE-2026-79221 Uninitialized resource in Dawn | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79221> |
| 102 | Chromium: CVE-2026-79109 Improper input validation in Printing | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79109> |
| 103 | Chromium: CVE-2026-79012 Use after free in Safebrowsing | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79012> |
| 104 | Chromium: CVE-2026-79223 Integer overflow in Chromium | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79223> |
| 105 | Chromium: CVE-2026-79110 Missing authorization in Preload | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79110> |
| 106 | Chromium: CVE-2026-79013 Improper input validation in Sync | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79013> |
| 107 | Chromium: CVE-2026-79224 Use after free in Chromecast | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79224> |
| 108 | Chromium: CVE-2026-79111 Improper input validation in Dawn | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79111> |
| 109 | Chromium: CVE-2026-79014 Race condition in Autofill | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79014> |
| 110 | Chromium: CVE-2026-79225 Incorrect authorization in Browser | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79225> |
| 111 | Chromium: CVE-2026-79112 Out of bounds read in Skia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79112> |
| 112 | Chromium: CVE-2026-79015 Improper input validation in ServiceWorker | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79015> |
| 113 | Chromium: CVE-2026-79226 Improper privilege management in Regional Capabilities | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79226> |
| 114 | Chromium: CVE-2026-79116 Missing authorization in Viz | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79116> |
| 115 | Chromium: CVE-2026-79016 Observable discrepancy in SVG | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79016> |
| 116 | Chromium: CVE-2026-79227 Type confusion in DevTools | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79227> |
| 117 | Chromium: CVE-2026-79118 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79118> |
| 118 | Chromium: CVE-2026-79017 Race condition in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79017> |
| 119 | Chromium: CVE-2026-79228 Incorrect authorization in SiteIsolation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79228> |
| 120 | Chromium: CVE-2026-79119 Use after free in PDF | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79119> |
| 121 | Chromium: CVE-2026-79018 Information leak in FoldableAPIs | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79018> |
| 122 | Chromium: CVE-2026-79229 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79229> |
| 123 | Chromium: CVE-2026-79120 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79120> |
| 124 | Chromium: CVE-2026-79019 Out of bounds write in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79019> |
| 125 | Chromium: CVE-2026-79230 Improper input validation in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79230> |
| 126 | Chromium: CVE-2026-79121 Improper input validation in Chromecast | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79121> |
| 127 | Chromium: CVE-2026-79020 Out of bounds read in Skia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79020> |
| 128 | Chromium: CVE-2026-79231 Buffer overflow in Media | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79231> |
| 129 | Chromium: CVE-2026-79122 Information leak in SignIn | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79122> |
| 130 | Chromium: CVE-2026-79021 Missing authorization in InterestGroups | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79021> |
| 131 | Chromium: CVE-2026-79232 Use after free in Aura | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79232> |
| 132 | Chromium: CVE-2026-79123 Improper input validation in NTP Footer | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79123> |
| 133 | Chromium: CVE-2026-79022 UI misrepresentation in Transactions Platform | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79022> |
| 134 | Chromium: CVE-2026-79234 Injection in CSS | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79234> |
| 135 | Chromium: CVE-2026-79124 Information leak in Intents | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79124> |
| 136 | Chromium: CVE-2026-79023 Incorrect authorization in Editing | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79023> |
| 137 | Chromium: CVE-2026-79235 Use after free in WebGL | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79235> |
| 138 | Chromium: CVE-2026-79125 Information leak in XR | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79125> |
| 139 | Chromium: CVE-2026-79024 Information leak in ServiceWorker | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79024> |
| 140 | Chromium: CVE-2026-79236 Type confusion in V8 | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79236> |
| 141 | Chromium: CVE-2026-79237 Incorrect authorization in Navigation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79237> |
| 142 | Chromium: CVE-2026-79238 Incorrect authorization in ServiceWorker | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79238> |
| 143 | Chromium: CVE-2026-79025 Improper input validation in Workers | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79025> |
| 144 | Chromium: CVE-2026-79126 Incorrect provision of specified functionality in Proxy | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79126> |
| 145 | Chromium: CVE-2026-79239 Out of bounds read in Tint | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79239> |
| 146 | Chromium: CVE-2026-79026 Use after free in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79026> |
| 147 | Chromium: CVE-2026-79127 Out of bounds write in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79127> |
| 148 | Chromium: CVE-2026-79240 Out of bounds write in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79240> |
| 149 | Chromium: CVE-2026-79027 Use after free in WebRTC | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79027> |
| 150 | Chromium: CVE-2026-79128 Use after free in Views | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79128> |
| 151 | Chromium: CVE-2026-79242 Observable discrepancy in HTML | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79242> |
| 152 | Chromium: CVE-2026-79028 Observable discrepancy in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79028> |
| 153 | Chromium: CVE-2026-79130 Buffer overflow in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79130> |
| 154 | Chromium: CVE-2026-79030 Observable discrepancy in Autofill | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79030> |
| 155 | Chromium: CVE-2026-79243 Improper input validation in ReadingList | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79243> |
| 156 | Chromium: CVE-2026-79131 Out of bounds write in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79131> |
| 157 | Chromium: CVE-2026-79244 Use after free in Animation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79244> |
| 158 | Chromium: CVE-2026-79133 Incorrect authorization in Forms | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79133> |
| 159 | Chromium: CVE-2026-79245 Use after free in UI | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79245> |
| 160 | Chromium: CVE-2026-79134 Incorrect authorization in GetUserMedia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79134> |
| 161 | Chromium: CVE-2026-79246 Information leak in DataTransfer | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79246> |
| 162 | Chromium: CVE-2026-79136 Incorrect authorization in ServiceWorker | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79136> |
| 163 | Chromium: CVE-2026-79247 Use after free in Chromoting | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79247> |
| 164 | Chromium: CVE-2026-79137 Incorrect authorization in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79137> |
| 165 | Chromium: CVE-2026-79248 Incorrect authorization in Input | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79248> |
| 166 | Chromium: CVE-2026-79138 Out of bounds write in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79138> |
| 167 | Chromium: CVE-2026-79249 Code injection in Bisection | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79249> |
| 168 | Chromium: CVE-2026-79139 Improper input validation in Media | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79139> |
| 169 | Chromium: CVE-2026-79250 UI misrepresentation in Navigation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79250> |
| 170 | Chromium: CVE-2026-79140 Use after free in Views | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79140> |
| 171 | Chromium: CVE-2026-79251 Improper input validation in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79251> |
| 172 | Chromium: CVE-2026-79141 Incorrect authorization in Browser | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79141> |
| 173 | Chromium: CVE-2026-79252 Information leak in ServiceWorker | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79252> |
| 174 | Chromium: CVE-2026-79142 Buffer overflow in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79142> |
| 175 | Chromium: CVE-2026-79253 Improper input validation in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79253> |
| 176 | Chromium: CVE-2026-79143 Incorrect authorization in FileSystem | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79143> |
| 177 | Chromium: CVE-2026-79255 Improper input validation in WebRTC | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79255> |
| 178 | Chromium: CVE-2026-79144 Information leak in Skia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79144> |
| 179 | Chromium: CVE-2026-79257 Use after free in Views | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79257> |
| 180 | Chromium: CVE-2026-79147 Information leak in Skia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79147> |
| 181 | Chromium: CVE-2026-79148 Off-by-one error in DevTools | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79148> |
| 182 | Chromium: CVE-2026-79258 Incorrect authorization in WebXR | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79258> |
| 183 | Chromium: CVE-2026-79149 Use after free in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79149> |
| 184 | Chromium: CVE-2026-79259 Improper input validation in Safebrowsing | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79259> |
| 185 | Chromium: CVE-2026-79150 Use after free in Views | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79150> |
| 186 | Chromium: CVE-2026-79151 Improper input validation in Safebrowsing | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79151> |
| 187 | Chromium: CVE-2026-79261 Incorrect authorization in Controls | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79261> |
| 188 | Chromium: CVE-2026-79154 Missing authorization in DevTools | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79154> |
| 189 | Chromium: CVE-2026-79262 Incorrect authorization in Network | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79262> |
| 190 | Chromium: CVE-2026-79155 Race condition in FileSystem | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79155> |
| 191 | Chromium: CVE-2026-79263 Race condition in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79263> |
| 192 | Chromium: CVE-2026-79173 UI misrepresentation in WebAppInstalls | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79173> |
| 193 | Chromium: CVE-2026-79264 Incorrect reference resolution in Preload | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79264> |
| 194 | Chromium: CVE-2026-79174 Incorrect authorization in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79174> |
| 195 | Chromium: CVE-2026-79265 Incomplete cleanup in GetUserMedia | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79265> |
| 196 | Chromium: CVE-2026-79175 Type confusion in Accessibility | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79175> |
| 197 | Chromium: CVE-2026-79266 Use after free in DevTools | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79266> |
| 198 | Chromium: CVE-2026-79176 UI misrepresentation in Extensions | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79176> |
| 199 | Chromium: CVE-2026-79267 Race condition in Workers | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79267> |
| 200 | Chromium: CVE-2026-79177 Incorrect authorization in Media | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79177> |
| 201 | Chromium: CVE-2026-79269 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79269> |
| 202 | Chromium: CVE-2026-79270 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79270> |
| 203 | Chromium: CVE-2026-79179 Incorrect authorization in DOM | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79179> |
| 204 | Chromium: CVE-2026-79271 Information leak in DOM | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79271> |
| 205 | Chromium: CVE-2026-79272 Improper input validation in FindInPage | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79272> |
| 206 | Chromium: CVE-2026-79274 Information leak in GPU | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79274> |
| 207 | Chromium: CVE-2026-79275 Use after free in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79275> |
| 208 | Chromium: CVE-2026-79276 Improper privilege management in FileSystem | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79276> |
| 209 | Chromium: CVE-2026-79283 UI misrepresentation in Geometry | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79283> |
| 210 | Chromium: CVE-2026-79284 UI misrepresentation in Core | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79284> |
| 211 | Chromium: CVE-2026-79285 Uninitialized resource in ANGLE | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79285> |
| 212 | Chromium: CVE-2026-79287 Observable discrepancy in Forms | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79287> |
| 213 | Chromium: CVE-2026-79289 Improper control of a resource through its lifetime in Workers | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79289> |
| 214 | Chromium: CVE-2026-79290 Use after free in Aura | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79290> |
| 215 | Chromium: CVE-2026-79291 Information leak in CSS | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79291> |
| 216 | Chromium: CVE-2026-79292 Integer overflow in Chromecast | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79292> |
| 217 | Chromium: CVE-2026-79293 Information leak in Animation | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-79293> |
| 218 | CVE-2026-88078 Microsoft Edge (Chromium-based) Spoofing Vulnerability | Microsoft — Security Update Guide | 2026-10-29 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-88078> |
| 219 | Cisco Secure Email Gateway Arbitrary File Write Vulnerability | Cisco — Security Advisories | 2026-10-14 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-esa-afw-zqYJkjxp?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Email%20Gateway%20Arbitrary%20File%20Write%20Vulnerability%26vs_k=1> |
| 220 | Cisco Expressway Series Remote Code Execution Vulnerability | Cisco — Security Advisories | 2026-10-21 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Expressway%20Series%20Remote%20Code%20Execution%20Vulnerability%26vs_k=1> |
| 221 | Siemens Software Center | CISA — Cybersecurity Advisories | 2026-10-22 | 2026-10-29 | <https://www.cisa.gov/news-events/ics-advisories/icsa-26-295-03> |
| 222 | OperTraitors: How Kubernetes Operators Betray Your Security Posture | Palo Alto Networks — Unit 42 | 2026-09-29 | 2026-10-29 | <https://unit42.paloaltonetworks.com/agentic-ai-kubernetes-operator-risks/> |
| 223 | The Shift to cgroup v2 in Kubernetes: What You Need to Know | Kubernetes Blog (filtré sécurité) | 2026-10-06 | 2026-10-29 | <https://kubernetes.io/blog/2026/10/06/kubernetes-cgroups-v2-shift/> |
| 224 | 3 lessons from frontier AI vulnerability research | Microsoft Security Blog | 2026-10-07 | 2026-10-29 | <https://www.microsoft.com/en-us/security/blog/2026/10/07/3-lessons-from-frontier-ai-vulnerability-research/> |
| 225 | How AI workloads are reshaping Kubernetes autoscaling | CNCF — Blog | 2026-10-19 | 2026-10-29 | <https://www.cncf.io/blog/2026/10/19/how-ai-workloads-are-reshaping-kubernetes-autoscaling/> |
| 226 | Before you evaluate an AI SRE, give your existing agent context | CNCF — Blog | 2026-10-21 | 2026-10-29 | <https://www.cncf.io/blog/2026/10/21/before-you-evaluate-an-ai-sre-give-your-existing-agent-context/> |
| 227 | Kernel eviction notice: What wesp.sys reveals about the Windows Endpoint Security Platform | Elastic Security Labs | 2026-10-26 | 2026-10-29 | <https://www.elastic.co/security-labs/blog/windows-endpoint-security-platform-wesp> |
| 228 | Announcing the Workload Conformance Working Group | Kubernetes Blog (filtré sécurité) | 2026-10-27 | 2026-10-29 | <https://kubernetes.io/blog/2026/10/27/announcing-workload-conformance-wg/> |
| 229 | An insecure neighbor: how a vulnerability chain led to an isolation bypass in cloud infrastructure | Securelist (Kaspersky GReAT) | 2026-10-27 | 2026-10-29 | <https://securelist.com/cloud-infrastructure-isolation-bypass/121609/> |
| 230 | Japan's GMO Offers $1 Million Bounty to Catch Hackers Behind FX Trading Cloud Breach | The Hacker News | 2026-10-28 | 2026-10-29 | <https://thehackernews.com/2026/10/japans-gmo-offers-1-million-bounty-to.html> |
| 231 | Application du chapitre V de la loi européenne sur l'IA | artificialintelligenceact.eu (non officiel) | n.c. | 2026-10-29 | <https://artificialintelligenceact.eu/enforcement-of-chapter-v-under-the-eu-ai-act/?utm_source=rss&utm_medium=rss&utm_campaign=enforcement-of-chapter-v-under-the-eu-ai-act> |
| 232 | La thérapie par IA au regard de la loi européenne sur l'IA | artificialintelligenceact.eu (non officiel) | n.c. | 2026-10-29 | <https://artificialintelligenceact.eu/ai-therapy-under-the-eu-ai-act/?utm_source=rss&utm_medium=rss&utm_campaign=ai-therapy-under-the-eu-ai-act> |
| 233 | Threat Brief: NetScaler Zero Days CVE-2026-88771 and CVE-2026-88772 Exploited in the Wild (Updated September 30) | Palo Alto Networks — Unit 42 | 2026-09-30 | 2026-10-29 | <https://unit42.paloaltonetworks.com/netscaler-zero-days-exploited/> |
| 234 | \[KEV\] CVE-2026-104935 — Ivanti Connect Secure : Ivanti Connect Secure Authentication Bypass by Spoofing Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-13 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-104935> |
| 235 | \[KEV\] CVE-2026-105133 — Ahsay AhsayCBS : Ahsay AhsayCBS Improper Authentication Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-14 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-105133> |
| 236 | \[KEV\] CVE-2026-105134 — Ahsay AhsayCBS : Ahsay AhsayCBS Command Injection Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-14 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-105134> |
| 237 | \[KEV\] CVE-2026-21589 — Atlassian Multiple Products : Atlassian Multiple Products Files or Directories Accessible to Exte | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-15 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-21589> |
| 238 | Beyond the patch: Protecting your NetScaler gateway against future vulnerabilities | Cloudflare Blog | 2026-10-19 | 2026-10-29 | <https://blog.cloudflare.com/protect-your-netscaler-gateway/> |
| 239 | PHP2Shell core RCE vulnerability patches (CVE-2026-109618 and CVE-2026-109619) | Fortinet — PSIRT Advisories | 2026-10-21 | 2026-10-29 | <https://fortiguard.fortinet.com/psirt/FG-IR-26-186> |
| 240 | How CVE-2026-73570 turns a Zimbra log file into remote code execution | Elastic Security Labs | 2026-10-23 | 2026-10-29 | <https://www.elastic.co/security-labs/threat-command/command-injection-zimbra-cve-2026-73570> |
| 241 | \[KEV\] CVE-2026-110447 — Collabora Collabora Online – Built-in CODE Server : Collabora Online – Built-in CODE Server OS C | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-23 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-110447> |
| 242 | CISA Adds One Known Exploited Vulnerability to Catalog | CISA — Cybersecurity Advisories | 2026-10-23 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog-0> |
| 243 | Node2Shell CVEs | Fortinet — PSIRT Advisories | 2026-10-26 | 2026-10-29 | <https://fortiguard.fortinet.com/psirt/FG-IR-26-187> |
| 244 | \[KEV\] CVE-2026-111497 — Google Brotli : Google Brotli Unchecked Return Value Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-27 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-111497> |
| 245 | CISA Adds Two Known Exploited Vulnerabilities to Catalog | CISA — Cybersecurity Advisories | 2026-10-27 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/27/cisa-adds-two-known-exploited-vulnerabilities-catalog> |
| 246 | Multiples vulnérabilités dans Palo Alto Networks PAN-OS (28 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-28 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1402/> |
| 247 | Adobe Commerce PolyShell Attacks Breach Hundreds of Stores as Brotli Exploit Traffic Emerges | The Hacker News | 2026-10-28 | 2026-10-29 | <https://thehackernews.com/2026/10/adobe-commerce-polyshell-attacks-breach.html> |
| 248 | Inside KeyDrift: Analyzing historical UAT-11473 activity on Cisco SD-WAN | Cisco Talos Intelligence | 2026-10-28 | 2026-10-29 | <https://blog.talosintelligence.com/uat-11473-keydrift/> |
| 249 | USN-8956-2: Brotli vulnerability | Ubuntu — Security Notices | 2026-10-27 | 2026-10-29 | <https://ubuntu.com/security/notices/USN-8956-2> |
| 250 | Linux Kernel TCP Flaw With 9.8 CVSS Score Affects Ubuntu, Red Hat and Other Distributions | The Hacker News | 2026-10-29 | 2026-10-29 | <https://thehackernews.com/2026/10/linux-kernel-tcp-flaw-with-98-cvss.html> |
| 251 | Wazuh and AI for Enhanced SOC Workflows | The Hacker News | 2026-10-28 | 2026-10-29 | <https://thehackernews.com/2026/10/wazuh-and-ai-for-enhanced-soc-workflows.html> |
| 252 | \[KEV\] CVE-2026-76504 — Cisco Catalyst SD-WAN Manager : Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-09-30 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-76504> |
| 253 | \[KEV\] CVE-2026-102489 — Zammad GmbH Zammad : Zammad GmbH Zammad Session Fixation Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-02 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-102489> |
| 254 | \[KEV\] CVE-2026-102490 — Zammad GmbH Zammad : Zammad GmbH Zammad Improper Privilege Management Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-02 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-102490> |
| 255 | \[KEV\] CVE-2026-88779 — Citrix NetScaler : Citrix NetScaler Improper Restriction of Operations within the Bounds of a Mem | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-04 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-88779> |
| 256 | \[KEV\] CVE-2026-102764 — BeyondTrust Remote Support : BeyondTrust Remote Support Authentication Bypass by Spoofing Vulner | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-16 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-102764> |
| 257 | Multiples vulnérabilités dans les produits VMware (26 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-26 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1385/> |
| 258 | \[KEV\] CVE-2026-48356 — Adobe Commerce and Magento : Adobe Commerce and Magento Unrestricted Upload of File with Dangerou | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-27 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-48356> |
| 259 | Multiples vulnérabilités dans les produits Apple (27 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-27 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1387/> |
| 260 | Apple Backports Fix for Exploited CoreGraphics Flaw to Older iPhones and iPads | The Hacker News | 2026-10-27 | 2026-10-29 | <https://thehackernews.com/2026/10/apple-backports-fix-for-exploited.html> |
| 261 | Multiples vulnérabilités dans les produits Veeam (28 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-28 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1399/> |
| 262 | Multiples vulnérabilités dans PostgreSQL Anonymizer (29 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-29 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1413/> |
| 263 | Microsoft Patches More Than 1,400 Security Flaws | Krebs on Security | 2026-10-13 | 2026-10-29 | <https://krebsonsecurity.com/2026/10/microsoft-patches-more-than-1400-security-flaws/> |
| 264 | Why Is My Kubernetes Job Still Pending? Tracing Kueue Admission with Headlamp | Kubernetes Blog (filtré sécurité) | 2026-10-14 | 2026-10-29 | <https://kubernetes.io/blog/2026/10/14/tracing-kueue-admission-with-headlamp/> |
| 265 | What’s in the SOSS? Podcast \#76 – S3E28 Invisible Infrastructure, Autonomous Agents, and 10 Years of Cloud Native with C | OpenSSF — Blog | 2026-10-20 | 2026-10-29 | <https://openssf.org/podcast/2026/10/20/whats-in-the-soss-podcast-76-s3e28-invisible-infrastructure-autonomous-agents-and-10-years-of-cloud-native-with-cncfs-chris-aniszczyk/> |
| 266 | Cisco Secure Client Secure Firewall Posture Module Privilege Escalation Vulnerability | Cisco — Security Advisories | 2026-10-21 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-sec-client-priv-esc-muF8eZdm?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Client%20Secure%20Firewall%20Posture%20Module%20Privilege%20Escalation%20Vulnerability%26vs_k=1> |
| 267 | CVE-2026-57084 Windows File Explorer Information Disclosure Vulnerability | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-57084> |
| 268 | CVE-2026-57083 Windows Media Photo Codec Information Disclosure Vulnerability | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-57083> |
| 269 | CVE-2026-62877 Windows Win32k Elevation of Privilege Vulnerability | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62877> |
| 270 | CVE-2026-62740 Windows Imaging Component Information Disclosure Vulnerability | Microsoft — Security Update Guide | 2026-10-28 | 2026-10-29 | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-62740> |
| 271 | Le Forum consultatif : qu'est-ce que c'est et comment ça marche ? | artificialintelligenceact.eu (non officiel) | n.c. | 2026-10-29 | <https://artificialintelligenceact.eu/the-advisory-forum-what-is-it-and-how-does-it-work/?utm_source=rss&utm_medium=rss&utm_campaign=the-advisory-forum-what-is-it-and-how-does-it-work> |
| 272 | Le groupe d'experts scientifiques indépendants : qu'est-ce que c'est et comment fonctionne-t-il ? | artificialintelligenceact.eu (non officiel) | n.c. | 2026-10-29 | <https://artificialintelligenceact.eu/scientific-panel/?utm_source=rss&utm_medium=rss&utm_campaign=scientific-panel> |
| 273 | The Irish Data Protection Commission fines Google EUR 403 000 000 following Inquiry into Google’s processing of location | EDPB — Actualités | 2026-09-23 | 2026-10-29 | <https://www.edpb.europa.eu/news/the-irish-data-protection-commission-fines-google-403-000-000-eur-following-inquiry_en> |
| 274 | \[KEV\] CVE-2026-104286 — Fortinet FortiMail : Fortinet FortiMail Path Traversal Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-01 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-104286> |
| 275 | Cisco NX-OS Software Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-07 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-nxosw1-cWzSbtR?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20NX-OS%20Software%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 276 | Cisco Application Policy Infrastructure Controller Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-07 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-apic-UOXWtfh?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Application%20Policy%20Infrastructure%20Controller%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 277 | Cisco License (Smart Software Manager) On-Prem Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-07 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-ssm-Ph77wdhf?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20License%20(Smart%20Software%20Manager)%20On-Prem%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 278 | Dutch DPA fines Uber EUR 824 990 000 for unlawful automated decision-making and insufficient information on profiling | EDPB — Actualités | 2026-10-08 | 2026-10-29 | <https://www.edpb.europa.eu/news/dutch-dpa-fines-uber-eur-824-990-000-for-unlawful-automated-decision-making-and-insufficient_en> |
| 279 | Hellenic DPA decision on a data breach involving E.E.T.A.A. S.A. as processor for the Ministry of Social Cohesion and Fa | EDPB — Actualités | 2026-10-08 | 2026-10-29 | <https://www.edpb.europa.eu/news/hellenic-dpa-decision-on-a-data-breach-involving-eetaa-sa-as-processor-for-the-ministry-of_en> |
| 280 | Swedish DPA fines Miljödata i Karlskrona approximately EUR 160 000 for insufficient technical and organisational measure | EDPB — Actualités | 2026-10-08 | 2026-10-29 | <https://www.edpb.europa.eu/news/swedish-dpa-fines-miljodata-i-karlskrona-approximately-eur-160-000-for-insufficient-technical_en> |
| 281 | Italian DPA fines BBVA EUR 5 508 000 for failing to respect a customer’s objection to direct marketing | EDPB — Actualités | 2026-10-09 | 2026-10-29 | <https://www.edpb.europa.eu/news/italian-dpa-fines-bbva-eur-5-508-000-for-failing-to-respect-a-customers-objection-to-direct_en> |
| 282 | Italian DPA fines Emirates EUR 180 000 for infringements concerning passengers’ health data | EDPB — Actualités | 2026-10-09 | 2026-10-29 | <https://www.edpb.europa.eu/news/italian-dpa-fines-emirates-eur-180-000-for-infringements-concerning-passengers-health-data_en> |
| 283 | Italian DPA fines security company EUR 39 000 for violations concerning employees’ data | EDPB — Actualités | 2026-10-09 | 2026-10-29 | <https://www.edpb.europa.eu/news/italian-dpa-fines-security-company-eur-39-000-for-violations-concerning-employees-data_en> |
| 284 | Italian DPA fines IQVIA EUR 7 000 000 for unlawful processing of patients’ health data | EDPB — Actualités | 2026-10-09 | 2026-10-29 | <https://www.edpb.europa.eu/news/italian-dpa-fines-iqvia-eur-7-000-000-for-unlawful-processing-of-patients-health-data_en> |
| 285 | EDPB publishes statement on the data protection challenges of smart glasses | EDPB — Actualités | 2026-10-13 | 2026-10-29 | <https://www.edpb.europa.eu/news/edpb-publishes-statement-on-the-data-protection-challenges-of-smart-glasses_en> |
| 286 | Le CEPD publie une déclaration sur les enjeux de protection des données liés aux lunettes connectées | CNIL — Actualités | 2026-10-13 | 2026-10-29 | <https://www.cnil.fr/fr/cepd-declaration-lunettes-connectees> |
| 287 | \[KEV\] CVE-2026-0322 — Palo Alto Networks PAN-OS : Palo Alto Networks PAN-OS Code Injection Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-14 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-0322> |
| 288 | \[KEV\] CVE-2026-76519 — Cisco Secure Email Gateway : Cisco Secure Email Gateway Relative Path Traversal Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-14 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-76519> |
| 289 | Clôture de l’injonction prononcée à l’encontre de GOOGLE | CNIL — Actualités | 2026-10-14 | 2026-10-29 | <https://www.cnil.fr/fr/cloture-injonction-google> |
| 290 | Cisco Secure Email Gateway and Secure Email and Web Manager Security Hardening Release: September 2026 | Cisco — Security Advisories | 2026-10-14 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-esa-dfCrfXkm?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Email%20Gateway%20and%20Secure%20Email%20and%20Web%20Manager%20Security%20Hardening%20Release:%20September%202026%26vs_k=1> |
| 291 | Cisco Meraki Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-15 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-meraki-os-drbEX9GH?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Meraki%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 292 | Norwegian DPA fines Xandr EUR 8 600 000 for unlawful processing of personal data | EDPB — Actualités | 2026-10-16 | 2026-10-29 | <https://www.edpb.europa.eu/news/norwegian-dpa-fines-xandr-eur-8-600-000-for-unlawful-processing-of-personal-data_en> |
| 293 | Reconstitution d’adresses électroniques professionnelles : quels sont vos droits ? | CNIL — Actualités | 2026-10-16 | 2026-10-29 | <https://www.cnil.fr/fr/reconstitution-adresses-professionnelles-vos-droits> |
| 294 | Reconstitution d’adresses électroniques professionnelles : dans quel cadre est-ce autorisé ? | CNIL — Actualités | 2026-10-16 | 2026-10-29 | <https://www.cnil.fr/fr/reconstitution-adresses-professionnelles-quel-cadre> |
| 295 | De la protection des données à la création de valeur en finance : des autorités européennes publient une étude et des bo | CNIL — Actualités | 2026-10-16 | 2026-10-29 | <https://www.cnil.fr/fr/protection-donnees-valeur-finance-etude-autorites-europeennes> |
| 296 | \[KEV\] CVE-2026-110936 — Siemens Software Center : Siemens Software Center Uncontrolled Search Path Element Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-110936> |
| 297 | \[KEV\] CVE-2026-96652 — Plex Media Server : Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-96652> |
| 298 | \[KEV\] CVE-2026-96654 — Plex Media Server : Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Pag | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-96654> |
| 299 | \[KEV\] CVE-2026-96655 — Plex Media Server : Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-96655> |
| 300 | \[KEV\] CVE-2026-96656 — Plex Media Server : Plex Media Server External Control of File Name or Path Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-96656> |
| 301 | \[KEV\] CVE-2026-106931 — EG Secure Solutions SiteGuard Server Edition : EG Secure Solutions SiteGuard Server Edition OS C | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-20 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-106931> |
| 302 | Journée RGPD à Poitiers : cybersécurité, IA et conformité au cœur des enjeux de protection des données | CNIL — Actualités | 2026-10-20 | 2026-10-29 | <https://www.cnil.fr/fr/journee-rgpd-2026-poitiers> |
| 303 | Managing AI Token Consumption for Operational Resilience | CISA — Cybersecurity Advisories | 2026-10-22 | 2026-10-29 | <https://www.cisa.gov/resources-tools/resources/managing-ai-token-consumption-operational-resilience> |
| 304 | USN-8952-1: Tornado vulnerabilities | Ubuntu — Security Notices | 2026-10-22 | 2026-10-29 | <https://ubuntu.com/security/notices/USN-8952-1> |
| 305 | Multiple Cisco Products Snort 3 Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-22 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-hardening-snort3-ybgmhTQe?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Multiple%20Cisco%20Products%20Snort%203%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 306 | \[KEV\] CVE-2026-114625 — Arista VeloCloud Orchestrator : Arista VeloCloud Orchestrator SQL Injection Vulnerability | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-23 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-114625> |
| 307 | CISA Adds One Known Exploited Vulnerability to Catalog | CISA — Cybersecurity Advisories | 2026-10-23 | 2026-10-29 | <https://www.cisa.gov/news-events/alerts/2026/10/23/cisa-adds-one-known-exploited-vulnerability-catalog> |
| 308 | Cisco Unified Communications Products Security Hardening Release: October 2026 | Cisco — Security Advisories | 2026-10-27 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-voice-hardening-twgbH9e3?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Unified%20Communications%20Products%20Security%20Hardening%20Release:%20October%202026%26vs_k=1> |
| 309 | Sony ISP subsidiary data breach exposes 2.5 million customer records | BleepingComputer | 2026-10-28 | 2026-10-29 | <https://www.bleepingcomputer.com/news/security/sony-isp-subsidiary-data-breach-exposes-25-million-customer-records/> |
| 310 | Cisco Secure Firewall Adaptive Security Appliance and Secure Firewall Threat Defense Software Remote Access SSL VPN Tunn | Cisco — Security Advisories | 2026-10-28 | 2026-10-29 | <https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-asaftd-tunnel-dos-s6mgkb75?vs_f=Cisco%20Security%20Advisory%26vs_cat=Security%20Intelligence%26vs_type=RSS%26vs_p=Cisco%20Secure%20Firewall%20Adaptive%20Security%20Appliance%20and%20Secure%20Firewall%20Threat%20Defense%20Software%20Remote%20Access%20SSL%20VPN%20Tunnel%20Denial%20of%20Service%20Vulnerability%26vs_k=1> |
| 311 | \[KEV\] CVE-2026-76418 — Cisco Secure Firewall ASA Software and Cisco Secure FTD Software : Cisco Secure Firewall ASA Soft | CISA — Known Exploited Vulnerabilities (KEV) | 2026-10-29 | 2026-10-29 | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext=CVE-2026-76418> |
| 312 | Vulnérabilité dans les produits Cisco (29 octobre 2026) | CERT-FR — Avis de sécurité | 2026-10-29 | 2026-10-29 | <https://www.cert.cyber.gouv.fr/avis/CERTFR-2026-AVI-1412/> |
| 313 | Cisco Patches Actively Exploited ASA and FTD VPN Flaw That Can Crash Firewalls | The Hacker News | 2026-10-29 | 2026-10-29 | <https://thehackernews.com/2026/10/cisco-patches-actively-exploited-asa.html> |
| 314 | Cookies et application mobile : sanctions de 7 millions d’euros à l’encontre des sociétés FNAC DARTY PARTICIPATIONS ET S | CNIL — Actualités | 2026-10-29 | 2026-10-29 | <https://www.cnil.fr/fr/sanction-cookies-app-fnac> |
| 315 | DSA-6569-1 apache2 - security update | Debian — Security Advisories (DSA) | 2026-10-16 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00483.html> |
| 316 | DSA-6567-2 cifs-utils - regression update | Debian — Security Advisories (DSA) | 2026-10-18 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00484.html> |
| 317 | DSA-6570-1 haproxy - security update | Debian — Security Advisories (DSA) | 2026-10-18 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00485.html> |
| 318 | DSA-6571-1 xen - security update | Debian — Security Advisories (DSA) | 2026-10-18 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00486.html> |
| 319 | DSA-6572-1 ca-certificates - security update | Debian — Security Advisories (DSA) | 2026-10-20 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00487.html> |
| 320 | DSA-6573-1 firefox-esr - security update | Debian — Security Advisories (DSA) | 2026-10-21 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00488.html> |
| 321 | DSA-6574-1 php8.4 - security update | Debian — Security Advisories (DSA) | 2026-10-21 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00489.html> |
| 322 | DSA-6576-1 bind9 - security update | Debian — Security Advisories (DSA) | 2026-10-21 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00491.html> |
| 323 | DSA-6534-3 webkit2gtk - regression update | Debian — Security Advisories (DSA) | 2026-10-22 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00492.html> |
| 324 | DSA-6578-1 aide - security update | Debian — Security Advisories (DSA) | 2026-10-22 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00494.html> |
| 325 | DSA-6579-1 roundcube - security update | Debian — Security Advisories (DSA) | 2026-10-23 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00495.html> |
| 326 | DSA-6580-1 erlang - security update | Debian — Security Advisories (DSA) | 2026-10-23 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00496.html> |
| 327 | DSA-6581-1 unbound - security update | Debian — Security Advisories (DSA) | 2026-10-23 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00497.html> |
| 328 | DSA-6582-1 brotli - security update | Debian — Security Advisories (DSA) | 2026-10-23 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00498.html> |
| 329 | DSA-6583-1 libheif - security update | Debian — Security Advisories (DSA) | 2026-10-24 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00499.html> |
| 330 | DSA-6584-1 varnish - security update | Debian — Security Advisories (DSA) | 2026-10-25 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00502.html> |
| 331 | DSA-6585-1 thunderbird - security update | Debian — Security Advisories (DSA) | 2026-10-25 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00503.html> |
| 332 | DSA-6586-1 valkey - security update | Debian — Security Advisories (DSA) | 2026-10-27 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00504.html> |
| 333 | DSA-6587-1 pdns - security update | Debian — Security Advisories (DSA) | 2026-10-27 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00506.html> |
| 334 | DSA-6588-1 openjdk-21 - security update | Debian — Security Advisories (DSA) | 2026-10-27 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00507.html> |
| 335 | DSA-6585-2 thunderbird - regression update | Debian — Security Advisories (DSA) | 2026-10-27 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00505.html> |
| 336 | DSA-6590-1 firefox-esr - security update | Debian — Security Advisories (DSA) | 2026-10-28 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00509.html> |
| 337 | DSA-6591-1 openjdk-25 - security update | Debian — Security Advisories (DSA) | 2026-10-28 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00510.html> |
| 338 | DSA-6593-1 imagemagick - security update | Debian — Security Advisories (DSA) | 2026-10-29 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00512.html> |
| 339 | DSA-6594-1 python-git - security update | Debian — Security Advisories (DSA) | 2026-10-29 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00513.html> |
| 340 | DSA-6595-1 tor - security update | Debian — Security Advisories (DSA) | 2026-10-29 | 2026-10-29 | <https://lists.debian.org/debian-security-announce/2026/msg00514.html> |
| 341 | Localizing compliance at scale: achieving South Korea’s ISMS certification | Cloudflare Blog | 2026-10-22 | 2026-10-29 | <https://blog.cloudflare.com/k-isms/> |
| 342 | NIST Report Provides Guidelines for Transition to Post-Quantum Cryptography Standards | NIST — Actualités (filtrées sécurité) | 2026-10-27 | 2026-10-29 | <https://www.nist.gov/news-events/news/2026/10/nist-report-provides-guidelines-transition-post-quantum-cryptography> |
| 343 | NIK C2: The new AI-enabled command-and-control framework | Cisco Talos Intelligence | 2026-10-29 | 2026-10-29 | <https://blog.talosintelligence.com/nik-c2-new-ai-enabled-framework/> |
| 344 | AWS Continuum sets a new standard in autonomous code security | AWS Security Blog | 2026-10-05 | 2026-10-29 | <https://aws.amazon.com/blogs/security/aws-continuum-sets-a-new-standard-in-autonomous-code-security/> |
| 345 | Introducing Privateer: AI-Assisted Security & Compliance Evaluation Framework Joins the OpenSSF Sandbox | OpenSSF — Blog | 2026-10-13 | 2026-10-29 | <https://openssf.org/blog/2026/10/13/introducing-privateer-ai-assisted-security-compliance-evaluation-framework-joins-the-openssf-sandbox/> |
| 346 | Design Tenets for Agent Identity Management Systems | NIST — Cybersecurity Insights (blog) | 2026-10-27 | 2026-10-29 | <https://www.nist.gov/blogs/cybersecurity-insights/design-tenets-agent-identity-management-systems> |
| 347 | Securing Water and Wastewater Operational Technology Environments | NIST — Cybersecurity Insights (blog) | 2026-10-01 | 2026-10-29 | <https://www.nist.gov/blogs/cybersecurity-insights/securing-water-and-wastewater-operational-technology-environments> |
| 348 | Case Study: GitHub Expands Malware Advisories Across Eight Ecosystems with OpenSSF | OpenSSF — Blog | 2026-10-16 | 2026-10-29 | <https://openssf.org/blog/2026/10/16/case-study-github-expands-malware-advisories-across-eight-ecosystems-with-openssf/> |


### Références officielles du référentiel réglementaire et normatif

| Texte / norme | Référence | Sources officielles | Vérifié le |
|---|---|---|---|
| RGPD — Règlement général sur la protection des données | Règlement (UE) 2016/679 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32016R0679> | 2026-10-29 |
| NIS 2 — Directive sur la sécurité des réseaux et des systèmes d'information | Directive (UE) 2022/2555 ; règlement d'exécution (UE) 2024/2690 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022L2555,%20https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2690,%20https://monespacenis2.cyber.gouv.fr/> | 2026-10-29 |
| DORA — Résilience opérationnelle numérique du secteur financier | Règlement (UE) 2022/2554 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32022R2554> | 2026-10-29 |
| AI Act — Règlement européen sur l'intelligence artificielle | Règlement (UE) 2024/1689 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1689,%20https://ai-act-service-desk.ec.europa.eu/> | 2026-10-29 |
| CRA — Règlement sur la cyberrésilience | Règlement (UE) 2024/2847 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R2847> | 2026-10-29 |
| eIDAS 2 — Identité numérique européenne et services de confiance | Règlement (UE) 2024/1183 modifiant le règlement (UE) n° 910/2014 | <https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32024R1183> | 2026-10-29 |
| Dispositif OIV (loi de programmation militaire) | Code de la défense, art. L. 1332-6-1 et suivants | <https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006071307/LEGISCTA000028344696/> | 2026-10-29 |
| Certification Hébergeur de Données de Santé (HDS) | Code de la santé publique, art. L. 1111-8 ; référentiel de certification HDS | <https://esante.gouv.fr/produits-services/hds> | 2026-10-29 |
| PCI DSS — Sécurité des données de cartes de paiement | PCI DSS v4.0.1 (PCI Security Standards Council) | <https://www.pcisecuritystandards.org/document_library/> | 2026-10-29 |
| ISO/IEC 27001 — Systèmes de management de la sécurité de l'information | ISO/IEC 27001:2022 (+ Amd 1:2024) | <https://www.iso.org/standard/27001> | 2026-10-29 |
| ISO/IEC 27002 — Mesures de sécurité de l'information | ISO/IEC 27002:2022 | <https://www.iso.org/standard/75652.html> | 2026-10-29 |
| ISO/IEC 42001 — Système de management de l'IA | ISO/IEC 42001:2023 | <https://www.iso.org/standard/81230.html> | 2026-10-29 |
| NIST Cybersecurity Framework 2.0 | NIST CSWP 29 (CSF 2.0) | <https://www.nist.gov/cyberframework> | 2026-10-29 |
| Guide d'hygiène informatique de l'ANSSI et recommandations ANSSI | ANSSI — Guide d'hygiène informatique (42 mesures) et guides techniques | <https://cyber.gouv.fr/publications/guide-dhygiene-informatique> | 2026-10-29 |
| SecNumCloud — Référentiel de qualification des prestataires cloud | Référentiel SecNumCloud (ANSSI) | <https://cyber.gouv.fr/secnumcloud-pour-les-fournisseurs-de-services-cloud> | 2026-10-29 |
