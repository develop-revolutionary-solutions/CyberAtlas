"""
CyberAtlas Decode CLI.
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.decode.service import Decoder

console = Console()


def decode(
    text: str = typer.Argument(
        ...,
        help="Encoded text to decode.",
    ),
) -> None:
    """
    Detect and decode common CTF encodings.
    """

    try:
        result = Decoder.decode(text)

    except ValueError as exc:
        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="Decode Failed",
            )
        )
        raise typer.Exit(code=1)

    console.print(
        Panel.fit(
            "[bold green]Decode Successful[/bold green]",
            title="CyberAtlas Decode",
        )
    )

    table = Table(title="Decode Result")
    table.add_column("Field", style="cyan")
    table.add_column("Value", overflow="fold")

    table.add_row("Detected Encoding", result.encoding)
    table.add_row("Decoded Value", result.decoded)

    console.print(table)
