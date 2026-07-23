"""
CyberAtlas Wordlist CLI.

Provides local wordlist analysis utilities for:
- CTF workflows
- password auditing
- security assessments
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.crypto.wordlists import (
    WordlistManager,
)


console = Console()


def wordlist(
    path: str = typer.Argument(
        ...,
        help="Path to wordlist file.",
    ),
) -> None:
    """
    Analyze a local wordlist.
    """

    try:
        words = WordlistManager.load(
            Path(path)
        )

        stats = WordlistManager.statistics(
            words
        )

    except Exception as exc:

        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="Wordlist Analysis Failed",
            )
        )

        raise typer.Exit(
            code=1
        )

    console.print(
        Panel.fit(
            "[bold green]Wordlist Analysis Complete[/bold green]",
            title="CyberAtlas Wordlist",
        )
    )

    table = Table(
        title="Wordlist Statistics"
    )

    table.add_column(
        "Field",
        style="cyan",
    )

    table.add_column(
        "Value",
    )

    table.add_row(
        "Total Words",
        str(stats.total_words),
    )

    table.add_row(
        "Unique Words",
        str(stats.unique_words),
    )

    table.add_row(
        "Shortest Word",
        str(stats.shortest_word),
    )

    table.add_row(
        "Longest Word",
        str(stats.longest_word),
    )

    console.print(
        table
    )


def stats(
    path: str = typer.Argument(
        ...,
        help="Path to wordlist file.",
    ),
) -> None:
    """
    Display wordlist statistics.

    Alias command helper for future CLI expansion.
    """

    wordlist(path)
