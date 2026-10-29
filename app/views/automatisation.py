import pandas as pd
import streamlit as st

from ui import get_storage, page_header
from veille.ai import ai_configured, model_name
from veille.config import logs_dir
from veille.logging_setup import redact
from veille.notify import email_configured, send_email
from veille.organisation import get_settings, set_setting_override


def render():
    storage = get_storage()
    page_header("Automatisation et journaux", "Tâches planifiées, notifications, IA facultative, historique des exécutions")
    s = get_settings(storage)
    plan = s.get("planification", {})
    st.subheader("Planification")
    st.warning("**Conditions d'exécution** : le planificateur intégré ne fonctionne que **tant que le serveur Streamlit est lancé**. "
               "Pour une exécution continue (poste fermé, navigateur fermé), utilisez le service `python -m veille scheduler` "
               "(systemd, cron @reboot ou Docker — voir le README).")
    with st.form("plan"):
        c = st.columns(3)
        active = c[0].toggle("Tâches planifiées activées", bool(plan.get("active")))
        integ = c[1].toggle("Planificateur intégré à l'interface", bool(plan.get("integree", True)),
                            help="Désactiver si le service autonome est utilisé")
        interval = c[2].number_input("Vérification des sources dues (minutes)", 15, 1440, int(plan.get("intervalle_collecte_minutes", 30)))
        c = st.columns(3)
        freqs = ["hebdomadaire", "mensuel", "desactive"]
        freq = c[0].selectbox("Rapport automatique", freqs, index=freqs.index(plan.get("rapport_frequence", "hebdomadaire")))
        days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        day = c[1].selectbox("Jour (hebdomadaire)", days, index=days.index(plan.get("rapport_jour_semaine", "mon")),
                             format_func=dict(zip(days, ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"])).get)
        hour = c[2].number_input("Heure", 0, 23, int(plan.get("rapport_heure", 7)))
        if st.form_submit_button("Enregistrer"):
            for k, v in {"active": active, "integree": integ, "intervalle_collecte_minutes": int(interval), "rapport_frequence": freq,
                         "rapport_jour_semaine": day, "rapport_heure": int(hour)}.items():
                set_setting_override(storage, "planification", k, v)
            from ui import get_scheduler
            from veille.scheduler import configure
            if active and integ:
                configure(get_scheduler(), get_settings(storage))
            st.success("Paramètres enregistrés. Un planificateur déjà lancé applique l'activation/désactivation à sa prochaine échéance.")
    try:
        from ui import get_scheduler
        if plan.get("active") and plan.get("integree", True):
            jobs = get_scheduler().get_jobs()
            st.dataframe(pd.DataFrame([{"Tâche": j.id, "Prochaine exécution": str(j.next_run_time)} for j in jobs]), hide_index=True)
        else:
            st.caption("Planificateur intégré non démarré (tâches désactivées ou mode service).")
    except Exception as exc:
        st.error(f"Planificateur : {exc}")

    st.subheader("Notifications e-mail (facultatif)")
    n = s.get("notifications", {})
    st.markdown(f"Configuration SMTP (.env) : {'✅ présente' if email_configured() else '❌ absente (variables SMTP_* non renseignées)'}")
    c = st.columns(3)
    em = c[0].toggle("Notifications activées", bool(n.get("email_actif")), disabled=not email_configured())
    if c[1].button("Enregistrer", key="save_notif"):
        set_setting_override(storage, "notifications", "email_actif", bool(em))
        st.success("Enregistré.")
    if c[2].button("Envoyer un e-mail de test", disabled=not email_configured()):
        st.write("Envoyé ✅" if send_email("[Veille] Test de notification", "Message de test de l'outil de veille.") else "Échec (voir journaux)")

    st.subheader("Analyse IA (facultative)")
    ia = s.get("ia", {})
    st.markdown(f"Clé API et SDK : {'✅ configurés' if ai_configured() else '❌ non configurés (ANTHROPIC_API_KEY absente)'} — modèle : `{model_name()}`")
    st.caption("Utilisée uniquement pour rédiger des résumés en français des éléments utiles. Les contenus collectés sont traités comme "
               "des données non fiables ; seuls titre et résumé public sont transmis ; la classification et la priorité restent calculées par règles.")
    c = st.columns(2)
    ia_on = c[0].toggle("Résumés IA activés", bool(ia.get("active")), disabled=not ai_configured())
    if c[1].button("Enregistrer", key="save_ia"):
        set_setting_override(storage, "ia", "active", bool(ia_on))
        st.success("Enregistré.")

    st.subheader("Historique des exécutions")
    ex = storage.list_executions(100)
    if ex:
        st.dataframe(pd.DataFrame(ex), hide_index=True, width="stretch", height=300)
    st.subheader("Journal technique (dernières lignes, secrets masqués)")
    log = logs_dir() / "veille.log"
    if log.exists():
        lines = log.read_text(encoding="utf-8", errors="replace").splitlines()[-200:]
        st.code(redact("\n".join(lines)) or "(vide)", language=None)
