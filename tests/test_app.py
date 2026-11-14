"""Unit tests for the example WSGI application."""

import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from secure_app.app import application


class ApplicationTests(unittest.TestCase):
    def call_app(self, path="/health", method="GET"):
        captured = {}

        def start_response(status, headers):
            captured["status"] = status
            captured["headers"] = dict(headers)

        body = b"".join(
            application(
                {"REQUEST_METHOD": method, "PATH_INFO": path, "wsgi.input": None},
                start_response,
            )
        )
        captured["body"] = json.loads(body.decode("utf-8"))
        return captured

    def test_health_endpoint(self):
        result = self.call_app()
        self.assertEqual(result["status"], "200 OK")
        self.assertEqual(result["body"], {"status": "ok"})

    def test_greeting_endpoint(self):
        result = self.call_app("/api/greeting")
        self.assertEqual(result["status"], "200 OK")
        self.assertIn("message", result["body"])

    def test_unknown_route_is_not_found(self):
        result = self.call_app("/does-not-exist")
        self.assertEqual(result["status"], "404 Not Found")
        self.assertEqual(result["body"], {"error": "not_found"})

    def test_non_get_method_is_rejected(self):
        result = self.call_app("/health", "POST")
        self.assertEqual(result["status"], "405 Method Not Allowed")

    def test_security_headers_are_present(self):
        headers = self.call_app()["headers"]
        self.assertEqual(headers["X-Content-Type-Options"], "nosniff")
        self.assertEqual(headers["X-Frame-Options"], "DENY")
        self.assertEqual(headers["Cache-Control"], "no-store")
        self.assertIn("default-src 'none'", headers["Content-Security-Policy"])

    def test_response_does_not_reflect_query_input(self):
        result = self.call_app("/api/greeting?name=<script>alert(1)</script>")
        self.assertNotIn("<script>", json.dumps(result["body"]))


if __name__ == "__main__":
    unittest.main()
