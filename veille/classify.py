"""Classification par règles explicites (fonctionne sans IA).

Chaque décision est justifiable : on conserve les mots-clés qui ont déclenché une catégorie.
"""
from __future__ import annotations

import re
from functools import lru_cache

CATEGORIES = {
    "menace": "Menace ou campagne d'attaque",
    "vulnerabilite": "Vulnérabilité ou correctif",
    "technologie": "Évolution technologique",
    "reglementaire": "Évolution réglementaire",
    "normative": "Évolution normative",
    "bonne_pratique": "Bonne pratique ou recommandation",
    "incident": "Incident ou retour d'expérience",
    "non_pertinent": "Information non pertinente",
}

# Mots-clés FR/EN. Un mot en MAJUSCULES est un acronyme (recherche exacte, sensible à la casse) ;
# sinon la recherche est insensible à la casse et le mot peut être un radical (ex. « vulnérabilit »).
KEYWORDS: dict[str, list[str]] = {
    "menace": ["rançongiciel", "ransomware", "campagne", "campaign", "APT", "threat actor", "acteur malveillant",
               "mode opératoire", "malware", "logiciel malveillant", "hameçonnage", "phishing", "botnet",
               "infostealer", "stealer", "cheval de troie", "trojan", "backdoor", "porte dérobée", "espionnage",
               "espionage", "wiper", "DDoS", "loader", "threat brief", "threat intelligence", "cybercriminel",
               "cybercriminal", "extorsion", "extortion", "attaquants", "attackers", "hackers", "state-sponsored",
               "TTP", "IOC", "indicateurs de compromission", "C2", "spyware", "logiciel espion", "arnaque", "scam",
               "fraude", "fraud", "social engineering", "ingénierie sociale"],
    "vulnerabilite": ["vulnérabilit", "vulnerabilit", "CVE", "faille", "flaw", "correctif", "patch",
                      "security update", "mise à jour de sécurité", "avis de sécurité", "security advisory",
                      "advisory", "zero-day", "0-day", "RCE", "exécution de code", "code execution",
                      "injection", "contournement", "bypass", "élévation de privilèges", "privilege escalation",
                      "elevation of privilege", "buffer overflow", "débordement de tampon", "KEV", "USN",
                      "DSA", "exploited", "exploitée", "exploitation", "proof of concept", "PoC", "spoofing",
                      "denial of service", "déni de service", "security notice"],
    "technologie": ["intelligence artificielle", "artificial intelligence", "IA", "AI", "machine learning",
                    "apprentissage automatique", "LLM", "générative", "generative", "agentic", "agentique",
                    "agents IA", "AI agent", "post-quantique", "post-quantum", "PQC", "quantique", "quantum",
                    "zero trust", "SOAR", "SIEM", "EDR", "XDR", "NDR", "SBOM", "DevSecOps", "conteneur",
                    "container", "Kubernetes", "cloud", "passkey", "FIDO", "MFA", "authentification",
                    "authentication", "identity", "identité", "IAM", "cryptograph", "chiffrement", "encryption",
                    "secrets management", "gestion des secrets", "supply chain", "chaîne d'approvisionnement",
                    "introducing", "announcing", "nouvelle fonctionnalité", "new feature", "innovation",
                    "detection engineering", "ingénierie de détection", "memory safety", "Rust", "eBPF",
                    "confidential computing", "observability", "automatisation", "automation"],
    "reglementaire": ["règlement", "regulation", "directive", "loi ", "projet de loi", "décret", "ordonnance n", "arrêté du", "arrêté ministériel",
                      "legislation", "législation", "sanction", "amende", "fine ", "fines ", "fined", "CNIL", "EDPB",
                      "Journal officiel", "Official Journal", "consultation publique", "public consultation",
                      "lignes directrices", "guidelines", "transposition", "conformité", "compliance", "RGPD",
                      "GDPR", "NIS2", "NIS 2", "DORA", "AI Act", "Cyber Resilience Act", "eIDAS", "Data Act",
                      "data protection", "protection des données", "données personnelles",
                      "données à caractère personnel", "juridique", "legal", "autorité de contrôle",
                      "supervisory authority", "CELEX", "délibération", "mise en demeure", "omnibus",
                      "acte d'exécution", "implementing act", "delegated act", "acte délégué"],
    "normative": ["ISO", "IEC", "norme", "standard", "NIST SP", "SP 800", "FIPS", "CSF", "Cybersecurity Framework",
                  "référentiel", "framework", "certification", "SecNumCloud", "PCI DSS", "guide de l'ANSSI",
                  "guide ANSSI", "qualification", "SLSA", "OpenSSF Scorecard", "benchmark CIS", "CIS Controls",
                  "draft", "projet de norme", "édition", "edition", "révision", "revision", "public comment"],
    "bonne_pratique": ["recommandation", "recommend", "bonnes pratiques", "bonne pratique", "best practice",
                       "guide", "guidance", "durcissement", "hardening", "conseils", "tips", "mitigation",
                       "atténuation", "checklist", "sensibilisation", "awareness", "comment se protéger",
                       "how to protect", "how to", "secure configuration", "configuration sécurisée",
                       "mesures de sécurité", "security measures", "hygiène"],
    "incident": ["incident", "fuite de données", "data breach", "breach", "compromission", "compromised",
                 "piratage", "hacked", "cyberattaque", "cyberattack", "victime", "victim", "leak", "fuite",
                 "exposed", "outage", "panne", "retour d'expérience", "post-mortem", "lessons learned", "DFIR",
                 "intrusion", "revendique", "claims", "stolen", "volé", "dérobé", "notification de violation"],
}
NOISE = ["webinar", "webinaire", "podcast", "sponsored", "partenaire", "giveaway", "deal", "promo", "hiring",
         "recrutement", "job ", "replay", "week in review", "newsletter", "conference", "keynote", "call for papers",
         "appel à communications", "anniversary", "award"]

