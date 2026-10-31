# Sources de veille : sélection, justification, fiabilité et limites

Toutes les sources actives ont été testées les **29 et 31/10/2026** : réponse HTTP 200, flux
analysable et éléments lus. Elles ont ensuite été collectées avec succès lors d'une collecte complète, sur
**48 sources actives sur 48** le 29/10, puis à nouveau 48 sur 48 lors de la collecte incrémentale du 31/10. L'état de fonctionnement est réévalué à chaque collecte et visible dans la page
*Sources et méthodologie* (statut, dernier succès, dernière erreur, historique des vérifications).

## 1. Critères de sélection et d'évaluation de la fiabilité

| Critère | Question posée | Effet dans l'outil |
|---|---|---|
| Nature de l'émetteur | Autorité publique, éditeur concerné, presse, recherche, communauté ? | Champ `nature` |
| Caractère primaire | L'information est-elle produite par la source ou relayée ? | Confiance élevée réservée aux sources primaires |
| Historique et réputation | La source est-elle reconnue et corrige-t-elle ses erreurs ? | Champ `confiance` |
| Transparence | Date, auteur, références et identifiants (CVE, CELEX) sont-ils fournis ? | Extraction des CVE et dates ; points « à vérifier » |
| Biais possibles | Intérêt commercial, contexte géopolitique, contenu sponsorisé ? | Mentionnés dans la justification ; « à recouper » |
| Accessibilité autorisée | Flux RSS ou API publique ; conditions d'utilisation et robots.txt respectés ? | Collecte automatique ou source manuelle |

**Une source accessible n'est pas réputée fiable pour autant.** Pour les informations issues de sources de confiance
moyenne, l'analyse ajoute systématiquement « Source secondaire : recouper avec une source primaire ». Une exploitation
active n'est considérée comme **vérifiée** que si elle figure au catalogue CISA KEV.

## 2. Catalogue adapté au profil AéroStar

Le catalogue initial (51 sources, vérifiées le 29/10/2026) a été adapté le 31/10/2026 au contexte d'AéroStar :

