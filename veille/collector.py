"""Orchestrateur de collecte : interroge les sources dues, gère les erreurs et conserve l'historique."""
from __future__ import annotations

import logging
import os
import socket
import time
from datetime import timedelta
from typing import Callable

from veille.collectors import CollectorError, NotConfigured
from veille.collectors.cisa_kev import parse_kev
from veille.collectors.feedly import collect_feedly
from veille.collectors.iso_opendata import build_items, parse_iso
from veille.collectors.rss import parse_feed
from veille.net import BlockedRequest, FetchError, SafeFetcher
from veille.normalize import canonical_url, content_hash, iso, parse_date, utcnow
from veille.organisation import get_settings
from veille.sources import allowed_domains
from veille.storage import Storage

log = logging.getLogger("veille.collector")
LOCK_NAME = "collecte"


def make_fetcher(storage: Storage, settings: dict | None = None, **overrides) -> SafeFetcher:
    settings = settings or get_settings(storage)
    c = settings.get("collecte", {})
    from veille.config import env
    nvd_delay = 0.7 if env("NVD_API_KEY") else 6.5  # limites publiées par le NVD : 50 ou 5 requêtes / 30 s
    kwargs = dict(
        allowed_domains=allowed_domains(storage, settings),
        user_agent=c.get("user_agent", "VeilleCyber/1.0"),
        timeout=float(c.get("timeout_secondes", 20)),
        max_bytes=int(c.get("max_octets", 20_000_000)),
        retries=int(c.get("tentatives", 3)),
        min_delay_same_host=float(c.get("delai_min_meme_hote_secondes", 1.0)),
        respect_robots=bool(c.get("respecter_robots_txt", True)),
        host_delays={"services.nvd.nist.gov": nvd_delay},
    )
    kwargs.update(overrides)
    return SafeFetcher(**kwargs)


def is_due(source: dict, now=None) -> bool:
    now = now or utcnow()
    last = parse_date(source.get("derniere_verification"))
    return last is None or now - last >= timedelta(minutes=int(source.get("frequence_minutes") or 1440))


def keyword_filter(items: list[dict], keywords: list[str]) -> tuple[list[dict], int]:
    if not keywords:
        return items, 0
    kws = [k.casefold() for k in keywords]
    kept = [i for i in items if any(k in f"{i['titre']} {i.get('resume_source') or ''}".casefold() for k in kws)]
    return kept, len(items) - len(kept)


def collect_source(storage: Storage, fetcher: SafeFetcher, src: dict, settings: dict) -> dict:
    """Collecte une source. Renvoie un compte rendu ; lève FetchError/BlockedRequest/CollectorError."""
    opts = src.get("options") or {}
    max_items = int(opts.get("max_items") or settings.get("collecte", {}).get("max_items_par_source", 60))
    result = {"code_http": None, "elements": 0, "nouveaux": 0, "doublons": 0, "filtres": 0, "non_modifie": False,
              "avertissements": [], "ids": []}
    etag, last_mod = src.get("etag"), src.get("last_modified")

    if src["type"] == "feedly":
        items = collect_feedly(fetcher, max_items=max_items)
        res = None
    else:
        if src["type"] == "cisa_kev" and storage.kev_count() == 0:
            etag = last_mod = None  # premier chargement : forcer le téléchargement complet
        if src["type"] == "iso_opendata":
            etag = last_mod = None
        res = fetcher.fetch(src["url"], etag=etag, last_modified=last_mod,
                            max_bytes=opts.get("max_octets"))
        result["code_http"] = res.status
        if res.not_modified:
            result["non_modifie"] = True
            return result
        if src["type"] == "rss":
            items, warns = parse_feed(res.content, src.get("langue"), max_items=max_items)
            result["avertissements"] += warns
        elif src["type"] == "cisa_kev":
            window = int(settings.get("collecte", {}).get("kev_fenetre_jours", 30))
            rows, items = parse_kev(res.content, window_days=window)
            storage.upsert_kev(rows)
        elif src["type"] == "iso_opendata":
            watched = opts.get("references_surveillees") or []
            found = parse_iso(res.content, watched)
            known = {n["reference"]: n for n in storage.query("SELECT * FROM normes")}
            items, rows = build_items(found, known)
            for r in rows:
                storage.upsert_norme(r)
        else:
            raise CollectorError(f"Type de source non collectable automatiquement : {src['type']}")

    items, filtered = keyword_filter(items, src.get("filtre_mots_cles") or [])
    result["filtres"] = filtered
    result["elements"] = len(items) + filtered
    now = iso(utcnow())
    for it in items:
        art = {
            "source_id": src["id"],
            "url": it["url"],
            "url_canonique": it.get("url_canonique") or canonical_url(it["url"]),
            "empreinte": content_hash(it["titre"], it.get("resume_source") or ""),
            "titre": it["titre"][:500],
            "auteur": (it.get("auteur") or None) and str(it["auteur"])[:200],
            "resume_source": it.get("resume_source"),
            "langue": it.get("langue") or src.get("langue"),
            "publie_le": it.get("publie_le"),
            "collecte_le": now,
            "origine": it.get("origine"),
            "donnees": it.get("donnees"),
        }
        art_id, status = storage.insert_article(art)
        if art_id:
            result["nouveaux"] += 1
            result["ids"].append(art_id)
        else:
            result["doublons"] += 1
    if res is not None:
        result["etag"] = res.headers.get("etag")
        result["last_modified"] = res.headers.get("last-modified")
    return result


