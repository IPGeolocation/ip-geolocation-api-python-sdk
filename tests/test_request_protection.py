import asyncio
import gzip
import json
import logging
import secrets
import threading
import traceback
import zlib
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, quote, urlsplit

import httpx
import pytest

from ipgeolocation import (
    ApiException,
    AsyncIpGeolocationClient,
    BulkLookupIpGeolocationRequest,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    JsonOutputMode,
    Language,
    LookupIpGeolocationRequest,
    RateLimitException,
    SerializationException,
    TransportException,
    to_json,
    to_pretty_json,
)
from ipgeolocation._transport import HttpxAsyncTransport, RequestsHttpTransport


@contextmanager
def server(answer):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            data = self.rfile.read(int(self.headers.get("Content-Length", 0)))
            status, headers, body = answer(self.command, urlsplit(self.path), self.headers, data)
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            for name, value in headers.items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)

        do_POST = do_GET

        def log_message(self, *args):
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as listener:
        thread = threading.Thread(target=listener.serve_forever, kwargs={"poll_interval": 0.01})
        thread.start()
        try:
            yield f"http://127.0.0.1:{listener.server_port}"
        finally:
            listener.shutdown()
            thread.join()


@pytest.fixture(params=["sync", "async"])
def call(request):
    def run(url, method, lookup, *, key="example", limit=128 * 1024 * 1024, follow=False):
        config = IpGeolocationClientConfig(api_key=key, base_url=url)
        if request.param == "sync":
            transport = RequestsHttpTransport(max_response_body_chars=limit)
            try:
                with IpGeolocationClient(config, transport) as client:
                    return getattr(client, method)(lookup)
            finally:
                transport.close()

        async def run_async():
            async with httpx.AsyncClient(follow_redirects=follow, trust_env=False) as http:
                transport = HttpxAsyncTransport(http, max_response_body_chars=limit)
                async with AsyncIpGeolocationClient(config, transport) as client:
                    return await getattr(client, method)(lookup)

        return asyncio.run(run_async())

    return run


def test_config_output_masks_key_and_keeps_authentication_value():
    key = secrets.token_hex(12)
    config = IpGeolocationClientConfig(api_key=key, base_url="https://example.test/" + key)
    assert config.api_key == key
    assert key not in repr(config)
    for dump in (to_json, to_pretty_json):
        for mode in JsonOutputMode:
            text = dump([config], mode)
            assert key not in text
            assert json.loads(text)[0]["api_key"] == "[REDACTED]"


def test_logs_and_api_errors_hide_the_configured_key(call, caplog):
    key = secrets.token_hex(12) + " /+"
    encoded = quote(key, safe="")
    caplog.set_level(logging.DEBUG)

    def respond(method, url, headers, body):
        assert parse_qs(url.query)["apiKey"] == [key]
        return 401, {}, json.dumps({"message": f"denied {key} {encoded}"}).encode()

    with server(respond) as url:
        with pytest.raises(ApiException) as error:
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), key=key)
    assert error.value.status_code == 401
    assert error.value.api_message == "denied [REDACTED] [REDACTED]"
    assert key not in caplog.text and encoded not in caplog.text


def test_connection_error_drops_request_url(call):
    key = secrets.token_hex(12)
    with server(lambda *_: (200, {}, b"{}")) as url:
        pass
    with pytest.raises(TransportException) as error:
        call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), key=key)
    assert key not in "".join(traceback.format_exception(error.value))
    assert error.value.__context__ is None
    assert error.value.__cause__ is None


@pytest.mark.parametrize("status", [307, 308])
def test_cross_origin_redirect_never_replays_bulk_data_or_headers(call, status):
    delivered = []

    def destination(*args):
        delivered.append(args)
        return 200, {}, b"[]"

    with server(destination) as second:
        with server(lambda *_: (status, {"Location": second + "/bulk"}, b"")) as first:
            req = BulkLookupIpGeolocationRequest(ips=["192.0.2.1"], headers={"X-Private": "test"})
            with pytest.raises(ApiException) as error:
                call(first, "bulk_lookup_ip_geolocation", req, follow=True)
    assert error.value.status_code == status
    assert not delivered


