"""
Tests for the Web module.
"""

from __future__ import annotations

import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

from assistant.modules.web.service import WebAnalyzer


class WebHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/robots.txt":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(
                b"User-agent: *\nDisallow: /admin\n"
            )
            return

        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.send_header("Server", "CyberAtlasTest")
        self.send_header(
            "Set-Cookie",
            "session=test123; Path=/"
        )
        self.end_headers()
        self.wfile.write(
            b"<html><body>Hello</body></html>"
        )

    def log_message(self, format, *args):
        # Silence HTTP server logging during tests.
        return


def test_web_analyzer():

    server = HTTPServer(
        ("127.0.0.1", 0),
        WebHandler,
    )

    thread = threading.Thread(
        target=server.serve_forever,
        daemon=True,
    )

    thread.start()

    host, port = server.server_address

    try:

        result = WebAnalyzer.analyze(
            f"http://{host}:{port}"
        )

        assert result.status_code == 200

        assert (
            result.headers["Content-Type"]
            == "text/html"
        )

        assert "Server" in result.headers

        assert len(result.cookies) == 1

        assert (
            result.cookies[0]["name"]
            == "session"
        )

        assert (
            result.cookies[0]["secure"]
            is False
        )

        assert (
            result.cookies[0]["domain"]
            == "127.0.0.1"
        )

        assert "Disallow" in result.robots

    finally:
        server.shutdown()
        server.server_close()
