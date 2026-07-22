"""
CyberAtlas Web CLI.
"""

from __future__ import annotations

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
import typer

from assistant.modules.web.service import WebAnalyzer

console = Console()


def web(
    url: str = typer.Argument(
        ...,
        help="Target URL (example: http://example.com)",
    ),
) -> None:
    """
    Analyze a web target.
    """

    result = WebAnalyzer.analyze(url)

    console.print(
        Panel.fit(
            f"[bold cyan]{result.url}[/bold cyan]",
            title="CyberAtlas Web Analysis",
        )
    )

    summary = Table(title="Summary")
    summary.add_column("Field", style="cyan")
    summary.add_column("Value", overflow="fold")

    summary.add_row("Status Code", str(result.status_code))

    summary.add_row(
        "Server",
        result.headers.get("Server", "Unknown"),
    )

    summary.add_row(
        "Content-Type",
        result.headers.get("Content-Type", "Unknown"),
    )

    summary.add_row(
        "Content-Length",
        str(len(result.content_length)),
    )

    summary.add_row(
        "Cookies",
        str(len(result.cookies)),
    )

    console.print(summary)

    headers = Table(title="HTTP Headers")
    headers.add_column("Header", style="cyan")
    headers.add_column("Value", overflow="fold")

    if result.headers:

        MAX_HEADER_VALUE = 120

        for key, value in sorted(result.headers.items()):
            display = value

            if len(display) > MAX_HEADER_VALUE:
                display = display[:MAX_HEADER_VALUE] + " ..."

            headers.add_row(key, display)
    else:
        headers.add_row("-", "No headers")

    console.print(headers)

    cookie_table = Table(title="Cookies")

    cookie_table.add_column("#", justify="right")
    cookie_table.add_column("Name")
    cookie_table.add_column("Domain")
    cookie_table.add_column("Secure")

    if result.cookies:
        for index, cookie in enumerate(result.cookies, start=1):
            cookie_table.add_row(
                str(index),
                cookie["name"],
                cookie["domain"],
                "Yes" if cookie["secure"] else "No",
            )
            
    else:
        cookie_table.add_row("-", "No cookies")

    console.print(cookie_table)

    robots = Panel.fit(
        result.robots if result.robots else "robots.txt not found",
        title="robots.txt",
    )

    console.print(robots)
