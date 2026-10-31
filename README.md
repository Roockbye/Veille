# VeilleCyber — veille technologique, technique, réglementaire et normative en cybersécurité

Application locale qui **collecte** automatiquement des informations auprès de sources fiables et vérifiées,
les **classe**, les **analyse** au regard du contexte d'une organisation, **priorise** les risques de manière
explicable, propose un **plan d'action** et génère un **rapport de veille** argumenté (PDF et Markdown).

L'outil est configuré pour **AéroStar SAS**, une organisation **fictive** servant de cas d'étude : bureau
d'études aéronautique de rang 2 (120 salariés, Blagnac), dépositaire des plans et maquettes de ses clients,
qui doit atteindre le niveau **AirCyber Bronze fin 2027** et renouveler son assurance cyber en 2027. Le contexte
d'AéroStar est inventé ; les sources, les référentiels et les informations collectées sont réels.

> L'outil est un outil de **veille et d'aide à la décision** : il ne réalise aucun scan, aucune modification
> du système d'information et aucune remédiation automatique.

---

## Sommaire

1. [Fonctionnalités](#fonctionnalités)
2. [Prérequis](#prérequis)
3. [Installation](#installation)
4. [Lancement](#lancement)
5. [Premier usage](#premier-usage)
6. [Ligne de commande](#ligne-de-commande)
7. [Automatisation](#automatisation-et-conditions-dexécution)
8. [Configuration](#configuration)
9. [Sécurité](#sécurité)
10. [Tests](#tests)
11. [Architecture](#architecture)
12. [Documentation associée](#documentation-associée)
13. [Dépannage](#dépannage)

---

## Fonctionnalités

| Domaine | Ce que fait l'application |
|---|---|
| Contexte | Profil de l'organisation : secteur, taille, maturité, rôles, activités, données traitées, inventaire technique (exposition, criticité, versions, gestionnaire, marque connue ou non, exclusions), contraintes, constats, **besoins de sécurité (DICT)**, **scénarios redoutés**, **échéances**, **parties prenantes**, **responsables**, exigences, thèmes surveillés. Hypothèses explicites si le profil est incomplet. |
| Sources | Catalogue de 57 sources (49 actives, vérifiées les 29 et 31/10/2026), adapté au profil (sources aéronautiques et parlementaires ajoutées, sources hors contexte désactivées avec justification), modifiable depuis l'interface : justification, confiance, fréquence, état de fonctionnement, alternative documentée. Import OPML (Feedly), export YAML. |
| Collecte | RSS/Atom, catalogue CISA KEV (JSON), métadonnées ISO Open Data, API Feedly facultative. Fréquence par source, robots.txt respecté, requêtes conditionnelles, reprises, journal par source, historique. |
| Déduplication | URL canonique (paramètres de suivi supprimés) puis empreinte du contenu. |
| Enrichissement | CVSS (API NVD), exploitation active (CISA KEV), probabilité d'exploitation (FIRST EPSS). **Aucune valeur n'est estimée.** |
| Analyse | 8 catégories, résumé en français, mots-clés, technologies du parc concernées, CVE, impacts C/I/D/conformité, **lien avec les scénarios redoutés**, pertinence, priorité justifiée, actions attribuées aux responsables de l'organisation (dont l'infogérant), échéance, urgence, confiance, points à vérifier. Fiches réglementaire et normative dédiées. |
| Priorisation | Score additif explicable (gravité, exploitation, présence et exposition dans le parc, criticité, scénario redouté, urgence, importance réglementaire, ancienneté) → Critique / Élevée / Modérée / Faible / À qualifier. |
| Réglementaire et normatif | Référentiel de 19 textes et normes (RGPD, NIS 2, DORA, AI Act, CRA, eIDAS 2, OIV, HDS, PCI DSS, Part-IS, biens à double usage, AirCyber, EN 9100, ISO 27001/27002/42001, NIST CSF, ANSSI, SecNumCloud) avec nature juridique et **orientation** d'applicabilité justifiée, jamais présentée comme une conclusion juridique ; suivi de la transposition française de NIS 2 via les flux du Sénat. |
| Plan d'action | Constat, risque/opportunité, action, justification, priorité, responsable, échéance, effort, bénéfice, **coût estimé**, preuves, statut ; modification et export CSV. Échéances de l'organisation (AirCyber, assurance) avec délai restant. |
| Suivi | Statut de chaque information (nouveau, lu, pertinent, non pertinent, à investiguer, traité) avec historique. |
| Rapports | Rapport en 18 sections, PDF et Markdown, période et périmètre au choix, prévisualisation. Faits, données vérifiées, analyses, hypothèses et recommandations étiquetés ; annexes avec URL et dates de consultation. |
| Automatisation | Planificateur intégré ou service autonome (systemd, cron, Docker), verrou anti-doublon, notifications e-mail facultatives. |
| IA (facultative) | Résumés en français via l'API Claude si une clé est fournie ; contenus collectés traités comme données non fiables ; la priorité reste calculée par règles. |

---

## Prérequis

- **Python 3.11 ou supérieur** (testé avec Python 3.13.5 sous Debian 13).
- Accès Internet sortant HTTPS vers les sources du catalogue.
- Linux, macOS ou Windows. Pour le PDF, la police DejaVu est utilisée si elle est présente
  (paquet `fonts-dejavu-core` sous Debian/Ubuntu) ; sinon Helvetica est utilisée avec substitution de quelques symboles.
- Facultatif : Docker et Docker Compose v2.24 ou supérieur.

Aucun compte, aucune clé API ni aucun service payant n'est nécessaire au fonctionnement principal.

## Installation

```bash
git clone <url-du-depot> Veille && cd Veille        # ou copier le répertoire du projet
python3 -m venv .venv
source .venv/bin/activate                            # Windows : .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                                 # facultatif : clés NVD / Feedly / IA / SMTP
python -m veille init                                # crée data/veille.db et charge le catalogue de sources
```

## Lancement

```bash
source .venv/bin/activate
streamlit run app/streamlit_app.py
```

Ouvrir ensuite <http://localhost:8501>. Le serveur écoute uniquement sur `localhost`
(voir [.streamlit/config.toml](.streamlit/config.toml)).

Avec Docker :

```bash
docker compose up -d --build      # interface + service de planification ; http://localhost:8501
```

## Premier usage

1. **Configuration de l'organisation** : le profil d'AéroStar (`config/organisation.example.yaml`) est chargé
   par défaut. Vérifiez-le puis enregistrez-le : il est écrit dans `config/organisation.yaml`, fichier non versionné.
   Après toute modification, cliquez sur « Réanalyser » pour appliquer le nouveau contexte.
2. **Tableau de bord**, bouton « Tout collecter » : la première collecte interroge les 49 sources actives et dure
   environ 5 à 8 minutes, à cause de la limite de débit de l'API NVD sans clé. Les collectes suivantes n'interrogent
   que les sources dont la fréquence est échue.
3. **Flux de veille** et **Vulnérabilités et menaces** : sélectionnez un élément pour afficher sa fiche, puis
   qualifiez-le (statut, notes).
4. **Plan d'action** : validez, planifiez et suivez les actions proposées.
5. **Rapports** : choisissez la période et le périmètre, prévisualisez, puis générez le PDF et le Markdown.

**Exemple de rapport** : [exemples/EXEMPLE_rapport_veille_AeroStar_2026-10-24_2026-10-31.pdf](exemples/EXEMPLE_rapport_veille_AeroStar_2026-10-24_2026-10-31.pdf)
et sa [version Markdown](exemples/EXEMPLE_rapport_veille_AeroStar_2026-10-24_2026-10-31.md), généré à partir de collectes
**réelles** des 29 et 31/10/2026 analysées avec le profil d'AéroStar (organisation fictive).

## Ligne de commande

```bash
python -m veille init                         # initialise la base et le catalogue
python -m veille collect                      # collecte les sources dues, enrichit, analyse, met à jour le plan d'action
python -m veille collect --all                # toutes les sources actives
python -m veille collect --source cnil        # une source (option répétable)
python -m veille analyze --all                # réanalyse tout, par exemple après modification du profil
python -m veille report --jours 7             # rapport des 7 derniers jours (PDF + MD dans data/rapports/)
python -m veille report --debut 2026-10-01 --fin 2026-10-31 --categories reglementaire,normative --formats pdf
python -m veille scheduler                    # service de planification en premier plan
python -m veille status                       # état de la base
python -m veille sources-export > sources.yaml
```

## Automatisation et conditions d'exécution

| Mode | Fonctionnement | Quand l'utiliser |
|---|---|---|
| Planificateur **intégré** | Démarré par le serveur Streamlit si « Tâches planifiées activées » est coché (page *Automatisation*). **Il s'arrête avec le serveur.** | Démonstration, poste allumé en permanence. |
| **Service** systemd | `python -m veille scheduler` lancé par [docs/deploiement/veille-scheduler.service](docs/deploiement/veille-scheduler.service). Tourne sans interface ni navigateur. | Serveur ou poste dédié. |
| **cron** | Collecte horaire et rapport hebdomadaire ([docs/deploiement/crontab.example](docs/deploiement/crontab.example)). | Exécution ponctuelle sans service permanent. |
| **Docker Compose** | Service `scheduler` séparé de l'interface (`VEILLE_SCHEDULER_INTEGRE=0`). | Déploiement conteneurisé. |

- Les tâches planifiées sont **désactivées par défaut**. Activez-les dans la page *Automatisation et journaux*.
  Le service systemd/Docker respecte ce même interrupteur.
- La collecte planifiée vérifie toutes les 30 minutes (valeur paramétrable) les sources « dues » selon leur propre fréquence.
  Les rapports sont générés le lundi à 7 h (hebdomadaire) ou le 1er du mois (mensuel).
- Un verrou en base empêche deux collectes simultanées (interface et service).
- Journaux : `data/logs/veille.log` (secrets masqués) et historique des exécutions dans l'interface.
- Notifications e-mail : facultatives, actives uniquement si les variables `SMTP_*` sont renseignées dans `.env`
  **et** que l'option est activée.

## Configuration

| Fichier | Rôle |
|---|---|
| `config/organisation.yaml` | Profil de l'organisation enregistré depuis l'interface (non versionné). |
| `config/organisation.example.yaml` | Profil d'exemple : AéroStar, organisation fictive (cas d'étude). |
| `config/sources.yaml` | Catalogue initial des sources. Ensuite, la base fait foi : modifications dans l'interface, export YAML possible. |
| `config/referentiels.yaml` | Textes réglementaires et normes : nature juridique, dates, obligations possibles, règles d'applicabilité. |
| `config/settings.yaml` | Paramètres par défaut : collecte, enrichissement, planification, notifications, IA. Les modifications faites dans l'interface sont stockées en base. |
| `.env` | Secrets facultatifs (`NVD_API_KEY`, `FEEDLY_ACCESS_TOKEN`, `ANTHROPIC_API_KEY`, `SMTP_*`). Ne jamais le versionner. |

- **Feedly** : voir [docs/FEEDLY.md](docs/FEEDLY.md). Sans jeton API, utilisez l'import OPML.
- **IA facultative** : renseignez `ANTHROPIC_API_KEY` dans `.env`, puis activez l'option dans *Automatisation*.
  Le modèle se règle avec `VEILLE_AI_MODEL` (par défaut `claude-opus-5-5` ; `claude-haiku-5-5` est moins coûteux
  pour un gros volume). Les requêtes activent le repli côté serveur (`fallbacks: "default"`) en cas de refus du modèle.

## Sécurité

- Aucun secret dans le code. `.env.example` ne contient aucune valeur réelle. `.gitignore` exclut `.env`,
  `data/` et le profil réel.
- **Requêtes sortantes limitées** aux domaines des sources configurées et des API d'enrichissement (liste blanche).
- **Protection SSRF** : seules les URL `http(s)` sont acceptées, sans identifiants intégrés et sur les ports 80/443 ;
  les adresses IP littérales sont refusées. L'adresse résolue doit être publique : 127/8, 10/8, 172.16/12,
  192.168/16, 169.254/16 (métadonnées cloud) et IPv6 locales sont refusées, y compris l'IPv4 embarquée en NAT64.
  Chaque redirection est revalidée.
- Taille des réponses et délais bornés, reprises limitées, délai minimal par hôte, robots.txt respecté.
- Contenus collectés traités comme **non fiables** : HTML converti en texte, échappement Markdown dans l'interface
  et les rapports, liens limités à `http(s)`, YAML lu avec `safe_load`, OPML sans entités XML.
- **SQL entièrement paramétré**, validation des saisies (sources, profil, actions).
- **IA** : aucun outil déclaré, sortie contrainte par un schéma puis revalidée. Seuls le titre et le résumé public
  sont transmis, jamais l'inventaire ni le profil. Le délimiteur du contenu est aléatoire.
- Journaux : masquage des clés, jetons et mots de passe. Le jeton Feedly n'apparaît dans aucun message d'erreur.
- L'interface n'a **pas d'authentification** : elle écoute sur `localhost` uniquement. Pour un usage partagé,
  placez-la derrière un reverse proxy avec authentification (et HTTPS).

## Tests

```bash
source .venv/bin/activate
python -m pytest
```

Les 123 tests ne font **aucun appel réseau** : les transports HTTP sont simulés. Ils couvrent la normalisation,
la protection SSRF, les connecteurs (RSS, Atom, flux malformés, KEV, ISO, Feedly), la déduplication, la reprise
après erreur sans perte de données, la classification, la priorisation (y compris l'absence de CVSS inventé),
l'applicabilité, la génération des rapports, la sécurité de l'IA, le masquage des secrets, la planification
et le rendu des 10 pages de l'interface, ainsi que la cohérence du profil AéroStar avec sa fiche et des fichiers de configuration.

## Architecture

```
app/                     Interface Streamlit (10 pages) — streamlit_app.py, ui.py, views/
veille/
  config.py              Chemins, YAML, variables d'environnement
  organisation.py        Profil de l'organisation, hypothèses, paramètres effectifs
  sources.py             Gestion du catalogue (validation, OPML, export, liste blanche)
  net.py                 Client HTTP sécurisé (SSRF, robots.txt, reprises, limites)
  collector.py           Orchestrateur de collecte (fréquences, verrou, statuts, historique)
  collectors/            rss.py, cisa_kev.py, iso_opendata.py, feedly.py, enrichment.py (NVD, EPSS)
  normalize.py           URL canonique, empreinte, nettoyage HTML, dates
  storage.py, schema.sql Stockage SQLite (voir docs/SCHEMA_BDD.md)
  classify.py            Classification par règles, impacts, thèmes, inventaire
  knowledge.py           Référentiel réglementaire et normatif, applicabilité
  analysis.py            Fiche d'analyse, priorisation explicable, recommandations
  actions.py             Génération du plan d'action
  reports/               builder.py (contenu), markdown.py, pdf.py (ReportLab)
  scheduler.py           APScheduler (intégré ou service)
  pipeline.py            Collecte → enrichissement → analyse → actions → IA → notification
  ai.py, notify.py       IA facultative (SDK anthropic), e-mail facultatif
  cli.py                 Ligne de commande
config/                  Fichiers de configuration (séparés du code)
tests/                   Tests pytest et jeux de données de test
docs/                    FEEDLY.md, SCHEMA_BDD.md, deploiement/
exemples/                Exemple de rapport AéroStar (PDF + Markdown)
```

## Documentation associée

- [METHODOLOGIE_VEILLE.md](METHODOLOGIE_VEILLE.md) : démarche de veille.
- [SOURCES_ET_JUSTIFICATION.md](SOURCES_ET_JUSTIFICATION.md) : pertinence, fiabilité et limites des sources.
- [GUIDE_DEMONSTRATION.md](GUIDE_DEMONSTRATION.md) : scénario de présentation de l'outil.
- [LIMITES_ET_AMELIORATIONS.md](LIMITES_ET_AMELIORATIONS.md) : limites connues et améliorations futures.
- [docs/FEEDLY.md](docs/FEEDLY.md) : intégration Feedly.
- [docs/SCHEMA_BDD.md](docs/SCHEMA_BDD.md) : schéma de la base de données.

## Dépannage

| Symptôme | Cause probable / solution |
|---|---|
| Source « Bloquée — robots.txt » | Le site interdit la collecte du chemin : utiliser l'alternative documentée. |
| Source « Bloquée — redirection … refusée » | Le site a changé de domaine : vérifier la redirection, puis mettre à jour l'URL de la source (page *Sources*). |
| Source « Bloquée — adresse non publique » | DNS interne ou proxy transparent : vérifier la résolution DNS du poste. |
| CVSS « non disponible » | CVE non encore évaluée par le NVD ou limite de débit (40 CVE par exécution sans clé) : ajouter `NVD_API_KEY`. |
| Première collecte longue | Normal : environ 6,5 s entre deux requêtes NVD sans clé API. |
| PDF avec symboles remplacés | Installer `fonts-dejavu-core`. |
| `streamlit: command not found` | Activer l'environnement virtuel (`source .venv/bin/activate`). |
