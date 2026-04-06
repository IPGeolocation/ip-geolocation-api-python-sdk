"""Client configuration tests."""

from __future__ import annotations

from datetime import timedelta

import pytest

from ipgeolocation import IpGeolocationClientConfig


def test_config_trims_trailing_slash() -> None:
    config = IpGeolocationClientConfig(api_key="k", base_url="https://api.ipgeolocation.io///")
    assert config.base_url == "https://api.ipgeolocation.io"


def test_config_trims_surrounding_whitespace_from_api_key_and_base_url() -> None:
    config = IpGeolocationClientConfig(
        api_key="  key-with-spaces  ",
        request_origin="  https://app.example.com/  ",
        base_url="  https://api.ipgeolocation.io/  ",
    )
    assert config.api_key == "key-with-spaces"
    assert config.request_origin == "https://app.example.com"
    assert config.base_url == "https://api.ipgeolocation.io"


def test_config_rejects_blank_api_key() -> None:
    with pytest.raises(ValueError, match="api_key must not be blank"):
        IpGeolocationClientConfig(api_key="   ")


def test_config_rejects_non_string_api_key() -> None:
    with pytest.raises(TypeError, match="api_key must be a string"):
        IpGeolocationClientConfig(api_key=123)


def test_config_rejects_blank_request_origin() -> None:
    with pytest.raises(ValueError, match="request_origin must not be blank"):
        IpGeolocationClientConfig(api_key="k", request_origin="   ")


def test_config_rejects_non_string_request_origin() -> None:
    with pytest.raises(TypeError, match="request_origin must be a string"):
        IpGeolocationClientConfig(api_key="k", request_origin=123)


def test_config_rejects_request_origin_with_newlines() -> None:
    with pytest.raises(ValueError, match="request_origin must not contain CR or LF"):
        IpGeolocationClientConfig(api_key="k", request_origin="https://a\r\nb.example")


def test_config_rejects_request_origin_without_http_scheme() -> None:
    with pytest.raises(ValueError, match="request_origin must be an absolute http or https origin"):
        IpGeolocationClientConfig(api_key="k", request_origin="app.example.com")


def test_config_rejects_request_origin_with_path_query_fragment_or_userinfo() -> None:
    with pytest.raises(ValueError, match="request_origin must not include a path"):
        IpGeolocationClientConfig(api_key="k", request_origin="https://app.example.com/path")

    with pytest.raises(
        ValueError,
        match="request_origin must not include params, query, or fragment",
    ):
        IpGeolocationClientConfig(api_key="k", request_origin="https://app.example.com?x=1")

    with pytest.raises(
        ValueError,
        match="request_origin must not include params, query, or fragment",
    ):
        IpGeolocationClientConfig(api_key="k", request_origin="https://app.example.com#frag")

    with pytest.raises(ValueError, match="request_origin must not include userinfo"):
        IpGeolocationClientConfig(api_key="k", request_origin="https://user:pass@app.example.com")


def test_config_accepts_request_origin_with_port() -> None:
    config = IpGeolocationClientConfig(
        api_key="k",
        request_origin="http://localhost:3000/",
    )
    assert config.request_origin == "http://localhost:3000"


def test_config_rejects_blank_base_url() -> None:
    with pytest.raises(ValueError, match="base_url must not be blank"):
        IpGeolocationClientConfig(api_key="k", base_url=" ")


def test_config_rejects_non_string_base_url() -> None:
    with pytest.raises(TypeError, match="base_url must be a string"):
        IpGeolocationClientConfig(api_key="k", base_url=123)


def test_config_rejects_none_base_url() -> None:
    with pytest.raises(TypeError, match="base_url must not be None"):
        IpGeolocationClientConfig(api_key="k", base_url=None)


def test_config_rejects_base_url_without_http_scheme() -> None:
    with pytest.raises(ValueError, match="base_url must be an absolute http or https URL"):
        IpGeolocationClientConfig(api_key="k", base_url="api.ipgeolocation.io")


def test_config_rejects_base_url_with_query_or_fragment() -> None:
    with pytest.raises(ValueError, match="base_url must not include params, query, or fragment"):
        IpGeolocationClientConfig(api_key="k", base_url="https://api.ipgeolocation.io?debug=1")

    with pytest.raises(ValueError, match="base_url must not include params, query, or fragment"):
        IpGeolocationClientConfig(api_key="k", base_url="https://api.ipgeolocation.io#frag")


def test_config_rejects_non_positive_timeouts() -> None:
    with pytest.raises(ValueError, match="connect_timeout must be greater than zero"):
        IpGeolocationClientConfig(api_key="k", connect_timeout=0)

    with pytest.raises(ValueError, match="read_timeout must be greater than zero"):
        IpGeolocationClientConfig(api_key="k", read_timeout=timedelta(seconds=0))


def test_config_rejects_invalid_timeout_types() -> None:
    with pytest.raises(TypeError, match="connect_timeout must be a float, int, or timedelta"):
        IpGeolocationClientConfig(api_key="k", connect_timeout="10")

    with pytest.raises(TypeError, match="read_timeout must be a float, int, or timedelta"):
        IpGeolocationClientConfig(api_key="k", read_timeout=True)


def test_config_rejects_non_finite_timeouts() -> None:
    with pytest.raises(ValueError, match="connect_timeout must be finite"):
        IpGeolocationClientConfig(api_key="k", connect_timeout=float("nan"))

    with pytest.raises(ValueError, match="read_timeout must be finite"):
        IpGeolocationClientConfig(api_key="k", read_timeout=float("inf"))


def test_config_requires_connect_timeout_not_exceed_read_timeout() -> None:
    with pytest.raises(ValueError, match="connect_timeout must be <= read_timeout"):
        IpGeolocationClientConfig(api_key="k", connect_timeout=10, read_timeout=5)
