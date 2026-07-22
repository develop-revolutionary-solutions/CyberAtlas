"""
CyberAtlas PCAP Service.

Fast PCAP inspection for HTB and CTF challenges.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PCAPResult:
    path: str
    packet_count: int
    protocols: list[str]
    dns_queries: list[str]
    http_hosts: list[str]
    http_uris: list[str]
    ipv4_addresses: list[str]


class PCAPAnalyzer:
    """
    Analyze packet captures using tshark.
    """

    @staticmethod
    def _run(*command: str) -> str:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout.strip()

    @classmethod
    def analyze(cls, filename: str) -> PCAPResult:

        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(filename)

        #
        # Packet Count
        #

        capinfos = cls._run(
            "capinfos",
            "-c",
            str(path),
        )

        packet_count = 0

        for line in capinfos.splitlines():

            if "Number of packets" in line:

                try:
                    packet_count = int(
                        line.split(":", 1)[1].strip()
                    )
                except ValueError:
                    packet_count = 0

                break

        #
        # Protocol Summary
        #

        protocol_output = cls._run(
            "tshark",
            "-r",
            str(path),
            "-T",
            "fields",
            "-e",
            "_ws.col.Protocol",
        )

        protocols = sorted(
            {
                p.strip()
                for p in protocol_output.splitlines()
                if p.strip()
            }
        )

        #
        # DNS Queries
        #

        dns_output = cls._run(
            "tshark",
            "-r",
            str(path),
            "-Y",
            "dns.qry.name",
            "-T",
            "fields",
            "-e",
            "dns.qry.name",
        )

        dns_queries = sorted(
            {
                q.strip()
                for q in dns_output.splitlines()
                if q.strip()
            }
        )

        #
        # HTTP Hosts
        #

        host_output = cls._run(
            "tshark",
            "-r",
            str(path),
            "-Y",
            "http.host",
            "-T",
            "fields",
            "-e",
            "http.host",
        )

        http_hosts = sorted(
            {
                h.strip()
                for h in host_output.splitlines()
                if h.strip()
            }
        )

        #
        # HTTP URIs
        #

        uri_output = cls._run(
            "tshark",
            "-r",
            str(path),
            "-Y",
            "http.request.uri",
            "-T",
            "fields",
            "-e",
            "http.request.uri",
        )

        http_uris = sorted(
            {
                u.strip()
                for u in uri_output.splitlines()
                if u.strip()
            }
        )

        #
        # IPv4 Addresses
        #

        ip_output = cls._run(
            "tshark",
            "-r",
            str(path),
            "-T",
            "fields",
            "-e",
            "ip.src",
            "-e",
            "ip.dst",
        )

        ips: set[str] = set()

        for line in ip_output.splitlines():

            for ip in line.split():

                ip = ip.strip()

                if ip:
                    ips.add(ip)

        return PCAPResult(
            path=str(path.resolve()),
            packet_count=packet_count,
            protocols=protocols,
            dns_queries=dns_queries,
            http_hosts=http_hosts,
            http_uris=http_uris,
            ipv4_addresses=sorted(ips),
        )
