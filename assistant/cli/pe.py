"""
CyberAtlas PE CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.pe.service import PEAnalyzer

console = Console()


def pe(
    filename: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        resolve_path=True,
        help="PE executable or DLL to analyze.",
    ),
) -> None:
    """
    Analyze a Windows PE executable.
    """

    result = PEAnalyzer.analyze(str(filename))

    console.print(
        Panel.fit(
            f"[bold cyan]{result.path}[/bold cyan]",
            title="CyberAtlas PE Analysis",
        )
    )

    table = Table(title="PE Information")
    table.add_column("Field", style="cyan")
    table.add_column("Value", overflow="fold")

    table.add_row("File Type", result.file_type)
    table.add_row("Architecture", result.architecture)
    table.add_row("Format", result.bits)
    table.add_row("Image Base", result.image_base)
    table.add_row("Entry Point", result.entry_point)
    table.add_row("ASLR", result.aslr)
    table.add_row("DEP", result.dep)

    console.print(table)

    sections = Table(title="Sections")
    sections.add_column("#", justify="right")
    sections.add_column("Section")

    if result.sections:
        for index, section in enumerate(result.sections, start=1):
            sections.add_row(str(index), section)
    else:
        sections.add_row("-", "No sections found")

    console.print(sections)

    imports = Table(title="Imported DLLs")
    imports.add_column("#", justify="right")
    imports.add_column("DLL")

    if result.imports:
        for index, dll in enumerate(result.imports, start=1):
            imports.add_row(str(index), dll)
    else:
        imports.add_row("-", "No imported DLLs")

    console.print(imports)
