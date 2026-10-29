# Schéma de la base de données

Base **SQLite** (`data/veille.db`), en mode WAL pour les lectures concurrentes de l'interface et du planificateur.
La définition exécutable se trouve dans [veille/schema.sql](../veille/schema.sql). Les colonnes suffixées « JSON »
contiennent des listes ou objets sérialisés. Toutes les requêtes sont paramétrées.

```
sources 1───* articles 1───1 analyses
                 │  1───* historique_statuts
                 │  1───* actions (article_id facultatif : actions manuelles)
sources 1───* verifications_sources *───1 executions
cve (enrichissement NVD/EPSS) ── référencé par analyses.cves (JSON)
kev (catalogue CISA)          ── référencé par analyses.cves[].kev
normes (ISO Open Data)        ── état de référence pour la détection des changements
rapports, settings, verrous
```

| Table | Rôle | Colonnes principales |
|---|---|---|
| `sources` | Catalogue des sources | `id`, `nom`, `url`, `type` (rss, cisa_kev, iso_opendata, feedly, manuel), `categorie`, `nature`, `confiance`, `frequence_minutes`, `justification`, `alternative`, `filtre_mots_cles` (JSON), `technologies` (JSON), `options` (JSON), `actif`, `statut` (non_verifie, ok, erreur, bloque, desactive), `derniere_verification`, `dernier_succes`, `derniere_erreur`, `echecs_consecutifs`, `etag`, `last_modified` |
| `articles` | Éléments collectés | `id`, `source_id`, `url`, `url_canonique` (UNIQUE), `empreinte` (SHA-256), `titre`, `auteur`, `resume_source` (texte nettoyé), `langue`, `publie_le` (date de la source), `collecte_le` (date de consultation), `origine`, `donnees` (JSON : KEV, ISO), `statut` (nouveau, lu, pertinent, non_pertinent, a_investiguer, traite), `notes` |
| `historique_statuts` | Traçabilité du traitement | `article_id`, `ancien`, `nouveau`, `modifie_le` |
| `analyses` | Fiche d'analyse (recalculable) | `categories` (JSON), `categorie_principale`, `mots_cles`, `technologies`, `produits_cites`, `themes`, `cves` (JSON : id, cvss, source, epss, kev), `impacts`, `pertinence`, `pertinence_motifs`, `priorite`, `score`, `facteurs` (JSON : facteur, points, justification, verifie, source), `actions`, `echeance`, `urgence`, `confiance`, `a_verifier`, `resume_fr`, `methode_resume`, `reglementaire` (JSON), `normatif` (JSON), `version_analyse`, `analyse_le` |
| `cve` | Données de référence par CVE | `cve_id`, `cvss_score`, `cvss_version`, `cvss_vecteur`, `severite`, `cvss_source`, `nvd_statut` (ok, introuvable, erreur, non_interroge), `epss`, `epss_percentile` |
| `kev` | Catalogue CISA KEV complet | `cve_id`, `fournisseur`, `produit`, `nom`, `ajoute_le`, `echeance_cisa`, `rancongiciel`, `action_requise` |
| `normes` | Dernier état connu des normes surveillées | `reference`, `titre`, `edition`, `stade`, `date_publication`, `remplace`, `remplacee_par`, `iso_id` |
| `actions` | Plan d'action | `article_id`, `cle` (dédoublonnage des actions automatiques), `origine` (auto, manuel), `constat`, `risque`, `action`, `justification`, `priorite`, `responsable`, `echeance`, `effort`, `benefice`, `preuves`, `statut` (a_etudier, a_valider, planifiee, en_cours, terminee, abandonnee), `commentaire` |
| `executions` | Historique des exécutions | `type`, `declencheur` (manuel, planifie, cli), `debut`, `fin`, `statut` (succes, partiel, echec), `sources_ok`, `sources_erreur`, `nouveaux`, `doublons`, `message` |
| `verifications_sources` | Détail par source et par exécution | `source_id`, `verifie_le`, `statut`, `code_http`, `elements`, `nouveaux`, `doublons`, `filtres`, `duree_ms`, `erreur` |
| `rapports` | Rapports générés | `periode_debut`, `periode_fin`, `perimetre`, `chemin_md`, `chemin_pdf`, `declencheur`, `nb_articles` |
| `settings` | Paramètres modifiés dans l'interface | `cle`, `valeur` (JSON) |
| `verrous` | Verrou de collecte inter-processus | `nom`, `detenteur`, `expire_le` |

## Règles d'intégrité

- **Déduplication** : `articles.url_canonique` est UNIQUE ; une empreinte déjà présente est également refusée.
- Une source rattachée à des articles n'est pas supprimée mais **désactivée**, pour conserver la traçabilité.
- Les actions automatiques ne sont jamais écrasées. Elles ne sont retirées par une réanalyse que si personne ne les
  a modifiées (`modifie_le = cree_le`) et qu'elles sont encore au statut « à étudier » ou « à valider ».
- Chaque opération est une transaction : en cas d'erreur, rien n'est écrit partiellement.

## Conservation et données personnelles

Seules des informations publiques sont stockées. Le nom d'auteur publié est conservé et les adresses e-mail sont
supprimées. Aucune donnée personnelle des utilisateurs n'est collectée. Le profil de l'organisation est stocké
dans `config/organisation.yaml`, hors de la base et non versionné.
