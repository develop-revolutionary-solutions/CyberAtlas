"""
CyberAtlas Password CLI.

Provides password analysis commands for:
- password auditing
- CTF challenges
- security assessments
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.crypto.passwords import (
    PasswordAnalyzer,
)


console = Console()


def password(
    value: str = typer.Argument(
        ...,
        help="Password to analyze.",
    ),
) -> None:
    """
    Analyze password security.
    """

    try:
        result = PasswordAnalyzer.analyze(
            value
        )

        patterns = PasswordAnalyzer.detect_patterns(
            value
        )

        mask = PasswordAnalyzer.create_mask(
            value
        )

    except Exception as exc:

        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="Password Analysis Failed",
            )
        )

        raise typer.Exit(
            code=1
        )

    console.print(
        Panel.fit(
            "[bold green]Password Analysis Complete[/bold green]",
            title="CyberAtlas Password",
        )
    )

    overview = Table(
        title="Password Overview"
    )

    overview.add_column(
        "Field",
        style="cyan",
    )

    overview.add_column(
        "Value",
        overflow="fold",
    )

    overview.add_row(
        "Length",
        str(result.password_length),
    )

    overview.add_row(
        "Entropy",
        str(result.entropy),
    )

    overview.add_row(
        "Score",
        f"{result.score}/6",
    )

    overview.add_row(
        "Strength",
        result.strength,
    )

    overview.add_row(
        "Mask",
        mask,
    )

    console.print(
        overview
    )

    classes = Table(
        title="Character Classes"
    )

    classes.add_column(
        "Type",
        style="cyan",
    )

    classes.add_column(
        "Present",
    )

    classes.add_row(
        "Lowercase",
        "✓" if result.has_lowercase else "✗",
    )

    classes.add_row(
        "Uppercase",
        "✓" if result.has_uppercase else "✗",
    )

    classes.add_row(
        "Digits",
        "✓" if result.has_digits else "✗",
    )

    classes.add_row(
        "Symbols",
        "✓" if result.has_symbols else "✗",
    )

    console.print(
        classes
    )

    warnings = Table(
        title="Security Warnings"
    )

    warnings.add_column(
        "Warning",
        style="yellow",
    )

    if result.warnings:

        for warning in result.warnings:
            warnings.add_row(
                warning
            )

    else:

        warnings.add_row(
            "No security warnings detected."
        )

    console.print(
        warnings
    )

    detected = Table(
        title="Detected Patterns"
    )

    detected.add_column(
        "Pattern",
        style="cyan",
    )

    detected.add_column(
        "Matches",
    )

    if patterns:

        for pattern in patterns:

            detected.add_row(
                pattern.pattern,
                ", ".join(
                    pattern.matches
                ),
            )

    else:

        detected.add_row(
            "None",
            "-",
        )

    console.print(
        detected
    )
