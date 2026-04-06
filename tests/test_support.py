"""Shared test helpers."""

from __future__ import annotations

from collections import deque
from typing import Deque, Dict, List, Optional

from ipgeolocation._transport import HttpRequestData, HttpResponseData


class TestTransport:
    """Simple queued transport for client tests."""

    __test__ = False

    def __init__(self) -> None:
        self.responses: Deque[HttpResponseData] = deque()
        self.captured_requests: List[HttpRequestData] = []
        self.closed = False

    def enqueue_response(
        self,
        status_code: int,
        body: str,
        headers: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        self.responses.append(HttpResponseData(status_code, body, headers or {}))

    def send(self, request: HttpRequestData) -> HttpResponseData:
        self.captured_requests.append(request)
        if not self.responses:
            raise AssertionError("No queued response available")
        return self.responses.popleft()

    def close(self) -> None:
        self.closed = True


class AsyncTestTransport:
    """Simple queued async transport for client tests."""

    __test__ = False

    def __init__(self) -> None:
        self.responses: Deque[HttpResponseData] = deque()
        self.captured_requests: List[HttpRequestData] = []
        self.closed = False

    def enqueue_response(
        self,
        status_code: int,
        body: str,
        headers: Optional[Dict[str, List[str]]] = None,
    ) -> None:
        self.responses.append(HttpResponseData(status_code, body, headers or {}))

    async def send(self, request: HttpRequestData) -> HttpResponseData:
        self.captured_requests.append(request)
        if not self.responses:
            raise AssertionError("No queued response available")
        return self.responses.popleft()

    async def close(self) -> None:
        self.closed = True


def headers(*pairs: str) -> Dict[str, List[str]]:
    """Create a headers dictionary from flat key/value pairs."""
    if len(pairs) % 2 != 0:
        raise ValueError("pairs must contain an even number of values")
    result: Dict[str, List[str]] = {}
    for index in range(0, len(pairs), 2):
        result[pairs[index]] = [pairs[index + 1]]
    return result
