# Méthodologie de veille

Ce document décrit la démarche de veille technologique, technique, réglementaire et normative mise en œuvre avec
l'outil, depuis le cadrage jusqu'à l'exploitation des résultats. Chaque étape est reliée au module qui la réalise.

## 1. Cycle de veille

```
 Cadrage ──► Sourcing ──► Collecte ──► Traitement ──► Analyse ──► Diffusion ──► Exploitation ──► Évaluation
 (profil)   (catalogue)  (automatique) (dédoublonnage,  (pertinence,  (rapport,     (plan d'action,  (état des sources,
                                         classification, priorité,     tableau de    statuts)         ajustement du
                                         enrichissement) impacts)      bord)                          périmètre)
     ▲                                                                                                    │
     └────────────────────────────────────────── amélioration continue ◄──────────────────────────────────┘
```

| Étape | Objectif | Mise en œuvre dans l'outil |
|---|---|---|
| Cadrage | Définir qui est concerné, ce qu'on surveille et pourquoi. | Profil de l'organisation (page *Configuration*, `config/organisation.yaml`) : secteur, taille, rôles, activités, données, inventaire, exigences, thèmes, fréquences. |
| Sourcing | Choisir des sources fiables et justifiées. | Catalogue (`config/sources.yaml`, page *Sources*) : catégorie, nature, confiance, justification, fréquence, alternative. |
| Collecte | Récupérer les informations de façon automatique et traçable. | `veille/collector.py`, `veille/collectors/*`, `veille/net.py`. |
| Traitement | Normaliser, dédoublonner, classer, enrichir. | `normalize.py`, `classify.py`, `collectors/enrichment.py`. |
| Analyse | Évaluer la pertinence, les impacts et la priorité ; identifier obligations et opportunités. | `analysis.py`, `knowledge.py`, `technologies.py`. |
| Diffusion | Restituer de manière exploitable. | Tableau de bord, fiches, rapports PDF/Markdown (`reports/`). |
| Exploitation | Décider et agir. | Plan d'action (`actions.py`, page *Plan d'action*), statuts de traitement. |
| Évaluation | Vérifier l'efficacité de la veille. | État et historique des sources, historique des exécutions, limites listées dans chaque rapport. |

## 2. Cadrage : le contexte de l'organisation

La pertinence d'une information dépend du contexte. L'outil n'applique **jamais** une réglementation par défaut :
l'applicabilité est évaluée à partir du profil déclaré.

- **Inventaire technique** : chaque technologie a des mots-clés de détection, des versions, une **exposition**
  (Internet, DMZ, interne) et une **criticité** métier. Ces deux derniers attributs pondèrent la priorité.
  *Bonne pratique* : préférer des noms de produit (« FortiGate », « Exchange Server ») aux noms d'éditeur, trop larges.
- **Rôles** (responsable de traitement, prestataire TIC du secteur financier, déployeur d'IA, hébergeur de données
  de santé, etc.) : ils sont déterminants pour l'applicabilité des textes.
- **Gestionnaire de chaque technologie** (équipe interne, infogérant, fournisseur SaaS) : il détermine à qui
  revient l'action. Pour AéroStar, le pare-feu et le VPN SSL sont gérés par l'infogérant : l'action devient
  « demander le correctif à l'infogérant et une confirmation écrite ». Pour Microsoft 365, l'outil rappelle la
  responsabilité partagée avec le fournisseur.
- **Marque non documentée** : la fiche AéroStar ne précise pas le modèle du pare-feu ni celui du NAS. Ces
  équipements sont décrits par des mots-clés génériques (« SSL VPN », « NAS ») et marqués `marque_inconnue`.
  Une vulnérabilité de ce type de produit est signalée, mais la présence dans le parc reste « à confirmer » et la
  première action proposée est d'identifier la marque auprès du gestionnaire.
- **Exclusions** : expressions qui désignent un autre produit portant un nom proche, par exemple
  « Veeam Backup for Microsoft 365 » pour Microsoft 365.
- **Scénarios redoutés** : ce sont les risques majeurs de l'organisation, avec des mots-clés. Pour AéroStar :
  rançongiciel via compte volé et compromission de l'AD, compromission de messagerie Microsoft 365 par
  hameçonnage, fuite de plans clients. Les éléments de veille qui s'y rattachent sont signalés et comptés : ils
  renseignent la vraisemblance de chaque scénario dans l'analyse de risques.
