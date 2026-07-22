"""
CyberAtlas PE Service.

Fast Windows PE binary inspection for HTB and CTF challenges.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class PEResult:
    path: str
    file_type: str
    architecture: str
    bits: str
    image_base: str
    entry_point: str
    aslr: str
    dep: str
    sections: list[str]
    imports: list[str]


class PEAnalyzer:
    """
    Analyze PE binaries using standard Linux tools.
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
    def analyze(cls, filename: str) -> PEResult:
        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(filename)

        file_output = cls._run("file", str(path))
        objdump_output = cls._run("objdump", "-x", str(path))

        architecture = "Unknown"
        bits = "Unknown"
        image_base = "Unknown"
        entry_point = "Unknown"
        aslr = "Unknown"
        dep = "Unknown"

        sections: list[str] = []
        imports: list[str] = []

        #
        # Determine architecture / bitness
        #

        if "PE32+" in file_output:
            bits = "PE32+ (64-bit)"
        elif "PE32" in file_output:
            bits = "PE32 (32-bit)"

        lower = file_output.lower()

        if "x86-64" in lower or "x86_64" in lower:
            architecture = "x86-64"
        elif "intel 80386" in lower:
            architecture = "x86"
        elif "aarch64" in lower:
            architecture = "ARM64"
        elif "arm" in lower:
            architecture = "ARM"

        #
        # Parse objdump
        #

        in_sections = False
        in_imports = False

        for raw in objdump_output.splitlines():

            line = raw.strip()

            #
            # Image base
            #

            if line.startswith("ImageBase"):
                parts = line.split()

                if len(parts) >= 2:
                    image_base = parts[-1]

            #
            # Entry point
            #

            elif line.startswith("AddressOfEntryPoint"):
                parts = line.split()

                if len(parts) >= 2:
                    entry_point = parts[-1]

            #
            # DLL Characteristics
            #

            elif "DYNAMIC_BASE" in line:
                aslr = "Enabled"

            elif "NX_COMPAT" in line:
                dep = "Enabled"

            #
            # Section table
            #

            if line.startswith("Sections:"):
                in_sections = True
                in_imports = False
                continue

            if line.startswith("SYMBOL TABLE:"):
                in_sections = False

            if in_sections:

                tokens = line.split()

                if len(tokens) >= 2:

                    name = tokens[1]

                    if (
                        name.startswith(".")
                        and name not in sections
                    ):
                        sections.append(name)

            #
            # Import table
            #

            if "The Import Tables" in line:
                in_imports = True
                in_sections = False
                continue

            if in_imports:

                if line.startswith("DLL Name:"):

                    dll = (
                        line.split(":", 1)[1]
                        .strip()
                    )

                    if dll not in imports:
                        imports.append(dll)

        if aslr == "Unknown":
            aslr = "Disabled"

        if dep == "Unknown":
            dep = "Disabled"

        return PEResult(
            path=str(path.resolve()),
            file_type=file_output,
            architecture=architecture,
            bits=bits,
            image_base=image_base,
            entry_point=entry_point,
            aslr=aslr,
            dep=dep,
            sections=sections,
            imports=imports,
        )
