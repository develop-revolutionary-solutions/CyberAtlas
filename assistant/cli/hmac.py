"""
CyberAtlas HMAC CLI.

Provides HMAC utilities for:
- CTF workflows
- API security testing
- Message authentication analysis
- Cryptographic verification
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.crypto.hmac import (
    HMACService,
)


app = typer.Typer(
    name="hmac",
    help="HMAC cryptographic operations.",
    no_args_is_help=True,
)


console = Console()

service = HMACService()


@app.command("generate")
def generate(
    message: str = typer.Option(
        ...,
        "--message",
        "-m",
        help="Message to authenticate.",
    ),
    key: str = typer.Option(
        ...,
        "--key",
        "-k",
        help="HMAC secret key.",
    ),
    algorithm: str = typer.Option(
        "sha256",
        "--algorithm",
        "-a",
        help="HMAC algorithm.",
    ),
) -> None:
    """
    Generate HMAC digest.
    """

    try:
        result = service.generate(
            message=message,
            key=key,
            algorithm=algorithm,
        )

    except Exception as exc:

        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="HMAC Generation Failed",
            )
        )

        raise typer.Exit(
            code=1
        )

    console.print(
        Panel.fit(
            "[bold green]HMAC Generated Successfully[/bold green]",
            title="CyberAtlas HMAC",
        )
    )

    table = Table(
        title="HMAC Result"
    )

    table.add_column(
        "Field",
        style="cyan",
    )

    table.add_column(
        "Value",
    )

    table.add_row(
        "Algorithm",
        result.algorithm,
    )

    table.add_row(
        "Digest",
        result.digest,
    )

    table.add_row(
        "Digest Size",
        f"{result.digest_size} bytes",
    )

    console.print(
        table
    )


@app.command("verify")
def verify(
    message: str = typer.Option(
        ...,
        "--message",
        "-m",
        help="Original message.",
    ),
    key: str = typer.Option(
        ...,
        "--key",
        "-k",
        help="HMAC secret key.",
    ),
    digest: str = typer.Option(
        ...,
        "--digest",
        "-d",
        help="Expected HMAC digest.",
    ),
    algorithm: str = typer.Option(
        "sha256",
        "--algorithm",
        "-a",
        help="HMAC algorithm.",
    ),
) -> None:
    """
    Verify HMAC digest.
    """

    try:
        result = service.verify(
            message=message,
            key=key,
            expected_digest=digest,
            algorithm=algorithm,
        )

    except Exception as exc:

        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="HMAC Verification Failed",
            )
        )

        raise typer.Exit(
            code=1
        )

    if result:

        console.print(
            Panel.fit(
                "[bold green]Valid HMAC Signature[/bold green]",
                title="Verification Result",
            )
        )

    else:

        console.print(
            Panel.fit(
                "[bold red]Invalid HMAC Signature[/bold red]",
                title="Verification Result",
            )
        )


@app.command("keygen")
def keygen(
    length: int = typer.Option(
        32,
        "--length",
        "-l",
        help="Key length in bytes.",
    ),
) -> None:
    """
    Generate secure HMAC key.
    """

    try:

        key = service.generate_key(
            length
        )

    except Exception as exc:

        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="Key Generation Failed",
            )
        )

        raise typer.Exit(
            code=1
        )

    console.print(
        Panel.fit(
            key,
            title="Generated HMAC Key",
        )
    )


@app.command("identify")
def identify(
    digest: str = typer.Argument(
        ...,
        help="Digest value.",
    ),
) -> None:
    """
    Identify possible digest algorithms.
    """

    result = service.identify_digest(
        digest
    )

    table = Table(
        title="Digest Identification"
    )

    table.add_column(
        "Field",
        style="cyan",
    )

    table.add_column(
        "Value",
    )

    table.add_row(
        "Digest Length",
        str(result["digest_length"]),
    )

    table.add_row(
        "Possible Algorithms",
        ", ".join(
            result["possible_algorithms"]
        )
        or "Unknown",
    )

    console.print(
        table
    )


@app.command("analyze-key")
def analyze_key(
    key: str = typer.Argument(
        ...,
        help="HMAC secret key.",
    ),
) -> None:
    """
    Analyze HMAC key strength.
    """

    result = service.analyze_key(
        key
    )

    table = Table(
        title="HMAC Key Analysis"
    )

    table.add_column(
        "Property",
        style="cyan",
    )

    table.add_column(
        "Value",
    )

    for item, value in result.items():

        table.add_row(
            item.replace(
                "_",
                " ",
            ).title(),
            str(value),
        )

    console.print(
        table
    )
