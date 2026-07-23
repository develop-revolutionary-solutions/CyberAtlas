"""
CyberAtlas Core Engine Exceptions.

Defines the common exception hierarchy used throughout the CyberAtlas
execution engine. Module-specific exceptions should inherit from these
where appropriate.
"""

from __future__ import annotations


class EngineError(Exception):
    """
    Base exception for all engine-related errors.
    """


class PluginError(EngineError):
    """
    Base exception for plugin-related failures.
    """


class PluginNotFoundError(PluginError):
    """
    Raised when a requested plugin is not registered.
    """

    def __init__(self, plugin_name: str) -> None:
        self.plugin_name = plugin_name
        super().__init__(f"Plugin '{plugin_name}' is not registered.")


class DuplicatePluginError(PluginError):
    """
    Raised when attempting to register a plugin more than once.
    """

    def __init__(self, plugin_name: str) -> None:
        self.plugin_name = plugin_name
        super().__init__(f"Plugin '{plugin_name}' is already registered.")


class PluginValidationError(PluginError):
    """
    Raised when a plugin fails validation before execution.
    """


class CapabilityError(EngineError):
    """
    Raised when a required capability is unavailable.
    """


class ExecutionError(EngineError):
    """
    Raised when plugin execution fails.
    """


class TimeoutError(ExecutionError):
    """
    Raised when execution exceeds the configured timeout.
    """
