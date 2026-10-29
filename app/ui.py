"""Éléments communs de l'interface Streamlit."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import pandas as pd  # noqa: E402
import streamlit as st  # noqa: E402

from veille.classify import CATEGORIES, THEMES  # noqa: E402
from veille.logging_setup import setup_logging  # noqa: E402
from veille.normalize import safe_http_url  # noqa: E402
from veille.organisation import get_settings, has_profile, hypotheses  # noqa: E402
from veille.storage import Storage  # noqa: E402

PRIORITES = ["Critique", "Élevée", "Modérée", "Faible", "À qualifier"]
PRIO_COLOR = {"Critique": "red", "Élevée": "orange", "Modérée": "violet", "Faible": "green", "À qualifier": "blue"}
PRIO_ICON = {"Critique": "🔴", "Élevée": "🟠", "Modérée": "🟡", "Faible": "🟢", "À qualifier": "🔵"}
STATUTS_ARTICLE = {"nouveau": "Nouveau", "lu": "Lu", "pertinent": "Pertinent", "non_pertinent": "Non pertinent",
                   "a_investiguer": "À investiguer", "traite": "Traité"}
STATUTS_ACTION = {"a_etudier": "À étudier", "a_valider": "À valider", "planifiee": "Planifiée", "en_cours": "En cours",
                  "terminee": "Terminée", "abandonnee": "Abandonnée"}
STATUT_SOURCE = {"ok": "✅ Fonctionnelle", "erreur": "❌ En erreur", "bloque": "⛔ Bloquée", "non_verifie": "⏳ Non vérifiée",
                 "desactive": "⏸️ Désactivée"}
PERTINENCE = {"forte": "Forte", "moyenne": "Moyenne", "faible": "Faible", "a_qualifier": "À qualifier", "non_pertinent": "Non pertinente"}
CONFIANCE = {"elevee": "Élevée", "moyenne": "Moyenne", "faible": "Faible"}

_MD = re.compile(r"([\\`*_\[\]<>#|~$])")


def esc(text) -> str:
    """Échappe un texte non fiable avant affichage en Markdown (titres et résumés issus des sources)."""
    return _MD.sub(r"\\\1", str(text or ""))


def link(label: str, url: str) -> str:
    u = safe_http_url(url or "")
    return f"[{esc(label)}]({u.replace(')', '%29').replace(' ', '%20')})" if u else esc(label)


def prio_badge(p: str | None) -> str:
    p = p or "À qualifier"
    return f":{PRIO_COLOR.get(p, 'gray')}[**{PRIO_ICON.get(p, '')} {p}**]"


@st.cache_resource
def get_storage() -> Storage:
    setup_logging()
    s = Storage()
    s.init_db()
    if not s.scalar("SELECT COUNT(*) FROM sources"):
        from veille.sources import seed_sources
        seed_sources(s)
    return s


@st.cache_resource
def get_scheduler():
    """Planificateur intégré : actif uniquement tant que ce serveur Streamlit tourne."""
    from veille.scheduler import start_background
    return start_background(get_storage())


def ensure_scheduler() -> None:
    import os
    if os.environ.get("VEILLE_SCHEDULER_INTEGRE", "1") == "0":
        return  # planification assurée par le service autonome (ex. Docker Compose)
    s = get_storage()
    plan = get_settings(s).get("planification", {})
    if plan.get("active") and plan.get("integree", True):
        get_scheduler()


def profile() -> dict:
    from veille.pipeline import current_profile
    return current_profile()


def page_header(title: str, caption: str | None = None) -> None:
    st.title(title)
    if caption:
        st.caption(caption)
    if not has_profile():
        st.info("Profil d'organisation non configuré : le **profil de démonstration (organisation fictive)** est utilisé. "
                "Configurez votre organisation dans la page *Configuration*.", icon="ℹ️")


def show_hypotheses(p: dict) -> None:
    h = hypotheses(p)
    if h:
        with st.expander(f"Hypothèses de travail explicitement signalées ({len(h)})"):
            for x in h:
                st.markdown(f"- {esc(x)}")


def articles_df(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame([{
        "id": r["id"],
        "Priorité": r.get("priorite") or "—",
        "Score": r.get("score"),
        "Titre": r["titre"],
        "Source": r["source_nom"],
        "Catégorie": CATEGORIES.get(r.get("categorie_principale"), "—"),
        "Pertinence": PERTINENCE.get(r.get("pertinence"), "—"),
        "Publié": (r.get("publie_le") or "")[:10],
        "Collecté": (r.get("collecte_le") or "")[:10],
        "Statut": STATUTS_ARTICLE.get(r["statut"], r["statut"]),
        "URL": r["url"],
    } for r in rows])


def render_fiche(storage: Storage, art: dict, key_prefix: str = "f") -> None:
    """Fiche d'analyse structurée d'un article + gestion du statut de traitement."""
    st.markdown(f"### {esc(art['titre'])}")
    c1, c2, c3, c4 = st.columns([1.2, 1, 1, 1])
    c1.markdown(prio_badge(art.get("priorite")) + f" — score {art.get('score')}")
    c2.markdown(f"**Pertinence** : {PERTINENCE.get(art.get('pertinence'), '—')}")
    c3.markdown(f"**Confiance** : {CONFIANCE.get(art.get('confiance'), '—')}")
    c4.markdown(f"**Échéance** : {art.get('echeance') or '—'}")
    st.markdown(f"**Source** : {esc(art['source_nom'])} — publié le {(art.get('publie_le') or 'n.c.')[:10]}, "
                f"collecté le {art['collecte_le'][:10]}" + (f" — {esc(art['origine'])}" if art.get("origine") else ""))
    url = safe_http_url(art["url"])
    if url:
        st.link_button("Ouvrir la source originale ↗", url)
    st.markdown("**Catégories** : " + ", ".join(CATEGORIES.get(c, c) for c in art.get("categories") or [])
                + (f" — **Mots-clés** : {esc(', '.join(art.get('mots_cles') or []))}" if art.get("mots_cles") else ""))
    meth = art.get("methode_resume") or ""
    lab = {"extrait_source": "extrait de la source", "synthese_regles": "synthèse automatique par règles"}.get(meth, f"généré par IA ({meth[3:]})" if meth.startswith("ia:") else meth)
    st.markdown(f"**Résumé en français** _( {lab} )_")
    st.write(art.get("resume_fr") or "—")
    tabs = st.tabs(["Analyse", "Priorisation", "Recommandations", "Réglementaire / normatif", "Texte source", "Traitement"])
    with tabs[0]:
        if art.get("technologies"):
            st.markdown("**Technologies du parc concernées**")
            st.dataframe(pd.DataFrame([{"Technologie": t["nom"], "Exposition": t["exposition"], "Criticité": t["criticite"],
                                        "Versions du parc": ", ".join(t["versions_parc"]),
                                        "Versions citées": ", ".join(t["versions_citees"]) or "—"} for t in art["technologies"]]),
                         hide_index=True, width="stretch")
        if art.get("produits_cites"):
            st.markdown("**Produits cités** : " + esc(", ".join(art["produits_cites"])))
        if art.get("cves"):
            st.markdown("**CVE** (données issues du NVD, de la CISA et de FIRST ; aucune valeur estimée)")
            st.dataframe(pd.DataFrame([{"CVE": c["id"], "CVSS": c.get("cvss"), "Version": c.get("cvss_version"),
                                        "Sévérité": c.get("severite"), "Source CVSS": c.get("cvss_source") or "non disponible",
                                        "EPSS": c.get("epss"), "KEV (exploitée)": "oui" if c.get("kev") else "non"}
                                       for c in art["cves"]]), hide_index=True, width="stretch")
        expl = next((f for f in art.get("facteurs") or [] if f["facteur"] == "_exploitation"), None)
        if expl:
            st.markdown(f"**Exploitation** : {esc(expl['justification'])}" + (" ✅ vérifiée" if expl["verifie"] else ""))
        st.markdown("**Impact potentiel** : " + (", ".join(f"{i['libelle']} _(indices : {esc(', '.join(i['indices']))})_"
                                                         for i in art.get("impacts") or []) or "non déterminé"))
        st.markdown("**Pertinence** : " + esc(" ".join(art.get("pertinence_motifs") or [])))
        if art.get("a_verifier"):
            st.markdown("**Informations restant à vérifier**")
            for v in art["a_verifier"]:
                st.markdown(f"- {esc(v)}")
    with tabs[1]:
        facts = [f for f in art.get("facteurs") or [] if not f["facteur"].startswith("_")]
        if facts:
            st.dataframe(pd.DataFrame([{"Facteur": f["facteur"], "Points": f["points"], "Justification": f["justification"],
                                        "Vérifié": "oui" if f["verifie"] else "déclaré / à confirmer",
                                        "Origine": f["source"] if isinstance(f["source"], str) else ""} for f in facts]),
                         hide_index=True, width="stretch")
        just = next((f["justification"] for f in art.get("facteurs") or [] if f["facteur"] == "_justification"), "")
        st.caption(just)
        st.markdown(f"**Urgence** : {art.get('urgence')} — **échéance proposée** : {art.get('echeance')}")
    with tabs[2]:
        for r in art.get("actions") or []:
            st.markdown(f"- **{esc(r['type'])}** — {esc(r['action'])} _(responsable suggéré : {esc(r['responsable'])})_")
        st.caption("Recommandations d'aide à la décision : l'outil n'effectue aucune modification ni aucun scan du SI.")
    with tabs[3]:
        reg, norm = art.get("reglementaire"), art.get("normatif")
        if not reg and not norm:
            st.write("Sans objet pour cet élément.")
        if reg:
            st.markdown(f"**Nature de l'évolution** : {esc(reg['nature_evolution'])}  \n**Statut juridique** : {esc(reg['statut_detecte'])}")
            if reg.get("dates_mentionnees"):
                st.markdown("**Dates mentionnées par la source** : " + ", ".join(d["date"] for d in reg["dates_mentionnees"]))
            for t in reg.get("textes") or []:
                with st.expander(f"{t['nom']} — {t['applicabilite']}"):
                    st.markdown(f"**Référence** : {esc(t['reference'])}  \n**Nature** : {esc(t['nature_juridique'])}  \n"
                                f"**Statut (référentiel)** : {esc(t['statut_referentiel'])}  \n**Motif** : {esc(t['motif'])}")
                    if t.get("note_statut"):
                        st.warning(t["note_statut"])
                    st.markdown(f"**Organisations concernées** : {esc(t.get('concernes'))}")
                    st.markdown("**Obligations possibles (à vérifier)**\n" + "\n".join(f"- {esc(o)}" for o in t["obligations_possibles"]))
                    st.markdown("**Démarches pour qualifier l'applicabilité**\n" + "\n".join(f"- {esc(o)}" for o in t["demarches"]))
                    st.markdown("**Sources officielles** : " + ", ".join(link(u, u) for u in t["sources_officielles"]))
            st.caption(reg.get("avertissement", ""))
        if norm:
            st.markdown(f"**Type de document** : {esc(norm['type_libelle'])}")
            st.info(norm["avertissement"])
            if norm.get("changements"):
                st.markdown("**Évolutions constatées** : " + esc("; ".join(norm["changements"])))
    with tabs[4]:
        st.text(art.get("resume_source") or "(aucun résumé fourni par la source)")
        st.caption("Contenu brut nettoyé (balises et scripts supprimés), affiché comme texte non interprété.")
    with tabs[5]:
        with st.form(f"{key_prefix}_statut_{art['id']}"):
            keys = list(STATUTS_ARTICLE)
            new = st.selectbox("Statut de traitement", keys, index=keys.index(art["statut"]), format_func=STATUTS_ARTICLE.get)
            notes = st.text_area("Notes de l'analyste", value=art.get("notes") or "", max_chars=5000)
            if st.form_submit_button("Enregistrer"):
                storage.set_article_status(art["id"], new, notes)
                st.success("Statut enregistré (historisé).")
                st.rerun()
        hist = storage.query("SELECT ancien, nouveau, modifie_le FROM historique_statuts WHERE article_id = ? ORDER BY id DESC", (art["id"],))
        if hist:
            st.caption("Historique : " + " ; ".join(f"{h['modifie_le'][:16]} {STATUTS_ARTICLE.get(h['ancien'])} → {STATUTS_ARTICLE.get(h['nouveau'])}" for h in hist))


def selectable_table(df: pd.DataFrame, key: str, height: int = 420) -> int | None:
    """Affiche un tableau sélectionnable ; renvoie l'id de la ligne choisie."""
    if df.empty:
        st.info("Aucun élément ne correspond aux filtres.")
        return None
    event = st.dataframe(df.drop(columns=["URL"], errors="ignore"), hide_index=True, width="stretch", height=height,
                         on_select="rerun", selection_mode="single-row", key=key,
                         column_config={"id": None, "Score": st.column_config.NumberColumn(width="small")})
    rows = event.selection.rows if event and event.selection else []
    return int(df.iloc[rows[0]]["id"]) if rows else None


CSS = """
<style>
.block-container {padding-top: 2rem; max-width: 1400px;}
[data-testid="stMetricValue"] {font-size: 1.8rem;}
</style>
"""
