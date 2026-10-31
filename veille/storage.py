"""Stockage SQLite : toutes les requêtes sont paramétrées (aucune concaténation de valeurs utilisateur)."""
from __future__ import annotations

import json
import sqlite3
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Iterator

from veille.config import db_path
from veille.normalize import iso, utcnow

SCHEMA_FILE = Path(__file__).with_name("schema.sql")

JSON_COLUMNS = {
    "filtre_mots_cles", "technologies", "options", "donnees", "categories", "mots_cles", "produits_cites",
    "cves", "impacts", "pertinence_motifs", "facteurs", "actions", "a_verifier", "reglementaire", "normatif",
    "perimetre", "themes", "scenarios",
}

ARTICLE_STATUSES = ["nouveau", "lu", "pertinent", "non_pertinent", "a_investiguer", "traite"]
ACTION_STATUSES = ["a_etudier", "a_valider", "planifiee", "en_cours", "terminee", "abandonnee"]


def _dumps(v: Any) -> str | None:
    return None if v is None else json.dumps(v, ensure_ascii=False)


def _row(r: sqlite3.Row | None) -> dict | None:
    if r is None:
        return None
    d = dict(r)
    for k, v in d.items():
        if k in JSON_COLUMNS and isinstance(v, str):
            try:
                d[k] = json.loads(v)
            except ValueError:
                pass
    return d