@pytest.mark.parametrize(("status", "method"), [(302, "GET"), (307, "POST")])
def test_same_origin_redirect_preserves_method_rules_and_skips_body(call, status, method):
    def respond(actual, url, headers, body):
        if url.path.endswith("ipgeo-bulk"):
            return (
                status,
                {"Location": "/final", "Content-Encoding": "gzip"},
                gzip.compress(b"x" * 65536),
            )
        assert actual == method and headers["X-Trace"] == "retained"
        assert json.loads(body)["ips"] == ["192.0.2.1"] if body else method == "GET"
        return 200, {}, b'[{"ip":"192.0.2.1"}]'

    with server(respond) as url:
        req = BulkLookupIpGeolocationRequest(ips=["192.0.2.1"], headers={"X-Trace": "retained"})
        result = call(url, "bulk_lookup_ip_geolocation", req, limit=32, follow=True)
        assert result.data[0].data.ip == "192.0.2.1"


@pytest.mark.parametrize("mode", ["oversized", "truncated", "invalid-gzip"])
def test_unreadable_error_preserves_status(call, mode):
    cases = {
        "oversized": ({"Content-Encoding": "gzip"}, gzip.compress(b"x" * 100_000)),
        "truncated": ({"Content-Length": "200"}, b'{"message":'),
        "invalid-gzip": ({"Content-Encoding": "gzip"}, b"invalid data"),
    }
    headers, body = cases[mode]
    with server(lambda *_: (429, headers, body)) as url:
        with pytest.raises(RateLimitException) as error:
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), limit=64)
    assert error.value.status_code == 429 and error.value.api_message is None


@pytest.mark.parametrize("diff", [-1, 1])
def test_typed_bulk_rejects_wrong_count_but_raw_returns_original(call, diff):
    rows = json.dumps([{"ip": "192.0.2.1"}] * (2 + diff))
    req = BulkLookupIpGeolocationRequest(ips=["192.0.2.1", "192.0.2.1"])
    with server(lambda *_: (200, {}, rows.encode())) as url:
        with pytest.raises(SerializationException, match="Expected 2 bulk results"):
            call(url, "bulk_lookup_ip_geolocation", req)
        assert call(url, "bulk_lookup_ip_geolocation_raw", req).data == rows


def test_bulk_hides_echoed_key_in_errors_only(call):
    key = secrets.token_hex(12)
    rows = json.dumps([{"message": "denied " + key}, {"ip": "192.0.2.1", "hostname": key}])
    req = BulkLookupIpGeolocationRequest(ips=["invalid", "192.0.2.1"])
    with server(lambda *_: (200, {}, rows.encode())) as url:
        typed = call(url, "bulk_lookup_ip_geolocation", req, key=key).data
        assert typed[0].error.message == "denied [REDACTED]"
        assert typed[1].data.hostname == key
        assert call(url, "bulk_lookup_ip_geolocation_raw", req, key=key).data == rows


def test_arabic_single_and_full_size_bulk_lookup(call):
    city = "الرياض"

    def respond(method, url, headers, body):
        query = parse_qs(url.query)
        assert query["lang"] == ["ar"]
        if method == "POST":
            rows = [{"ip": ip} for ip in json.loads(body)["ips"]]
        else:
            rows = {
                "ip": query["ip"][0],
                "location": {"city": city},
                "network": {"is_cdn": True},
                "security": {
                    "bot_operator_name": "test",
                    "proxy_days_seen_7d": 2,
                    "is_corporate_gateway": False,
                },
            }
        return (
            200,
            {"Content-Encoding": "gzip"},
            gzip.compress(json.dumps(rows, ensure_ascii=False).encode()),
        )

    ips = [f"192.0.{i // 256}.{i % 256}" for i in range(50_000)]
    with server(respond) as url:
        single = call(
            url, "lookup_ip_geolocation", LookupIpGeolocationRequest(ip=ips[0], lang=Language.AR)
        )
        assert single.data.location.city == city and single.data.network.is_cdn is True
        assert single.data.security.bot_operator_name == "test"
        assert single.data.security.proxy_days_seen_7d == 2
        assert single.data.security.is_corporate_gateway is False
        bulk = call(
            url, "bulk_lookup_ip_geolocation", BulkLookupIpGeolocationRequest(ips=ips, lang="ar")
        )
        assert [item.data.ip for item in bulk.data] == ips


