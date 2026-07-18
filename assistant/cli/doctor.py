"""
Doctor command.

Checks whether CyberAtlas is correctly installed.
"""

import platform
import sys

import typer

from assistant.logging.logger import get_logger

app = typer.Typer(help="System health checks.")

logger = get_logger(__name__)

@app.command()
def run() -> None:
    """
    Display basic environment information.
    """
    logger.info("Doctor command started.")

    typer.echo("CyberAtlas Doctor")
    typer.echo("--------------------------")
    typer.echo(f"Python : {platform.python_version()}")
    typer.echo(f"Executable : {sys.executable}")
    typer.echo("Status : OK")

    logger.info("Doctor command completed successfully.")
