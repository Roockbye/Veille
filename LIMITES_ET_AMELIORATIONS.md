# Limites connues et améliorations futures

## Limites connues

### Collecte
- **Légifrance et cyber.gouv.fr** ne sont pas collectés automatiquement : protections anti-robot, que l'outil ne
  contourne pas. Il faut les consulter manuellement ou développer un connecteur à l'API PISTE.
- **NIST CSRC et ENISA** n'ont pas de flux RSS fonctionnel à la date de vérification ; des alternatives partielles
  sont en place.
- Seuls le **titre et le résumé** fournis par les flux sont analysés, pas le contenu intégral des articles.
- Un flux n'expose que ses derniers éléments : une interruption longue de la collecte peut faire manquer des publications.
- La limite de débit du **NVD** sans clé (5 requêtes / 30 s) plafonne l'enrichissement à 40 CVE par exécution.
  Les autres CVE sont enrichies aux exécutions suivantes.
- Le premier chargement d'un flux ramène des éléments anciens. Ils sont pénalisés et exclus des rapports, mais
  restent visibles dans le flux.
- Risque résiduel de **DNS rebinding** : l'adresse est vérifiée avant la connexion, mais la bibliothèque HTTP
  résout à nouveau le nom. Le risque est limité par la liste blanche de domaines.

### Analyse
- La **classification par mots-clés** produit des faux positifs et négatifs. Exemples : un article de blog
  généraliste classé « vulnérabilité » ; un texte réglementaire formulé sans les mots-clés attendus.
- La **correspondance avec l'inventaire** porte sur des noms de produits. Les **versions affectées** ne sont pas
  comparées automatiquement aux versions du parc ; elles sont signalées « à vérifier ».
- Sans IA, les **résumés de sources anglophones** sont des synthèses structurées accompagnées d'un extrait original,
  sans traduction.
- Les **impacts C/I/D** sont déduits d'indices textuels. Ce sont des potentialités, pas des constats.
- Les poids du score et les seuils sont des choix méthodologiques documentés, à calibrer selon l'organisation.
- Le **rattachement aux scénarios redoutés** repose sur des mots-clés : un élément peut être rattaché à tort
  (mot-clé générique) ou manqué (vocabulaire différent). Les mots-clés se règlent dans le profil.
- Les équipements dont la **marque n'est pas documentée** (pare-feu/VPN et NAS d'AéroStar) sont détectés par des
  mots-clés génériques : les vulnérabilités de produits de ce type remontent toutes en « présence à confirmer »,
  tant que l'inventaire n'est pas complété.
- Le regroupement des sujets identiques (« confirmé par N sources ») repose sur des CVE communes. Les sujets sans CVE
  ne sont pas regroupés.

### Réglementaire et normatif
- La **base de connaissance** (`referentiels.yaml`) a été révisée le 31/10/2026 et doit être tenue à jour. Ses dates
  n'ont **pas été vérifiées automatiquement** : EUR-Lex et Légifrance refusent les clients automatisés. En
  particulier, les dates d'application de Part-IS et du règlement sur les biens à double usage sont à confirmer. Points à
  vérifier : transposition française de NIS 2, calendrier de l'AI Act (propositions de modification), actes
  d'exécution du CRA.
- L'applicabilité est une **orientation** fondée sur le profil déclaré, pas un avis juridique.
- Les normes ISO ne sont suivies que par leurs **métadonnées** ; le contenu des révisions n'est pas analysé.
- Le détail des exigences **AirCyber** (Bronze, Silver, Gold) n'est pas public : l'outil suit le programme et
  l'échéance, mais ne réalise pas d'analyse d'écarts automatique par rapport au niveau Bronze.
- **EN 9100** n'est pas couverte par l'ISO Open Data : une révision de la série 9100 doit être suivie manuellement
  (annonces de l'IAQG).

### Application
- L'interface n'a pas d'**authentification** ni de gestion des rôles : elle est prévue pour un usage local
  (`localhost`) ou derrière un reverse proxy authentifiant.
- **SQLite** convient à un usage mono-organisation. Il n'est pas adapté à de nombreux utilisateurs concurrents.
- Le planificateur intégré ne fonctionne que **pendant l'exécution du serveur Streamlit**.
- Le connecteur **Feedly** n'a pas pu être testé contre l'API réelle, faute de compte disposant d'un jeton.
  Il est testé avec des réponses simulées conformes à la documentation publique.

## Améliorations futures recommandées

| Priorité | Amélioration | Bénéfice |
|---|---|---|
| Haute | Connecteur API Légifrance (PISTE, OAuth client credentials) | Veille réglementaire française automatisée (transposition NIS 2, décrets) |
| Haute | Grille d'auto-évaluation AirCyber Bronze reliée au plan d'action (à partir des exigences communiquées par les clients) | Mesure de l'écart avant l'échéance de fin 2027 |
| Haute | Comparaison automatique des versions affectées (données CPE du NVD) avec les versions de l'inventaire | Moins de faux positifs, priorisation plus fine |
| Haute | Import de l'inventaire depuis un outil de gestion de parc (CSV, GLPI, export EDR) | Inventaire exhaustif et à jour |
| Moyenne | Authentification (SSO/OIDC) et rôles (analyste, RSSI, lecteur) | Usage multi-utilisateurs |
| Moyenne | Récupération du contenu complet des articles (dans le respect des conditions d'utilisation) | Analyse plus précise |
| Moyenne | Traduction locale (modèle hébergé en interne) | Résumés en français sans service externe |
| Moyenne | Regroupement sémantique des sujets (similarité de titres) | Synthèse plus lisible |
| Moyenne | Chiffrage assisté des actions (catalogue de coûts, aides Cyber Boost) | Arbitrage budgétaire sur l'enveloppe de 180 k€ |
| Moyenne | Indicateurs de performance de la veille (délai de traitement, taux de faux positifs) | Pilotage et amélioration continue |
| Basse | Export vers un outil de ticketing (GLPI, Jira) | Intégration au processus de changement |
| Basse | Passage à PostgreSQL | Montée en charge |
| Basse | Calibrage des poids du score à partir des décisions passées de l'analyste | Priorisation adaptée à l'organisation |