IMPACT_KEYWORDS = {
    "confidentialite": ["fuite", "leak", "exfiltr", "divulgation", "disclosure", "information disclosure",
                        "data breach", "espionnage", "espionage", "vol de données", "data theft", "credential",
                        "identifiants", "mot de passe", "password", "confidentialité", "confidentiality",
                        "lecture arbitraire", "arbitrary file read", "données personnelles", "infostealer",
                        "stealer", "spyware", "logiciel espion", "sensitive data", "données sensibles"],
    "integrite": ["exécution de code", "code execution", "RCE", "injection", "tampering", "falsification",
                  "élévation de privilèges", "privilege escalation", "elevation of privilege", "contournement",
                  "bypass", "usurpation", "spoofing", "intégrité", "integrity", "supply chain",
                  "chaîne d'approvisionnement", "arbitrary file write", "écriture arbitraire", "backdoor",
                  "porte dérobée", "modification", "rançongiciel", "ransomware", "cross-site", "XSS", "CSRF"],
    "disponibilite": ["déni de service", "denial of service", "DoS", "DDoS", "rançongiciel", "ransomware",
                      "wiper", "crash", "panne", "outage", "disponibilité", "availability", "interruption",
                      "plantage", "chiffrement des données", "destruct", "sabotage"],
}

THEMES = {
    "ia_generative": ("Intelligence artificielle et IA générative",
                      ["intelligence artificielle", "artificial intelligence", "IA", "AI", "LLM", "générative",
                       "generative", "GenAI", "agentic", "agentique", "AI agent", "agents IA", "prompt injection",
                       "injection de prompt", "chatbot", "ChatGPT", "Claude", "Gemini", "Copilot", "MCP"]),
    "ia_cybersecurite": ("Machine learning appliqué à la cybersécurité",
                         ["machine learning", "apprentissage automatique", "AI-powered", "AI-driven", "anomaly detection",
                          "détection d'anomalies", "AI for security", "IA pour la cybersécurité", "AI-assisted",
                          "model-based detection", "behavioral analytics"]),
    "soar": ("Automatisation de la sécurité et SOAR",
             ["SOAR", "automatisation", "automation", "playbook", "orchestration", "auto-remediation",
              "remédiation automatique"]),
    "siem_edr_xdr": ("SIEM, EDR, XDR, détection et réponse aux incidents",
                     ["SIEM", "EDR", "XDR", "NDR", "MDR", "SOC", "detection", "détection", "threat hunting",
                      "chasse aux menaces", "incident response", "réponse aux incidents", "Sigma", "YARA", "telemetry"]),
    "zero_trust_iam": ("Zero Trust, IAM, MFA et gestion des identités",
                       ["zero trust", "IAM", "MFA", "multi-factor", "multifacteur", "passkey", "FIDO", "identity",
                        "identité", "authentification", "authentication", "SSO", "OAuth", "Entra", "Active Directory",
                        "PAM", "privileged access", "accès à privilèges"]),
    "cloud_conteneurs": ("Sécurité du cloud, des conteneurs et de la chaîne logicielle",
                         ["cloud", "AWS", "Azure", "GCP", "Kubernetes", "conteneur", "container", "Docker",
                          "serverless", "CNAPP", "CSPM", "supply chain", "chaîne d'approvisionnement",
                          "chaîne logicielle", "workload identity"]),
    "post_quantique": ("Cryptographie, post-quantique et gestion des secrets",
                       ["post-quantique", "post-quantum", "PQC", "quantique", "quantum", "ML-KEM", "ML-DSA",
                        "Kyber", "cryptograph", "chiffrement", "encryption", "TLS", "certificat", "certificate",
                        "secrets management", "gestion des secrets", "HSM", "key management", "gestion des clés"]),
    "devsecops_sbom": ("DevSecOps, SBOM et sécurité des dépendances",
                       ["DevSecOps", "SBOM", "dependency", "dépendance", "open source", "npm", "PyPI", "crates.io",
                        "package", "paquet", "SLSA", "Scorecard", "SAST", "DAST", "CI/CD", "pipeline",
                        "secret scanning", "code scanning", "memory safety", "Rust"]),
    "detection_remediation": ("Nouvelles méthodes de détection, de prévention et de remédiation",
                              ["detection engineering", "ingénierie de détection", "remédiation", "remediation",
                               "prevention", "prévention", "mitigation", "atténuation", "durcissement",
                               "hardening", "eBPF", "deception", "leurre", "honeypot", "exposure management",
                               "gestion de l'exposition", "attack surface", "surface d'attaque"]),
}

