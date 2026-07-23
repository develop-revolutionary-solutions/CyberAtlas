"""
CyberAtlas Core Engine.

The Core Engine provides the common execution framework used by all
CyberAtlas modules. It standardizes plugin registration, execution,
capability validation, lifecycle management, and result handling.

Modules such as Recon, Crypto, Malware, DFIR, Web, OSINT, Cloud,
Windows, and Active Directory build upon this engine rather than
implementing their own execution framework.
"""

from assistant.core.engine.base import BasePlugin
from assistant.core.engine.capabilities import (
    BinaryCapability,
    Capability,
    DirectoryCapability,
    FileCapability,
    FilesystemCapability,
    NetworkCapability,
    PythonCapability,
)
from assistant.core.engine.context import ExecutionContext
from assistant.core.engine.engine import Engine
from assistant.core.engine.exceptions import (
    CapabilityError,
    DuplicatePluginError,
    EngineError,
    ExecutionError,
    PluginError,
    PluginNotFoundError,
    PluginValidationError,
    TimeoutError,
)
from assistant.core.engine.registry import PluginRegistry
from assistant.core.engine.result import (
    EngineResult,
    ExecutionMetadata,
    ResultStatus,
)
from assistant.core.engine.runner import PluginRunner

__all__ = [
    # Engine
    "Engine",
    "PluginRunner",
    "PluginRegistry",

    # Base
    "BasePlugin",

    # Context
    "ExecutionContext",

    # Results
    "EngineResult",
    "ExecutionMetadata",
    "ResultStatus",

    # Capabilities
    "Capability",
    "BinaryCapability",
    "PythonCapability",
    "NetworkCapability",
    "FilesystemCapability",
    "FileCapability",
    "DirectoryCapability",

    # Exceptions
    "EngineError",
    "PluginError",
    "PluginNotFoundError",
    "DuplicatePluginError",
    "PluginValidationError",
    "CapabilityError",
    "ExecutionError",
    "TimeoutError",
]
