"""Exception types raised by the SDK."""

from __future__ import annotations

from typing import Optional


class IpGeolocationException(Exception):
    """Base exception for SDK failures."""


class ValidationException(IpGeolocationException):
    """Raised when request or configuration validation fails before I/O."""


class SerializationException(IpGeolocationException):
    """Raised when JSON serialization or deserialization fails."""


class TransportException(IpGeolocationException):
    """Raised when the HTTP transport fails."""


class RequestTimeoutException(TransportException):
    """Raised when the HTTP request times out."""


class ApiException(IpGeolocationException):
    """Raised when the API returns a non-2xx response."""

    def __init__(self, message: str, status_code: int, api_message: Optional[str] = None):
        super().__init__(message)
        self.status_code = status_code
        self.api_message = api_message


class BadRequestException(ApiException):
    """Raised for HTTP 400 responses."""


class UnauthorizedException(ApiException):
    """Raised for HTTP 401 responses."""


class NotFoundException(ApiException):
    """Raised for HTTP 404 responses."""


class MethodNotAllowedException(ApiException):
    """Raised for HTTP 405 responses."""


class PayloadTooLargeException(ApiException):
    """Raised for HTTP 413 responses."""


class UnsupportedMediaTypeException(ApiException):
    """Raised for HTTP 415 responses."""


class LockedException(ApiException):
    """Raised for HTTP 423 responses."""


class RateLimitException(ApiException):
    """Raised for HTTP 429 responses."""


class ClientClosedRequestException(ApiException):
    """Raised for HTTP 499 responses."""


class ServerErrorException(ApiException):
    """Raised for HTTP 5xx responses."""
