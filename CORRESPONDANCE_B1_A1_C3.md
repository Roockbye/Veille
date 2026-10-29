# Correspondance avec la compétence B1.A1.C3

> **B1.A1.C3** — *Assurer une veille technologique, technique, réglementaire et normative à l'aide d'outils
> adaptés, en surveillant les innovations technologiques, les évolutions des cadres légaux et des standards
> applicables, en analysant leurs impacts sur l'organisation afin d'identifier les obligations et les opportunités
> d'amélioration en matière de sécurité du système d'information.*

Le tableau décompose l'énoncé en critères observables. Pour chacun, il indique les fonctionnalités qui y répondent
et les **preuves** que l'on peut montrer. Les numéros de section renvoient au rapport généré
(exemple : [exemples/EXEMPLE_rapport_veille_demo_2026-10-22_2026-10-29.pdf](exemples/EXEMPLE_rapport_veille_demo_2026-10-22_2026-10-29.pdf)).

## 1. Tableau de correspondance

| # | Critère issu de l'énoncé | Fonctionnalités | Preuves disponibles |
|---|---|---|---|
| C1 | **Veille technique** (vulnérabilités, menaces, correctifs) | Flux CERT-FR (alertes, avis, menaces, bulletins), CISA (avis, KEV), NCSC, éditeurs du parc (Microsoft, Cisco, Fortinet, Ubuntu, Debian), recherche et presse ; enrichissement CVSS/KEV/EPSS | Page *Vulnérabilités et menaces* (onglets KEV × inventaire, CVE enrichies) ; rapport §6 et §7 ; `config/sources.yaml` |
| C2 | **Veille technologique** et **innovations** | 9 thèmes : IA générative, ML pour la cybersécurité, SOAR, SIEM/EDR/XDR, Zero Trust/IAM, cloud/conteneurs, post-quantique, DevSecOps/SBOM, détection/remédiation ; grille usages, bénéfices, risques, prérequis | Page *Technologies et innovations* ; rapport §8 et §13 ; `veille/technologies.py` |
| C3 | **Veille réglementaire** : évolutions des **cadres légaux** | Flux CNIL, EDPB, EUR-Lex (législation, propositions, JO série L, filtrés), AI Act Service Desk, Commission, EBA ; référentiel RGPD, NIS 2, DORA, AI Act, CRA, eIDAS 2, OIV, HDS ; fiche réglementaire (nature, statut, dates sourcées, organisations concernées, obligations possibles, démarches) | Page *Réglementation et normes* (onglets Textes, Évolutions) ; rapport §9 et §12 ; `config/referentiels.yaml` |
| C4 | **Veille normative** : **standards applicables** | Suivi des versions ISO/IEC 27001, 27002, 27005, 27701, 27017, 27018, 27035, 42001 et ISO 22301 (ISO Open Data, détection des changements) ; NIST CSF et publications NIST ; OpenSSF ; distinction norme / référentiel / recommandation / exigence contractuelle / obligation légale | Page *Réglementation et normes* (onglet Normes) ; rapport §10 ; table `normes` |
| C5 | **À l'aide d'outils adaptés** | Application dédiée : collecte RSS/API automatisée, base SQLite, classification et priorisation, interface web, rapports PDF/MD, planification ; Feedly en complément (API ou OPML) ; IA facultative | Rapport §4 (justification des outils) ; README ; `docs/FEEDLY.md` ; tests (`python -m pytest`) |
| C6 | **Sources fiables et justifiées** | Catalogue avec justification, nature, niveau de confiance, fréquence, état de fonctionnement et alternatives ; aucun contournement d'accès ; signalement « à recouper » pour les sources secondaires | [SOURCES_ET_JUSTIFICATION.md](SOURCES_ET_JUSTIFICATION.md) ; page *Sources et méthodologie* ; rapport §5 |
| C7 | **Surveiller** (caractère continu et traçable) | Fréquence par source, planification (intégrée, systemd, cron, Docker), historique des exécutions et des vérifications de sources, dates de publication et de collecte distinctes | Page *Automatisation et journaux* ; tables `executions`, `verifications_sources` ; tableau de bord (évolution du volume) ; rapport §3 |
| C8 | **Analyser les impacts sur l'organisation** | Profil de l'organisation (secteur, taille, rôles, données, inventaire avec exposition et criticité) ; pertinence ; technologies du parc concernées ; impacts C/I/D/conformité ; score explicable | Page *Configuration* ; fiche d'analyse (onglets Analyse, Priorisation) ; rapport §11 ; [METHODOLOGIE_VEILLE.md](METHODOLOGIE_VEILLE.md) §6 |
| C9 | **Identifier les obligations** | Orientation d'applicabilité justifiée par texte (probable, indirect, à qualifier, peu probable, non évaluable), obligations possibles, échéances futures et sources officielles ; jamais présentée comme une conclusion juridique | Rapport §9 et §12 ; page *Réglementation et normes* |
| C10 | **Identifier les opportunités d'amélioration** | Actions de type « étude d'opportunité », bonnes pratiques, grille technologique | Rapport §13 ; page *Technologies et innovations* (opportunités) |
| C11 | **Amélioration de la sécurité du SI** (plan d'action) | Plan d'action : constat, risque, action, justification, priorité, responsable, échéance, effort, bénéfice, preuves, statut ; réponses proportionnées (vérification, mise à jour, mesure compensatoire, contrôle de configuration, conformité, sensibilisation, étude) | Page *Plan d'action* (édition, export CSV) ; rapport §14 |
| C12 | **Rigueur** : faits, hypothèses, analyses et recommandations distingués | Étiquettes [Fait], [Donnée vérifiée], [Analyse], [Hypothèse], [Recommandation], [À vérifier] ; aucun CVSS, aucune exploitation ni aucune obligation inventés ; section « Aucune donnée » plutôt que des résultats fabriqués ; limites listées | Rapport (toutes sections) et §15 ; tests `test_aucun_cvss_invente`, `test_rapport_vide_ne_fabrique_rien`, `test_recommandation_jamais_obligation` |
| C13 | **Restitution exploitable** | Rapport périodique de 18 sections (PDF et Markdown), prévisualisation, choix de la période et du périmètre, tableau de bord, annexes avec URL et dates de consultation | Page *Rapports* ; dossier `exemples/` |

## 2. Preuves à présenter au jury

1. **Le rapport de veille** (`exemples/` ou un rapport régénéré pendant la démonstration) : preuve principale qui
   couvre l'ensemble des critères.
2. **Le catalogue des sources** et sa justification (page *Sources*, `SOURCES_ET_JUSTIFICATION.md`) : C5, C6.
3. **Une fiche d'analyse** prise de bout en bout, par exemple la vulnérabilité PHP « PHP2Shell » présente au KEV.
   Elle relie une information collectée (C1) à son impact sur un actif exposé du parc (C8), à une priorité justifiée
   et à une action avec preuves attendues (C11).
4. **La matrice d'applicabilité** (page *Réglementation et normes*) : C3, C9.
5. **Le suivi des versions ISO** (onglet Normes) : C4.
6. **Le plan d'action** filtré et exporté : C11.
7. **L'historique des exécutions** et l'état des sources : C7.
8. **La méthodologie** ([METHODOLOGIE_VEILLE.md](METHODOLOGIE_VEILLE.md)) et les **limites** ([LIMITES_ET_AMELIORATIONS.md](LIMITES_ET_AMELIORATIONS.md)) : démarche réflexive.

## 3. Points d'attention pour la soutenance

- Le profil fourni est **fictif** (démonstration). Pour le dossier de titre, renseignez l'organisation réelle ou
  étudiée, réanalysez (*Configuration* › Réanalyser), puis régénérez le rapport.
- Les orientations d'applicabilité doivent être présentées comme des **hypothèses de travail à confirmer** avec le
  juriste ou le DPO, ce que l'outil affiche lui-même.
- La qualité de l'analyse d'impact dépend de l'**inventaire** : montrer comment un mot-clé trop large (« Exchange »)
  génère des faux positifs et comment il a été corrigé illustre une démarche critique.
