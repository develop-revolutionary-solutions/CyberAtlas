"""
Doctor service.

Performs environment validation for CyberAtlas.
"""

from __future__ import annotations

import platform
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path


REQUIRED_TOOLS = [
    "file",
    "strings",
    "readelf",
    "objdump",
    "checksec",
    "tshark",
    "curl",
    "wget",
    "nmap",
    "ffuf",
    "gobuster",
    "binwalk",
    "exiftool",
    "steghide",
    "john",
    "hashcat",
    "sqlmap",
    "yara",
    "r2",
    "gdb",
]


@dataclass(slots=True)
class ToolStatus:
    """Status of an external tool."""

    name: str
    installed: bool
    path: str | None


def check_tools() -> list[ToolStatus]:
    """Check required external tools."""

    results: list[ToolStatus] = []

    for tool in REQUIRED_TOOLS:
        location = shutil.which(tool)

        results.append(
            ToolStatus(
                name=tool,
                installed=location is not None,
                path=location,
            )
        )

    return results


def python_version() -> str:
    """Return Python version."""

    return platform.python_version()


def operating_system() -> str:
    """Return OS information."""

    return f"{platform.system()} {platform.release()}"


def workspace_writable(path: Path | None = None) -> bool:
    """Check whether workspace is writable."""

    if path is None:
        path = Path.cwd()

    try:
        test = path / ".cyberatlas_test"

        test.write_text("ok")

        test.unlink()

        return True

    except Exception:
        return False


def overall_status() -> dict:
    """Return complete environment status."""

    return {
        "python": python_version(),
        "os": operating_system(),
        "workspace": workspace_writable(),
        "tools": check_tools(),
        "executable": sys.executable,
    }
