import pandas as pd
import streamlit as st

from ui import articles_df, get_storage, page_header, profile, render_fiche, selectable_table
from views.flux import filters, sort_rows


def render():
    storage = get_storage()
    page_header("Vulnérabilités et menaces", "Vulnérabilités récentes, exploitation vérifiée et présence potentielle dans le parc")
    tabs = st.tabs(["Vulnérabilités et menaces collectées", "Catalogue KEV × inventaire", "CVE enrichies"])
    with tabs[0]:
        f = filters(storage, "vuln", default_cats=["vulnerabilite", "menace", "incident"])
        only_parc = st.toggle("Uniquement les éléments concernant le parc déclaré", value=False)
        rows = sort_rows([r for r in storage.list_articles(**f) if r.get("priorite")], "vuln")
        if only_parc:
            rows = [r for r in rows if r.get("technologies")]
        df = articles_df(rows)
        if not df.empty:
            df.insert(4, "Parc concerné", [", ".join(t["nom"] for t in r.get("technologies") or []) or "—" for r in rows])
            df.insert(5, "CVE", [", ".join(c["id"] for c in (r.get("cves") or [])[:3]) + ("…" if len(r.get("cves") or []) > 3 else "") for r in rows])
            df.insert(6, "CVSS max (NVD)", pd.to_numeric(pd.Series([max([c["cvss"] for c in r.get("cves") or [] if c.get("cvss") is not None],
                                                                        default=None) for r in rows], dtype="object"), errors="coerce"))
            df.insert(7, "KEV", ["oui" if any(c.get("kev") for c in r.get("cves") or []) else "" for r in rows])
        sel = selectable_table(df, "vuln_table")
        if sel:
            st.divider()
            render_fiche(storage, storage.get_article_full(sel), "vuln")
    with tabs[1]:
        st.markdown("Entrées du catalogue **CISA KEV** (exploitation active confirmée) dont le fournisseur ou le produit "
                    "correspond à une technologie de l'inventaire. Correspondance par nom : la version reste à vérifier.")
        from veille.classify import match_inventory
        p = profile()
        kev = storage.query("SELECT * FROM kev ORDER BY ajoute_le DESC")
        hits = []
        for k in kev:
            m = match_inventory(f"{k['fournisseur']} {k['produit']} {k['nom']}", p.get("technologies") or [])
            if m:
                hits.append({"CVE": k["cve_id"], "Ajoutée le": k["ajoute_le"], "Fournisseur": k["fournisseur"], "Produit": k["produit"],
                             "Vulnérabilité": k["nom"], "Technologie du parc": ", ".join(x["nom"] for x in m),
                             "Rançongiciel": k["rancongiciel"], "Action requise (CISA)": k["action_requise"]})
        st.caption(f"{len(kev)} entrées KEV en base, {len(hits)} correspondant à l'inventaire.")
        if hits:
            st.dataframe(pd.DataFrame(hits), hide_index=True, width="stretch", height=480)
    with tabs[2]:
        rows = storage.query("SELECT c.*, k.cve_id IS NOT NULL AS kev FROM cve c LEFT JOIN kev k ON k.cve_id = c.cve_id "
                             "ORDER BY c.cvss_score DESC NULLS LAST LIMIT 1000")
        st.caption("Données de référence : CVSS (API NVD), EPSS (FIRST), exploitation (CISA KEV). Valeur vide = non disponible, jamais estimée.")
        st.dataframe(pd.DataFrame([{"CVE": r["cve_id"], "CVSS": r["cvss_score"], "Version": r["cvss_version"], "Sévérité": r["severite"],
                                    "Source CVSS": r["cvss_source"], "Statut NVD": r["nvd_statut"], "EPSS": r["epss"],
                                    "Percentile EPSS": r["epss_percentile"], "KEV": "oui" if r["kev"] else ""} for r in rows]),
                     hide_index=True, width="stretch", height=480)
