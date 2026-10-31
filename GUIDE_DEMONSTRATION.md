# Guide de démonstration

Durée cible : **15 à 20 minutes**, puis questions. Le fil conducteur est le cas **AéroStar**, un bureau d'études
aéronautique fictif de 120 personnes. Ses clients exigent le niveau AirCyber Bronze fin 2027, son assureur exige le
MFA et des sauvegardes testées en 2027, et il a subi une compromission de messagerie en mars 2026. Le scénario suit
le cycle de veille : contexte → sources → collecte → analyse → décision → restitution.

## Préparation (la veille ou une heure avant)

```bash
cd Veille && source .venv/bin/activate
python -m veille init
python -m veille collect --all        # 5 à 8 minutes : à faire AVANT la présentation
python -m pytest                      # vérifier que tous les tests passent
streamlit run app/streamlit_app.py    # http://localhost:8501
```

- Ouvrir à l'avance : l'application, le rapport d'exemple (`exemples/EXEMPLE_rapport_veille_AeroStar_…pdf`) et ce guide.
- **Plan de secours sans Internet** : la base déjà alimentée et le rapport d'exemple suffisent ; seule la collecte en
  direct a besoin du réseau.

## Déroulé

| Temps | Page / action | Message clé |
|---|---|---|
| 0–2 min | Présentation orale | AéroStar dépend à 75 % de deux clients qui lui confient leurs plans : une fuite ou un arrêt la met en danger. Elle a trois échéances (AirCyber Bronze fin 2027, assurance 2027, programme de 18 mois) et ni RSSI ni supervision. La veille doit transformer un flux d'informations en décisions proportionnées à ces moyens. L'outil aide à décider et n'agit pas sur le SI. |
| 2–4 min | **Configuration de l'organisation** | Le contexte d'abord. Montrer : l'inventaire (gestionnaire « infogérant » du VPN, « marque inconnue » du pare-feu et du NAS, exclusion « Veeam Backup for Microsoft 365 »), les besoins DICT, les 3 scénarios redoutés, les échéances, les responsables (responsable IT référent, infogérant, direction). Puis les hypothèses affichées automatiquement. |
| 4–6 min | **Sources et méthodologie** | 57 sources, dont 49 actives. Primaires officielles (CERT-FR, CISA, CNIL, EUR-Lex, ISO, EASA), filière (BoostAeroSpace), Sénat pour la transposition de NIS 2, éditeurs, presse « à recouper ». Montrer une justification, puis les sources **désactivées** car hors contexte (EBA/DORA, AWS…) et **bloquées** (Légifrance, ANSSI, Dassault) avec leur alternative, sans aucun contournement. |
| 6–7 min | **Tableau de bord** → « Collecter les sources dues » | Collecte en direct. Échéances avec délai restant (AirCyber Bronze), alertes ouvertes, éléments liés aux scénarios redoutés, état des sources. |
| 7–11 min | **Vulnérabilités et menaces** → une faille de pare-feu / VPN SSL (ex. Cisco ASA) | Fiche complète. La marque du pare-feu d'AéroStar n'est pas documentée : présence « à confirmer », priorité plafonnée à « Élevée », première action « identifier le modèle auprès de l'infogérant », puis demande de correctif avec confirmation écrite. Scénario « rançongiciel via compte volé » rattaché. Onglet *Priorisation* : chaque point justifié, CVSS jamais estimé. Passer le statut à « À investiguer ». |
| 11–13 min | **Réglementation et normes** | Matrice : RGPD probable, AirCyber probable (exigence contractuelle), EN 9100 probable (norme), NIS 2 *à qualifier* (filière, transposition en discussion, suivie via le Sénat), Part-IS *indirect*, double usage *à vérifier projet par projet*, ISO 27001 *cible volontaire*. Onglet *Normes* : versions ISO suivies (ISO/IEC 27002:2022, révision engagée). Une norme n'est pas une obligation légale. |
| 13–14 min | **Technologies et innovations** | Thèmes choisis pour AéroStar : MFA résistante à l'hameçonnage (incident de mars, exigence de l'assureur), sauvegarde et restauration (assureur, scénario rançongiciel). Usages, bénéfices, risques, prérequis. |
| 14–16 min | **Plan d'action** | Les responsables sont ceux d'AéroStar. Renseigner un **coût estimé** (la direction exige que chaque mesure soit chiffrée et justifiée par un gain), une échéance et le statut « Planifiée ». Exporter en CSV. |
| 16–19 min | **Rapports** → 7 derniers jours → Prévisualiser → Générer | Le PDF contient : résumé exécutif avec les échéances et les sujets regroupés (« confirmé par N sources ») ; contexte d'AéroStar (contraintes, DICT, scénarios, parties prenantes) ; liens avec les scénarios et confrontation aux besoins ; engagements contractuels ; obligations ; plan d'action ; limites ; annexes avec URL et dates de consultation. |
| 19–20 min | **Automatisation et journaux** | Planification activable, conditions d'exécution (service systemd/Docker), historique des collectes, journaux sans secrets. |

## Questions probables et éléments de réponse

- **« Comment évitez-vous les faux positifs ? »** Par des règles explicites et justifiées, des mots-clés de produit
  précis, des exclusions et la requalification manuelle par statut. Deux exemples vécus : « Veeam Backup for
  Microsoft 365 » rattaché à tort à Microsoft 365, corrigé par une exclusion ; une virgule dans un nom du profil YAML
  qui tronquait les technologies, détectée à la relecture du PDF et désormais couverte par un test.
- **« Pourquoi aucune alerte critique cette semaine ? »** Le niveau « Critique » exige une technologie du parc
  identifiée **et** une gravité ou une exploitation vérifiée. Les failles de VPN SSL restent « Élevées » tant que la
  marque du pare-feu n'est pas confirmée par l'infogérant. Compléter l'inventaire est donc une action en soi.
- **« AéroStar est-elle soumise à NIS 2 ? »** C'est une orientation argumentée : un bureau d'études n'est a priori
  pas visé directement, mais ses clients le sont peut-être et répercutent leurs obligations. La loi de transposition
  est suivie via les flux du Sénat. La décision revient au juriste.
- **« Pourquoi ne pas tout confier à une IA ? »** Pour que le résultat reste explicable, gratuit et reproductible.
  L'IA est facultative et limitée aux résumés ; les contenus collectés sont traités comme des données non fiables.
- **« Que se passe-t-il si l'application est fermée ? »** Le planificateur intégré s'arrête. Pour une veille
  continue, on utilise le service systemd, cron ou Docker Compose fournis.
- **« Comment intégrer Feedly ? »** Par l'API officielle si l'offre le permet, sinon par import OPML. Aucun mot de
  passe n'est demandé (`docs/FEEDLY.md`).

## Points de vigilance

- Annoncer qu'AéroStar est **fictive**, mais que les données collectées sont **réelles**.
- Ne pas présenter une orientation d'applicabilité comme une obligation certaine.
- Les dates du référentiel réglementaire sont à revérifier sur la source officielle : l'outil le signale lui-même.
