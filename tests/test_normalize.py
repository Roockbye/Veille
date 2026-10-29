from veille.normalize import canonical_url, content_hash, html_to_text, parse_date, safe_http_url


def test_canonical_url_supprime_suivi_et_fragment():
    a = canonical_url("http://www.Example.com/Article/?utm_source=rss&id=3&fbclid=x#section")
    b = canonical_url("https://example.com/Article?id=3")
    assert a == b == "https://example.com/Article?id=3"


def test_canonical_url_trie_les_parametres():
    assert canonical_url("https://a.test/p?b=2&a=1") == canonical_url("https://a.test/p?a=1&b=2")


def test_empreinte_insensible_casse_et_accents():
    assert content_hash("Vulnérabilité CRITIQUE", "Texte") == content_hash("vulnerabilite critique", "texte")
    assert content_hash("A", "x") != content_hash("B", "x")


def test_html_to_text_supprime_scripts_et_balises():
    t = html_to_text("<p>Bonjour <b>monde</b></p><script>alert('x')</script><style>p{}</style>")
    assert "Bonjour monde" in t and "alert" not in t and "<" not in t


def test_html_to_text_tronque():
    assert len(html_to_text("mot " * 5000, max_len=100)) < 120


def test_safe_http_url_refuse_schemas_dangereux():
    assert safe_http_url("javascript:alert(1)") == ""
    assert safe_http_url("data:text/html,x") == ""
    assert safe_http_url("file:///etc/passwd") == ""
    assert safe_http_url("https://ok.test/a") == "https://ok.test/a"


def test_parse_date_formats():
    assert parse_date("2026-10-27").year == 2026
    assert parse_date("2026-10-27T10:00:00Z").tzinfo is not None
    assert parse_date("pas une date") is None