- **Besoins de sécurité (DICT), échéances, parties prenantes et responsables** : ils sont repris dans le rapport.
  Exemples : AirCyber Bronze fin 2027, renouvellement de l'assurance cyber en 2027. Les responsables nommés
  remplacent un « RSSI » générique ; AéroStar n'en a pas, c'est le responsable IT qui est référent sécurité.
- **Profil incomplet** : l'outil continue de fonctionner avec des **hypothèses explicitement signalées** dans
  l'interface et dans chaque rapport. Par exemple : « Inventaire technique vide : les vulnérabilités sont classées
  À qualifier plutôt qu'écartées ».

## 3. Sourcing : sélection des sources

Critères de sélection (détail dans [SOURCES_ET_JUSTIFICATION.md](SOURCES_ET_JUSTIFICATION.md)) :

1. **Primauté** : la source primaire (autorité, éditeur, texte officiel) est préférée au relais.
2. **Autorité de l'émetteur** : agences nationales (ANSSI/CERT-FR, CISA, NCSC, NIST), autorités de contrôle (CNIL, EDPB),
   institutions de l'UE (EUR-Lex, Commission), organismes de normalisation (ISO).
3. **Couverture** : les quatre axes (technique, réglementaire, normatif, technologique) et les éditeurs du parc.
4. **Accessibilité autorisée** : flux RSS ou interface publique documentée. Aucune protection anti-robot n'est contournée.
5. **Diversité** : sources francophones et internationales ; presse spécialisée et recherche pour la réactivité,
   signalées « à recouper ».

Chaque source porte un **niveau de confiance attendu** (élevée, moyenne, faible). Ce niveau entre dans le calcul
de la confiance de chaque analyse. Une source accessible n'est pas réputée fiable pour autant.

## 4. Collecte

- **Fréquence par source** (de 1 h pour les alertes CERT-FR à 7 jours pour les métadonnées ISO). Le planificateur
  vérifie régulièrement quelles sources sont « dues ».
- **Respect des sites** : robots.txt (RFC 9309, redirections suivies), délai minimal entre requêtes vers un même hôte
  (et `Crawl-delay`), requêtes conditionnelles `ETag` / `If-Modified-Since`, limites de débit du NVD (6,5 s sans clé).
- **Robustesse** : délai d'attente, reprises exponentielles sur erreurs transitoires (réseau, 429, 5xx), flux mal
  formés tolérés (les éléments lisibles sont conservés), page HTML renvoyée à la place d'un flux détectée.
  Une erreur sur une source n'interrompt pas les autres. Chaque écriture est transactionnelle : aucune donnée
  déjà collectée n'est perdue.
- **Traçabilité** : chaque élément conserve son URL d'origine, sa source, sa **date de publication** et sa **date de
  collecte**, qui sert de date de consultation. Chaque exécution et chaque interrogation de source sont historisées
  (tables `executions` et `verifications_sources`).
- **Minimisation** : seuls le titre, le résumé, l'URL, la date et le nom d'auteur publié sont conservés. Les adresses
  e-mail des auteurs sont supprimées.
- **Filtrage à la source** : pour les flux généralistes (EUR-Lex, NIST, Commission), un filtre par mots-clés ne
  conserve que les éléments liés au numérique et à la sécurité. Le nombre d'éléments écartés est tracé.

## 5. Traitement

1. **Déduplication** : URL canonique (schéma, hôte, suppression des paramètres `utm_*`, `fbclid`, etc., tri des
   paramètres, sans fragment), puis empreinte SHA-256 du titre et du début du résumé normalisés. Cette seconde
   étape détecte les republications sous une autre URL.
2. **Classification** en 8 catégories, éventuellement plusieurs par élément : menace, vulnérabilité/correctif,
   évolution technologique, réglementaire, normative, bonne pratique, incident/retour d'expérience, non pertinent.
   Elle repose sur des règles explicites : mots-clés FR/EN avec un poids double dans le titre, acronymes en
   recherche exacte, indices tirés de la catégorie et du type de source, pénalité pour les contenus promotionnels.
   Les mots déclencheurs sont conservés pour justifier la décision.
3. **Enrichissement** des CVE citées : CVSS depuis l'API NVD (score « Primary » prioritaire, version et source
   mémorisées), exploitation active depuis le catalogue CISA KEV, probabilité EPSS depuis FIRST. Les CVE exploitées
   et les plus récentes sont interrogées en priorité. **Une valeur absente reste absente** et elle est signalée
   « à vérifier ».

## 6. Analyse et priorisation

### 6.1 Pertinence

