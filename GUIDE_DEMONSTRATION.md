# Guide de démonstration devant le jury

Durée cible : **15 à 20 minutes**, puis questions. Le scénario suit le cycle de veille : contexte → sources →
collecte → analyse → décision → restitution.

## Préparation (la veille ou une heure avant)

```bash
cd Veille && source .venv/bin/activate
python -m veille init
python -m veille collect --all        # 5 à 8 minutes : à faire AVANT la démonstration
python -m pytest                      # vérifier que tous les tests passent
streamlit run app/streamlit_app.py    # http://localhost:8501
```

- Configurer le profil de l'organisation présentée, ou garder le profil de démonstration en l'annonçant comme fictif.
- Garder ouverts : l'application, le rapport PDF d'exemple (`exemples/`) et ce guide.
- **Plan de secours sans Internet** : la base déjà alimentée et le rapport d'exemple suffisent pour la démonstration ;
  seule la collecte en direct nécessite le réseau.

## Déroulé

| Temps | Page / action | Message clé | Critère |
|---|---|---|---|
| 0–2 min | Présentation orale | Le besoin : transformer un flux d'informations en décisions de sécurité adaptées à l'organisation. L'outil est une aide à la décision et n'agit pas sur le SI. | — |
| 2–4 min | **Configuration de l'organisation** | Le contexte d'abord : secteur, taille, rôles, données, inventaire avec exposition et criticité. Montrer les hypothèses affichées quand une information manque. | C8 |
| 4–6 min | **Sources et méthodologie** | 51 sources : primaires officielles (CERT-FR, CISA, CNIL, EUR-Lex, ISO, NIST), éditeurs du parc, presse « à recouper ». Montrer une justification, un niveau de confiance et les sources **bloquées** (Légifrance, ANSSI) avec leur alternative, sans contournement. | C5, C6 |
| 6–7 min | **Tableau de bord** → « Collecter les sources dues » | Collecte en direct (quelques secondes si peu de sources sont dues). Indicateurs, répartition, état des sources, dernière collecte. | C7 |
| 7–11 min | **Vulnérabilités et menaces** → sélectionner une ligne critique (ex. *PHP2Shell*, KEV) | Fiche complète : résumé, PHP exposé sur Internet dans le parc, KEV = exploitation **vérifiée**, EPSS, CVSS « non disponible » **non inventé**. Onglet *Priorisation* : chaque point justifié. Onglet *Recommandations* : vérification, correctif, mesure compensatoire, recherche de compromission. Passer le statut à « À investiguer ». | C1, C8, C12 |
| 11–13 min | **Réglementation et normes** | Matrice d'applicabilité : NIS 2 *probable — à confirmer* (secteur et taille), DORA *peu probable*. Montrer une évolution (ex. AI Act) et sa fiche réglementaire, puis l'onglet *Normes* (ISO 27001:2022, révision 27002 engagée). Insister : une norme ou une recommandation n'est pas une obligation légale. | C3, C4, C9 |
| 13–14 min | **Technologies et innovations** | Un thème (post-quantique ou IA générative) : usages, bénéfices, risques, prérequis ; opportunités. | C2, C10 |
| 14–16 min | **Plan d'action** | Modifier une action : responsable, échéance, statut « Planifiée ». Montrer les preuves attendues et exporter en CSV. | C11 |
| 16–19 min | **Rapports** → 7 derniers jours → Prévisualiser → Générer | Ouvrir le PDF : résumé exécutif avec les sujets regroupés (« confirmé par N sources »), étiquettes Fait / Analyse / Hypothèse / Recommandation, obligations et échéances, plan d'action, limites, annexes avec URL et dates de consultation. | C12, C13 |
| 19–20 min | **Automatisation et journaux** | Planification activable ; conditions d'exécution (service systemd/Docker pour une exécution hors interface) ; historique ; journaux sans secrets. | C7 |

## Questions probables et éléments de réponse

- **« Comment évitez-vous les faux positifs ? »** Des règles explicites et justifiées, des mots-clés de produit
  précis, une requalification manuelle par statut et une réanalyse. Exemple vécu : « Exchange » correspondait à
  « key exchange » ; le mot-clé a été remplacé par « Exchange Server » / « Exchange Online ».
- **« Pourquoi ne pas tout confier à une IA ? »** Le fonctionnement doit rester explicable, gratuit et
  reproductible. L'IA est facultative et limitée aux résumés. Les contenus collectés sont des données non fiables
  (risque d'injection de prompt), sans outils ni influence sur la priorité.
- **« Une source peut-elle mentir ou être compromise ? »** Le niveau de confiance est tracé, les sources secondaires
  sont signalées « à recouper » et l'exploitation n'est vérifiée que par le KEV. Le client réseau est sécurisé
  (liste blanche, anti-SSRF, taille bornée) et le contenu est échappé.
- **« L'organisation est-elle soumise à NIS 2 ? »** L'outil donne une orientation argumentée (secteur, taille),
  les démarches de qualification et le simulateur de l'ANSSI. La décision revient au juriste, et le statut de
  transposition française doit être vérifié sur Légifrance.
- **« Que se passe-t-il si l'application est fermée ? »** Le planificateur intégré s'arrête. Pour une veille
  continue, on utilise le service systemd, cron ou Docker Compose fournis.
- **« Comment intégrer Feedly ? »** Par l'API officielle avec un jeton si l'offre le permet, sinon par import OPML
  des abonnements. Aucun mot de passe n'est demandé (`docs/FEEDLY.md`).

## Points de vigilance

- Annoncer clairement que le profil de démonstration est **fictif** et que les données collectées sont **réelles**.
- Ne pas présenter une orientation d'applicabilité comme une obligation certaine.
- Sans clé NVD, les CVE très récentes peuvent ne pas avoir de CVSS : c'est un comportement voulu (aucune estimation).
