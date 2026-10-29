"""Client HTTP sécurisé pour la collecte.

Garanties :
- seules les URL http(s) dont l'hôte appartient à la liste blanche (domaines des sources configurées
  + API d'enrichissement) sont interrogées ;
- l'adresse IP résolue doit être publique (protection SSRF : refus de 127.0.0.0/8, 10/8, 172.16/12,
  192.168/16, 169.254/16 dont les métadonnées cloud, IPv6 locales, etc.) ;
- chaque redirection est revalidée ; taille de réponse et délai bornés ;
- robots.txt respecté (configurable), délai minimal entre deux requêtes vers un même hôte ;
- reprises avec temporisation exponentielle sur erreurs transitoires (réseau, 429, 5xx) ;
- requêtes conditionnelles (ETag / Last-Modified) pour limiter la charge sur les sources.
"""
from __future__ import annotations

import ipaddress
import logging
import socket
import time
import urllib.robotparser
from dataclasses import dataclass, field
from typing import Callable
from urllib.parse import urljoin, urlsplit

import httpx

log = logging.getLogger("veille.net")

MAX_REDIRECTS = 5
NAT64_WKP = ipaddress.ip_network("64:ff9b::/96")


class BlockedRequest(Exception):
    """Requête refusée par la politique de sécurité (hôte non autorisé, IP interne, robots.txt...)."""


class FetchError(Exception):
    def __init__(self, message: str, status: int | None = None, transient: bool = False):
        super().__init__(message)
        self.status = status
        self.transient = transient


@dataclass
class FetchResult:
    url: str
    final_url: str
    status: int
    content: bytes = b""
    headers: dict = field(default_factory=dict)
    not_modified: bool = False
    elapsed_ms: int = 0


def host_allowed(host: str, allowed: set[str]) -> bool:
    host = (host or "").lower().rstrip(".")
    for dom in allowed:
        dom = dom.lower().lstrip(".")
        if host == dom or host.endswith("." + dom):
            return True
    return False


