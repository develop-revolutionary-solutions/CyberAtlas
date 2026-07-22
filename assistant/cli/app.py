import typer

from assistant.cli.doctor import app as doctor_app
from assistant.cli.version import app as version_app
from assistant.cli.inspect import inspect
from assistant.cli.workspace import workspace


app = typer.Typer(
    name="CyberAtlas",
    help="AI-assisted Cyber Security Assistant.",
    no_args_is_help=True,
)


@app.callback()
def main() -> None:
    """CyberAtlas CLI."""
    pass


app.command()(inspect)
app.command()(workspace)


app.add_typer(
    version_app,
    name="version",
)


app.add_typer(
    doctor_app,
    name="doctor",
)