COMMON_PRODUCTS = [
    "Microsoft", "Windows", "Exchange", "SharePoint", "Office", "Outlook", "Teams", "Azure", "Entra ID", "Edge",
    "Apple", "iOS", "macOS", "Safari", "Android", "Google Chrome", "Chrome", "Chromium", "Firefox", "Thunderbird",
    "Linux", "Linux kernel", "noyau Linux", "Ubuntu", "Debian", "Red Hat", "RHEL", "SUSE", "Cisco", "IOS XE",
    "Fortinet", "FortiOS", "FortiGate", "FortiWeb", "FortiProxy", "FortiManager", "Palo Alto", "PAN-OS",
    "GlobalProtect", "Ivanti", "Citrix", "NetScaler", "VMware", "ESXi", "vCenter", "Oracle", "Java", "SAP",
    "Adobe", "Acrobat", "Apache", "Tomcat", "Nginx", "PHP", "OpenSSL", "OpenSSH", "Jenkins", "GitLab", "GitHub",
    "Atlassian", "Confluence", "Jira", "WordPress", "Drupal", "Joomla", "SonicWall", "Juniper", "Junos", "F5",
    "BIG-IP", "Veeam", "Zimbra", "Kubernetes", "Docker", "PostgreSQL", "MySQL", "MariaDB", "Redis", "Elastic",
    "Splunk", "Synology", "QNAP", "Zyxel", "MOVEit", "Progress", "Tenable", "IBM", "HPE", "Aruba", "Dell",
    "Siemens", "Schneider Electric", "Rockwell", "Hitachi Energy", "Mitsubishi Electric", "Moxa", "Node.js",
    "Python", "npm", "Grafana", "Wazuh", "Keycloak", "Okta", "SolarWinds", "Sophos", "Check Point", "WatchGuard",
    "Trend Micro", "ConnectWise", "ScreenConnect", "Veritas", "Commvault", "Nextcloud", "Roundcube", "Samba",
    "Kerberos", "Active Directory", "Brotli", "glibc", "sudo", "Tor", "Mozilla", "Thunderbird", "Zoom", "Slack",
]


def _compile(term: str) -> re.Pattern:
    t = term.strip()
    is_acronym = t.isupper() or any(ch.isdigit() for ch in t) and t.upper() == t
    esc = re.escape(t)
    if is_acronym:
        return re.compile(rf"(?<![\w-]){esc}s?(?![\w])")
    return re.compile(rf"(?<![\w]){esc}", re.IGNORECASE)


@lru_cache(maxsize=4096)
def pattern(term: str) -> re.Pattern:
    return _compile(term)


def find_terms(text: str, terms: list[str]) -> list[str]:
    return [t for t in terms if pattern(t).search(text)]


def match_exact_word(text: str, term: str) -> bool:
    """Recherche d'un nom de produit comme mot entier (insensible à la casse)."""
    return re.search(rf"(?<![\w-]){re.escape(term)}(?![\w])", text, re.IGNORECASE) is not None


