"""
CyberAtlas Engine Base Classes.

Defines the abstract base class that every CyberAtlas plugin must
implement. Plugins may wrap external CLI tools, Python libraries,
or native Python logic while exposing a consistent execution model.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from assistant.core.engine.result import EngineResult


class BasePlugin(ABC):
    """
    Abstract base class for all CyberAtlas plugins.
    """

    #: Unique plugin identifier.
    name: str

    #: Human-readable plugin description.
    description: str = ""

    #: Module category (e.g. recon, crypto, malware).
    category: str = ""

    #: Semantic version.
    version: str = "1.0.0"

    @abstractmethod
    def validate(self, **kwargs) -> None:
        """
        Validate input parameters and runtime prerequisites.

        Raises
        ------
        PluginValidationError
            If validation fails.
        """

    @abstractmethod
    def execute(self, **kwargs) -> EngineResult:
        """
        Execute the plugin.

        Returns
        -------
        EngineResult
            Standardized execution result.
        """

    @abstractmethod
    def capabilities(self) -> list[str]:
        """
        Return the capabilities required by this plugin.

        Examples
        --------
        ["python"]

        ["binary:nmap"]

        ["binary:nuclei"]

        ["network"]

        ["filesystem"]
        """

    def initialize(self) -> None:
        """
        Optional initialization hook.

        Called once before first execution.
        """

    def cleanup(self) -> None:
        """
        Optional cleanup hook.

        Called after execution if needed.
        """
