"""
CyberAtlas JWT CLI.
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.crypto.jwt import JWTAnalyzer


console = Console()


def jwt(
    token: str = typer.Argument(
        ...,
        help="JWT token to analyze.",
    ),
) -> None:
    """
    Analyze a JSON Web Token.
    """

    try:
        result = JWTAnalyzer.analyze(token)

    except ValueError as exc:
        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="JWT Analysis Failed",
            )
        )

        raise typer.Exit(code=1)

    console.print(
        Panel.fit(
            "[bold green]JWT Analysis Complete[/bold green]",
            title="CyberAtlas JWT",
        )
    )

    overview = Table(
        title="JWT Overview"
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
        "Algorithm",
        result.algorithm,
    )

    overview.add_row(
        "Signature Present",
        str(result.signature_present),
    )

    overview.add_row(
        "Expired",
        str(result.expired),
    )

    console.print(overview)

    header = Table(
        title="JWT Header"
    )

    header.add_column(
        "Key",
        style="cyan",
    )

    header.add_column(
        "Value",
        overflow="fold",
    )

    for key, value in result.header.items():
        header.add_row(
            str(key),
            str(value),
        )

    console.print(header)

    payload = Table(
        title="JWT Payload"
    )

    payload.add_column(
        "Key",
        style="cyan",
    )

    payload.add_column(
        "Value",
        overflow="fold",
    )

    for key, value in result.payload.items():
        payload.add_row(
            str(key),
            str(value),
        )

    console.print(payload)

    warnings = Table(
        title="Security Warnings"
    )

    warnings.add_column(
        "Warning",
        style="yellow",
    )

    if result.warnings:

        for warning in result.warnings:
            warnings.add_row(warning)

    else:

        warnings.add_row(
            "No security warnings detected."
        )

    console.print(warnings)