def ip_is_public(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return False
    if isinstance(addr, ipaddress.IPv6Address):
        if addr.ipv4_mapped:
            addr = addr.ipv4_mapped
        elif addr in NAT64_WKP:
            # Réseau NAT64/DNS64 : l'adresse réelle de destination est l'IPv4 embarquée (RFC 6052)
            addr = ipaddress.IPv4Address(int(addr) & 0xFFFFFFFF)
    return addr.is_global and not (addr.is_private or addr.is_loopback or addr.is_link_local
                                   or addr.is_multicast or addr.is_reserved or addr.is_unspecified)


Resolver = Callable[[str], list[str]]


def default_resolver(host: str) -> list[str]:
    infos = socket.getaddrinfo(host, None, proto=socket.IPPROTO_TCP)
    return sorted({info[4][0] for info in infos})


class SafeFetcher:
    def __init__(
        self,
        allowed_domains: set[str],
        user_agent: str = "VeilleCyber/1.0",
        timeout: float = 20.0,
        max_bytes: int = 20_000_000,
        retries: int = 3,
        min_delay_same_host: float = 1.0,
        respect_robots: bool = True,
        resolver: Resolver | None = None,
        transport: httpx.BaseTransport | None = None,
        sleep: Callable[[float], None] = time.sleep,
        host_delays: dict[str, float] | None = None,
    ) -> None:
        self.allowed = {d.lower() for d in allowed_domains if d}
        self.user_agent = user_agent
        self.timeout = timeout
        self.max_bytes = max_bytes
        self.retries = max(1, retries)
        self.min_delay = min_delay_same_host
        self.respect_robots = respect_robots
        self.resolver = resolver or default_resolver
        self.sleep = sleep
        self.host_delays = {k.lower(): v for k, v in (host_delays or {}).items()}
        self._last_hit: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}
        self._crawl_delay: dict[str, float] = {}
        self.client = httpx.Client(
            timeout=httpx.Timeout(timeout, connect=min(10.0, timeout)),
            follow_redirects=False,  # redirections suivies manuellement pour revalider chaque saut
            headers={"User-Agent": user_agent, "Accept-Encoding": "gzip, deflate"},
            transport=transport,
            trust_env=False,  # n'utilise pas de proxy implicite de l'environnement
        )

    # ------------------------------------------------------------------ validation
    def check_url(self, url: str) -> None:
        try:
            parts = urlsplit(url)
        except ValueError as exc:
            raise BlockedRequest(f"URL invalide : {exc}") from exc
        if parts.scheme not in ("http", "https"):
            raise BlockedRequest(f"Schéma non autorisé : {parts.scheme or '(vide)'}")
        if parts.username or parts.password:
            raise BlockedRequest("Identifiants dans l'URL refusés")
        host = parts.hostname or ""
        if not host:
            raise BlockedRequest("Hôte absent")
        if parts.port not in (None, 80, 443):
            raise BlockedRequest(f"Port non autorisé : {parts.port}")
        try:
            ipaddress.ip_address(host)
            raise BlockedRequest("Adresse IP littérale refusée : utiliser un nom de domaine de la liste blanche")
        except ValueError:
            pass
        if not host_allowed(host, self.allowed):
            raise BlockedRequest(f"Hôte hors liste blanche des sources configurées : {host}")
        try:
            ips = self.resolver(host)
        except OSError as exc:
            raise FetchError(f"Résolution DNS impossible pour {host} : {exc}", transient=True) from exc
        if not ips:
            raise FetchError(f"Aucune adresse pour {host}", transient=True)
        bad = [ip for ip in ips if not ip_is_public(ip)]
        if bad:
            raise BlockedRequest(f"{host} résout vers une adresse non publique ({', '.join(bad)}) : requête bloquée")

    # ------------------------------------------------------------------ politesse
    def _throttle(self, host: str) -> None:
        delay = max(self.min_delay, self.host_delays.get(host, 0.0), min(self._crawl_delay.get(host, 0.0), 60.0))
        last = self._last_hit.get(host)
        if last is not None:
            wait = delay - (time.monotonic() - last)
            if wait > 0:
                self.sleep(wait)
        self._last_hit[host] = time.monotonic()

    def _robots_allows(self, url: str) -> bool:
        if not self.respect_robots:
            return True
        parts = urlsplit(url)
        host = parts.hostname or ""
        key = f"{parts.scheme}://{parts.netloc}"
        if key not in self._robots:
            rp: urllib.robotparser.RobotFileParser | None = urllib.robotparser.RobotFileParser()
            try:
                robots_url = key + "/robots.txt"
                for _ in range(MAX_REDIRECTS):
                    res = self._get_once(robots_url, {}, 500_000)
                    if res.status in (301, 302, 303, 307, 308) and res.headers.get("location"):
                        robots_url = urljoin(robots_url, res.headers["location"])
                        continue
                    break
                if res.status == 200:
                    rp.parse(res.content.decode("utf-8", "replace").splitlines())
                    cd = rp.crawl_delay(self.user_agent)
                    if cd:
                        self._crawl_delay[host] = float(cd)
                elif 400 <= res.status < 500:
                    rp = None  # pas de robots.txt : tout est autorisé
                elif res.status >= 500:
                    rp.disallow_all = True  # erreur serveur : abstention prudente (RFC 9309)
                else:
                    rp = None
            except (FetchError, BlockedRequest, httpx.HTTPError):
                rp = None  # robots.txt injoignable : on n'empêche pas la collecte, la requête suivante échouera le cas échéant
            self._robots[key] = rp
        rp = self._robots[key]
        return True if rp is None else rp.can_fetch(self.user_agent, url)

    # ------------------------------------------------------------------ requêtes
    def _get_once(self, url: str, headers: dict, max_bytes: int) -> FetchResult:
        self.check_url(url)
        host = urlsplit(url).hostname or ""
        self._throttle(host)
        start = time.monotonic()
        try:
            with self.client.stream("GET", url, headers=headers) as resp:
                declared = resp.headers.get("content-length")
                if declared and declared.isdigit() and int(declared) > max_bytes:
                    raise FetchError(f"Réponse trop volumineuse ({declared} octets > {max_bytes})")
                buf = bytearray()
                for chunk in resp.iter_bytes():
                    buf.extend(chunk)
                    if len(buf) > max_bytes:
                        raise FetchError(f"Réponse tronquée : dépasse {max_bytes} octets")
                return FetchResult(url=url, final_url=url, status=resp.status_code, content=bytes(buf),
                                   headers=dict(resp.headers), not_modified=resp.status_code == 304,
                                   elapsed_ms=int((time.monotonic() - start) * 1000))
        except httpx.TimeoutException as exc:
            raise FetchError(f"Délai d'attente dépassé ({self.timeout}s)", transient=True) from exc
        except httpx.TransportError as exc:
            raise FetchError(f"Erreur réseau : {type(exc).__name__}", transient=True) from exc

    def fetch(self, url: str, etag: str | None = None, last_modified: str | None = None,
              max_bytes: int | None = None, accept: str | None = None,
              headers: dict | None = None, check_robots: bool = True) -> FetchResult:
        max_bytes = max_bytes or self.max_bytes
        headers = dict(headers or {})
        if accept:
            headers["Accept"] = accept
        if etag:
            headers["If-None-Match"] = etag
        if last_modified:
            headers["If-Modified-Since"] = last_modified

        if check_robots and not self._robots_allows(url):
            raise BlockedRequest("Collecte interdite par le fichier robots.txt de la source")

        last_exc: Exception | None = None
        for attempt in range(1, self.retries + 1):
            try:
                current = url
                for _ in range(MAX_REDIRECTS + 1):
                    try:
                        res = self._get_once(current, headers, max_bytes)
                    except BlockedRequest as exc:
                        if current != url:
                            raise BlockedRequest(
                                f"Redirection de {urlsplit(url).hostname} vers {urlsplit(current).hostname} refusée ({exc}). "
                                "Si cette redirection est légitime, mettre à jour l'URL de la source.") from exc
                        raise
                    if res.status in (301, 302, 303, 307, 308):
                        loc = res.headers.get("location")
                        if not loc:
                            raise FetchError("Redirection sans destination", res.status)
                        current = urljoin(current, loc)
                        continue
                    break
                else:
                    raise FetchError("Trop de redirections")
                res.url = url
                res.final_url = current
                if res.status == 429 or res.status >= 500:
                    retry_after = res.headers.get("retry-after", "")
                    wait = float(retry_after) if retry_after.isdigit() else 2 ** attempt
                    last_exc = FetchError(f"HTTP {res.status}", res.status, transient=True)
                    if attempt < self.retries:
                        self.sleep(min(wait, 30.0))
                        continue
                    raise last_exc
                if res.status >= 400:
                    raise FetchError(f"HTTP {res.status}", res.status, transient=False)
                return res
            except FetchError as exc:
                last_exc = exc
                if not exc.transient or attempt >= self.retries:
                    raise
                log.warning("Tentative %s/%s échouée pour %s : %s", attempt, self.retries, urlsplit(url).hostname, exc)
                self.sleep(min(2 ** attempt, 30.0))
        raise last_exc or FetchError("Échec inconnu")  # pragma: no cover

    def close(self) -> None:
        self.client.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()
