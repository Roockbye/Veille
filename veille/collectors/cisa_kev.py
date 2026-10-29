"""Connecteur du catalogue CISA Known Exploited Vulnerabilities (JSON officiel)."""
from __future__ import annotations

import json
from datetime import timedelta

from veille.collectors import CollectorError
from veille.normalize import iso, parse_date, utcnow

KEV_SEARCH_URL = "https://www.cisa.gov/known-exploited-vulnerabilities-catalog?search_api_fulltext={cve}"


def parse_kev(content: bytes, window_days: int = 30) -> tuple[list[dict], list[dict]]:
    """Renvoie (lignes pour la table kev, éléments à créer comme articles pour les ajouts récents)."""
    try:
        data = json.loads(content)
        vulns = data["vulnerabilities"]
    except (ValueError, KeyError, TypeError) as exc:
        raise CollectorError(f"Catalogue KEV illisible : {type(exc).__name__}") from exc
    rows, items = [], []
    limit = utcnow() - timedelta(days=window_days)
    for v in vulns:
        cve = str(v.get("cveID", "")).strip().upper()
        if not cve.startswith("CVE-"):
            continue
        row = {
            "cve_id": cve,
            "fournisseur": v.get("vendorProject"),
            "produit": v.get("product"),
            "nom": v.get("vulnerabilityName"),
            "ajoute_le": v.get("dateAdded"),
            "echeance_cisa": v.get("dueDate"),
            "rancongiciel": v.get("knownRansomwareCampaignUse"),
            "action_requise": v.get("requiredAction"),
            "description": v.get("shortDescription"),
        }
        rows.append(row)
        added = parse_date(v.get("dateAdded"))
        if added and added >= limit:
            summary = (f"{row['description'] or ''}\n"
                       f"Ajoutée au catalogue KEV le {row['ajoute_le']} (exploitation active confirmée par la CISA). "
                       f"Action requise (CISA) : {row['action_requise'] or 'n.c.'} "
                       f"Échéance fixée aux agences fédérales américaines : {row['echeance_cisa'] or 'n.c.'}. "
                       + ("Utilisation connue dans des campagnes de rançongiciel (CISA)."
                          if (row["rancongiciel"] or "").lower() == "known"
                          else "Aucun usage par des groupes criminels connu de la CISA à ce jour."))
            items.append({
                "url": KEV_SEARCH_URL.format(cve=cve),
                "titre": f"[KEV] {cve} — {row['fournisseur']} {row['produit']} : {row['nom']}",
                "auteur": None,
                "resume_source": summary.strip(),
                "publie_le": iso(added),
                "langue": "en",
                "origine": "CISA KEV",
                "donnees": {"kev": row},
            })
    return rows, items