- **Ajoutées et vérifiées** : actualités de l'EASA (Part-IS), BoostAeroSpace (référentiel AirCyber exigé par les
  clients), nginx (serveur de l'intranet), textes et rapports du Sénat. Ces derniers servent à suivre le projet de loi
  de transposition de NIS 2, signalé « point à suivre » dans la fiche de l'organisation.
- **Ajoutée comme source manuelle** : avis de sécurité de Dassault Systèmes (CATIA, 3DEXPERIENCE), sans flux RSS.
- **Désactivées avec justification** : EBA (DORA, secteur financier), Kubernetes, CNCF et AWS (technologies absentes
  du SI). Elles restent dans le catalogue et peuvent être réactivées.
- **Filtres EUR-Lex** étendus au double usage et à l'aviation (2021/821, 2022/1645, 2023/203).
- **Filtres du Sénat** resserrés après un premier passage trop large : 29 textes sans rapport avec la cybersécurité
  ont été retenus puis supprimés le 31/10/2026.

### Veille technique et cybersécurité

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 31/10/2026 |
|---|---|---|---|---|---|
| [CERT-FR — Alertes de sécurité](https://cert.cyber.gouv.fr/alerte/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 1 h | Centre gouvernemental de veille, d'alerte et de réponse aux attaques informatiques (ANSSI). Les alertes signalent des vulnérabilités activement exploitées ou critiques nécessitant une action rapide. | Collectée avec succès |
| [CERT-FR — Avis de sécurité](https://cert.cyber.gouv.fr/avis/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 1 h | Avis décrivant les vulnérabilités publiées par les éditeurs, les produits affectés et les correctifs. Source de référence francophone pour la gestion des correctifs. | Collectée avec succès |
| [CERT-FR — Menaces et incidents](https://cert.cyber.gouv.fr/cti/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 12 h | Rapports de menace (modes opératoires, rançongiciels, campagnes) produits par l'ANSSI. | Collectée avec succès |
| [CERT-FR — Bulletins d'actualité](https://cert.cyber.gouv.fr/actualite/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 12 h | Bulletins hebdomadaires synthétisant les vulnérabilités significatives et les recommandations associées. | Collectée avec succès |
| [CISA — Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | CISA (États-Unis) — Source officielle | Élevée | 6 h | Catalogue officiel des vulnérabilités dont l'exploitation active est confirmée par la CISA. Utilisé pour vérifier le critère « exploitation active » de la priorisation. | Collectée avec succès |
| [CISA — Cybersecurity Advisories](https://www.cisa.gov/cybersecurity-advisories/all.xml) | CISA (États-Unis) — Source officielle | Élevée | 3 h | Avis techniques (dont systèmes industriels) et alertes conjointes avec les agences partenaires. | Collectée avec succès |
| [CISA — Actualités](https://www.cisa.gov/news.xml) | CISA (États-Unis) — Source officielle | Élevée | 1 j | Annonces de la CISA (stratégies, guides conjoints, campagnes). | Collectée avec succès |
| [Cybermalveillance.gouv.fr — Actualités](https://www.cybermalveillance.gouv.fr/feed/atom-flux-actualites) | GIP ACYMA — Source officielle | Élevée | 12 h | Alertes sur les campagnes d'hameçonnage et d'escroquerie ; utile pour la sensibilisation des utilisateurs. | Collectée avec succès |
| [NCSC (Royaume-Uni) — Publications](https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml) | National Cyber Security Centre (UK) — Source officielle | Élevée | 1 j | Agence nationale homologue de l'ANSSI ; guides et recommandations de sécurité. | Collectée avec succès |
| [Microsoft — Security Update Guide](https://api.msrc.microsoft.com/update-guide/rss) | Microsoft MSRC — Éditeur / fournisseur | Élevée | 12 h | Source primaire des vulnérabilités et correctifs Microsoft (flux volumineux, limité aux 150 entrées les plus récentes). | Collectée avec succès |
| [Cisco — Security Advisories](https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml) | Cisco PSIRT — Éditeur / fournisseur | Élevée | 12 h | Avis de sécurité officiels Cisco (réseau, sécurité, collaboration). | Collectée avec succès |
| [Fortinet — PSIRT Advisories](https://filestore.fortinet.com/fortiguard/rss/ir.xml) | Fortinet PSIRT — Éditeur / fournisseur | Élevée | 12 h | Avis officiels Fortinet ; équipements fréquemment ciblés en périmètre réseau. | Collectée avec succès |
| [Ubuntu — Security Notices](https://ubuntu.com/security/notices/rss.xml) | Canonical — Éditeur / fournisseur | Élevée | 12 h | Bulletins de sécurité officiels de la distribution Ubuntu. | Collectée avec succès |
| [Debian — Security Advisories (DSA)](https://www.debian.org/security/dsa) | Projet Debian — Éditeur / fournisseur | Élevée | 12 h | Bulletins de sécurité officiels de Debian. | Collectée avec succès |
| [BleepingComputer](https://www.bleepingcomputer.com/feed/) | BleepingComputer — Presse spécialisée | Moyenne | 2 h | Actualité rapide sur les rançongiciels, incidents et vulnérabilités ; à recouper avec une source primaire. | Collectée avec succès |
| [The Hacker News](https://feeds.feedburner.com/TheHackersNews) | The Hacker News — Presse spécialisée | Moyenne | 3 h | Couverture large des menaces et vulnérabilités ; contenu parfois sponsorisé, à recouper. | Collectée avec succès |
| [SANS Internet Storm Center — Diaries](https://isc.sans.edu/rssfeed_full.xml) | SANS Institute — Recherche / laboratoire | Élevée | 6 h | Analyses techniques quotidiennes par des incident handlers (observations terrain, détection). | Collectée avec succès |
| [Krebs on Security](https://krebsonsecurity.com/feed/) | Brian Krebs — Presse spécialisée | Moyenne | 1 j | Enquêtes sur la cybercriminalité et les incidents majeurs. | Collectée avec succès |
| [ZATAZ](https://www.zataz.com/feed/) | ZATAZ — Presse spécialisée | Moyenne | 6 h | Actualité francophone sur les fuites de données et la cybercriminalité ; à recouper. | Collectée avec succès |
| [WeLiveSecurity (ESET) — FR](https://www.welivesecurity.com/fr/rss/feed/) | ESET — Recherche / laboratoire | Moyenne | 12 h | Recherches sur les logiciels malveillants en français ; source éditeur (biais commercial possible). | Collectée avec succès |
| [SecurityWeek](https://www.securityweek.com/feed/) | SecurityWeek — Presse spécialisée | Moyenne | 6 h | Actualité vulnérabilités, ICS et réglementation. | Collectée avec succès |
| [Palo Alto Networks — Unit 42](https://unit42.paloaltonetworks.com/feed/) | Palo Alto Networks — Recherche / laboratoire | Moyenne | 12 h | Analyses de campagnes et de modes opératoires ; source éditeur. | Collectée avec succès |
| [Cisco Talos Intelligence](https://blog.talosintelligence.com/rss/) | Cisco Talos — Recherche / laboratoire | Moyenne | 12 h | Recherche sur les menaces et vulnérabilités ; source éditeur. | Collectée avec succès |
| [Securelist (Kaspersky GReAT)](https://securelist.com/feed/) | Kaspersky — Recherche / laboratoire | Moyenne | 12 h | Analyses APT et logiciels malveillants ; à recouper (contexte géopolitique de l'éditeur). | Collectée avec succès |
| [The DFIR Report](https://thedfirreport.com/feed/) | The DFIR Report — Recherche / laboratoire | Moyenne | 1 j | Retours d'expérience détaillés d'intrusions réelles (chaînes d'attaque, détections). | Collectée avec succès |
| [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/feed/) | Microsoft — Éditeur / fournisseur | Moyenne | 1 j | Renseignement sur la menace (Microsoft Threat Intelligence) et nouveautés sécurité. | Collectée avec succès |
| [Dassault Systèmes — Avis de sécurité (Trust Center)](https://www.3ds.com/trust-center/security/security-advisories) | Dassault Systèmes — Éditeur / fournisseur | Élevée | 7 j | Éditeur des outils métier critiques du bureau d'études (CATIA V5, 3DEXPERIENCE, serveur de licences). | Non collectée automatiquement — voir alternative |
| [nginx — Actualités (correctifs de sécurité)](https://nginx.org/index.rss) | nginx — Éditeur / fournisseur | Élevée | 1 j | Annonces officielles de versions correctives de nginx (serveur de l'intranet). Filtre : security, vulnerab, CVE… | Collectée avec succès |
| [Feedly — Flux personnels (API officielle)](https://cloud.feedly.com/v3/streams/contents) | Feedly — Communauté / fondation / agrégateur | Moyenne | 6 h | Source complémentaire facultative : agrège les flux suivis dans le compte Feedly de l'utilisateur. La fiabilité dépend des flux d'origine (indiqués pour chaque article). | Désactivée par défaut : jeton Feedly requis (alternative : import OPML) |

### Veille réglementaire

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 31/10/2026 |
|---|---|---|---|---|---|
| [CNIL — Actualités](https://www.cnil.fr/fr/rss.xml) | CNIL — Source officielle | Élevée | 12 h | Autorité française de protection des données ; recommandations, sanctions, référentiels RGPD. | Collectée avec succès |
| [EDPB — Actualités](https://www.edpb.europa.eu/feed/news_en) | Comité européen de la protection des données — Source officielle | Élevée | 1 j | Lignes directrices et décisions contraignantes interprétant le RGPD au niveau européen. | Collectée avec succès |
| [EUR-Lex — Législation du Parlement et du Conseil (filtrée)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=162) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Source officielle des textes législatifs de l'UE (identifiant CELEX, date de publication). Flux généraliste : un filtre par mots-clés ne conserve que les textes liés au numérique et à la sécurité. Filtre : double usage, 2021/821, aviation, sécurité aérienne, 2022/1645, 2023/203… | Collectée avec succès |
| [EUR-Lex — Propositions de la Commission (filtrées)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=161) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Propositions législatives (statut « projet ») permettant d'anticiper les évolutions réglementaires. Filtre : cybersécurité, cyber, sécurité des réseaux, données à caractère personnel, protection des données, intelligence artificielle… | Collectée avec succès |
| [EUR-Lex — Actes du Journal officiel série L (filtrés)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=222) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Actes publiés au JOUE, notamment les règlements d'exécution et délégués précisant NIS2, DORA, AI Act, CRA. Filtre : double usage, 2021/821, aviation, sécurité aérienne, 2022/1645, 2023/203… | Collectée avec succès |
| [Commission européenne — AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/rss.xml) | Commission européenne (AI Office) — Source officielle | Élevée | 1 j | Point d'information officiel de la Commission sur la mise en œuvre du règlement IA. | Collectée avec succès |
| [Commission européenne — Stratégie numérique (filtrée)](https://digital-strategy.ec.europa.eu/en/rss.xml) | Commission européenne (DG CONNECT) — Source officielle | Élevée | 1 j | Annonces officielles (actes d'exécution, consultations, lignes directrices) sur NIS2, AI Act, CRA, eIDAS. Filtre : cyber, NIS2, NIS 2, AI Act, Artificial Intelligence Act, Cyber Resilience… | Collectée avec succès |
| [Autorité bancaire européenne (EBA) — Actualités (filtrées)](https://www.eba.europa.eu/rss.xml) | EBA — Source officielle | Élevée | 1 j | Normes techniques et orientations liées à DORA pour le secteur financier. Filtre : DORA, ICT, cyber, operational resilience, third-party, outsourcing… | Désactivée pour le profil AéroStar — DORA ne concerne que le secteur financier (applicabilité peu probable) |
| [artificialintelligenceact.eu (non officiel)](https://artificialintelligenceact.eu/feed/) | Future of Life Institute — Communauté / fondation / agrégateur | Moyenne | 1 j | Site d'analyse NON officiel du règlement IA, utile pour suivre les débats ; toute information doit être confirmée sur EUR-Lex. | Collectée avec succès |
| [Légifrance — Journal officiel (JORF)](https://www.legifrance.gouv.fr/) | DILA — Source officielle | Élevée | 7 j | Source officielle des textes législatifs et réglementaires français (transposition NIS2, lois, décrets). | Non collectée automatiquement — voir alternative |
| [Sénat — Derniers textes (filtrés)](https://www.senat.fr/rss/textes.xml) | Sénat — Source officielle | Élevée | 1 j | Textes déposés et adoptés au Sénat : permet de suivre l'avancement du projet de loi de transposition de NIS 2 (en discussion au Parlement en octobre 2026), Légifrance n'étant pas collectable automatiquement. Filtre : cybersécurité, cyberattaque, résilience des infrastructures critiques, NIS 2, NIS2, 2022/2555… | Collectée avec succès |
| [Sénat — Derniers rapports (filtrés)](https://www.senat.fr/rss/rapports.xml) | Sénat — Source officielle | Élevée | 1 j | Rapports de commission (dont ceux sur le projet de loi de transposition NIS 2) éclairant le contenu et le calendrier des obligations. Filtre : cybersécurité, cyberattaque, résilience des infrastructures critiques, NIS 2, NIS2, 2022/2555… | Collectée avec succès |
| [EASA — Actualités (filtrées cybersécurité)](https://www.easa.europa.eu/en/newsroom-and-events/news/feed.xml) | Agence de l'Union européenne pour la sécurité aérienne — Source officielle | Élevée | 1 j | Autorité européenne de l'aviation : publications relatives au règlement Part-IS (sécurité de l'information), susceptibles d'être répercutées par les clients de rang 1 sur leurs sous-traitants. Filtre : cyber, information security, Part-IS, cybersecurity, security risk… | Collectée avec succès |

### Veille normative

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 31/10/2026 |
|---|---|---|---|---|---|
| [ISO Open Data — Métadonnées des normes surveillées](https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/iso_deliverables_metadata/json/iso_deliverables_metadata.jsonl) | ISO — Source officielle | Élevée | 7 j | Jeu de données ouvert publié par l'ISO (métadonnées : référence, titre, édition, stade, date de publication, remplacements). Permet de détecter une nouvelle édition, un amendement ou une révision sans accéder au texte des normes, qui reste payant et n'est jamais reproduit. | Collectée avec succès |
| [NIST — Cybersecurity Insights (blog)](https://www.nist.gov/blogs/cybersecurity-insights/rss.xml) | NIST — Source officielle | Élevée | 1 j | Annonces du NIST sur le Cybersecurity Framework, les SP 800, la cryptographie post-quantique et la sécurité de l'IA. | Collectée avec succès |
| [NIST — Actualités (filtrées sécurité)](https://www.nist.gov/news-events/news/rss.xml) | NIST — Source officielle | Élevée | 1 j | Actualités officielles du NIST, filtrées sur la sécurité (normes FIPS, SP 800, PQC, IA). Filtre : cyber, security, cryptograph, post-quantum, privacy, identity… | Collectée avec succès |
| [ANSSI — Guides et publications (cyber.gouv.fr)](https://cyber.gouv.fr/publications) | ANSSI — Source officielle | Élevée | 7 j | Guides d'hygiène, recommandations de configuration, référentiels (SecNumCloud, PASSI, etc.). | Non collectée automatiquement — voir alternative |
| [OpenSSF — Blog](https://openssf.org/feed/) | Open Source Security Foundation — Communauté / fondation / agrégateur | Moyenne | 1 j | Référentiels de bonnes pratiques pour la sécurité de la chaîne d'approvisionnement logicielle (SLSA, SBOM). | Collectée avec succès |
| [BoostAeroSpace — Actualités (AirCyber)](https://boostaerospace.com/feed/) | BoostAeroSpace — Source officielle | Élevée | 7 j | Opérateur du référentiel de maturité AirCyber exigé par les clients (Bronze fin 2027). Flux valide mais sans publication au 31/10/2026 ; surveillé pour détecter toute évolution du programme. | Collectée avec succès |

### Veille technologique

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 31/10/2026 |
|---|---|---|---|---|---|
| [Google Online Security Blog](https://security.googleblog.com/feeds/posts/default) | Google — Éditeur / fournisseur | Moyenne | 1 j | Innovations (post-quantique, sécurité de l'IA, mémoire sûre) publiées par les équipes sécurité de Google. | Collectée avec succès |
| [AWS Security Blog](https://aws.amazon.com/blogs/security/feed/) | Amazon Web Services — Éditeur / fournisseur | Moyenne | 1 j | Nouveautés et bonnes pratiques de sécurité AWS (IAM, détection, chiffrement). | Désactivée pour le profil AéroStar — pas d'usage d'AWS déclaré (le cloud se limite à Microsoft 365 et à l'ERP en SaaS) |
| [Cloudflare Blog](https://blog.cloudflare.com/rss/) | Cloudflare — Éditeur / fournisseur | Moyenne | 1 j | Retours techniques sur le déploiement post-quantique, le Zero Trust et les attaques DDoS. | Collectée avec succès |
| [Kubernetes Blog (filtré sécurité)](https://kubernetes.io/feed.xml) | CNCF / Kubernetes — Communauté / fondation / agrégateur | Élevée | 1 j | Annonces officielles du projet Kubernetes (fonctionnalités de sécurité, dépréciations). Filtre : security, CVE, vulnerab, RBAC, policy, secret… | Désactivée pour le profil AéroStar — pas de conteneurs dans le SI |
| [CNCF — Blog](https://www.cncf.io/feed/) | Cloud Native Computing Foundation — Communauté / fondation / agrégateur | Moyenne | 1 j | Tendances cloud natif (sécurité des conteneurs, identité des charges de travail, IA). Filtre : security, zero trust, SBOM, supply chain, identity, policy… | Désactivée pour le profil AéroStar — pas d'environnement cloud natif |
| [GitHub Blog — Security](https://github.blog/category/security/feed/) | GitHub — Éditeur / fournisseur | Moyenne | 1 j | DevSecOps, sécurité des dépendances, analyse de code, gestion des secrets. | Collectée avec succès |
| [Elastic Security Labs](https://www.elastic.co/security-labs/rss/feed.xml) | Elastic — Recherche / laboratoire | Moyenne | 1 j | Recherches sur l'ingénierie de détection et les nouvelles techniques d'attaque. | Collectée avec succès |
| [CrowdStrike Blog](https://www.crowdstrike.com/blog/feed/) | CrowdStrike — Éditeur / fournisseur | Moyenne | 1 j | Tendances EDR/XDR et sécurité de l'IA ; source éditeur (biais commercial). | Collectée avec succès |
| [Schneier on Security](https://www.schneier.com/feed/atom/) | Bruce Schneier — Recherche / laboratoire | Moyenne | 1 j | Analyses d'expert reconnu en cryptographie et en politique de sécurité. | Collectée avec succès |

Total : 57 sources, dont 49 actives.

### Sources d'enrichissement (interrogées pour les CVE citées, non affichées comme sources d'articles)

| Service | Usage | Fiabilité | Limites |
|---|---|---|---|
| [API NVD 2.0](https://nvd.nist.gov/developers/vulnerabilities) (NIST) | Score CVSS, vecteur, sévérité, source du score | Élevée (référence officielle) | Délai d'évaluation des CVE récentes ; 5 requêtes / 30 s sans clé (clé gratuite : `NVD_API_KEY`) |
| [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Exploitation active **confirmée** | Élevée | Centré sur les produits utilisés par l'administration américaine ; l'absence du KEV ne prouve pas l'absence d'exploitation |
| [FIRST EPSS](https://www.first.org/epss/) | Probabilité d'exploitation à 30 jours | Élevée (modèle statistique documenté) | Indicateur probabiliste, pas une preuve d'exploitation |

## 3. Sources non collectées automatiquement et alternatives

| Source souhaitée | Constat du 29/10/2026 | Décision | Alternative documentée |
|---|---|---|---|
| **Légifrance** (JORF, textes français) | Les URL RSS renvoient une page de vérification anti-robot Cloudflare (HTTP 403). | Aucune tentative de contournement ; source « manuelle », désactivée. | API Légifrance officielle via le portail **PISTE** (compte et identifiants OAuth requis : connecteur à développer) ; consultation manuelle hebdomadaire ; textes européens via EUR-Lex. |
| **ANSSI — cyber.gouv.fr** (guides, référentiels) | Site protégé par Incapsula ; pas de flux RSS exploitable. | Aucune tentative de contournement ; source « manuelle », désactivée. | Flux **CERT-FR** (même organisme) collectés automatiquement ; consultation manuelle mensuelle des publications ; référentiel ANSSI décrit dans `config/referentiels.yaml`. |
| **NIST CSRC** (flux des publications SP 800 / FIPS) | Les anciennes URL de flux renvoient HTTP 404. | Non intégré. | Blog NIST *Cybersecurity Insights* et actualités NIST filtrées (collectés). |
| **ENISA** (actualités) | URL RSS testées en HTTP 404. | Non intégré. | Stratégie numérique de la Commission (filtrée) et EUR-Lex. |
| **ISO** (pages de normes) | Pages iso.org protégées (HTTP 403 pour un client automatisé). | Pas de collecte des pages. | Jeu **ISO Open Data** (métadonnées publiques) collecté chaque semaine. |
| **Feedly** | Dépend de l'offre et d'un jeton de l'utilisateur. | Connecteur fourni, désactivé par défaut. | Import OPML des abonnements (voir `docs/FEEDLY.md`). |
| **Dassault Systèmes** (avis de sécurité) | Page HTML sans flux RSS (31/10/2026). | Source « manuelle ». | CVE remontées par le NVD, le KEV et le CERT-FR ; consultation mensuelle de la page. |
| **GIFAS** (programme Cyber Boost) | Pas de flux RSS trouvé (HTTP 404, 31/10/2026). | Non intégré. | Suivi via BoostAeroSpace et contact direct du programme. |
| **EUR-Lex** (pages de documents) | Défi anti-robot (HTTP 202 vide) pour les clients automatisés. | Les flux RSS EUR-Lex restent collectés ; les dates du référentiel ne sont pas vérifiées automatiquement. | Vérification manuelle des dates sur EUR-Lex. |

**Changement d'URL constaté** : le CERT-FR a migré de `www.cert.ssi.gouv.fr` vers `cert.cyber.gouv.fr` (redirection
302 observée le 29/10/2026). Le catalogue utilise le nouveau domaine. Par sécurité, une redirection vers un domaine
hors liste blanche est refusée et signalée avec un message explicite. Le changement doit alors être validé dans le catalogue.

## 4. Limites générales des sources

- **Couverture** : la veille couvre les sources du catalogue, pas l'ensemble de l'actualité. Plusieurs éditeurs du
  parc d'AéroStar n'ont pas de flux RSS public : Dassault Systèmes, MSC/Hexagon (Nastran, Patran), l'éditeur de l'ERP
  SaaS, la plateforme d'échange de la filière. Le constructeur du pare-feu et du NAS n'est pas connu. Leurs
  vulnérabilités ne remontent que via le NVD, le KEV, le CERT-FR ou la presse.
- **Langue** : de nombreuses sources sont en anglais. Sans IA, le résumé en français est une synthèse par règles,
  accompagnée d'un extrait original.
- **Profondeur** : seuls le titre et le résumé des flux sont analysés, pas l'article complet.
- **Flux généralistes** : EUR-Lex et la Commission sont filtrés par mots-clés. Un texte pertinent formulé autrement
  peut être écarté ; les mots-clés sont ajustables.
- **Historique des flux** : un flux ne fournit que ses N derniers éléments. Une collecte interrompue longtemps peut
  manquer des publications ; le KEV et les métadonnées ISO sont en revanche complets.
- **Sources éditeurs et presse** : biais commerciaux possibles ; le contenu sponsorisé est pénalisé, sans garantie.
- **Réglementaire** : la base de connaissance (`referentiels.yaml`) est datée et doit être revérifiée. Les textes
  nationaux ne sont pas collectés automatiquement.

## 5. Ajouter ou modifier une source

Page *Sources et méthodologie*, onglet « Ajouter / modifier ». Une justification est obligatoire. La nouvelle source
démarre au statut « non vérifiée » ; le bouton « Tester » confirme son fonctionnement. Son domaine est
automatiquement ajouté à la liste blanche réseau. L'export YAML permet de versionner le catalogue.
