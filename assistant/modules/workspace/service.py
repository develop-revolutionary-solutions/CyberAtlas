"""
CyberAtlas Workspace Service.

Creates a standard workspace for HTB/CTF challenges.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


DIRECTORIES = (
    "binaries",
    "evidence",
    "loot",
    "notes",
    "output",
    "pcap",
    "screenshots",
    "web",
)


@dataclass(slots=True)
class WorkspaceResult:
    root: Path
    created: list[Path]
    readme_created: bool
    writeup_created: bool



class Workspace:

    @staticmethod
    def create(name: str, base: Path | None = None) -> WorkspaceResult:
        """
        Create a workspace for a challenge.
        """

        if not name.strip():
            raise ValueError("Workspace name cannot be empty.")

        if base is None:
            base = Path.cwd() / "HTB"

        root = base / name
        root.mkdir(parents=True, exist_ok=True)

        created: list[Path] = []

        for directory in DIRECTORIES:
            path = root / directory
            path.mkdir(exist_ok=True)
            created.append(path)

        readme = root / "README.md"
        readme_created = False

        if not readme.exists():
            readme.write_text(
                f"# {name}\n\n"
                "Challenge notes.\n",
                encoding="utf-8",
            )
            readme_created = True


        writeup = root / "writeup.md"
        writeup_created = False

        if not writeup.exists():
            writeup.write_text(
                f"# {name} Writeup\n\n"
                "Document your methodology here.\n",
                encoding="utf-8",
            )
            writeup_created = True


        return WorkspaceResult(
            root=root,
            created=created,
            readme_created=readme_created,
            writeup_created=writeup_created,
        )