| Niveau | Règle |
|---|---|
| Forte | Une technologie de l'inventaire est citée, ou un texte dont l'applicabilité est probable. |
| Moyenne | Thème surveillé, impact indirect (clients, contrats), ou menace générique transposable. |
| À qualifier | Information potentiellement importante, mais le profil ne permet pas de conclure (inventaire vide, applicabilité non évaluable). |
| Faible | Produits cités absents de l'inventaire, ou aucun lien établi. Une vulnérabilité, ou une campagne exploitant des CVE, sur un produit absent du parc reste « faible », même si elle évoque un thème surveillé. Les produits associés aux CVE par le catalogue KEV sont pris en compte. |
| Non pertinente | Aucun indicateur de veille (bruit, promotion). |

### 6.2 Score explicable

Chaque point attribué est accompagné de sa justification, de son origine et de la mention **vérifié** ou
**déclaré par la source**.

| Facteur | Points | Donnée utilisée |
|---|---|---|
| Gravité technique | 30 (CVSS ≥ 9), 20 (≥ 7), 10 (≥ 4), 3 | CVSS du NVD (vérifié) |
| | 12 | Gravité « critique » annoncée par la source, sans CVSS (non vérifié) |
| Exploitation active | 30 (+5 si rançongiciel) | CVE présente dans le KEV (vérifié) |
| | 18 / 8 | Exploitation ou preuve de concept signalée par la source (non vérifié) |
| Probabilité d'exploitation | 10 (EPSS ≥ 0,5), 5 (≥ 0,1) | FIRST EPSS |
| Présence dans le parc | 25 (+5 si version citée) ; 10 si la marque n'est pas documentée (présence à confirmer) | Inventaire déclaré |
| Exposition | 15 (Internet), 8 (DMZ) | Inventaire déclaré |
| Impact sur les activités | 10 / 6 / 3 selon la criticité | Inventaire déclaré |
| Scénario redouté | 10 | Mots-clés des scénarios redoutés du profil (menaces, vulnérabilités, incidents, bonnes pratiques) |
| Urgence | 10 | Alerte CERT-FR |
| Importance réglementaire ou normative | 30 (obligation légale probable), 15 (norme probable ou impact indirect), 8 (à qualifier) | Référentiel et profil |
| Évolution normative | 20 (changement constaté), 10 (révision engagée) | ISO Open Data |
| Thème surveillé | 10 | Profil |
| Menace transposable | 8 | Contenu |
| Fiabilité de la source faible | −5 | Catalogue |
| Ancienneté | −15 (> 90 j), −25 (> 1 an) | Date de publication |
| Bruit | −10 | Contenu promotionnel |

### 6.3 Niveaux

| Niveau | Condition |
|---|---|
| **Critique** | Score ≥ 75 **et** technologie du parc **identifiée** (marque connue) **et** gravité ou exploitation **vérifiée** (KEV, CVSS ≥ 9 ou alerte CERT-FR). |
| **Élevée** | Score ≥ 50, ou ≥ 75 sans les conditions du niveau critique (plafonnement justifié). |
| **Modérée** | Score ≥ 25. |
| **Faible** | Score < 25, ou information non pertinente. |
| **À qualifier** | Pertinence non déterminable avec le profil actuel et score < 50. |

Plafonnements explicites :
- pertinence faible → au plus Modérée ;
- plus de 90 jours → au plus Élevée ;
- plus d'un an → au plus Modérée ;
- évolution uniquement réglementaire ou normative → au plus Élevée.

### 6.4 Réponse proposée

Selon la catégorie et le contexte, l'outil propose une réponse **proportionnée** :
- vérification de l'exposition et des versions ;
- mise à jour ;
- mesure compensatoire, si la technologie est exposée ;
- recherche de compromission, si l'exploitation est active ;
- contrôle de configuration et couverture de détection ;
- sensibilisation (hameçonnage) et vérification des sauvegardes (rançongiciel) ;
- analyse de conformité (applicabilité puis analyse d'écarts) ;
- étude complémentaire ou d'opportunité.

Si la maturité déclarée est faible, l'outil recommande de privilégier les mesures simples à fort effet.
L'échéance dépend du niveau : Critique 48 h, Élevée 7 j, Modérée 30 j, Faible 90 j, À qualifier 7 j pour la qualification.

### 6.5 Veille réglementaire et normative

- **Référentiel** (`config/referentiels.yaml`) : il donne pour chaque texte sa référence, sa **nature juridique**,
  son statut, ses dates avec la source officielle, les organisations concernées, les obligations possibles et les
  démarches pour qualifier l'applicabilité. Cette base de connaissance de configuration est datée (`revise_le`)
  et présentée comme telle, distincte des informations collectées. Ses dates **n'ont pas été vérifiées
  automatiquement** (EUR-Lex et Légifrance refusent les clients automatisés) : elles sont à revérifier sur la source officielle.
- **Statut « cible »** d'une exigence : un référentiel volontaire visé mais non exigé (ISO/IEC 27001 pour AéroStar)
  reste « à qualifier » et n'est jamais présenté comme une obligation.
- **Applicabilité** : des règles sur le secteur, la taille, les rôles, les données et les exigences déclarées
  produisent une **orientation**, jamais une conclusion : *probable — à confirmer*, *indirect*, *à qualifier*,
  *peu probable*, *non évaluable (informations manquantes)*.
- **Fiche réglementaire** par élément : texte concerné, nature de l'évolution (projet, adoption, publication,
  entrée en application, lignes directrices, sanction…), statut juridique. Le statut n'est déduit que d'indices
  explicites, comme l'identifiant CELEX ; sinon il reste « à vérifier ». La fiche donne aussi les dates mentionnées
  avec leur URL, les organisations concernées, les obligations possibles, les démarches et l'impact.
