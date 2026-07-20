"""
Centralized configuration manager for CyberAtlas.

The ConfigManager is responsible for loading, validating, caching,
and providing access to application configuration.

Other parts of the application should use this class instead of
interacting directly with ConfigLoader or ConfigValidator.
"""

from __future__ import annotations

import copy

from pathlib import Path
from typing import Any

from assistant.config.loader import ConfigLoader
from assistant.config.validator import ConfigValidator
from assistant.logging import get_logger


class ConfigManager:
    """
    Provides centralized access to application configuration.

    Configuration is loaded once, validated, cached in memory,
    and accessed through class methods.
    """

    _config: dict[str, Any] | None = None
    _loaded: bool = False
    _SENTINEL = object()

    _logger = get_logger(__name__)
    _PROJECT_ROOT = Path(__file__).resolve().parents[2]
    _CONFIG_DIR = _PROJECT_ROOT / "configs"

    @classmethod
    def _merge_dicts(
        cls,
        base: dict[str, Any],
        override: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Recursively merge two dictionaries.

        Values from 'override' take precedence.
        """

        merged = base.copy()

        for key, value in override.items():

            if (
                key in merged
                and isinstance(merged[key], dict)
                and isinstance(value, dict)
            ):
                merged[key] = cls._merge_dicts(merged[key], value)

            else:
                merged[key] = value

        return merged

    @classmethod
    def load(cls) -> None:
        """
        Load, merge, validate, and cache configuration.
        """

        if cls._loaded:
            return

        cls._logger.info("Loading configuration...")

        default_config = ConfigLoader.load(
            cls._CONFIG_DIR / "default.yaml"
        )

        development_path = cls._CONFIG_DIR / "development.yaml"

        if development_path.exists():
            development_config = ConfigLoader.load(
                development_path
            )

            config = cls._merge_dicts(
                default_config,
                development_config,
            )
        else:
            config = default_config

        ConfigValidator.validate(config)

        cls._config = config
        cls._loaded = True

        cls._logger.info(
            "Configuration loaded successfully."
        )

    @classmethod
    def reload(cls) -> None:
        """Reload configuration from disk."""

        cls._logger.info("Reloading configuration...")

        cls._config = None
        cls._loaded = False

        cls.load()

    @classmethod
    def get(cls, key: str, default: Any = None) -> Any:
        """Return a configuration value using dot notation.

        Example:
            ConfigManager.get("logging.level")"""

        if not cls._loaded:
            cls.load()

        assert cls._config is not None

        current: Any = cls._config

        for part in key.split("."):

            if not isinstance(current, dict):
                return default

            if part not in current:
                return default

            current = current[part]

        return current

    @classmethod
    def has(cls, key: str) -> bool:
        """Return True if the configuration key exists."""

        return cls.get(key, cls._SENTINEL) is not cls._SENTINEL

    @classmethod
    def all(cls) -> dict[str, Any]:
        """Return a copy of the complete configuration."""

        if not cls._loaded:
            cls.load()

        assert cls._config is not None

        return copy.deepcopy(cls._config)
