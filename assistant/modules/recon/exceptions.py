"""
CyberAtlas Recon Intelligence Exceptions

Custom exception hierarchy for the Recon Intelligence Framework.
"""

from __future__ import annotations


class ReconError(Exception):
    """
    Base exception for all Recon Intelligence errors.
    """

    pass


class ToolNotInstalledError(ReconError):
    """
    Raised when a required reconnaissance tool is not installed.
    """

    def __init__(self, tool: str) -> None:
        self.tool = tool
        super().__init__(f"Required tool '{tool}' is not installed.")


class CommandExecutionError(ReconError):
    """
    Raised when a reconnaissance command fails.
    """

    def __init__(
        self,
        command: list[str],
        return_code: int,
        stderr: str = "",
    ) -> None:
        self.command = command
        self.return_code = return_code
        self.stderr = stderr

        message = (
            f"Command failed with exit code {return_code}: "
            f"{' '.join(command)}"
        )

        if stderr.strip():
            message += f"\n{stderr.strip()}"

        super().__init__(message)


class CommandTimeoutError(ReconError):
    """
    Raised when a reconnaissance command exceeds the timeout.
    """

    def __init__(
        self,
        command: list[str],
        timeout: int,
    ) -> None:
        self.command = command
        self.timeout = timeout

        super().__init__(
            f"Command timed out after {timeout} seconds: "
            f"{' '.join(command)}"
        )


class InvalidTargetError(ReconError):
    """
    Raised when an invalid hostname, IP address, URL,
    or file path is supplied.
    """

    def __init__(self, target: str) -> None:
        self.target = target
        super().__init__(f"Invalid target: {target}")


class UnsupportedToolError(ReconError):
    """
    Raised when attempting to use an unsupported reconnaissance tool.
    """

    def __init__(self, tool: str) -> None:
        self.tool = tool
        super().__init__(f"Unsupported reconnaissance tool: {tool}")


class FileAnalysisError(ReconError):
    """
    Raised when local file analysis cannot be completed.
    """

    def __init__(self, path: str, reason: str = "") -> None:
        self.path = path
        self.reason = reason

        message = f"Unable to analyze file: {path}"

        if reason:
            message += f" ({reason})"

        super().__init__(message)
