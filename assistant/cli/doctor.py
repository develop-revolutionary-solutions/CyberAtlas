"""
CyberAtlas Doctor CLI.

Checks the local environment and required external tools.
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from assistant.modules.doctor.service import overall_status

app = typer.Typer(
    help="Check CyberAtlas environment.",
    no_args_is_help=False,
)

console = Console()


@app.callback(invoke_without_command=True)
def doctor() -> None:
    """Run environment diagnostics."""

    status = overall_status()

    console.print("\n[bold cyan]CyberAtlas Environment Report[/bold cyan]\n")

    console.print(f"[bold]Python:[/bold]     {status['python']}")
    console.print(f"[bold]OS:[/bold]         {status['os']}")
    console.print(f"[bold]Executable:[/bold] {status['executable']}")

    if status["workspace"]:
        console.print("[bold]Workspace:[/bold] [green]Writable[/green]")
    else:
        console.print("[bold]Workspace:[/bold] [red]Not Writable[/red]")

    table = Table(title="Installed Tools")

    table.add_column("Tool", style="cyan")
    table.add_column("Status", justify="center")
    table.add_column("Location")

    installed = 0

    for tool in status["tools"]:
        if tool.installed:
            installed += 1
            table.add_row(
                tool.name,
                "[green]✓[/green]",
                tool.path or "",
            )
        else:
            table.add_row(
                tool.name,
                "[red]✗[/red]",
                "-",
            )

    console.print()
    console.print(table)

    total = len(status["tools"])

    console.print()
    console.print(
        f"[bold]Installed:[/bold] {installed}/{total}"
    )

    if installed == total:
        console.print("[bold green]Environment looks good![/bold green]")
    else:
        console.print(
            "[bold yellow]Some recommended tools are missing.[/bold yellow]"
        )
