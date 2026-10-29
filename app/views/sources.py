import pandas as pd
import streamlit as st

from ui import STATUT_SOURCE, esc, get_storage, page_header
from veille.sources import (CATEGORIES, CONFIANCES, NATURES, TYPES, SourceValidationError, export_catalog, parse_opml,
                            validate_source)

METHODO = """
**Démarche de veille** (détaillée dans `METHODOLOGIE_VEILLE.md`) :
1. **Cadrage** : profil de l'organisation (secteur, taille, activités, données, inventaire technique, exigences, thèmes).
2. **Sélection des sources** : priorité aux sources primaires officielles (ANSSI/CERT-FR, CISA, NIST, CNIL, EUR-Lex, ISO),
   complétées par les éditeurs du parc, la presse spécialisée et la recherche, chaque source ayant une justification et un niveau de confiance.
3. **Collecte automatisée** : flux RSS/Atom et API publiques, fréquence par source, robots.txt respecté, aucune protection contournée.
4. **Traitement** : déduplication, classification, enrichissement (NVD, KEV, EPSS), analyse de pertinence et priorisation explicable.
5. **Exploitation** : qualification par l'analyste (statuts), plan d'action, rapports périodiques.
6. **Amélioration continue** : suivi de l'état des sources, ajustement du catalogue et du profil.
"""


def source_form(storage, src: dict | None, key: str) -> None:
    src = src or {}
    with st.form(key):
        c = st.columns(2)
        nom = c[0].text_input("Nom *", src.get("nom", ""), max_chars=200)
        url = c[1].text_input("URL du flux / de l'API *", src.get("url", ""), max_chars=2000)
        c = st.columns(4)
        typ = c[0].selectbox("Type", TYPES, index=TYPES.index(src.get("type", "rss")))
        cats = list(CATEGORIES)
        cat = c[1].selectbox("Catégorie", cats, index=cats.index(src.get("categorie", "technique")), format_func=CATEGORIES.get)
        confs = list(CONFIANCES)
        conf = c[2].selectbox("Niveau de confiance", confs, index=confs.index(src.get("confiance", "moyenne")), format_func=CONFIANCES.get)
        nats = list(NATURES)
        nat = c[3].selectbox("Nature", nats, index=nats.index(src["nature"]) if src.get("nature") in nats else 0, format_func=NATURES.get)
        c = st.columns(4)
        freq = c[0].number_input("Fréquence (minutes)", 15, 43200, int(src.get("frequence_minutes", 1440)), step=15)
        lang = c[1].selectbox("Langue", ["fr", "en", "autre"], index=["fr", "en", "autre"].index(src.get("langue") or "en") if (src.get("langue") or "en") in ("fr", "en") else 2)
        maxi = c[2].number_input("Éléments max. par collecte", 1, 1000, int((src.get("options") or {}).get("max_items", 60)))
        actif = c[3].checkbox("Active", bool(src.get("actif", True)))
        sous = st.text_input("Sous-catégorie", src.get("sous_categorie") or "", max_chars=200)
        org = st.text_input("Organisme", src.get("organisme") or "", max_chars=200)
        just = st.text_area("Justification de la sélection *", src.get("justification") or "", max_chars=3000)
        filt = st.text_input("Filtre par mots-clés (séparés par des virgules ; vide = aucun filtre)", ", ".join(src.get("filtre_mots_cles") or []))
        techs = st.text_input("Technologies concernées (flux éditeur)", ", ".join(src.get("technologies") or []))
        alt = st.text_area("Alternative en cas d'indisponibilité", src.get("alternative") or "", max_chars=3000)
        if st.form_submit_button("Enregistrer"):
            data = {"id": src.get("id"), "nom": nom, "url": url, "type": typ, "categorie": cat, "confiance": conf, "nature": nat,
                    "frequence_minutes": freq, "langue": lang, "actif": actif, "sous_categorie": sous, "organisme": org,
                    "justification": just, "filtre_mots_cles": filt, "technologies": techs, "alternative": alt,
                    "options": {**(src.get("options") or {}), "max_items": maxi}}
            try:
                v = validate_source(data)
                if not v.get("justification"):
                    raise SourceValidationError("La justification est obligatoire (traçabilité du choix de la source).")
                if src.get("id"):
                    storage.update_source(src["id"], v)
                    if src.get("url") != v["url"]:
                        storage.update_source(src["id"], {"statut": "non_verifie", "etag": None, "last_modified": None})
                    st.success("Source mise à jour. Le nouveau domaine est ajouté à la liste blanche réseau.")
                else:
                    if storage.get_source(v["id"]):
                        raise SourceValidationError("Une source avec cet identifiant existe déjà.")
                    storage.upsert_source(v)
                    st.success(f"Source « {v['nom']} » ajoutée (statut : non vérifiée). Testez-la pour confirmer son fonctionnement.")
            except SourceValidationError as exc:
                st.error(str(exc))


