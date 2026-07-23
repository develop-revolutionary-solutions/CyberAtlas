"""
CyberAtlas Engine.

High-level orchestration layer for executing CyberAtlas plugins.

The Engine is responsible for:

- Plugin registration
- Plugin lookup
- Plugin lifecycle
- Capability validation
- Execution coordination

The Engine delegates execution to PluginRunner and never contains
plugin-specific business logic.
"""

from __future__ import annotations

from assistant.core.engine.base import BasePlugin
from assistant.core.engine.registry import PluginRegistry
from assistant.core.engine.runner import PluginRunner
from assistant.core.engine.result import EngineResult


class Engine:
    """
    CyberAtlas execution engine.
    """

    def __init__(self) -> None:
        self._registry = PluginRegistry()
        self._runner = PluginRunner()

    @property
    def registry(self) -> PluginRegistry:
        """
        Return the plugin registry.
        """
        return self._registry

    def register(self, plugin: BasePlugin) -> None:
        """
        Register a plugin.
        """
        self._registry.register(plugin)

    def unregister(self, name: str) -> None:
        """
        Remove a registered plugin.
        """
        self._registry.unregister(name)

    def execute(
        self,
        plugin_name: str,
        **kwargs,
    ) -> EngineResult:
        """
        Execute a registered plugin.

        Parameters
        ----------
        plugin_name
            Registered plugin identifier.

        **kwargs
            Arguments forwarded to the plugin.

        Returns
        -------
        EngineResult
        """

        plugin = self._registry.get(plugin_name)

        return self._runner.run(
            plugin,
            **kwargs,
        )

    def plugins(self) -> list[str]:
        """
        Return all registered plugin names.
        """
        return self._registry.list()

    def exists(self, plugin_name: str) -> bool:
        """
        Return True if a plugin exists.
        """
        return self._registry.exists(plugin_name)

    def clear(self) -> None:
        """
        Remove all registered plugins.

        Primarily intended for testing.
        """
        self._registry.clear()

    def __len__(self) -> int:
        return len(self._registry)
