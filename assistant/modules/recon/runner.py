"""
CyberAtlas Recon Command Runner

Provides a secure, reusable interface for executing local reconnaissance tools.

Design Goals
------------
- Local-first
- CPU-friendly
- No shell=True
- Centralized timeout handling
- Common error handling
- Reusable across all Recon Intelligence modules
"""

from __future__ import annotations

import shutil
import subprocess
import time
from typing import Iterable

from .exceptions import (
    CommandExecutionError,
    CommandTimeoutError,
    ToolNotInstalledError,
)
from .models import CommandResult


class CommandRunner:
    """
    Generic command execution engine for Recon Intelligence.
    """

    DEFAULT_TIMEOUT = 300

    @staticmethod
    def tool_exists(tool: str) -> bool:
        """
        Return True if a binary exists on PATH.
        """
        return shutil.which(tool) is not None

    @staticmethod
    def require_tool(tool: str) -> None:
        """
        Ensure a required binary exists.
        """
        if not CommandRunner.tool_exists(tool):
            raise ToolNotInstalledError(tool)

    @staticmethod
    def execute(
        command: Iterable[str],
        timeout: int | None = None,
    ) -> CommandResult:
        """
        Execute a command and return a normalized result.
        """

        command = list(command)

        if not command:
            raise ValueError("Command cannot be empty.")

        CommandRunner.require_tool(command[0])

        start = time.perf_counter()

        try:
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=timeout or CommandRunner.DEFAULT_TIMEOUT,
                check=False,
            )

        except subprocess.TimeoutExpired as exc:
            raise CommandTimeoutError(
                command,
                timeout or CommandRunner.DEFAULT_TIMEOUT,
            ) from exc

        duration = time.perf_counter() - start

        output = CommandResult(
            command=command,
            return_code=result.returncode,
            stdout=result.stdout,
            stderr=result.stderr,
            duration=duration,
        )

        if result.returncode != 0:
            raise CommandExecutionError(
                command=command,
                return_code=result.returncode,
                stderr=result.stderr,
            )

        return output
