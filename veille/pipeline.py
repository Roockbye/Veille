"""Chaîne complète : collecte → enrichissement CVE → analyse → plan d'action → (IA facultative) → notification."""
from __future__ import annotations

import logging
from typing import Callable

from veille.actions import sync_actions
from veille.analysis import analyze
from veille.collector import collect, make_fetcher
from veille.collectors.enrichment import enrich_cves, extract_cves
from veille.organisation import get_settings, has_profile, load_demo_profile, load_profile
from veille.storage import Storage

log = logging.getLogger("veille.pipeline")


def current_profile() -> dict:
    """Profil enregistré (config/organisation.yaml) si présent, sinon profil d'exemple AéroStar (organisation fictive)."""
    return load_profile() if has_profile() else load_demo_profile()


def analyze_articles(storage: Storage, ids: list[int] | None = None, profile: dict | None = None) -> int:
    profile = profile or current_profile()
    ids = ids if ids is not None else storage.articles_to_analyze()
    n = 0
    for aid in ids:
        art = storage.get_article(aid)
        if not art:
            continue
        text = f"{art['titre']}\n{art.get('resume_source') or ''}"
        cves = extract_cves(text)
        result = analyze(art, profile, storage.get_kev(cves), storage.get_cves(cves))
        prev = storage.query("SELECT methode_resume, resume_fr FROM analyses WHERE article_id = ?", (aid,))
        if prev and (prev[0]["methode_resume"] or "").startswith("ia:"):
            # conserve un résumé IA déjà produit lors d'une réanalyse
            result["resume_fr"], result["methode_resume"] = prev[0]["resume_fr"], prev[0]["methode_resume"]
        storage.save_analysis(aid, result)
        n += 1
    return n


def reanalyze_all(storage: Storage) -> int:
    n = analyze_articles(storage, storage.articles_to_analyze(all_articles=True, limit=100000))
    sync_actions(storage)
    return n


def enrich_for(storage: Storage, ids: list[int], settings: dict | None = None) -> dict:
    settings = settings or get_settings(storage)
    e = settings.get("enrichissement", {})
    cves: list[str] = []
    for aid in ids:
        art = storage.get_article(aid)
        if art:
            cves += extract_cves(f"{art['titre']}\n{art.get('resume_source') or ''}")
    if not cves:
        return {}
    # priorité aux CVE exploitées (KEV) puis aux plus récentes, la limite de débit du NVD étant faible
    kev = storage.get_kev(sorted(set(cves)))
    cves = sorted(set(cves), key=lambda c: (c not in kev, -int(c.split("-")[1]), -int(c.split("-")[2])))
    with make_fetcher(storage, settings) as fetcher:
        return enrich_cves(storage, fetcher, cves, max_nvd=int(e.get("max_cve_par_execution", 40)),
                           use_nvd=bool(e.get("nvd_actif", True)), use_epss=bool(e.get("epss_actif", True)))


def ai_summaries(storage: Storage, ids: list[int], limit: int = 20) -> int:
    from veille.ai import AIUnavailable, ai_configured, summarize
    if not ai_configured():
        return 0
    done = 0
    for aid in ids:
        if done >= limit:
            break
        art = storage.get_article(aid)
        row = storage.query("SELECT priorite, methode_resume FROM analyses WHERE article_id = ?", (aid,))
        if not art or not row or row[0]["methode_resume"] != "synthese_regles":
            continue
        if row[0]["priorite"] not in ("Critique", "Élevée", "Modérée", "À qualifier"):
            continue  # le coût de l'IA est réservé aux éléments utiles
        try:
            out = summarize(art)
        except (AIUnavailable, ValueError) as exc:
            log.warning("Résumé IA non produit pour l'article %s : %s", aid, exc)
            if isinstance(exc, AIUnavailable):
                break
            continue
        storage.update_summary(aid, out["resume_fr"] + " (Résumé généré par IA à partir de la source — à vérifier.)",
                               out["methode"])
        done += 1
    return done


def notify_critical(storage: Storage, ids: list[int], settings: dict) -> None:
    n = settings.get("notifications", {})
    if not n.get("email_actif") or not ids:
        return
    from veille.notify import send_email
    levels = n.get("alerte_niveaux") or ["Critique"]
    rows = storage.query(
        f"""SELECT a.titre, a.url, s.nom AS source, n.priorite, n.echeance FROM articles a
            JOIN analyses n ON n.article_id = a.id JOIN sources s ON s.id = a.source_id
            WHERE a.id IN ({','.join('?' * len(ids))}) AND n.priorite IN ({','.join('?' * len(levels))})""",
        [*ids, *levels])
    if rows:
        body = "Nouvelles alertes de veille :\n\n" + "\n".join(
            f"- [{r['priorite']}] {r['titre']} ({r['source']}) — échéance proposée {r['echeance']}\n  {r['url']}" for r in rows)
        send_email(f"[Veille] {len(rows)} alerte(s) {', '.join(levels)}", body)


def run_pipeline(storage: Storage, trigger: str = "manuel", only_due: bool = True,
                 source_ids: list[str] | None = None,
                 progress: Callable[[str, int, int], None] | None = None) -> dict:
    settings = get_settings(storage)
    summary = collect(storage, trigger=trigger, only_due=only_due, source_ids=source_ids, progress=progress)
    if summary.get("statut") == "deja_en_cours":
        return summary
    ids = summary.get("ids", [])
    try:
        summary["enrichissement"] = enrich_for(storage, ids, settings)
    except Exception as exc:  # l'enrichissement est un bonus : ne bloque jamais l'analyse
        log.warning("Enrichissement interrompu : %s", exc)
        summary["enrichissement"] = {"erreur": str(exc)}
    pending = storage.articles_to_analyze()
    summary["analyses"] = analyze_articles(storage, pending)
    summary["actions_creees"] = sync_actions(storage, pending)
    if settings.get("ia", {}).get("active"):
        summary["resumes_ia"] = ai_summaries(storage, pending, int(settings["ia"].get("max_articles_par_execution", 20)))
    notify_critical(storage, ids, settings)
    return summary
