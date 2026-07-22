"""
CyberAtlas Web Service.

Fast web enumeration for HTB and CTF challenges.
"""

from __future__ import annotations

from dataclasses import dataclass
from http.cookiejar import CookieJar
from urllib.error import HTTPError, URLError
from urllib.request import HTTPCookieProcessor, Request, build_opener


DEFAULT_TIMEOUT = 10


@dataclass(slots=True)
class WebResult:
    url: str
    status_code: int
    headers: dict[str, str]
    cookies: list[dict[str, object]]
    robots: str


class WebAnalyzer:
    """
    Lightweight HTTP enumeration.
    """

    @staticmethod
    def analyze(url: str) -> WebResult:

        if not url.startswith(("http://", "https://")):
            url = f"http://{url}"

        cookie_jar = CookieJar()
        opener = build_opener(
            HTTPCookieProcessor(cookie_jar)
        )

        request = Request(
            url,
            headers={
                "User-Agent": "CyberAtlas/0.1"
            },
        )

        try:
            response = opener.open(
                request,
                timeout=DEFAULT_TIMEOUT,
            )

            status_code = response.status

            headers = {
                key: value
                for key, value in response.headers.items()
            }
            
        except HTTPError as exc:

            status_code = exc.code

            headers = {
                key: value
                for key, value in exc.headers.items()
            }

        except URLError as exc:
            raise ConnectionError(str(exc)) from exc

        cookies = [
            {
                "name": cookie.name,
                "domain": cookie.domain,
                "secure": cookie.secure,
            }
            for cookie in cookie_jar
        ]

        robots = ""

        robots_url = url.rstrip("/") + "/robots.txt"

        try:

            response = opener.open(
                robots_url,
                timeout=DEFAULT_TIMEOUT,
            )

            robots = (
                response.read()
                .decode("utf-8", errors="replace")
                .strip()
            )

            MAX_LINES = 50

            lines = robots.splitlines()

            if len(lines) > MAX_LINES:
                robots = "\n".join(lines[:MAX_LINES])
                robots += "\n\n... truncated ..."

        except Exception:
            robots = ""

        return WebResult(
            url=url,
            status_code=status_code,
            headers=headers,
            cookies=cookies,
            robots=robots,
        )
