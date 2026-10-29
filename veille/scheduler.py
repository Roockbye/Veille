"""Planification des tâches (APScheduler).

Deux modes d'exécution, documentés dans le README :
- intégré à l'interface Streamlit : les tâches ne tournent QUE tant que le serveur Streamlit est actif ;
- service autonome (`python -m veille scheduler`) : à lancer via systemd, cron @reboot ou Docker pour
  une exécution continue indépendante du navigateur.
Un verrou en base empêche deux collectes simultanées si les deux modes coexistent.
"""
from __future__ import annotations

import logging
import signal
from datetime import date, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

from veille.organisation import get_settings
from veille.storage import Storage

log = logging.getLogger("veille.scheduler")
JOB_COLLECT = "collecte_planifiee"
JOB_REPORT = "rapport_planifie"


def job_collect() -> None:
    from veille.pipeline import run_pipeline
    storage = Storage()
    storage.init_db()
    if not get_settings(storage).get("planification", {}).get("active"):
        log.info("Planification désactivée : collecte ignorée.")
        return
    try:
        res = run_pipeline(storage, trigger="planifie", only_due=True)
        log.info("Collecte planifiée : %s (%s nouveaux)", res.get("statut"), res.get("nouveaux"))
    except Exception:
        log.exception("Échec de la collecte planifiée")


def report_period(freq: str, today: date | None = None) -> tuple[date, date]:
    today = today or date.today()
    end = today - timedelta(days=1)
    if freq == "mensuel":
        last_month_end = today.replace(day=1) - timedelta(days=1)
        return last_month_end.replace(day=1), last_month_end
    return end - timedelta(days=6), end


def job_report() -> None:
    from veille.reports.builder import generate_report
    storage = Storage()
    storage.init_db()
    s = get_settings(storage)
    plan = s.get("planification", {})
    if not plan.get("active") or plan.get("rapport_frequence", "desactive") == "desactive":
        return
    start, end = report_period(plan.get("rapport_frequence"))
    try:
        res = generate_report(storage, start, end, trigger="planifie")
        log.info("Rapport planifié généré : %s", res.get("chemin_pdf"))
        n = s.get("notifications", {})
        if n.get("email_actif") and n.get("rapport_disponible"):
            from veille.notify import send_email
            send_email(f"[Veille] Rapport disponible ({start} → {end})",
                       f"Le rapport de veille de la période {start} → {end} a été généré "
                       f"({res['nb_articles']} éléments).", [res.get("chemin_pdf")])
    except Exception:
        log.exception("Échec de la génération planifiée du rapport")


def configure(scheduler, settings: dict) -> None:
    plan = settings.get("planification", {})
    scheduler.add_job(job_collect, IntervalTrigger(minutes=max(15, int(plan.get("intervalle_collecte_minutes", 30)))),
                      id=JOB_COLLECT, replace_existing=True, max_instances=1, coalesce=True)
    freq = plan.get("rapport_frequence", "hebdomadaire")
    hour = int(plan.get("rapport_heure", 7))
    if freq == "mensuel":
        trig = CronTrigger(day=1, hour=hour, minute=0)
    else:
        trig = CronTrigger(day_of_week=plan.get("rapport_jour_semaine", "mon"), hour=hour, minute=0)
    if freq != "desactive":
        scheduler.add_job(job_report, trig, id=JOB_REPORT, replace_existing=True, max_instances=1, coalesce=True)
    elif scheduler.get_job(JOB_REPORT):
        scheduler.remove_job(JOB_REPORT)


def start_background(storage: Storage) -> BackgroundScheduler:
    sched = BackgroundScheduler(timezone="Europe/Paris")
    configure(sched, get_settings(storage))
    sched.start()
    log.info("Planificateur intégré démarré (actif tant que l'application tourne).")
    return sched


def run_blocking() -> None:
    storage = Storage()
    storage.init_db()
    sched = BlockingScheduler(timezone="Europe/Paris")
    configure(sched, get_settings(storage))
    signal.signal(signal.SIGTERM, lambda *_: sched.shutdown(wait=False))
    plan = get_settings(storage).get("planification", {})
    log.info("Service de planification démarré. Planification %s.",
             "ACTIVE" if plan.get("active") else "DÉSACTIVÉE (activer depuis l'interface ou settings.yaml)")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        log.info("Service de planification arrêté.")
