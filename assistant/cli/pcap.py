"""
CyberAtlas PCAP CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.pcap.service import PCAPAnalyzer

console = Console()


def pcap(
    filename: Path = typer.Argument(
        ...,
        exists=True,
        readable=True,
        resolve_path=True,
        help="PCAP/PCAPNG file to analyze.",
    ),
) -> None:
    """
    Analyze a packet capture.
    """

    result = PCAPAnalyzer.analyze(str(filename))

    console.print(
        Panel.fit(
            f"[bold cyan]{result.path}[/bold cyan]",
            title="CyberAtlas PCAP Analysis",
        )
    )

    summary = Table(title="Capture Summary")
    summary.add_column("Field", style="cyan")
    summary.add_column("Value", overflow="fold")

    summary.add_row("Packets", str(result.packet_count))
    summary.add_row(
        "Protocols",
        ", ".join(result.protocols) if result.protocols else "None",
    )

    console.print(summary)

    dns_table = Table(title="DNS Queries")
    dns_table.add_column("#", justify="right")
    dns_table.add_column("Query")

    if result.dns_queries:
        for index, query in enumerate(result.dns_queries, start=1):
            dns_table.add_row(str(index), query)
    else:
        dns_table.add_row("-", "No DNS queries")

    console.print(dns_table)

    http_table = Table(title="HTTP Hosts")
    http_table.add_column("#", justify="right")
    http_table.add_column("Host")

    if result.http_hosts:
        for index, host in enumerate(result.http_hosts, start=1):
            http_table.add_row(str(index), host)
    else:
        http_table.add_row("-", "No HTTP hosts")

    console.print(http_table)

    uri_table = Table(title="HTTP URIs")
    uri_table.add_column("#", justify="right")
    uri_table.add_column("URI")

    if result.http_uris:
        for index, uri in enumerate(result.http_uris, start=1):
            uri_table.add_row(str(index), uri)
    else:
        uri_table.add_row("-", "No HTTP URIs")

    console.print(uri_table)

    ip_table = Table(title="IPv4 Addresses")
    ip_table.add_column("#", justify="right")
    ip_table.add_column("Address")

    if result.ipv4_addresses:
        for index, ip in enumerate(result.ipv4_addresses, start=1):
            ip_table.add_row(str(index), ip)
    else:
        ip_table.add_row("-", "No IPv4 addresses")

    console.print(ip_table)
