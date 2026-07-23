"""
CyberAtlas Engine Execution Context.

Provides immutable execution context shared between the Engine,
Runner, and plugins during execution.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared execution context passed to plugins.

    The context contains execution metadata and user-supplied
    parameters while remaining independent of any specific module.
    """

    plugin: str

    parameters: dict[str, Any] = field(default_factory=dict)

    started_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    timeout: int = 300

    working_directory: str | None = None

    environment: dict[str, str] = field(default_factory=dict)

    tags: list[str] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def get(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve a parameter value.
        """
        return self.parameters.get(key, default)

    def has(self, key: str) -> bool:
        """
        Return True if a parameter exists.
        """
        return key in self.parameters

    def add_tag(self, tag: str) -> None:
        """
        Add an execution tag.
        """
        if tag not in self.tags:
            self.tags.append(tag)

    def set_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Store arbitrary execution metadata.
        """
        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default: Any = None,
    ) -> Any:
        """
        Retrieve metadata.
        """
        return self.metadata.get(key, default)
