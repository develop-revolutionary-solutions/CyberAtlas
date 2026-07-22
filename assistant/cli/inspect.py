"""
CyberAtlas Inspect CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.inspect.service import Inspector

console = Console()


def inspect(
    filename: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        resolve_path=True,
    ),
) -> None:
    """Quick file inspection."""

    result = Inspector.inspect(str(filename))

    console.print(
        Panel.fit(
            f"[bold cyan]{result.path}[/bold cyan]",
            title="CyberAtlas Inspect",
        )
    )

    info = Table(title="General Information")
    info.add_column("Field")
    info.add_column("Value")

    info.add_row("Size", f"{result.size:,} bytes")
    info.add_row("Type", result.file_type)
    info.add_row("Entropy", f"{result.entropy:.3f}")

    console.print(info)

    # Hash table
    hashes = Table(title="Hashes")
    hashes.add_column("Algorithm", style="cyan")
    hashes.add_column("Digest", overflow="fold")

    hashes.add_row("MD5", result.md5)
    hashes.add_row("SHA1", result.sha1)
    hashes.add_row("SHA256", result.sha256)
    hashes.add_row("SHA512", result.sha512)

    console.print(hashes)



    # Helper function
    def print_results(title: str, values: list[str]) -> None:
        table = Table(title=title)
        table.add_column(title)

        if values:
            for value in values:
                table.add_row(value)
        else:
            table.add_row("[dim]None[/dim]")

        console.print(table)


    # Print extracted artifacts
    print_results("URLs", result.urls)
    print_results("Emails", result.emails)
    print_results("IPv4", result.ips)
    print_results("Flags", result.flags)



    # Recommendations
    if result.recommendations:
        recommendations = Table(title="Recommended Next Steps")
        recommendations.add_column("Action")
 
        for item in result.recommendations:
            recommendations.add_row(item)

        console.print(recommendations)