def collect(storage: Storage, trigger: str = "manuel", source_ids: list[str] | None = None,
            only_due: bool = True, fetcher: SafeFetcher | None = None,
            progress: Callable[[str, int, int], None] | None = None) -> dict:
    settings = get_settings(storage)
    holder = f"{socket.gethostname()}:{os.getpid()}:{time.time()}"
    if not storage.acquire_lock(LOCK_NAME, holder, ttl_seconds=3600):
        return {"statut": "deja_en_cours", "message": "Une collecte est déjà en cours (autre processus)."}
    exec_id = storage.start_execution("collecte", trigger)
    summary = {"statut": "succes", "execution_id": exec_id, "sources_ok": 0, "sources_erreur": 0,
               "nouveaux": 0, "doublons": 0, "ids": [], "details": []}
    own_fetcher = fetcher is None
    fetcher = fetcher or make_fetcher(storage, settings)
    try:
        sources = [s for s in storage.list_sources(active_only=True) if s["type"] != "manuel"]
        if source_ids:
            sources = [s for s in sources if s["id"] in source_ids]
        if only_due:
            sources = [s for s in sources if is_due(s)]
        for i, src in enumerate(sources, 1):
            if progress:
                progress(src["nom"], i, len(sources))
            started = time.monotonic()
            now = iso(utcnow())
            try:
                r = collect_source(storage, fetcher, src, settings)
                dur = int((time.monotonic() - started) * 1000)
                fields = {"statut": "ok", "derniere_verification": now, "dernier_succes": now,
                          "echecs_consecutifs": 0, "derniere_erreur": "; ".join(r["avertissements"]) or None}
                if r.get("etag") is not None or r.get("last_modified") is not None:
                    fields["etag"], fields["last_modified"] = r.get("etag"), r.get("last_modified")
                storage.update_source(src["id"], fields)
                storage.add_check(exec_id, src["id"], "non_modifie" if r["non_modifie"] else "ok",
                                  code_http=r["code_http"], elements=r["elements"], nouveaux=r["nouveaux"],
                                  doublons=r["doublons"], filtres=r["filtres"], duree_ms=dur,
                                  erreur="; ".join(r["avertissements"]) or None)
                summary["sources_ok"] += 1
                summary["nouveaux"] += r["nouveaux"]
                summary["doublons"] += r["doublons"]
                summary["ids"] += r["ids"]
                summary["details"].append({"source": src["id"], "statut": "ok", **{k: r[k] for k in ("nouveaux", "doublons", "filtres")}})
                log.info("Source %s : %s nouveaux, %s doublons, %s filtrés", src["id"], r["nouveaux"], r["doublons"], r["filtres"])
            except (BlockedRequest, NotConfigured) as exc:
                statut = "bloque" if isinstance(exc, BlockedRequest) else "non_configure"
                storage.update_source(src["id"], {"statut": "bloque" if statut == "bloque" else "erreur",
                                                  "derniere_verification": now, "derniere_erreur": str(exc)[:500]})
                storage.add_check(exec_id, src["id"], "bloque", erreur=str(exc)[:500],
                                  duree_ms=int((time.monotonic() - started) * 1000))
                summary["sources_erreur"] += 1
                summary["details"].append({"source": src["id"], "statut": statut, "erreur": str(exc)})
                log.warning("Source %s non collectée : %s", src["id"], exc)
            except (FetchError, CollectorError, ValueError, OSError) as exc:
                storage.update_source(src["id"], {"statut": "erreur", "derniere_verification": now,
                                                  "derniere_erreur": str(exc)[:500],
                                                  "echecs_consecutifs": int(src.get("echecs_consecutifs") or 0) + 1})
                storage.add_check(exec_id, src["id"], "erreur", code_http=getattr(exc, "status", None),
                                  erreur=str(exc)[:500], duree_ms=int((time.monotonic() - started) * 1000))
                summary["sources_erreur"] += 1
                summary["details"].append({"source": src["id"], "statut": "erreur", "erreur": str(exc)})
                log.warning("Erreur sur la source %s : %s", src["id"], exc)
        if summary["sources_erreur"] and summary["sources_ok"]:
            summary["statut"] = "partiel"
        elif summary["sources_erreur"]:
            summary["statut"] = "echec"
        msg = f"{len(sources)} source(s) interrogée(s)" if sources else "Aucune source due"
        storage.finish_execution(exec_id, summary["statut"], sources_ok=summary["sources_ok"],
                                 sources_erreur=summary["sources_erreur"], nouveaux=summary["nouveaux"],
                                 doublons=summary["doublons"], message=msg)
    except Exception as exc:  # erreur inattendue : l'exécution est tracée, les données déjà écrites sont conservées
        log.exception("Collecte interrompue")
        storage.finish_execution(exec_id, "echec", message=f"Erreur inattendue : {type(exc).__name__}: {exc}"[:500])
        summary["statut"] = "echec"
        summary["message"] = str(exc)
    finally:
        storage.release_lock(LOCK_NAME, holder)
        if own_fetcher:
            fetcher.close()
    return summary
