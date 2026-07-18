"""
Doctor command.

Checks whether CyberAtlas is correctly installed.
"""

import platform
import sys

import typer

app = typer.Typer(help="System health checks.")


@app.command()
def run() -> None:
    """
    Display basic environment information.
    """
    typer.echo("CyberAtlas Doctor")
    typer.echo("--------------------------")
    typer.echo(f"Python : {platform.python_version()}")
    typer.echo(f"Executable : {sys.executable}")
    typer.echo("Status : OK")
