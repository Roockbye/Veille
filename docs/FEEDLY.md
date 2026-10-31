# Intégration de Feedly (facultative)

L'application **fonctionne entièrement sans Feedly** grâce à ses propres connecteurs RSS. Feedly est une source
complémentaire, utile si vous suivez déjà des flux dans votre compte.

> Aucune hypothèse n'est faite sur votre abonnement. Les fonctionnalités ci-dessous dépendent de votre offre Feedly
> et doivent être vérifiées dans votre compte. **Ne communiquez jamais votre mot de passe Feedly** : l'application
> ne le demande pas et n'utilise que des mécanismes officiels.

## Options d'intégration

| Option | Prérequis | Mise en œuvre | État dans l'application |
|---|---|---|---|
| 1. Import OPML des abonnements | Export OPML depuis Feedly (fonction d'organisation des sources) | Page *Sources* › Import / export › Importer un fichier OPML. Chaque flux devient une source RSS collectée **directement** auprès de son éditeur. | Implémenté et testé (`parse_opml`). **Recommandé.** |
| 2. Flux RSS publics des éditeurs | Aucun | Ajouter la source dans le catalogue. | Implémenté |
| 3. Flux RSS exportés par Feedly (dossier ou tableau partagé en RSS) | Fonction disponible selon l'offre Feedly : à vérifier | Ajouter l'URL fournie par Feedly comme source de type `rss`, puis la tester. | Implémenté (connecteur RSS générique) |
| 4. API officielle Feedly (`cloud.feedly.com/v3`) | Jeton d'accès délivré par Feedly selon l'offre (jeton développeur ou accès entreprise) : à vérifier dans les paramètres du compte | Renseigner `FEEDLY_ACCESS_TOKEN` (et éventuellement `FEEDLY_STREAM_ID`) dans `.env`, puis activer la source « Feedly — Flux personnels » dans la page *Sources*. | Implémenté (`veille/collectors/feedly.py`), testé avec des réponses simulées ; **non testé contre l'API réelle** faute de jeton. |
| 5. Export d'articles (tableaux / *boards*) | Selon l'offre | Utiliser l'option 3 si un flux RSS est proposé, sinon l'import OPML. | Pas de format d'export d'articles spécifique implémenté |

## Fonctionnement du connecteur API

1. Authentification par en-tête `Authorization: Bearer <jeton>` (ou `OAuth <jeton>` avec `FEEDLY_AUTH_SCHEME=OAuth`, forme utilisée par la documentation historique de Feedly). Le jeton est lu depuis l'environnement, il n'est
   ni stocké en base ni journalisé, et les messages d'erreur ne le contiennent jamais (vérifié par un test).
2. Sans `FEEDLY_STREAM_ID`, le profil (`GET /v3/profile`) fournit l'identifiant utilisateur et le flux
   `user/<id>/category/global.all` est lu.
3. Lecture des derniers éléments : `GET /v3/streams/contents?streamId=…&count=N&ranked=newest`, avec N borné par
   `max_items`, 100 par défaut.
4. Chaque article conserve l'URL d'origine (lien `alternate`) et le nom du flux d'origine (« Feedly — <flux> »),
   pour que sa fiabilité soit évaluée d'après la source réelle.
5. Erreurs : `401/403` → « jeton invalide, expiré ou offre sans accès API » ; `429` → reprise différée ; absence de
   jeton → statut « non configuré », sans incidence sur les autres sources.

Le domaine `cloud.feedly.com` est autorisé dans la liste blanche réseau, car il figure dans le catalogue.

## Limites

- Les quotas et la durée de validité des jetons dépendent de Feedly (un jeton développeur peut expirer).
  En cas d'échec, l'état de la source l'indique.
- Les articles Feedly passent par l'agrégateur : la fiabilité dépend du flux d'origine, et la confiance de la source
  « Feedly » est donc fixée à « moyenne ».
- Pour une présentation, l'**import OPML** est l'option la plus simple et la plus robuste : il ne dépend d'aucun jeton.
