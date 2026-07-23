"""
CyberAtlas Plugin Registry.

Maintains the registry of all available CyberAtlas plugins.

The registry is responsible for:

- Plugin registration
- Plugin lookup
- Plugin enumeration
- Duplicate prevention

The registry does NOT execute plugins.
"""

from __future__ import annotations

from collections.abc import Iterator

from assistant.core.engine.base import BasePlugin
from assistant.core.engine.exceptions import (
    DuplicatePluginError,
    PluginNotFoundError,
)


class PluginRegistry:
    """
    Registry for CyberAtlas plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, BasePlugin] = {}

    def register(self, plugin: BasePlugin) -> None:
        """
        Register a plugin instance.

        Raises
        ------
        DuplicatePluginError
            If the plugin name already exists.
        """

        name = plugin.name.strip().lower()

        if name in self._plugins:
            raise DuplicatePluginError(name)

        self._plugins[name] = plugin

    def unregister(self, name: str) -> None:
        """
        Remove a plugin from the registry.

        Raises
        ------
        PluginNotFoundError
            If the plugin does not exist.
        """

        key = name.strip().lower()

        if key not in self._plugins:
            raise PluginNotFoundError(key)

        del self._plugins[key]

    def get(self, name: str) -> BasePlugin:
        """
        Retrieve a registered plugin.

        Raises
        ------
        PluginNotFoundError
            If no plugin is registered under the given name.
        """

        key = name.strip().lower()

        try:
            return self._plugins[key]
        except KeyError as exc:
            raise PluginNotFoundError(key) from exc

    def exists(self, name: str) -> bool:
        """
        Return True if the plugin is registered.
        """

        return name.strip().lower() in self._plugins

    def list(self) -> list[str]:
        """
        Return all registered plugin names.
        """

        return sorted(self._plugins.keys())

    def plugins(self) -> list[BasePlugin]:
        """
        Return all registered plugin instances.
        """

        return list(self._plugins.values())

    def clear(self) -> None:
        """
        Remove all registered plugins.

        Primarily intended for testing.
        """

        self._plugins.clear()

    def __len__(self) -> int:
        """
        Return the number of registered plugins.
        """

        return len(self._plugins)

    def __contains__(self, name: object) -> bool:
        """
        Support the `in` operator.

        Example
        -------
        "nmap" in registry
        """

        if not isinstance(name, str):
            return False

        return self.exists(name)

    def __iter__(self) -> Iterator[BasePlugin]:
        """
        Iterate over registered plugin instances.
        """

        return iter(self._plugins.values())
