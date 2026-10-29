-- Schéma de la base de veille (SQLite). Documentation : docs/SCHEMA_BDD.md
PRAGMA foreign_keys = ON;

-- Catalogue des sources (initialisé depuis config/sources.yaml, modifiable depuis l'interface)
CREATE TABLE IF NOT EXISTS sources (
    id                  TEXT PRIMARY KEY,
    nom                 TEXT NOT NULL,
    url                 TEXT NOT NULL,
    type                TEXT NOT NULL CHECK (type IN ('rss','cisa_kev','iso_opendata','feedly','manuel')),
    categorie           TEXT NOT NULL CHECK (categorie IN ('technique','reglementaire','normative','technologique')),
    sous_categorie      TEXT,
    organisme           TEXT,
    nature              TEXT,
    confiance           TEXT NOT NULL DEFAULT 'moyenne' CHECK (confiance IN ('elevee','moyenne','faible')),
    langue              TEXT DEFAULT 'en',
    frequence_minutes   INTEGER NOT NULL DEFAULT 1440,
    justification       TEXT,
    alternative         TEXT,
    filtre_mots_cles    TEXT,               -- JSON (liste)
    technologies        TEXT,               -- JSON (liste)
    options             TEXT,               -- JSON (max_items, max_octets, references_surveillees...)
    actif               INTEGER NOT NULL DEFAULT 1,
    statut              TEXT NOT NULL DEFAULT 'non_verifie',  -- non_verifie | ok | erreur | bloque | desactive
    derniere_verification TEXT,
    dernier_succes      TEXT,
    derniere_erreur     TEXT,
    echecs_consecutifs  INTEGER NOT NULL DEFAULT 0,
    etag                TEXT,
    last_modified       TEXT,
    cree_le             TEXT NOT NULL,
    modifie_le          TEXT NOT NULL
);

-- Articles collectés : la date de publication (source) et la date de collecte sont distinctes
CREATE TABLE IF NOT EXISTS articles (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    source_id       TEXT NOT NULL REFERENCES sources(id) ON UPDATE CASCADE,
    url             TEXT NOT NULL,
    url_canonique   TEXT NOT NULL UNIQUE,
    empreinte       TEXT NOT NULL,
    titre           TEXT NOT NULL,
    auteur          TEXT,
    resume_source   TEXT,
    langue          TEXT,
    publie_le       TEXT,                    -- date fournie par la source (peut être absente)
    collecte_le     TEXT NOT NULL,           -- date de collecte = date de consultation
    origine         TEXT,                    -- précision d'origine (ex. flux Feedly d'origine)
    donnees         TEXT,                    -- JSON : données structurées propres au connecteur (KEV, ISO)
    statut          TEXT NOT NULL DEFAULT 'nouveau'
                    CHECK (statut IN ('nouveau','lu','pertinent','non_pertinent','a_investiguer','traite')),
    notes           TEXT
);
CREATE INDEX IF NOT EXISTS idx_articles_empreinte ON articles(empreinte);
CREATE INDEX IF NOT EXISTS idx_articles_publie ON articles(publie_le);
CREATE INDEX IF NOT EXISTS idx_articles_collecte ON articles(collecte_le);
CREATE INDEX IF NOT EXISTS idx_articles_source ON articles(source_id);

-- Historique des changements de statut (traçabilité du traitement)
CREATE TABLE IF NOT EXISTS historique_statuts (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id  INTEGER NOT NULL REFERENCES articles(id) ON DELETE CASCADE,
    ancien      TEXT,
    nouveau     TEXT NOT NULL,
    modifie_le  TEXT NOT NULL
);