- **Distinction normative** : norme (volontaire), référentiel de bonnes pratiques, recommandation (non contraignante),
  exigence contractuelle, obligation légale. **Une recommandation n'est jamais présentée comme une obligation légale.**
- **Normes payantes** : seules les métadonnées publiques ISO (édition, stade, remplacements) sont suivies, avec
  détection des changements entre deux collectes. Le texte n'est jamais consulté ni reproduit.

### 6.6 Veille technologique

Une grille d'analyse par thème (`veille/technologies.py`) couvre les usages possibles, les bénéfices attendus, les
risques associés et les prérequis de sécurité. Les éléments des thèmes surveillés de priorité modérée ou plus
alimentent les **opportunités d'amélioration** du plan d'action.

## 7. Distinction des natures d'information

Dans les fiches et les rapports, chaque affirmation est étiquetée :

| Étiquette | Signification |
|---|---|
| [Fait] | Information issue d'une source consultable (URL citée en annexe). |
| [Donnée vérifiée] | Valeur issue d'une base de référence (NVD, CISA KEV, FIRST EPSS, ISO Open Data). |
| [Analyse] | Résultat des règles de l'outil (catégorie, pertinence, priorité, impact). |
| [Hypothèse] | Supposition liée à un profil incomplet ou à une donnée déclarative. |
| [Recommandation] | Proposition d'action, à valider par un responsable. |
| [À vérifier] | Point non confirmé (CVSS absent, exploitation non confirmée, statut juridique…). |

## 8. Diffusion et exploitation

- **Tableau de bord** : volumes, alertes critiques et élevées ouvertes, état des sources, actions.
- **Qualification** par l'analyste : statut historisé (nouveau → lu / pertinent / non pertinent / à investiguer →
  traité) et notes. Les éléments marqués non pertinents sont exclus des rapports.
- **Plan d'action** : les actions sont créées automatiquement pour les priorités critiques et élevées, ainsi que pour
  les évolutions réglementaires et normatives et les opportunités pertinentes. L'analyste les complète, les valide et
  les suit jusqu'à « terminée » avec les preuves attendues. Une action modifiée par un utilisateur n'est jamais
  écrasée par une réanalyse.
- **Rapport périodique** (hebdomadaire ou mensuel, ou à la demande) en 18 sections. Les éléments publiés plus de
  30 jours avant la période sont exclus, et ce nombre est indiqué. Les sujets couverts par plusieurs sources sont
  regroupés dans le résumé exécutif (« confirmé par N sources »).

## 9. Rôles suggérés

| Rôle | Responsabilités dans la veille |
|---|---|
| RSSI | Pilote la veille, valide les priorités et le plan d'action, présente le rapport à la direction. |
| Équipe infrastructure / exploitation | Vérifie l'exposition, applique les correctifs et mesures compensatoires. |
| SOC / supervision | Vérifie la couverture de détection et recherche des traces de compromission. |
| Juriste / DPO | Qualifie l'applicabilité des textes et pilote les analyses d'écarts. |
| DSI / direction | Arbitre les opportunités technologiques et les moyens. |

## 10. Évaluation de la veille

Indicateurs disponibles dans l'outil :
- taux de sources fonctionnelles ;
- volume collecté par période et par catégorie ;
- nombre d'éléments critiques et élevés, et délai de traitement (historique des statuts) ;
- actions ouvertes et terminées ;
- nombre de points « à vérifier ».

Chaque rapport liste ses propres limites : sources non collectées, CVSS manquants, exploitation non confirmée,
résumés non traduits, hypothèses.
