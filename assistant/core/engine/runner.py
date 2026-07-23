"""
CyberAtlas Engine Runner.

Coordinates execution of a plugin by invoking its lifecycle methods in
a consistent manner. The runner is intentionally transport-agnostic:
plugins may use Python code, local binaries, or other mechanisms.
"""

from __future__ import annotations

import time

from assistant.core.engine.base import BasePlugin
from assistant.core.engine.result import EngineResult


class PluginRunner:
    """
    Executes a CyberAtlas plugin.
    """

    def run(
        self,
        plugin: BasePlugin,
        **kwargs,
    ) -> EngineResult:
        """
        Execute a plugin through the standard lifecycle.

        Lifecycle
        ---------
        initialize()
            ↓
        validate()
            ↓
        execute()
            ↓
        cleanup()
        """

        start = time.perf_counter()

        plugin.initialize()

        try:
            plugin.validate(**kwargs)

            result = plugin.execute(**kwargs)

            result.metadata.finished_at = result.metadata.started_at

            result.metadata.duration = time.perf_counter() - start

            return result

        finally:
            plugin.cleanup()
