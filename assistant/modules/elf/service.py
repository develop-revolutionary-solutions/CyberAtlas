"""
CyberAtlas ELF Service.

Fast ELF binary inspection for HTB and CTF challenges.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ELFResult:
    path: str
    file_type: str
    architecture: str
    bits: str
    endian: str
    entry_point: str
    pie: str
    nx: str
    relro: str
    canary: str
    stripped: str
    interpreter: str


class ELFAnalyzer:
    """
    Analyze ELF binaries using standard Linux tools.
    """

    @staticmethod
    def _run(*command: str) -> str:
        """
        Execute a command and return stdout.
        """

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=False,
        )

        return result.stdout.strip()

    @classmethod
    def analyze(cls, filename: str) -> ELFResult:
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(filename)

        file_output = cls._run("file", str(path))
        readelf_output = cls._run("readelf", "-h", str(path))
        program_headers = cls._run("readelf", "-l", str(path))
        checksec_output = cls._run(
            "checksec",
            f"--file={path}",
        )

        architecture = "Unknown"
        bits = "Unknown"
        endian = "Unknown"
        entry = "Unknown"
        interpreter = "None"

        for line in readelf_output.splitlines():

            line = line.strip()

            if line.startswith("Class:"):
                bits = line.split(":", 1)[1].strip()

            elif line.startswith("Machine:"):
                architecture = line.split(":", 1)[1].strip()

            elif line.startswith("Data:"):
                endian = line.split(":", 1)[1].strip()

            elif line.startswith("Entry point address:"):
                entry = line.split(":", 1)[1].strip()

        for line in program_headers.splitlines():
            if "Requesting program interpreter:" in line:
                interpreter = (
                    line.split(":", 1)[1]
                    .replace("]", "")
                    .strip()
                )

        pie = "Unknown"
        nx = "Unknown"
        relro = "Unknown"
        canary = "Unknown"

        if "PIE enabled" in checksec_output:
            pie = "Enabled"
        elif "No PIE" in checksec_output:
            pie = "Disabled"

        if "NX enabled" in checksec_output:
            nx = "Enabled"
        elif "NX disabled" in checksec_output:
            nx = "Disabled"

        if "Full RELRO" in checksec_output:
            relro = "Full"
        elif "Partial RELRO" in checksec_output:
            relro = "Partial"
        elif "No RELRO" in checksec_output:
            relro = "None"

        if "Canary found" in checksec_output:
            canary = "Present"
        elif "No canary found" in checksec_output:
            canary = "Absent"

        stripped = "Unknown"

        if "not stripped" in file_output:
            stripped = "No"
        elif "stripped" in file_output:
            stripped = "Yes"

        return ELFResult(
            path=str(path.resolve()),
            file_type=file_output,
            architecture=architecture,
            bits=bits,
            endian=endian,
            entry_point=entry,
            pie=pie,
            nx=nx,
            relro=relro,
            canary=canary,
            stripped=stripped,
            interpreter=interpreter,
        )
