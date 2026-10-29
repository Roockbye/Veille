import httpx
import pytest

from tests.conftest import make_fetcher
from veille.net import BlockedRequest, FetchError, ip_is_public

ALLOWED = {"feeds.test", "other.test"}


@pytest.mark.parametrize("ip,expected", [
    ("8.8.8.8", True), ("127.0.0.1", False), ("10.1.2.3", False), ("172.16.0.1", False), ("192.168.1.1", False),
    ("169.254.169.254", False), ("::1", False), ("fe80::1", False), ("fc00::1", False), ("::ffff:10.0.0.1", False),
    ("64:ff9b::808:808", True), ("64:ff9b::7f00:1", False), ("0.0.0.0", False),
])
def test_ip_is_public(ip, expected):
    assert ip_is_public(ip) is expected


def test_hote_hors_liste_blanche_refuse():
    f = make_fetcher({}, ALLOWED)
    with pytest.raises(BlockedRequest, match="liste blanche"):
        f.fetch("https://evil.test/feed")


@pytest.mark.parametrize("url", ["file:///etc/passwd", "ftp://feeds.test/x", "https://127.0.0.1/x",
                                 "https://user:pass@feeds.test/x", "https://feeds.test:8080/x", "gopher://feeds.test/"])
def test_urls_dangereuses_refusees(url):
    with pytest.raises(BlockedRequest):
        make_fetcher({}, ALLOWED).fetch(url)


@pytest.mark.parametrize("ip", ["127.0.0.1", "10.0.0.5", "169.254.169.254", "::1", "64:ff9b::a00:1"])
def test_resolution_vers_ip_interne_bloquee(ip):
    f = make_fetcher({"/feed": (200, "ok")}, ALLOWED, resolver=lambda h: [ip])
    with pytest.raises(BlockedRequest, match="non publique"):
        f.fetch("https://feeds.test/feed")


def test_redirection_vers_hote_non_autorise_bloquee():
    f = make_fetcher({"/feed": (302, "", {"location": "https://evil.test/x"})}, ALLOWED)
    with pytest.raises(BlockedRequest, match="Redirection"):
        f.fetch("https://feeds.test/feed")


def test_redirection_vers_ip_interne_bloquee():
    f = make_fetcher({"/feed": (302, "", {"location": "https://other.test/x"})}, ALLOWED,
                     resolver=lambda h: ["10.0.0.1"] if h == "other.test" else ["93.184.216.34"])
    with pytest.raises(BlockedRequest):
        f.fetch("https://feeds.test/feed")


def test_redirection_autorisee_suivie():
    f = make_fetcher({"/feed": (301, "", {"location": "https://other.test/new"}), "/new": (200, "contenu")}, ALLOWED)
    res = f.fetch("https://feeds.test/feed")
    assert res.status == 200 and res.content == b"contenu" and res.final_url == "https://other.test/new"


def test_limite_de_taille():
    f = make_fetcher({"/big": (200, b"x" * 5000)}, ALLOWED, max_bytes=1000)
    with pytest.raises(FetchError, match="octets"):
        f.fetch("https://feeds.test/big")


def test_reprise_sur_erreur_transitoire():
    calls = {"n": 0}

    def flaky(request):
        calls["n"] += 1
        return httpx.Response(503) if calls["n"] < 3 else httpx.Response(200, content=b"ok")

    res = make_fetcher({"/f": flaky}, ALLOWED, retries=3).fetch("https://feeds.test/f")
    assert res.content == b"ok" and calls["n"] == 3


def test_erreur_definitive_sans_reprise():
    calls = {"n": 0}

    def gone(request):
        calls["n"] += 1
        return httpx.Response(404)

    with pytest.raises(FetchError) as e:
        make_fetcher({"/f": gone}, ALLOWED, retries=3).fetch("https://feeds.test/f")
    assert e.value.status == 404 and calls["n"] == 1


def test_delai_depasse_est_transitoire():
    def timeout(request):
        raise httpx.ReadTimeout("lent", request=request)

    with pytest.raises(FetchError) as e:
        make_fetcher({"/f": timeout}, ALLOWED, retries=2).fetch("https://feeds.test/f")
    assert e.value.transient


def test_requete_conditionnelle_304():
    def cond(request):
        assert request.headers.get("if-none-match") == '"abc"'
        return httpx.Response(304)

    res = make_fetcher({"/f": cond}, ALLOWED).fetch("https://feeds.test/f", etag='"abc"')
    assert res.not_modified


def test_robots_txt_respecte():
    routes = {"/robots.txt": (200, "User-agent: *\nDisallow: /prive\n"), "/prive/feed": (200, "x"), "/public": (200, "ok")}
    f = make_fetcher(routes, ALLOWED, respect_robots=True)
    with pytest.raises(BlockedRequest, match="robots"):
        f.fetch("https://feeds.test/prive/feed")
    assert f.fetch("https://feeds.test/public").content == b"ok"


def test_robots_txt_redirige_est_suivi():
    routes = {"https://feeds.test/robots.txt": (302, "", {"location": "https://other.test/robots.txt"}),
              "https://other.test/robots.txt": (200, "User-agent: *\nDisallow: /pdf\n"), "/feed": (200, "ok")}
    f = make_fetcher(routes, ALLOWED, respect_robots=True)
    assert f.fetch("https://feeds.test/feed").content == b"ok"


def test_robots_absent_autorise():
    f = make_fetcher({"/feed": (200, "ok")}, ALLOWED, respect_robots=True)
    assert f.fetch("https://feeds.test/feed").content == b"ok"