-- Fiche d'analyse structurée (une par article, recalculable)
CREATE TABLE IF NOT EXISTS analyses (
    article_id          INTEGER PRIMARY KEY REFERENCES articles(id) ON DELETE CASCADE,
    categories          TEXT NOT NULL,       -- JSON liste
    categorie_principale TEXT NOT NULL,
    mots_cles           TEXT,                -- JSON liste
    technologies        TEXT,                -- JSON liste des technologies du parc concernées
    produits_cites      TEXT,                -- JSON liste
    themes              TEXT,                -- JSON liste des thèmes technologiques détectés
    cves                TEXT,                -- JSON liste
    impacts             TEXT,                -- JSON liste : confidentialite, integrite, disponibilite, conformite
    pertinence          TEXT NOT NULL,       -- forte | moyenne | faible | a_qualifier | non_pertinent
    pertinence_motifs   TEXT,                -- JSON liste
    priorite            TEXT NOT NULL,       -- Critique | Élevée | Modérée | Faible | À qualifier
    score               INTEGER NOT NULL,
    facteurs            TEXT,                -- JSON liste {facteur, points, justification, verifie}
    actions             TEXT,                -- JSON liste
    echeance            TEXT,
    urgence             TEXT,
    confiance           TEXT NOT NULL,       -- elevee | moyenne | faible
    a_verifier          TEXT,                -- JSON liste
    resume_fr           TEXT,
    methode_resume      TEXT,                -- extrait_source | synthese_regles | ia:<modele>
    reglementaire       TEXT,                -- JSON (fiche réglementaire) ou NULL
    normatif            TEXT,                -- JSON (fiche normative) ou NULL
    version_analyse     TEXT NOT NULL,
    analyse_le          TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_analyses_priorite ON analyses(priorite);

-- Enrichissement des CVE à partir de sources vérifiables (NVD, CISA KEV, FIRST EPSS)
CREATE TABLE IF NOT EXISTS cve (
    cve_id          TEXT PRIMARY KEY,
    cvss_score      REAL,
    cvss_version    TEXT,
    cvss_vecteur    TEXT,
    severite        TEXT,
    cvss_source     TEXT,
    description     TEXT,
    nvd_statut      TEXT,                    -- ok | introuvable | erreur | non_interroge
    nvd_le          TEXT,
    epss            REAL,
    epss_percentile REAL,
    epss_le         TEXT
);

CREATE TABLE IF NOT EXISTS kev (
    cve_id          TEXT PRIMARY KEY,
    fournisseur     TEXT,
    produit         TEXT,
    nom             TEXT,
    ajoute_le       TEXT,
    echeance_cisa   TEXT,
    rancongiciel    TEXT,
    action_requise  TEXT,
    description     TEXT,
    maj_le          TEXT NOT NULL
);

-- Suivi des versions des normes ISO surveillées (métadonnées publiques ISO Open Data)
CREATE TABLE IF NOT EXISTS normes (
    reference           TEXT PRIMARY KEY,
    titre               TEXT,
    edition             INTEGER,
    stade               TEXT,
    date_publication    TEXT,
    remplace            TEXT,
    remplacee_par       TEXT,
    comite              TEXT,
    iso_id              INTEGER,
    maj_le              TEXT NOT NULL
);

-- Plan d'action
CREATE TABLE IF NOT EXISTS actions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id      INTEGER REFERENCES articles(id) ON DELETE SET NULL,
    cle             TEXT UNIQUE,              -- clé de dédoublonnage des actions automatiques
    origine         TEXT NOT NULL DEFAULT 'auto' CHECK (origine IN ('auto','manuel')),
    constat         TEXT NOT NULL,
    risque          TEXT,
    action          TEXT NOT NULL,
    justification   TEXT,
    priorite        TEXT NOT NULL,
    responsable     TEXT,
    echeance        TEXT,
    effort          TEXT CHECK (effort IN ('faible','moyen','eleve')),
    benefice        TEXT,
    preuves         TEXT,
    statut          TEXT NOT NULL DEFAULT 'a_etudier'
                    CHECK (statut IN ('a_etudier','a_valider','planifiee','en_cours','terminee','abandonnee')),
    commentaire     TEXT,
    cree_le         TEXT NOT NULL,
    modifie_le      TEXT NOT NULL
);

-- Exécutions de collecte et détail par source (historique démontrable)
CREATE TABLE IF NOT EXISTS executions (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    type            TEXT NOT NULL,           -- collecte | analyse | enrichissement | rapport | verification
    declencheur     TEXT NOT NULL,           -- manuel | planifie | cli
    debut           TEXT NOT NULL,
    fin             TEXT,
    statut          TEXT NOT NULL DEFAULT 'en_cours',  -- en_cours | succes | partiel | echec
    sources_ok      INTEGER DEFAULT 0,
    sources_erreur  INTEGER DEFAULT 0,
    nouveaux        INTEGER DEFAULT 0,
    doublons        INTEGER DEFAULT 0,
    message         TEXT
);

CREATE TABLE IF NOT EXISTS verifications_sources (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    execution_id    INTEGER REFERENCES executions(id) ON DELETE CASCADE,
    source_id       TEXT NOT NULL,
    verifie_le      TEXT NOT NULL,
    statut          TEXT NOT NULL,           -- ok | non_modifie | erreur | bloque
    code_http       INTEGER,
    elements        INTEGER DEFAULT 0,
    nouveaux        INTEGER DEFAULT 0,
    doublons        INTEGER DEFAULT 0,
    filtres         INTEGER DEFAULT 0,
    duree_ms        INTEGER,
    erreur          TEXT
);
CREATE INDEX IF NOT EXISTS idx_verif_source ON verifications_sources(source_id, verifie_le);

CREATE TABLE IF NOT EXISTS rapports (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    genere_le       TEXT NOT NULL,
    periode_debut   TEXT NOT NULL,
    periode_fin     TEXT NOT NULL,
    perimetre       TEXT,                    -- JSON
    chemin_md       TEXT,
    chemin_pdf      TEXT,
    declencheur     TEXT NOT NULL,
    nb_articles     INTEGER
);

-- Paramètres modifiés depuis l'interface et verrous applicatifs
CREATE TABLE IF NOT EXISTS settings (
    cle     TEXT PRIMARY KEY,
    valeur  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS verrous (
    nom         TEXT PRIMARY KEY,
    detenteur   TEXT NOT NULL,
    expire_le   REAL NOT NULL
);
