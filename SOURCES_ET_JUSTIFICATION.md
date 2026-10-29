# Sources de veille : sélection, justification, fiabilité et limites

Toutes les sources marquées « Vérifiée, collectée » ont été testées le **29/10/2026** : réponse HTTP 200, flux
analysable et éléments lus. Elles ont ensuite été collectées avec succès lors d'une collecte complète, sur
**48 sources actives sur 48**. L'état de fonctionnement est réévalué à chaque collecte et visible dans la page
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

## 2. Catalogue initial

### Veille technique et cybersécurité

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 29/10/2026 |
|---|---|---|---|---|---|
| [CERT-FR — Alertes de sécurité](https://cert.cyber.gouv.fr/alerte/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 1 h | Centre gouvernemental de veille, d'alerte et de réponse aux attaques informatiques (ANSSI). Les alertes signalent des vulnérabilités activement exploitées ou critiques nécessitant une action rapide. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CERT-FR — Avis de sécurité](https://cert.cyber.gouv.fr/avis/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 1 h | Avis décrivant les vulnérabilités publiées par les éditeurs, les produits affectés et les correctifs. Source de référence francophone pour la gestion des correctifs. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CERT-FR — Menaces et incidents](https://cert.cyber.gouv.fr/cti/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 12 h | Rapports de menace (modes opératoires, rançongiciels, campagnes) produits par l'ANSSI. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CERT-FR — Bulletins d'actualité](https://cert.cyber.gouv.fr/actualite/feed/) | ANSSI / CERT-FR — Source officielle | Élevée | 12 h | Bulletins hebdomadaires synthétisant les vulnérabilités significatives et les recommandations associées. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CISA — Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | CISA (États-Unis) — Source officielle | Élevée | 6 h | Catalogue officiel des vulnérabilités dont l'exploitation active est confirmée par la CISA. Utilisé pour vérifier le critère « exploitation active » de la priorisation. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CISA — Cybersecurity Advisories](https://www.cisa.gov/cybersecurity-advisories/all.xml) | CISA (États-Unis) — Source officielle | Élevée | 3 h | Avis techniques (dont systèmes industriels) et alertes conjointes avec les agences partenaires. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CISA — Actualités](https://www.cisa.gov/news.xml) | CISA (États-Unis) — Source officielle | Élevée | 1 j | Annonces de la CISA (stratégies, guides conjoints, campagnes). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Cybermalveillance.gouv.fr — Actualités](https://www.cybermalveillance.gouv.fr/feed/atom-flux-actualites) | GIP ACYMA — Source officielle | Élevée | 12 h | Alertes sur les campagnes d'hameçonnage et d'escroquerie ; utile pour la sensibilisation des utilisateurs. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [NCSC (Royaume-Uni) — Publications](https://www.ncsc.gov.uk/api/1/services/v1/all-rss-feed.xml) | National Cyber Security Centre (UK) — Source officielle | Élevée | 1 j | Agence nationale homologue de l'ANSSI ; guides et recommandations de sécurité. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Microsoft — Security Update Guide](https://api.msrc.microsoft.com/update-guide/rss) | Microsoft MSRC — Éditeur / fournisseur | Élevée | 12 h | Source primaire des vulnérabilités et correctifs Microsoft (flux volumineux, limité aux 150 entrées les plus récentes). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Cisco — Security Advisories](https://sec.cloudapps.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml) | Cisco PSIRT — Éditeur / fournisseur | Élevée | 12 h | Avis de sécurité officiels Cisco (réseau, sécurité, collaboration). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Fortinet — PSIRT Advisories](https://filestore.fortinet.com/fortiguard/rss/ir.xml) | Fortinet PSIRT — Éditeur / fournisseur | Élevée | 12 h | Avis officiels Fortinet ; équipements fréquemment ciblés en périmètre réseau. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Ubuntu — Security Notices](https://ubuntu.com/security/notices/rss.xml) | Canonical — Éditeur / fournisseur | Élevée | 12 h | Bulletins de sécurité officiels de la distribution Ubuntu. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Debian — Security Advisories (DSA)](https://www.debian.org/security/dsa) | Projet Debian — Éditeur / fournisseur | Élevée | 12 h | Bulletins de sécurité officiels de Debian. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [BleepingComputer](https://www.bleepingcomputer.com/feed/) | BleepingComputer — Presse spécialisée | Moyenne | 2 h | Actualité rapide sur les rançongiciels, incidents et vulnérabilités ; à recouper avec une source primaire. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [The Hacker News](https://feeds.feedburner.com/TheHackersNews) | The Hacker News — Presse spécialisée | Moyenne | 3 h | Couverture large des menaces et vulnérabilités ; contenu parfois sponsorisé, à recouper. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [SANS Internet Storm Center — Diaries](https://isc.sans.edu/rssfeed_full.xml) | SANS Institute — Recherche / laboratoire | Élevée | 6 h | Analyses techniques quotidiennes par des incident handlers (observations terrain, détection). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Krebs on Security](https://krebsonsecurity.com/feed/) | Brian Krebs — Presse spécialisée | Moyenne | 1 j | Enquêtes sur la cybercriminalité et les incidents majeurs. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [ZATAZ](https://www.zataz.com/feed/) | ZATAZ — Presse spécialisée | Moyenne | 6 h | Actualité francophone sur les fuites de données et la cybercriminalité ; à recouper. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [WeLiveSecurity (ESET) — FR](https://www.welivesecurity.com/fr/rss/feed/) | ESET — Recherche / laboratoire | Moyenne | 12 h | Recherches sur les logiciels malveillants en français ; source éditeur (biais commercial possible). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [SecurityWeek](https://www.securityweek.com/feed/) | SecurityWeek — Presse spécialisée | Moyenne | 6 h | Actualité vulnérabilités, ICS et réglementation. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Palo Alto Networks — Unit 42](https://unit42.paloaltonetworks.com/feed/) | Palo Alto Networks — Recherche / laboratoire | Moyenne | 12 h | Analyses de campagnes et de modes opératoires ; source éditeur. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Cisco Talos Intelligence](https://blog.talosintelligence.com/rss/) | Cisco Talos — Recherche / laboratoire | Moyenne | 12 h | Recherche sur les menaces et vulnérabilités ; source éditeur. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Securelist (Kaspersky GReAT)](https://securelist.com/feed/) | Kaspersky — Recherche / laboratoire | Moyenne | 12 h | Analyses APT et logiciels malveillants ; à recouper (contexte géopolitique de l'éditeur). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [The DFIR Report](https://thedfirreport.com/feed/) | The DFIR Report — Recherche / laboratoire | Moyenne | 1 j | Retours d'expérience détaillés d'intrusions réelles (chaînes d'attaque, détections). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/feed/) | Microsoft — Éditeur / fournisseur | Moyenne | 1 j | Renseignement sur la menace (Microsoft Threat Intelligence) et nouveautés sécurité. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Feedly — Flux personnels (API officielle)](https://cloud.feedly.com/v3/streams/contents) | Feedly — Communauté / fondation / agrégateur | Moyenne | 6 h | Source complémentaire facultative : agrège les flux suivis dans le compte Feedly de l'utilisateur. La fiabilité dépend des flux d'origine (indiqués pour chaque article). | Désactivée par défaut (configuration requise) |

### Veille réglementaire

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 29/10/2026 |
|---|---|---|---|---|---|
| [CNIL — Actualités](https://www.cnil.fr/fr/rss.xml) | CNIL — Source officielle | Élevée | 12 h | Autorité française de protection des données ; recommandations, sanctions, référentiels RGPD. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [EDPB — Actualités](https://www.edpb.europa.eu/feed/news_en) | Comité européen de la protection des données — Source officielle | Élevée | 1 j | Lignes directrices et décisions contraignantes interprétant le RGPD au niveau européen. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [EUR-Lex — Législation du Parlement et du Conseil (filtrée)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=162) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Source officielle des textes législatifs de l'UE (identifiant CELEX, date de publication). Flux généraliste : un filtre par mots-clés ne conserve que les textes liés au numérique et à la sécurité. Filtre : cybersécurité, cyber, sécurité des réseaux, systèmes d'information, données à caractère personnel, protection des données… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [EUR-Lex — Propositions de la Commission (filtrées)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=161) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Propositions législatives (statut « projet ») permettant d'anticiper les évolutions réglementaires. Filtre : cybersécurité, cyber, sécurité des réseaux, données à caractère personnel, protection des données, intelligence artificielle… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [EUR-Lex — Actes du Journal officiel série L (filtrés)](https://eur-lex.europa.eu/FR/display-feed.rss?rssId=222) | Office des publications de l'UE — Source officielle | Élevée | 1 j | Actes publiés au JOUE, notamment les règlements d'exécution et délégués précisant NIS2, DORA, AI Act, CRA. Filtre : cybersécurité, cyber, sécurité des réseaux, données à caractère personnel, intelligence artificielle, résilience opérationnelle… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Commission européenne — AI Act Service Desk](https://ai-act-service-desk.ec.europa.eu/en/rss.xml) | Commission européenne (AI Office) — Source officielle | Élevée | 1 j | Point d'information officiel de la Commission sur la mise en œuvre du règlement IA. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Commission européenne — Stratégie numérique (filtrée)](https://digital-strategy.ec.europa.eu/en/rss.xml) | Commission européenne (DG CONNECT) — Source officielle | Élevée | 1 j | Annonces officielles (actes d'exécution, consultations, lignes directrices) sur NIS2, AI Act, CRA, eIDAS. Filtre : cyber, NIS2, NIS 2, AI Act, Artificial Intelligence Act, Cyber Resilience… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Autorité bancaire européenne (EBA) — Actualités (filtrées)](https://www.eba.europa.eu/rss.xml) | EBA — Source officielle | Élevée | 1 j | Normes techniques et orientations liées à DORA pour le secteur financier. Filtre : DORA, ICT, cyber, operational resilience, third-party, outsourcing… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [artificialintelligenceact.eu (non officiel)](https://artificialintelligenceact.eu/feed/) | Future of Life Institute — Communauté / fondation / agrégateur | Moyenne | 1 j | Site d'analyse NON officiel du règlement IA, utile pour suivre les débats ; toute information doit être confirmée sur EUR-Lex. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Légifrance — Journal officiel (JORF)](https://www.legifrance.gouv.fr/) | DILA — Source officielle | Élevée | 7 j | Source officielle des textes législatifs et réglementaires français (transposition NIS2, lois, décrets). | Non collectée automatiquement — voir alternative |

### Veille normative

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 29/10/2026 |
|---|---|---|---|---|---|
| [ISO Open Data — Métadonnées des normes surveillées](https://isopublicstorageprod.blob.core.windows.net/opendata/_latest/iso_deliverables_metadata/json/iso_deliverables_metadata.jsonl) | ISO — Source officielle | Élevée | 7 j | Jeu de données ouvert publié par l'ISO (métadonnées : référence, titre, édition, stade, date de publication, remplacements). Permet de détecter une nouvelle édition, un amendement ou une révision sans accéder au texte des normes, qui reste payant et n'est jamais reproduit. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [NIST — Cybersecurity Insights (blog)](https://www.nist.gov/blogs/cybersecurity-insights/rss.xml) | NIST — Source officielle | Élevée | 1 j | Annonces du NIST sur le Cybersecurity Framework, les SP 800, la cryptographie post-quantique et la sécurité de l'IA. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [NIST — Actualités (filtrées sécurité)](https://www.nist.gov/news-events/news/rss.xml) | NIST — Source officielle | Élevée | 1 j | Actualités officielles du NIST, filtrées sur la sécurité (normes FIPS, SP 800, PQC, IA). Filtre : cyber, security, cryptograph, post-quantum, privacy, identity… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [ANSSI — Guides et publications (cyber.gouv.fr)](https://cyber.gouv.fr/publications) | ANSSI — Source officielle | Élevée | 7 j | Guides d'hygiène, recommandations de configuration, référentiels (SecNumCloud, PASSI, etc.). | Non collectée automatiquement — voir alternative |
| [OpenSSF — Blog](https://openssf.org/feed/) | Open Source Security Foundation — Communauté / fondation / agrégateur | Moyenne | 1 j | Référentiels de bonnes pratiques pour la sécurité de la chaîne d'approvisionnement logicielle (SLSA, SBOM). | Vérifiée, collectée (HTTP 200, flux analysable) |

### Veille technologique

| Source | Organisme / nature | Confiance | Fréquence | Justification | État au 29/10/2026 |
|---|---|---|---|---|---|
| [Google Online Security Blog](https://security.googleblog.com/feeds/posts/default) | Google — Éditeur / fournisseur | Moyenne | 1 j | Innovations (post-quantique, sécurité de l'IA, mémoire sûre) publiées par les équipes sécurité de Google. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [AWS Security Blog](https://aws.amazon.com/blogs/security/feed/) | Amazon Web Services — Éditeur / fournisseur | Moyenne | 1 j | Nouveautés et bonnes pratiques de sécurité AWS (IAM, détection, chiffrement). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Cloudflare Blog](https://blog.cloudflare.com/rss/) | Cloudflare — Éditeur / fournisseur | Moyenne | 1 j | Retours techniques sur le déploiement post-quantique, le Zero Trust et les attaques DDoS. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Kubernetes Blog (filtré sécurité)](https://kubernetes.io/feed.xml) | CNCF / Kubernetes — Communauté / fondation / agrégateur | Élevée | 1 j | Annonces officielles du projet Kubernetes (fonctionnalités de sécurité, dépréciations). Filtre : security, CVE, vulnerab, RBAC, policy, secret… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CNCF — Blog](https://www.cncf.io/feed/) | Cloud Native Computing Foundation — Communauté / fondation / agrégateur | Moyenne | 1 j | Tendances cloud natif (sécurité des conteneurs, identité des charges de travail, IA). Filtre : security, zero trust, SBOM, supply chain, identity, policy… | Vérifiée, collectée (HTTP 200, flux analysable) |
| [GitHub Blog — Security](https://github.blog/category/security/feed/) | GitHub — Éditeur / fournisseur | Moyenne | 1 j | DevSecOps, sécurité des dépendances, analyse de code, gestion des secrets. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Elastic Security Labs](https://www.elastic.co/security-labs/rss/feed.xml) | Elastic — Recherche / laboratoire | Moyenne | 1 j | Recherches sur l'ingénierie de détection et les nouvelles techniques d'attaque. | Vérifiée, collectée (HTTP 200, flux analysable) |
| [CrowdStrike Blog](https://www.crowdstrike.com/blog/feed/) | CrowdStrike — Éditeur / fournisseur | Moyenne | 1 j | Tendances EDR/XDR et sécurité de l'IA ; source éditeur (biais commercial). | Vérifiée, collectée (HTTP 200, flux analysable) |
| [Schneier on Security](https://www.schneier.com/feed/atom/) | Bruce Schneier — Recherche / laboratoire | Moyenne | 1 j | Analyses d'expert reconnu en cryptographie et en politique de sécurité. | Vérifiée, collectée (HTTP 200, flux analysable) |

Total : 51 sources dont 48 actives

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

**Changement d'URL constaté** : le CERT-FR a migré de `www.cert.ssi.gouv.fr` vers `cert.cyber.gouv.fr` (redirection
302 observée le 29/10/2026). Le catalogue utilise le nouveau domaine. Par sécurité, une redirection vers un domaine
hors liste blanche est refusée et signalée avec un message explicite. Le changement doit alors être validé dans le catalogue.

## 4. Limites générales des sources

- **Couverture** : la veille couvre les sources du catalogue, pas l'ensemble de l'actualité. Les éditeurs du parc
  réel doivent être ajoutés (page *Sources*) : VMware/Broadcom, Veeam, GitLab, etc. n'ont pas tous un flux RSS public stable.
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