def render():
    storage = get_storage()
    page_header("Sources et méthodologie", "Catalogue des sources, justification, fiabilité, fréquence et état de fonctionnement")
    tabs = st.tabs(["Catalogue", "Ajouter / modifier", "Historique des vérifications", "Import / export", "Méthodologie"])
    sources = storage.list_sources()
    with tabs[0]:
        df = pd.DataFrame([{"Nom": s["nom"], "Catégorie": CATEGORIES[s["categorie"]].replace("Veille ", ""), "Type": s["type"],
                            "Nature": (NATURES.get(s.get("nature")) or "—").split(" (")[0], "Confiance": CONFIANCES[s["confiance"]],
                            "Fréquence (min)": s["frequence_minutes"], "État": STATUT_SOURCE.get(s["statut"], s["statut"]),
                            "Dernier succès": (s.get("dernier_succes") or "—")[:16].replace("T", " "),
                            "Articles": storage.scalar("SELECT COUNT(*) FROM articles WHERE source_id = ?", (s["id"],)),
                            "URL": s["url"]} for s in sources])
        st.dataframe(df, hide_index=True, width="stretch", height=520, column_config={"URL": st.column_config.LinkColumn()})
        sel = st.selectbox("Détail d'une source", [s["id"] for s in sources], format_func={s["id"]: s["nom"] for s in sources}.get)
        s = storage.get_source(sel)
        st.markdown(f"**{esc(s['nom'])}** — {esc(s.get('organisme') or '')} — {STATUT_SOURCE.get(s['statut'])}")
        st.markdown(f"**Justification** : {esc(s.get('justification'))}")
        if s.get("filtre_mots_cles"):
            st.markdown(f"**Filtre** : {esc(', '.join(s['filtre_mots_cles']))}")
        if s.get("derniere_erreur"):
            st.warning(f"Dernier message : {s['derniere_erreur']}")
        if s.get("alternative"):
            st.info(f"Alternative documentée : {s['alternative']}")
        c = st.columns(3)
        if c[0].button("🧪 Tester / collecter cette source maintenant", disabled=s["type"] == "manuel" or not s["actif"]):
            from veille.pipeline import run_pipeline
            with st.spinner("Collecte en cours…"):
                res = run_pipeline(storage, trigger="manuel", only_due=False, source_ids=[s["id"]])
            d = (res.get("details") or [{}])[0]
            (st.success if d.get("statut") == "ok" else st.error)(
                f"Résultat : {d.get('statut', res.get('statut'))} — {d.get('nouveaux', 0)} nouveaux, {d.get('doublons', 0)} doublons, "
                f"{d.get('filtres', 0)} filtrés. {d.get('erreur') or ''}")
        if c[1].button("⏯️ Activer / désactiver", disabled=s["type"] == "manuel"):
            storage.update_source(s["id"], {"actif": not s["actif"], "statut": "non_verifie" if not s["actif"] else "desactive"})
            st.rerun()
        if c[2].button("🗑️ Supprimer"):
            res = storage.delete_source(s["id"])
            st.success("Source supprimée." if res == "supprimee" else "Source désactivée (des articles y sont rattachés : conservation de la traçabilité).")
            st.rerun()
    with tabs[1]:
        mode = st.radio("Action", ["Ajouter une source", "Modifier une source existante"], horizontal=True)
        if mode.startswith("Ajouter"):
            source_form(storage, None, "add_src")
        else:
            sid = st.selectbox("Source", [s["id"] for s in sources], format_func={s["id"]: s["nom"] for s in sources}.get, key="edit_sel")
            source_form(storage, storage.get_source(sid), f"edit_{sid}")
        st.caption("Les requêtes sortantes sont limitées aux domaines des sources du catalogue ; les adresses internes sont refusées.")
    with tabs[2]:
        rows = storage.query("""SELECT v.verifie_le, s.nom, v.statut, v.code_http, v.elements, v.nouveaux, v.doublons, v.filtres, v.duree_ms, v.erreur
                                FROM verifications_sources v JOIN sources s ON s.id = v.source_id ORDER BY v.id DESC LIMIT 500""")
        st.dataframe(pd.DataFrame(rows), hide_index=True, width="stretch", height=520)
    with tabs[3]:
        st.download_button("Exporter le catalogue (YAML)", export_catalog(storage).encode("utf-8"), "sources.yaml", "application/x-yaml")
        st.markdown("**Importer des abonnements OPML** (ex. export Feedly : *Organize › Export OPML*)")
        up = st.file_uploader("Fichier OPML", type=["opml", "xml"])
        cat = st.selectbox("Catégorie attribuée aux flux importés", list(CATEGORIES), format_func=CATEGORIES.get)
        if up and st.button("Importer"):
            try:
                if up.size > 2_000_000:
                    raise SourceValidationError("Fichier trop volumineux.")
                found = parse_opml(up.getvalue(), cat)
                n = sum(1 for f in found if storage.upsert_source(f))
                st.success(f"{n} flux importé(s) sur {len(found)} trouvé(s) (statut : non vérifié, confiance : moyenne).")
            except Exception as exc:
                st.error(f"Import impossible : {exc}")
    with tabs[4]:
        st.markdown(METHODO)
        st.markdown("**Critères de fiabilité** : statut de l'émetteur (autorité, éditeur, presse, communauté), caractère primaire "
                    "de l'information, historique de qualité, transparence (date, auteur, références). Une source accessible "
                    "n'est pas réputée fiable pour autant ; les informations de sources secondaires sont signalées « à recouper ».")
