"""Configuration des tests : base temporaire, réseau simulé (aucun accès Internet pendant les tests)."""
import sys
from pathlib import Path

import httpx
import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
FIXTURES = Path(__file__).parent / "fixtures"


@pytest.fixture(autouse=True)
def isolated_data(tmp_path, monkeypatch):
    monkeypatch.setenv("VEILLE_DATA_DIR", str(tmp_path / "data"))
    for var in ("FEEDLY_ACCESS_TOKEN", "ANTHROPIC_API_KEY", "NVD_API_KEY", "SMTP_HOST"):
        monkeypatch.delenv(var, raising=False)
    yield


@pytest.fixture
def storage(tmp_path):
    from veille.storage import Storage
    s = Storage(tmp_path / "test.db")
    s.init_db()
    return s


def public_resolver(host):
    return ["93.184.216.34"]


def make_fetcher(routes: dict, allowed: set, resolver=public_resolver, **kw):
    """routes : {url_ou_chemin: (status, body, headers)} ; un callable peut aussi être fourni."""
    from veille.net import SafeFetcher

    def handler(request: httpx.Request):
        url = str(request.url)
        key = url if url in routes else request.url.path
        if key not in routes:
            return httpx.Response(404, content=b"not found")
        r = routes[key]
        if callable(r):
            return r(request)
        status, body, headers = (r + ({},))[:3] if len(r) == 2 else r
        return httpx.Response(status, content=body if isinstance(body, bytes) else body.encode(), headers=headers)

    kw.setdefault("sleep", lambda s: None)
    kw.setdefault("respect_robots", False)
    return SafeFetcher(allowed, transport=httpx.MockTransport(handler), resolver=resolver, **kw)


@pytest.fixture
def profil():
    from veille.organisation import load_demo_profile
    return load_demo_profile()


def fixture_bytes(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()
