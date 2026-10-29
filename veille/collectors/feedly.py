"""Connecteur Feedly (API officielle, facultatif).

- Authentification uniquement par jeton d'accès (variable d'environnement FEEDLY_ACCESS_TOKEN) ;
  aucun mot de passe n'est demandé ni stocké, le jeton n'est jamais journalisé.
- L'accès à l'API dépend de l'offre Feedly de l'utilisateur : sans jeton, le connecteur signale
  « non configuré » et l'application fonctionne avec ses propres flux RSS.
- Alternative sans API : export OPML des abonnements (voir veille.sources.parse_opml).
"""
from __future__ import annotations

import json
from urllib.parse import urlencode

from veille.collectors import CollectorError, NotConfigured
from veille.config import env
from veille.net import FetchError, SafeFetcher
from veille.normalize import clean_title, html_to_text, iso, safe_http_url
from datetime import datetime, timezone

API = "https://cloud.feedly.com/v3"


def collect_feedly(fetcher: SafeFetcher, max_items: int = 100) -> list[dict]:
    token = env("FEEDLY_ACCESS_TOKEN")
    if not token:
        raise NotConfigured("Jeton Feedly non configuré (FEEDLY_ACCESS_TOKEN). Voir docs/FEEDLY.md.")
    scheme = env("FEEDLY_AUTH_SCHEME") or "Bearer"  # « OAuth » selon la documentation historique de Feedly
    if scheme not in ("Bearer", "OAuth"):
        scheme = "Bearer"
    headers = {"Authorization": f"{scheme} {token}", "Accept": "application/json"}
    stream = env("FEEDLY_STREAM_ID")
    try:
        if not stream:
            prof = fetcher.fetch(f"{API}/profile", headers=headers, check_robots=False)
            user_id = json.loads(prof.content).get("id")
            if not user_id:
                raise CollectorError("Profil Feedly sans identifiant : définir FEEDLY_STREAM_ID.")
            stream = f"user/{user_id}/category/global.all"
        url = f"{API}/streams/contents?" + urlencode({"streamId": stream, "count": min(max_items, 250), "ranked": "newest"})
        res = fetcher.fetch(url, headers=headers, check_robots=False)
    except FetchError as exc:
        if exc.status in (401, 403):
            raise CollectorError("Accès Feedly refusé (jeton invalide, expiré ou offre sans accès API).") from exc
        raise
    try:
        data = json.loads(res.content)
    except ValueError as exc:
        raise CollectorError("Réponse Feedly illisible") from exc
    return parse_stream(data)


def parse_stream(data: dict) -> list[dict]:
    items = []
    for e in data.get("items", []):
        url = ""
        for alt in e.get("alternate") or []:
            url = safe_http_url(alt.get("href", ""))
            if url:
                break
        url = url or safe_http_url(e.get("canonicalUrl", "")) or safe_http_url(e.get("originId", ""))
        title = clean_title(e.get("title") or "")
        if not url or not title:
            continue
        body = (e.get("summary") or {}).get("content") or (e.get("content") or {}).get("content") or ""
        published = None
        if isinstance(e.get("published"), (int, float)):
            published = datetime.fromtimestamp(e["published"] / 1000, tz=timezone.utc)
        origin = (e.get("origin") or {}).get("title")
        items.append({
            "url": url, "titre": title, "auteur": (e.get("author") or None),
            "resume_source": html_to_text(body, 3000), "publie_le": iso(published),
            "langue": e.get("language"), "origine": f"Feedly — {origin}" if origin else "Feedly",
            "donnees": None,
        })
    return items
