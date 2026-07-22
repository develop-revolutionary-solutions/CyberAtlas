"""
CyberAtlas Workspace CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.workspace.service import Workspace

console = Console()


def workspace(
    name: str = typer.Argument(
        ...,
        help="Workspace name (challenge name).",
    ),
) -> None:
    """
    Create a new HTB workspace.
    """

    result = Workspace.create(name)

    console.print(
        Panel.fit(
            f"[bold green]{result.root}[/bold green]",
            title="Workspace Created",
        )
    )

    table = Table(title="Directories")
    table.add_column("Created")

    for directory in result.created:
        table.add_row(str(directory.relative_to(result.root)))

    console.print(table)

    if result.readme_created:
        console.print("[green]✓[/green] README.md created")
    else:
        console.print("[yellow]•[/yellow] README.md already exists")

    if result.writeup_created:
        console.print("[green]✓[/green] writeup.md created")
    else:
        console.print("[yellow]•[/yellow] writeup.md already exists")
