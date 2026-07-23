"""
CyberAtlas Recon Intelligence Models

Shared data models used by the Recon Intelligence Framework.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass(slots=True)
class ToolStatus:
    """
    Represents the availability of a reconnaissance tool.
    """

    name: str
    installed: bool
    version: str | None = None
    path: str | None = None


@dataclass(slots=True)
class CommandResult:
    """
    Represents the result of executing a reconnaissance command.
    """

    command: list[str]
    return_code: int
    stdout: str
    stderr: str
    duration: float | None = None


@dataclass(slots=True)
class FileInformation:
    """
    Metadata describing a file discovered during reconnaissance.
    """

    path: str
    description: str
    strings: list[str] = field(default_factory=list)


@dataclass(slots=True)
class WhoisInformation:
    """
    WHOIS lookup result.
    """

    target: str
    raw_output: str


@dataclass(slots=True)
class HttpResponse:
    """
    HTTP response captured from a local curl execution.
    """

    url: str
    body: str


@dataclass(slots=True)
class ReconReport:
    """
    Container for an entire reconnaissance session.
    """

    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    tools: list[ToolStatus] = field(default_factory=list)
    commands: list[CommandResult] = field(default_factory=list)
    files: list[FileInformation] = field(default_factory=list)
    whois: list[WhoisInformation] = field(default_factory=list)
    http: list[HttpResponse] = field(default_factory=list)

    def add_tool(self, tool: ToolStatus) -> None:
        """Add a discovered tool."""
        self.tools.append(tool)

    def add_command(self, command: CommandResult) -> None:
        """Add a command execution."""
        self.commands.append(command)

    def add_file(self, file_info: FileInformation) -> None:
        """Add file metadata."""
        self.files.append(file_info)

    def add_whois(self, info: WhoisInformation) -> None:
        """Add WHOIS information."""
        self.whois.append(info)

    def add_http(self, response: HttpResponse) -> None:
        """Add HTTP response."""
        self.http.append(response)
