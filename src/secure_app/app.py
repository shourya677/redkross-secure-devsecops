"""A tiny dependency-free WSGI API used to demonstrate secure defaults.

This is an educational starter, not a production web framework. For production
services, use a maintained framework and deployment-specific controls.
"""

from __future__ import annotations

import json
from typing import Any, Callable

MAX_BODY_BYTES = 1_024


def _response(
    start_response: Callable[..., Any],
    status: str,
    payload: dict[str, str],
) -> list[bytes]:
    body = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    headers = [
        ("Content-Type", "application/json; charset=utf-8"),
        ("Content-Length", str(len(body))),
        ("Cache-Control", "no-store"),
        ("X-Content-Type-Options", "nosniff"),
        ("X-Frame-Options", "DENY"),
        ("Referrer-Policy", "no-referrer"),
        ("Content-Security-Policy", "default-src 'none'; frame-ancestors 'none'"),
    ]
    start_response(status, headers)
    return [body]


def application(environ: dict[str, Any], start_response: Callable[..., Any]) -> list[bytes]:
    """Serve health and greeting endpoints with conservative input handling."""
    method = environ.get("REQUEST_METHOD", "GET").upper()
    path = environ.get("PATH_INFO", "/")

    if method != "GET":
        return _response(start_response, "405 Method Not Allowed", {"error": "method_not_allowed"})

    if path == "/health":
        return _response(start_response, "200 OK", {"status": "ok"})

    if path == "/api/greeting":
        # Never reflect arbitrary user-controlled data into a response.
        return _response(start_response, "200 OK", {"message": "Hello from the secure starter"})

    return _response(start_response, "404 Not Found", {"error": "not_found"})
