"""
Version command for CyberAtlas.
"""

import typer

app = typer.Typer(help="Display version information.")


@app.command()
def show() -> None:
    """
    Display the current CyberAtlas version.
    """
    typer.echo("CyberAtlas v0.1.0")