@pytest.mark.parametrize("coding", ["gzip", "deflate", "raw-deflate", "gzip, deflate"])
def test_compressed_text_limit_counts_characters(call, coding):
    body = "ع" * 125
    data = body.encode()
    if coding == "gzip":
        wire = gzip.compress(data[:1]) + gzip.compress(data[1:])
    elif coding == "raw-deflate":
        encoder = zlib.compressobj(wbits=-15)
        wire = encoder.compress(data) + encoder.flush()
    elif coding == "gzip, deflate":
        wire = zlib.compress(gzip.compress(data))
    else:
        wire = zlib.compress(data)
    headers = {"Content-Encoding": coding.replace("raw-", "")}
    with server(lambda *_: (200, headers, wire)) as url:
        req = LookupIpGeolocationRequest()
        assert call(url, "lookup_ip_geolocation_raw", req, limit=125).data == body
        with pytest.raises(TransportException, match="exceeded"):
            call(url, "lookup_ip_geolocation_raw", req, limit=124)


def test_deflate_header_and_multibyte_text_can_cross_chunks():
    from ipgeolocation._response import ResponseBody

    text = "مرحبا"
    reader = ResponseBody(len(text), "utf-8", "deflate")
    for byte in zlib.compress(text.encode()):
        reader.feed(bytes([byte]))
    assert reader.finish() == text


@pytest.mark.parametrize(
    ("coding", "wire", "error"),
    [
        ("gzip", gzip.compress(b"test")[:-3], "Incomplete"),
        ("deflate", b"x", "Incomplete"),
        ("bz2", b"", "Unsupported"),
        ("gzip," * 5 + "gzip", b"", "Too many"),
    ],
)
def test_invalid_compressed_success_is_a_transport_error(call, coding, wire, error):
    with server(lambda *_: (200, {"Content-Encoding": coding}, wire)) as url:
        with pytest.raises(TransportException, match=error):
            call(url, "lookup_ip_geolocation_raw", LookupIpGeolocationRequest())


def test_bounded_intermediate_layers():
    from ipgeolocation._response import ResponseBody

    empty_blocks = b"\x00\x00\x00\xff\xff" * 20000 + b"\x01\x00\x00\xff\xff"
    reader = ResponseBody(64, "utf-8", "deflate, gzip")
    with pytest.raises(TransportException, match="exceeded"):
        reader.feed(gzip.compress(empty_blocks))


@pytest.mark.parametrize("content", [b"plain text", "مرحبا".encode()])
def test_nontext_charset_uses_utf8(content):
    from ipgeolocation._response import ResponseBody

    reader = ResponseBody(64, "base64_codec", "identity")
    reader.feed(content)
    assert reader.finish() == content.decode()


def test_plaintext_error_redacts_before_truncation(call):
    key = secrets.token_hex(16)
    raw = ("x" * 507 + key + " end").encode()
    with server(lambda *_: (401, {}, raw)) as url:
        with pytest.raises(ApiException) as error:
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), key=key)
    assert error.value.api_message.startswith("x" * 507 + "[")
    assert len(error.value.api_message) == 512


@pytest.mark.parametrize("key", ["qa+a/b", "qa example", 'qa"quoted\\id'])
def test_key_encoding_in_api_errors(call, key):
    from urllib.parse import quote_plus

    encoded = quote_plus(key).replace("%2F", "%2f").replace("%2B", "%2b")
    escaped = json.dumps(key)[1:-1]
    wire = json.dumps({"message": f"denied {encoded} {escaped}"}).encode()
    with server(lambda *_: (401, {}, wire)) as url:
        with pytest.raises(ApiException) as error:
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), key=key)
    assert error.value.api_message == "denied [REDACTED] [REDACTED]"


def test_redirect_loop_ends_at_client_limit(call):
    with server(lambda *_: (307, {"Location": "/loop"}, b"")) as url:
        with pytest.raises(TransportException, match="Too many redirects"):
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest(), follow=True)


@pytest.mark.parametrize("data", [b"[" * 10000 + b"]" * 10000, b"1" * 5000])
def test_json_parser_limits_preserve_error_type(call, data):
    with server(lambda *_: (429, {}, data)) as url:
        with pytest.raises(RateLimitException) as error:
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest())
        assert error.value.status_code == 429
    with server(lambda *_: (200, {}, data)) as url:
        with pytest.raises(SerializationException):
            call(url, "lookup_ip_geolocation", LookupIpGeolocationRequest())
        with pytest.raises(SerializationException):
            call(url, "bulk_lookup_ip_geolocation", BulkLookupIpGeolocationRequest(ips=["test"]))


