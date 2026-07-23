"""
CyberAtlas Engine Capabilities.

Defines the capability model used by the CyberAtlas Engine to validate
plugin runtime requirements before execution.

Capabilities describe *what* a plugin needs, not *how* it is executed.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from pathlib import Path
import shutil


class Capability(ABC):
    """
    Base capability definition.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Human-readable capability name.
        """

    @abstractmethod
    def available(self) -> bool:
        """
        Return True if this capability is available.
        """


class BinaryCapability(Capability):
    """
    Represents a required executable on PATH.
    """

    def __init__(self, binary: str) -> None:
        self.binary = binary

    @property
    def name(self) -> str:
        return f"binary:{self.binary}"

    def available(self) -> bool:
        return shutil.which(self.binary) is not None


class PythonCapability(Capability):
    """
    Indicates the plugin only requires the Python runtime.
    """

    @property
    def name(self) -> str:
        return "python"

    def available(self) -> bool:
        return True


class FileCapability(Capability):
    """
    Represents a required file.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    @property
    def name(self) -> str:
        return f"file:{self.path}"

    def available(self) -> bool:
        return self.path.exists()


class DirectoryCapability(Capability):
    """
    Represents a required directory.
    """

    def __init__(self, path: str | Path) -> None:
        self.path = Path(path)

    @property
    def name(self) -> str:
        return f"directory:{self.path}"

    def available(self) -> bool:
        return self.path.is_dir()


class NetworkCapability(Capability):
    """
    Indicates the plugin requires network connectivity.

    Network reachability checks are intentionally not performed here.
    The engine records this requirement so higher-level policy can
    decide whether network-dependent plugins are permitted.
    """

    @property
    def name(self) -> str:
        return "network"

    def available(self) -> bool:
        return True


class FilesystemCapability(Capability):
    """
    Indicates the plugin requires filesystem access.
    """

    @property
    def name(self) -> str:
        return "filesystem"

    def available(self) -> bool:
        return True