class Storage:
    def __init__(self, path: Path | str | None = None) -> None:
        self.path = Path(path) if path else db_path()
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def conn(self) -> Iterator[sqlite3.Connection]:
        c = sqlite3.connect(self.path, timeout=30)
        c.row_factory = sqlite3.Row
        c.execute("PRAGMA foreign_keys = ON")
        c.execute("PRAGMA busy_timeout = 30000")
        try:
            yield c
            c.commit()
        except Exception:
            c.rollback()  # aucune donnée partiellement écrite en cas d'erreur
            raise
        finally:
            c.close()

    # Colonnes ajoutées après la première version : ajoutées aux bases existantes sans perte de données
    MIGRATIONS = [("analyses", "scenarios", "TEXT"), ("actions", "cout_estime", "TEXT")]

    def init_db(self) -> None:
        with self.conn() as c:
            c.execute("PRAGMA journal_mode = WAL")  # lectures concurrentes interface / planificateur
            c.executescript(SCHEMA_FILE.read_text(encoding="utf-8"))
            for table, col, typ in self.MIGRATIONS:
                cols = {r["name"] for r in c.execute(f"PRAGMA table_info({table})")}
                if col not in cols:
                    c.execute(f"ALTER TABLE {table} ADD COLUMN {col} {typ}")

    def query(self, sql: str, params: Iterable = ()) -> list[dict]:
        with self.conn() as c:
            return [_row(r) for r in c.execute(sql, tuple(params)).fetchall()]

    def scalar(self, sql: str, params: Iterable = ()):
        with self.conn() as c:
            r = c.execute(sql, tuple(params)).fetchone()
            return r[0] if r else None

    # ------------------------------------------------------------------ sources
    SOURCE_FIELDS = ["nom", "url", "type", "categorie", "sous_categorie", "organisme", "nature", "confiance",
                     "langue", "frequence_minutes", "justification", "alternative", "filtre_mots_cles",
                     "technologies", "options", "actif"]

    def upsert_source(self, src: dict, overwrite: bool = False) -> bool:
        """Insère une source ; si elle existe, ne la modifie que si overwrite=True. Renvoie True si insérée."""
        now = iso(utcnow())
        with self.conn() as c:
            exists = c.execute("SELECT 1 FROM sources WHERE id = ?", (src["id"],)).fetchone()
            values = {k: src.get(k) for k in self.SOURCE_FIELDS}
            for k in ("filtre_mots_cles", "technologies", "options"):
                values[k] = _dumps(values[k])
            values["actif"] = 1 if values.get("actif") else 0
            if exists:
                if overwrite:
                    sets = ", ".join(f"{k} = ?" for k in values)
                    c.execute(f"UPDATE sources SET {sets}, modifie_le = ? WHERE id = ?",
                              (*values.values(), now, src["id"]))
                    # cohérence du statut avec l'activation
                    c.execute("""UPDATE sources SET statut = CASE
                                     WHEN actif = 0 AND type != 'manuel' THEN 'desactive'
                                     WHEN actif = 1 AND statut = 'desactive' THEN 'non_verifie'
                                     ELSE statut END WHERE id = ?""", (src["id"],))
                return False
            statut = src.get("statut") or ("non_verifie" if values["actif"] else "desactive")
            cols = ["id", *values.keys(), "statut", "cree_le", "modifie_le"]
            c.execute(f"INSERT INTO sources ({', '.join(cols)}) VALUES ({', '.join('?' * len(cols))})",
                      (src["id"], *values.values(), statut, now, now))
            return True

    def list_sources(self, active_only: bool = False) -> list[dict]:
        sql = "SELECT * FROM sources" + (" WHERE actif = 1" if active_only else "") + " ORDER BY categorie, nom"
        return self.query(sql)

    def get_source(self, source_id: str) -> dict | None:
        rows = self.query("SELECT * FROM sources WHERE id = ?", (source_id,))
        return rows[0] if rows else None

    def update_source(self, source_id: str, fields: dict) -> None:
        allowed = set(self.SOURCE_FIELDS) | {"statut", "derniere_verification", "dernier_succes", "derniere_erreur",
                                             "echecs_consecutifs", "etag", "last_modified"}
        fields = {k: v for k, v in fields.items() if k in allowed}
        if not fields:
            return
        for k in ("filtre_mots_cles", "technologies", "options"):
            if k in fields:
                fields[k] = _dumps(fields[k])
        if "actif" in fields:
            fields["actif"] = 1 if fields["actif"] else 0
        sets = ", ".join(f"{k} = ?" for k in fields)  # noms de colonnes issus de la liste blanche ci-dessus
        with self.conn() as c:
            c.execute(f"UPDATE sources SET {sets}, modifie_le = ? WHERE id = ?",
                      (*fields.values(), iso(utcnow()), source_id))

    def delete_source(self, source_id: str) -> str:
        """Supprime une source sans article ; sinon la désactive pour conserver la traçabilité."""
        with self.conn() as c:
            n = c.execute("SELECT COUNT(*) FROM articles WHERE source_id = ?", (source_id,)).fetchone()[0]
            if n:
                c.execute("UPDATE sources SET actif = 0, statut = 'desactive', modifie_le = ? WHERE id = ?",
                          (iso(utcnow()), source_id))
                return "desactivee"
            c.execute("DELETE FROM sources WHERE id = ?", (source_id,))
            return "supprimee"

    # ------------------------------------------------------------------ articles
    def insert_article(self, art: dict) -> tuple[int | None, str]:
        """Insère un article. Renvoie (id, 'nouveau') ou (None, 'doublon_url'|'doublon_contenu')."""
        with self.conn() as c:
            if c.execute("SELECT 1 FROM articles WHERE url_canonique = ?", (art["url_canonique"],)).fetchone():
                return None, "doublon_url"
            if c.execute("SELECT 1 FROM articles WHERE empreinte = ?", (art["empreinte"],)).fetchone():
                return None, "doublon_contenu"
            cur = c.execute(
                """INSERT INTO articles (source_id, url, url_canonique, empreinte, titre, auteur, resume_source,
                       langue, publie_le, collecte_le, origine, donnees)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (art["source_id"], art["url"], art["url_canonique"], art["empreinte"], art["titre"],
                 art.get("auteur"), art.get("resume_source"), art.get("langue"), art.get("publie_le"),
                 art["collecte_le"], art.get("origine"), _dumps(art.get("donnees"))))
            return cur.lastrowid, "nouveau"

    def get_article(self, article_id: int) -> dict | None:
        rows = self.query(
            """SELECT a.*, s.nom AS source_nom, s.categorie AS source_categorie, s.confiance AS source_confiance,
                      s.nature AS source_nature, s.type AS source_type, s.technologies AS source_technologies,
                      s.sous_categorie AS sous_categorie
               FROM articles a JOIN sources s ON s.id = a.source_id WHERE a.id = ?""", (article_id,))
        return rows[0] if rows else None

    def get_article_full(self, article_id: int) -> dict | None:
        rows = self.query(
            """SELECT a.*, s.nom AS source_nom, s.categorie AS source_categorie, s.confiance AS source_confiance, n.*
               FROM articles a JOIN sources s ON s.id = a.source_id LEFT JOIN analyses n ON n.article_id = a.id
               WHERE a.id = ?""", (article_id,))
        if not rows:
            return None
        r = rows[0]
        r["id"] = article_id  # n.article_id ne doit pas masquer l'identifiant
        return r

    def articles_to_analyze(self, limit: int = 5000, all_articles: bool = False) -> list[int]:
        sql = "SELECT a.id FROM articles a LEFT JOIN analyses n ON n.article_id = a.id"
        if not all_articles:
            sql += " WHERE n.article_id IS NULL"
        sql += " ORDER BY a.id LIMIT ?"
        return [r["id"] for r in self.query(sql, (limit,))]

    def set_article_status(self, article_id: int, statut: str, notes: str | None = None) -> None:
        if statut not in ARTICLE_STATUSES:
            raise ValueError(f"Statut invalide : {statut}")
        with self.conn() as c:
            old = c.execute("SELECT statut FROM articles WHERE id = ?", (article_id,)).fetchone()
            if not old:
                raise KeyError(article_id)
            if notes is not None:
                c.execute("UPDATE articles SET statut = ?, notes = ? WHERE id = ?", (statut, notes[:5000], article_id))
            else:
                c.execute("UPDATE articles SET statut = ? WHERE id = ?", (statut, article_id))
            if old["statut"] != statut:
                c.execute("INSERT INTO historique_statuts (article_id, ancien, nouveau, modifie_le) VALUES (?, ?, ?, ?)",
                          (article_id, old["statut"], statut, iso(utcnow())))

    def list_articles(self, date_from: str | None = None, date_to: str | None = None,
                      source_ids: list[str] | None = None, categories: list[str] | None = None,
                      priorities: list[str] | None = None, statuses: list[str] | None = None,
                      search: str | None = None, technology: str | None = None,
                      date_field: str = "collecte_le", limit: int = 2000) -> list[dict]:
        """Liste les articles avec leur analyse. date_field ∈ {collecte_le, publie_le}."""
        if date_field not in ("collecte_le", "publie_le"):
            raise ValueError("date_field invalide")
        where, params = [], []
        date_expr = f"COALESCE(a.{date_field}, a.collecte_le)"
        if date_from:
            where.append(f"{date_expr} >= ?")
            params.append(date_from)
        if date_to:
            where.append(f"{date_expr} <= ?")
            params.append(date_to)
        if source_ids:
            where.append(f"a.source_id IN ({','.join('?' * len(source_ids))})")
            params += source_ids
        if priorities:
            where.append(f"n.priorite IN ({','.join('?' * len(priorities))})")
            params += priorities
        if statuses:
            where.append(f"a.statut IN ({','.join('?' * len(statuses))})")
            params += statuses
        if categories:
            where.append("(" + " OR ".join("n.categories LIKE ?" for _ in categories) + ")")
            params += [f'%"{c}"%' for c in categories]
        if search:
            where.append("(a.titre LIKE ? OR a.resume_source LIKE ? OR n.resume_fr LIKE ? OR n.mots_cles LIKE ? OR n.cves LIKE ?)")
            params += [f"%{search}%"] * 5
        if technology:
            where.append("(n.technologies LIKE ? OR n.produits_cites LIKE ?)")
            params += [f"%{technology}%"] * 2
        sql = f"""SELECT a.*, s.nom AS source_nom, s.categorie AS source_categorie, s.confiance AS source_confiance,
                         n.categories, n.categorie_principale, n.mots_cles, n.technologies, n.produits_cites, n.themes, n.scenarios, n.cves,
                         n.impacts, n.pertinence, n.pertinence_motifs, n.priorite, n.score, n.facteurs, n.actions,
                         n.echeance, n.urgence, n.confiance, n.a_verifier, n.resume_fr, n.methode_resume,
                         n.reglementaire, n.normatif
                  FROM articles a JOIN sources s ON s.id = a.source_id
                  LEFT JOIN analyses n ON n.article_id = a.id
                  {'WHERE ' + ' AND '.join(where) if where else ''}
                  ORDER BY {date_expr} DESC, a.id DESC LIMIT ?"""
        params.append(limit)
        return self.query(sql, params)

    # ------------------------------------------------------------------ analyses
    def save_analysis(self, article_id: int, a: dict) -> None:
        cols = ["categories", "categorie_principale", "mots_cles", "technologies", "produits_cites", "themes", "scenarios", "cves",
                "impacts", "pertinence", "pertinence_motifs", "priorite", "score", "facteurs", "actions",
                "echeance", "urgence", "confiance", "a_verifier", "resume_fr", "methode_resume",
                "reglementaire", "normatif", "version_analyse", "analyse_le"]
        vals = [_dumps(a.get(k)) if k in JSON_COLUMNS else a.get(k) for k in cols]
        with self.conn() as c:
            c.execute(f"""INSERT INTO analyses (article_id, {', '.join(cols)}) VALUES (?, {', '.join('?' * len(cols))})
                          ON CONFLICT(article_id) DO UPDATE SET {', '.join(f'{k} = excluded.{k}' for k in cols)}""",
                      (article_id, *vals))

    def update_summary(self, article_id: int, resume_fr: str, methode: str) -> None:
        with self.conn() as c:
            c.execute("UPDATE analyses SET resume_fr = ?, methode_resume = ? WHERE article_id = ?",
                      (resume_fr, methode, article_id))

    # ------------------------------------------------------------------ CVE / KEV / normes
    def upsert_kev(self, rows: list[dict]) -> None:
        now = iso(utcnow())
        with self.conn() as c:
            c.executemany(
                """INSERT INTO kev (cve_id, fournisseur, produit, nom, ajoute_le, echeance_cisa, rancongiciel,
                                    action_requise, description, maj_le)
                   VALUES (:cve_id, :fournisseur, :produit, :nom, :ajoute_le, :echeance_cisa, :rancongiciel,
                           :action_requise, :description, :maj_le)
                   ON CONFLICT(cve_id) DO UPDATE SET fournisseur = excluded.fournisseur, produit = excluded.produit,
                       nom = excluded.nom, ajoute_le = excluded.ajoute_le, echeance_cisa = excluded.echeance_cisa,
                       rancongiciel = excluded.rancongiciel, action_requise = excluded.action_requise,
                       description = excluded.description, maj_le = excluded.maj_le""",
                [{**r, "maj_le": now} for r in rows])

    def get_kev(self, cve_ids: list[str]) -> dict[str, dict]:
        if not cve_ids:
            return {}
        rows = self.query(f"SELECT * FROM kev WHERE cve_id IN ({','.join('?' * len(cve_ids))})", cve_ids)
        return {r["cve_id"]: r for r in rows}

    def kev_count(self) -> int:
        return self.scalar("SELECT COUNT(*) FROM kev") or 0

    def upsert_cve(self, cve_id: str, fields: dict) -> None:
        allowed = ["cvss_score", "cvss_version", "cvss_vecteur", "severite", "cvss_source", "description",
                   "nvd_statut", "nvd_le", "epss", "epss_percentile", "epss_le"]
        fields = {k: v for k, v in fields.items() if k in allowed}
        with self.conn() as c:
            c.execute("INSERT OR IGNORE INTO cve (cve_id, nvd_statut) VALUES (?, 'non_interroge')", (cve_id,))
            if fields:
                c.execute(f"UPDATE cve SET {', '.join(f'{k} = ?' for k in fields)} WHERE cve_id = ?",
                          (*fields.values(), cve_id))

    def get_cves(self, cve_ids: list[str]) -> dict[str, dict]:
        if not cve_ids:
            return {}
        rows = self.query(f"SELECT * FROM cve WHERE cve_id IN ({','.join('?' * len(cve_ids))})", cve_ids)
        return {r["cve_id"]: r for r in rows}

    def get_norme(self, reference: str) -> dict | None:
        rows = self.query("SELECT * FROM normes WHERE reference = ?", (reference,))
        return rows[0] if rows else None

    def upsert_norme(self, n: dict) -> None:
        with self.conn() as c:
            c.execute(
                """INSERT INTO normes (reference, titre, edition, stade, date_publication, remplace, remplacee_par,
                                       comite, iso_id, maj_le)
                   VALUES (:reference, :titre, :edition, :stade, :date_publication, :remplace, :remplacee_par,
                           :comite, :iso_id, :maj_le)
                   ON CONFLICT(reference) DO UPDATE SET titre = excluded.titre, edition = excluded.edition,
                       stade = excluded.stade, date_publication = excluded.date_publication,
                       remplace = excluded.remplace, remplacee_par = excluded.remplacee_par,
                       comite = excluded.comite, iso_id = excluded.iso_id, maj_le = excluded.maj_le""",
                {**n, "maj_le": iso(utcnow())})

    # ------------------------------------------------------------------ actions
    ACTION_FIELDS = ["constat", "risque", "action", "justification", "priorite", "responsable", "echeance",
                     "effort", "benefice", "preuves", "cout_estime", "statut", "commentaire"]

    def upsert_auto_action(self, cle: str, article_id: int | None, a: dict) -> bool:
        """Crée une action automatique si elle n'existe pas. Une action existante n'est jamais écrasée
        (l'utilisateur a pu la modifier). Renvoie True si créée."""
        now = iso(utcnow())
        with self.conn() as c:
            if c.execute("SELECT 1 FROM actions WHERE cle = ?", (cle,)).fetchone():
                # mise à jour silencieuse uniquement si personne n'a encore modifié l'action
                upd = {k: a.get(k) for k in ("constat", "risque", "action", "justification", "priorite", "responsable",
                                             "echeance", "effort", "benefice", "preuves")}
                c.execute(f"UPDATE actions SET {', '.join(f'{k} = ?' for k in upd)} "
                          "WHERE cle = ? AND origine = 'auto' AND modifie_le = cree_le", (*upd.values(), cle))
                return False
            vals = {k: a.get(k) for k in self.ACTION_FIELDS}
            vals["statut"] = vals["statut"] or "a_etudier"
            c.execute(f"""INSERT INTO actions (article_id, cle, origine, {', '.join(vals)}, cree_le, modifie_le)
                          VALUES (?, ?, 'auto', {', '.join('?' * len(vals))}, ?, ?)""",
                      (article_id, cle, *vals.values(), now, now))
            return True

    def add_manual_action(self, a: dict) -> int:
        now = iso(utcnow())
        vals = {k: a.get(k) for k in self.ACTION_FIELDS}
        vals["statut"] = vals["statut"] or "a_etudier"
        if not vals["constat"] or not vals["action"] or not vals["priorite"]:
            raise ValueError("Constat, action et priorité sont obligatoires")
        with self.conn() as c:
            cur = c.execute(f"""INSERT INTO actions (article_id, origine, {', '.join(vals)}, cree_le, modifie_le)
                                VALUES (?, 'manuel', {', '.join('?' * len(vals))}, ?, ?)""",
                            (a.get("article_id"), *vals.values(), now, now))
            return cur.lastrowid

    def update_action(self, action_id: int, fields: dict) -> None:
        fields = {k: v for k, v in fields.items() if k in self.ACTION_FIELDS}
        if "statut" in fields and fields["statut"] not in ACTION_STATUSES:
            raise ValueError("Statut d'action invalide")
        if not fields:
            return
        with self.conn() as c:
            c.execute(f"UPDATE actions SET {', '.join(f'{k} = ?' for k in fields)}, modifie_le = ? WHERE id = ?",
                      (*fields.values(), iso(utcnow()), action_id))

    def list_actions(self, statuses: list[str] | None = None, date_from: str | None = None,
                     date_to: str | None = None) -> list[dict]:
        where, params = [], []
        if statuses:
            where.append(f"x.statut IN ({','.join('?' * len(statuses))})")
            params += statuses
        if date_from:
            where.append("x.cree_le >= ?")
            params.append(date_from)
        if date_to:
            where.append("x.cree_le <= ?")
            params.append(date_to)
        return self.query(
            f"""SELECT x.*, a.titre AS article_titre, a.url AS article_url, s.nom AS source_nom
                FROM actions x LEFT JOIN articles a ON a.id = x.article_id LEFT JOIN sources s ON s.id = a.source_id
                {'WHERE ' + ' AND '.join(where) if where else ''}
                ORDER BY CASE x.priorite WHEN 'Critique' THEN 0 WHEN 'Élevée' THEN 1 WHEN 'À qualifier' THEN 2
                         WHEN 'Modérée' THEN 3 ELSE 4 END, x.echeance, x.id""", params)

    # ------------------------------------------------------------------ exécutions
    def start_execution(self, type_: str, trigger: str) -> int:
        with self.conn() as c:
            return c.execute("INSERT INTO executions (type, declencheur, debut) VALUES (?, ?, ?)",
                             (type_, trigger, iso(utcnow()))).lastrowid

    def finish_execution(self, exec_id: int, statut: str, **counts) -> None:
        allowed = {"sources_ok", "sources_erreur", "nouveaux", "doublons", "message"}
        counts = {k: v for k, v in counts.items() if k in allowed}
        sets = "".join(f", {k} = ?" for k in counts)
        with self.conn() as c:
            c.execute(f"UPDATE executions SET fin = ?, statut = ?{sets} WHERE id = ?",
                      (iso(utcnow()), statut, *counts.values(), exec_id))

    def add_check(self, exec_id: int | None, source_id: str, statut: str, **kw) -> None:
        with self.conn() as c:
            c.execute(
                """INSERT INTO verifications_sources (execution_id, source_id, verifie_le, statut, code_http, elements,
                                                      nouveaux, doublons, filtres, duree_ms, erreur)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (exec_id, source_id, iso(utcnow()), statut, kw.get("code_http"), kw.get("elements", 0),
                 kw.get("nouveaux", 0), kw.get("doublons", 0), kw.get("filtres", 0), kw.get("duree_ms"),
                 kw.get("erreur")))

    def list_executions(self, limit: int = 50) -> list[dict]:
        return self.query("SELECT * FROM executions ORDER BY id DESC LIMIT ?", (limit,))

    # ------------------------------------------------------------------ rapports
    def add_report(self, r: dict) -> int:
        with self.conn() as c:
            return c.execute(
                """INSERT INTO rapports (genere_le, periode_debut, periode_fin, perimetre, chemin_md, chemin_pdf,
                                         declencheur, nb_articles) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                (iso(utcnow()), r["periode_debut"], r["periode_fin"], _dumps(r.get("perimetre")), r.get("chemin_md"),
                 r.get("chemin_pdf"), r.get("declencheur", "manuel"), r.get("nb_articles"))).lastrowid

    def list_reports(self, limit: int = 50) -> list[dict]:
        return self.query("SELECT * FROM rapports ORDER BY id DESC LIMIT ?", (limit,))

    # ------------------------------------------------------------------ paramètres et verrous
    def get_setting(self, key: str, default: Any = None) -> Any:
        v = self.scalar("SELECT valeur FROM settings WHERE cle = ?", (key,))
        return default if v is None else json.loads(v)

    def set_setting(self, key: str, value: Any) -> None:
        with self.conn() as c:
            c.execute("INSERT INTO settings (cle, valeur) VALUES (?, ?) ON CONFLICT(cle) DO UPDATE SET valeur = excluded.valeur",
                      (key, json.dumps(value, ensure_ascii=False)))

    def acquire_lock(self, name: str, holder: str, ttl_seconds: int = 3600) -> bool:
        """Verrou applicatif inter-processus (interface et planificateur ne collectent pas en même temps)."""
        now = time.time()
        with self.conn() as c:
            c.execute("BEGIN IMMEDIATE")
            row = c.execute("SELECT detenteur, expire_le FROM verrous WHERE nom = ?", (name,)).fetchone()
            if row and row["expire_le"] > now and row["detenteur"] != holder:
                return False
            c.execute("INSERT INTO verrous (nom, detenteur, expire_le) VALUES (?, ?, ?) "
                      "ON CONFLICT(nom) DO UPDATE SET detenteur = excluded.detenteur, expire_le = excluded.expire_le",
                      (name, holder, now + ttl_seconds))
            return True

    def release_lock(self, name: str, holder: str) -> None:
        with self.conn() as c:
            c.execute("DELETE FROM verrous WHERE nom = ? AND detenteur = ?", (name, holder))
