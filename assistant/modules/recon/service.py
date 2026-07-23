"""
CyberAtlas Recon Intelligence Service

This module provides a local-first reconnaissance framework that wraps common
reconnaissance utilities into a consistent Python API.

Design Goals
------------
* Local-first
* Offline-friendly where possible
* CPU friendly
* No external API dependencies
* Safe execution
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Iterable


SUPPORTED_TOOLS = (
    "nmap",
    "ffuf",
    "nuclei",
    "amass",
    "subfinder",
    "httpx",
    "curl",
    "whois",
    "grep",
    "strings",
    "file",
    "binwalk",
    "hexdump",
)


class ReconService:
    """CyberAtlas Recon Service."""

    @staticmethod
    def tool_exists(tool: str) -> bool:
        """Return True if tool exists on PATH."""
        return shutil.which(tool) is not None

    @staticmethod
    def available_tools() -> list[str]:
        """Return installed supported tools."""
        return [
            tool
            for tool in SUPPORTED_TOOLS
            if ReconService.tool_exists(tool)
        ]

    @staticmethod
    def missing_tools() -> list[str]:
        """Return missing supported tools."""
        return [
            tool
            for tool in SUPPORTED_TOOLS
            if not ReconService.tool_exists(tool)
        ]

    @staticmethod
    def execute(
        command: Iterable[str],
        timeout: int = 300,
    ) -> subprocess.CompletedProcess[str]:
        """
        Execute a local command safely.

        Parameters
        ----------
        command:
            Iterable command.

        timeout:
            Maximum execution time.

        Returns
        -------
        subprocess.CompletedProcess
        """

        return subprocess.run(
            list(command),
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )

    @staticmethod
    def detect_file(path: str | Path) -> str:
        """
        Identify file type using the system 'file' utility.
        """

        result = ReconService.execute(
            ["file", str(path)]
        )

        return result.stdout.strip()

    @staticmethod
    def strings(path: str | Path) -> list[str]:
        """
        Extract printable strings.
        """

        result = ReconService.execute(
            ["strings", str(path)]
        )

        return result.stdout.splitlines()

    @staticmethod
    def whois(target: str) -> str:
        """
        Perform WHOIS lookup.
        """

        result = ReconService.execute(
            ["whois", target]
        )

        return result.stdout

    @staticmethod
    def curl(url: str) -> str:
        """
        Fetch URL contents.
        """

        result = ReconService.execute(
            ["curl", "-L", url]
        )

        return result.stdout
