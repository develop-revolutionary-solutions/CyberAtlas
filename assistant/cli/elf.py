"""
CyberAtlas ELF CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.elf.service import ELFAnalyzer

console = Console()


def elf(
    filename: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        resolve_path=True,
        help="ELF binary to analyze.",
    ),
) -> None:
    """
    Analyze an ELF executable.
    """

    result = ELFAnalyzer.analyze(str(filename))

    console.print(
        Panel.fit(
            f"[bold cyan]{result.path}[/bold cyan]",
            title="CyberAtlas ELF Analysis",
        )
    )

    table = Table(title="ELF Information")
    table.add_column("Field", style="cyan")
    table.add_column("Value", overflow="fold")

    table.add_row("File Type", result.file_type)
    table.add_row("Architecture", result.architecture)
    table.add_row("Class", result.bits)
    table.add_row("Endian", result.endian)
    table.add_row("Entry Point", result.entry_point)
    table.add_row("Interpreter", result.interpreter)
    table.add_row("PIE", result.pie)
    table.add_row("NX", result.nx)
    table.add_row("RELRO", result.relro)
    table.add_row("Canary", result.canary)
    table.add_row("Stripped", result.stripped)

    console.print(table)