SOURCE_HINTS = [
    (re.compile(r"vulnérabilit|correctif|alerte", re.I), "vulnerabilite"),
    (re.compile(r"menace|renseignement", re.I), "menace"),
    (re.compile(r"incident|retours? d'expérience", re.I), "incident"),
    (re.compile(r"recommandation|synthèse|sensibilisation", re.I), "bonne_pratique"),
]
CATEGORY_HINTS = {"reglementaire": "reglementaire", "normative": "normative", "technologique": "technologie"}


def classify(title: str, summary: str, source: dict | None = None) -> dict:
    """Renvoie {categories, principale, scores, declencheurs, themes, bruit}."""
    source = source or {}
    text = f"{title}\n{summary}"
    scores: dict[str, float] = {}
    triggers: dict[str, list[str]] = {}
    for cat, kws in KEYWORDS.items():
        in_title = find_terms(title, kws)
        in_text = find_terms(text, kws)
        s = len(in_text) + len(in_title)  # mot présent dans le titre : compte double
        if s:
            scores[cat] = float(s)
            triggers[cat] = in_text[:10]
    hint_cat = CATEGORY_HINTS.get(source.get("categorie") or source.get("source_categorie") or "")
    if hint_cat:
        scores[hint_cat] = scores.get(hint_cat, 0) + 2
        triggers.setdefault(hint_cat, []).append("catégorie de la source")
    sub = source.get("sous_categorie") or ""
    for rx, cat in SOURCE_HINTS:
        if rx.search(sub):
            scores[cat] = scores.get(cat, 0) + 2
            triggers.setdefault(cat, []).append(f"type de source : {sub}")
            break
    if source.get("type") == "cisa_kev" or source.get("source_type") == "cisa_kev":
        scores["vulnerabilite"] = scores.get("vulnerabilite", 0) + 5
        triggers.setdefault("vulnerabilite", []).append("catalogue KEV")
    if source.get("type") == "iso_opendata" or source.get("source_type") == "iso_opendata":
        scores["normative"] = scores.get("normative", 0) + 5
        triggers.setdefault("normative", []).append("métadonnées ISO")
    noise = find_terms(title, NOISE)
    if noise:
        for k in scores:
            scores[k] -= 2
    ranked = sorted(((c, s) for c, s in scores.items() if s >= 2), key=lambda x: -x[1])
    if not ranked:
        cats = ["non_pertinent"]
    else:
        top = ranked[0][1]
        cats = [c for c, s in ranked if s >= max(2, top * 0.4)][:3]
    themes = [k for k, (_, kws) in THEMES.items() if find_terms(text, kws)]
    return {"categories": cats, "principale": cats[0], "scores": scores, "declencheurs": triggers,
            "themes": themes, "bruit": noise}


def detect_impacts(text: str, categories: list[str]) -> dict[str, list[str]]:
    out = {k: find_terms(text, kws)[:5] for k, kws in IMPACT_KEYWORDS.items()}
    out = {k: v for k, v in out.items() if v}
    if "reglementaire" in categories or "normative" in categories:
        out["conformite"] = ["évolution réglementaire ou normative"]
    else:
        strong = find_terms(text, ["RGPD", "GDPR", "NIS2", "NIS 2", "DORA", "notification de violation", "data breach notification",
                                   "sanction", "amende", "données personnelles", "personal data"])
        if strong:
            out["conformite"] = strong[:3]
    return out


def match_inventory(text: str, technologies: list[dict], extra_terms: list[str] | None = None) -> list[dict]:
    """Technologies du parc citées dans le texte (ou dans les champs produit/fournisseur du KEV)."""
    haystack = text + "\n" + " ".join(extra_terms or [])
    matches = []
    for t in technologies:
        hits = [k for k in t.get("mots_cles", []) if match_exact_word(haystack, k)]
        if not hits:
            continue
        versions = [v for v in t.get("versions", []) if v and match_exact_word(haystack, v)]
        matches.append({"nom": t["nom"], "mots": hits, "versions_citees": versions,
                        "versions_parc": t.get("versions", []), "exposition": t.get("exposition", "inconnue"),
                        "criticite": t.get("criticite", "moyenne")})
    return matches


def products_cited(text: str, extra: list[str] | None = None) -> list[str]:
    found = [p for p in COMMON_PRODUCTS if match_exact_word(text, p)]
    for e in extra or []:
        if e and e not in found:
            found.append(e)
    # supprime les doublons inclus (« Chrome » si « Google Chrome »)
    return [p for p in found if not any(p != q and p.lower() in q.lower() for q in found)][:15]
