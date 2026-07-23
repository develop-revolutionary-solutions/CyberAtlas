"""
CyberAtlas Core Engine Result Models.

Defines the standardized execution result returned by every CyberAtlas
plugin. This provides a consistent interface regardless of whether the
plugin wraps a CLI tool, a Python library, or native Python logic.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any


class ResultStatus(str, Enum):
    """
    Standard execution status.
    """

    SUCCESS = "success"
    FAILURE = "failure"
    PARTIAL = "partial"
    SKIPPED = "skipped"


@dataclass(slots=True)
class ExecutionMetadata:
    """
    Metadata describing a plugin execution.
    """

    plugin: str
    started_at: datetime = field(default_factory=lambda: datetime.now(UTC))
    finished_at: datetime | None = None
    duration: float = 0.0
    command: list[str] = field(default_factory=list)


@dataclass(slots=True)
class EngineResult:
    """
    Standardized execution result returned by every plugin.

    Plugins should place structured intelligence into `data`.
    Raw tool output may be stored in `raw_output` when appropriate.
    """

    status: ResultStatus
    metadata: ExecutionMetadata

    data: dict[str, Any] = field(default_factory=dict)

    raw_output: str | None = None

    warnings: list[str] = field(default_factory=list)

    errors: list[str] = field(default_factory=list)

    artifacts: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)

    confidence: float = 1.0

    def succeeded(self) -> bool:
        """
        Return True if execution succeeded.
        """
        return self.status is ResultStatus.SUCCESS

    def failed(self) -> bool:
        """
        Return True if execution failed.
        """
        return self.status is ResultStatus.FAILURE

    def add_warning(self, message: str) -> None:
        """
        Add a warning.
        """
        self.warnings.append(message)

    def add_error(self, message: str) -> None:
        """
        Add an execution error.
        """
        self.errors.append(message)

    def add_artifact(self, path: str) -> None:
        """
        Register a generated artifact.
        """
        self.artifacts.append(path)

    def add_tag(self, tag: str) -> None:
        """
        Add a classification tag.
        """
        self.tags.append(tag)