def test_injected_session_headers_and_response_hook():
    import requests

    hooks = []
    encodings = []

    def answer(method, url, headers, body):
        encodings.append(headers["Accept-Encoding"])
        return (302, {"Location": "/final"}, b"") if url.path != "/final" else (200, {}, b"{}")

    with server(answer) as url, requests.Session() as session:
        session.headers["Accept-Encoding"] = "identity"
        session.hooks["response"] = lambda response, **kw: hooks.append(response.status_code)
        config = IpGeolocationClientConfig(api_key="example", base_url=url)
        with IpGeolocationClient(config, RequestsHttpTransport(session)) as client:
            assert client.lookup_ip_geolocation_raw(LookupIpGeolocationRequest()).data == "{}"
    assert encodings == ["identity", "identity"] and hooks == [302, 200]


def test_injected_async_client_keeps_encoding_header():
    async def run():
        def handle(request):
            assert request.headers["Accept-Encoding"] == "identity"
            return httpx.Response(200, content=b"{}")

        async with httpx.AsyncClient(
            transport=httpx.MockTransport(handle), headers={"Accept-Encoding": "identity"}
        ) as http:
            config = IpGeolocationClientConfig(api_key="example")
            async with AsyncIpGeolocationClient(config, HttpxAsyncTransport(http)) as client:
                result = await client.lookup_ip_geolocation_raw(LookupIpGeolocationRequest())
                assert result.data == "{}"

    asyncio.run(run())


@pytest.mark.parametrize("coding", ["br", "zstd"])
def test_optional_response_codings(coding):
    from urllib3 import response
    from urllib3.exceptions import DecodeError

    from ipgeolocation._response import ACCEPT_ENCODING, ResponseBody

    if coding not in ACCEPT_ENCODING.split(", "):
        pytest.skip(f"{coding} decoder is not installed")
    module = response.brotli if coding == "br" else response.zstd
    body = "مرحبا" * 1000
    wire = module.compress(body.encode())
    reader = ResponseBody(len(body), "utf-8", coding)
    reader.feed(wire)
    assert reader.finish() == body
    with pytest.raises(TransportException, match="exceeded"):
        ResponseBody(64, "utf-8", coding).feed(wire)
    broken = ResponseBody(len(body), "utf-8", coding)
    with pytest.raises((TransportException, DecodeError), match="(?i)incomplete"):
        broken.feed(wire[:-1])
        broken.finish()


@pytest.mark.parametrize("status", [204, 205])
def test_no_content_response_ignores_compression_headers(call, status):
    with server(lambda *_: (status, {"Content-Encoding": "gzip"}, b"")) as url:
        assert call(url, "lookup_ip_geolocation_raw", LookupIpGeolocationRequest()).data == ""


def test_raw_deflate_can_start_with_a_valid_zlib_header():
    from ipgeolocation._response import ResponseBody

    raw = bytes.fromhex("780100feff41010000ffff")
    for chunks in ((raw,), (raw[:3], raw[3:])):
        reader = ResponseBody(1, "utf-8", "deflate")
        for chunk in chunks:
            reader.feed(chunk)
        assert reader.finish() == "A"


def test_http2_logs_hide_keys_during_request_and_later_table_eviction(caplog):
    from hpack import Encoder

    from ipgeolocation._redaction import protect_api_key

    key = secrets.token_hex(16)
    encoder = Encoder()
    caplog.set_level(logging.DEBUG)
    with protect_api_key(key):
        encoder.encode(
            [(b":path", ("/v3/ipgeo?apiKey=" + key).encode()), (b"x-trace", key.encode())]
        )
    assert not any(record.name.startswith("hpack.") for record in caplog.records)
    encoder.header_table.maxsize = 1
    encoder.encode([(b":path", b"/normal")])
    assert key not in caplog.text and "/normal" in caplog.text


def test_async_setup_errors_hide_secrets():
    async def run(key, base_url, headers):
        config = IpGeolocationClientConfig(api_key=key, base_url=base_url)
        async with AsyncIpGeolocationClient(config) as client:
            with pytest.raises(TransportException) as error:
                await client.lookup_ip_geolocation(LookupIpGeolocationRequest(headers=headers))
            assert key not in str(error.value) and error.value.__context__ is None

    token = secrets.token_hex(10)
    asyncio.run(run(token, "http://example.test:" + token, {}))
    asyncio.run(run("ä" + token, "http://example.test", {"X-Test": "ä" + token}))
