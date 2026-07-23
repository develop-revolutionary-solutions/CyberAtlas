"""
Recon Intelligence Interfaces.

Defines the common interface implemented by every reconnaissance tool.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from .models import CommandResult


class ReconTool(ABC):
    """
    Base class for all reconnaissance tools.
    """

    #: Tool executable name.
    name: str

    @abstractmethod
    def available(self) -> bool:
        """
        Return True if the underlying executable exists.
        """

    @abstractmethod
    def build_command(self, *args, **kwargs) -> list[str]:
        """
        Construct the command to execute.
        """

    @abstractmethod
    def execute(self, *args, **kwargs) -> CommandResult:
        """
        Execute the reconnaissance tool.
        """

    @abstractmethod
    def parse(self, result: CommandResult):
        """
        Convert raw output into CyberAtlas intelligence.
        """
