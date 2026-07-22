import typer

from assistant.cli.doctor import app as doctor_app
from assistant.cli.version import app as version_app
from assistant.cli.inspect import inspect
from assistant.cli.workspace import workspace
from assistant.cli.decode import decode
from assistant.cli.elf import elf
from assistant.cli.pe import pe
from assistant.cli.pcap import pcap


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
app.command()(decode)
app.command()(elf)
app.command()(pe)
app.command()(pcap)


app.add_typer(
    version_app,
    name="version",
)

app.add_typer(
    doctor_app,
    name="doctor",
)
