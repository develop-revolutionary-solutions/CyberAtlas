"""
CyberAtlas Configuration Loader
===============================

This module is responsible for safely loading YAML configuration files.

Responsibilities:
- Read YAML files.
- Parse YAML into Python dictionaries.
- Raise CyberAtlas configuration exceptions.

It does NOT:
- Validate configuration values.
- Merge multiple configuration files.
- Apply default values.
"""

from pathlib import Path

import yaml

from assistant.config.exceptions import (
    InvalidConfigurationError,
    MissingConfigurationError,
)


class ConfigLoader:
    """
    Loads YAML configuration files.

    This class has a single responsibility:
    read a YAML file and return its contents as a dictionary.
    """

    @staticmethod
    def load(path: str | Path) -> dict:
        """
        Load a YAML configuration file.

        Args:
            path:
                Path to the YAML configuration file.

        Returns:
            dict:
                Parsed configuration.

        Raises:
            MissingConfigurationError:
                If the configuration file does not exist.

            InvalidConfigurationError:
                If the YAML file cannot be parsed.
        """

        config_path = Path(path)

        if not config_path.exists():
            raise MissingConfigurationError(
                f"Configuration file not found: {config_path}"
            )

        try:
            with config_path.open("r", encoding="utf-8") as file:
                data = yaml.safe_load(file)

            return data or {}

        except yaml.YAMLError as exc:
            raise InvalidConfigurationError(
                f"Invalid YAML in configuration file: {config_path}"
            ) from exc
