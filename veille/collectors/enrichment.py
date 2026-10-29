"""Enrichissement des CVE à partir de sources vérifiables : API NVD (CVSS) et FIRST EPSS.

Aucune valeur n'est estimée : en l'absence de donnée, le champ reste vide et l'analyse l'indique.
"""
from __future__ import annotations

import json
import logging
import re

from veille.config import env
from veille.net import BlockedRequest, FetchError, SafeFetcher
from veille.normalize import iso, utcnow
from veille.storage import Storage

log = logging.getLogger("veille.enrichment")
NVD_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve}"
EPSS_URL = "https://api.first.org/data/v1/epss?cve={cves}"
CVE_RE = re.compile(r"\bCVE-(\d{4})-(\d{4,7})\b", re.IGNORECASE)


def extract_cves(text: str) -> list[str]:
    seen = []
    for m in CVE_RE.finditer(text or ""):
        c = f"CVE-{m.group(1)}-{m.group(2)}"
        if c not in seen:
            seen.append(c)
    return seen


def parse_nvd(data: dict) -> dict | None:
    vulns = data.get("vulnerabilities") or []
    if not vulns:
        return None
    cve = vulns[0].get("cve", {})
    desc = next((d.get("value") for d in cve.get("descriptions", []) if d.get("lang") == "en"), None)
    metrics = cve.get("metrics", {})
    chosen = None
    for key, version in (("cvssMetricV40", "4.0"), ("cvssMetricV31", "3.1"), ("cvssMetricV30", "3.0"), ("cvssMetricV2", "2.0")):
        entries = metrics.get(key) or []
        if not entries:
            continue
        primary = [m for m in entries if m.get("type") == "Primary"]
        m = (primary or entries)[0]
        cd = m.get("cvssData", {})
        chosen = {
            "cvss_score": cd.get("baseScore"),
            "cvss_version": version,
            "cvss_vecteur": cd.get("vectorString"),
            "severite": cd.get("baseSeverity") or m.get("baseSeverity"),
            "cvss_source": f"NVD ({m.get('source', 'n.c.')}, {m.get('type', 'n.c.')})",
        }
        break
    out = {"description": (desc or "")[:2000], "nvd_statut": "ok", "nvd_le": iso(utcnow())}
    out.update(chosen or {"cvss_score": None, "severite": None, "cvss_source": "NVD : aucun score publié"})
    return out


def enrich_cves(storage: Storage, fetcher: SafeFetcher, cve_ids: list[str], max_nvd: int = 40,
                use_nvd: bool = True, use_epss: bool = True) -> dict:
    stats = {"nvd_ok": 0, "nvd_absent": 0, "nvd_erreur": 0, "epss_ok": 0}
    cve_ids = sorted(set(cve_ids))
    if not cve_ids:
        return stats
    known = storage.get_cves(cve_ids)
    if use_nvd:
        todo = [c for c in cve_ids if (known.get(c) or {}).get("nvd_statut") not in ("ok", "introuvable")][:max_nvd]
        headers = {"apiKey": env("NVD_API_KEY")} if env("NVD_API_KEY") else {}
        for cve in todo:
            try:
                res = fetcher.fetch(NVD_URL.format(cve=cve), headers=headers, check_robots=False)
                parsed = parse_nvd(json.loads(res.content))
                if parsed is None:
                    storage.upsert_cve(cve, {"nvd_statut": "introuvable", "nvd_le": iso(utcnow())})
                    stats["nvd_absent"] += 1
                else:
                    storage.upsert_cve(cve, parsed)
                    stats["nvd_ok"] += 1
            except (FetchError, BlockedRequest, ValueError) as exc:
                log.warning("NVD indisponible pour %s : %s", cve, exc)
                storage.upsert_cve(cve, {"nvd_statut": "erreur", "nvd_le": iso(utcnow())})
                stats["nvd_erreur"] += 1
    if use_epss:
        for i in range(0, len(cve_ids), 80):
            chunk = cve_ids[i:i + 80]
            try:
                res = fetcher.fetch(EPSS_URL.format(cves=",".join(chunk)), check_robots=False)
                for row in json.loads(res.content).get("data", []):
                    storage.upsert_cve(row["cve"].upper(), {"epss": float(row["epss"]),
                                                            "epss_percentile": float(row["percentile"]),
                                                            "epss_le": row.get("date")})
                    stats["epss_ok"] += 1
            except (FetchError, BlockedRequest, ValueError, KeyError) as exc:
                log.warning("EPSS indisponible : %s", exc)
    return stats
