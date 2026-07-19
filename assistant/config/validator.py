"""
CyberAtlas Configuration Validator
==================================

This module validates configuration dictionaries loaded by
ConfigLoader.

Responsibilities:
- Verify required sections exist.
- Verify required keys exist.
- Verify basic data types.

It does NOT:
- Load configuration files.
- Merge configurations.
- Manage configuration state.
"""

from assistant.config.exceptions import ConfigurationValidationError


class ConfigValidator:
    """
    Validates CyberAtlas configuration data.
    """

    REQUIRED_SCHEMA = {
        "application": [
            "name",
            "version",
            "environment",
        ],
        "logging": [
            "level",
            "file",
        ],
        "engine": [
            "timeout",
            "shell",
        ],
        "security": [
            "safe_mode",
            "allow_network_access",
        ],
        "workspace": [
            "evidence_directory",
            "reports_directory",
            "notes_directory",
        ],
        "tools": [
            "auto_discovery",
        ],
    }

    TYPE_SCHEMA = {
        ("engine", "timeout"): int,
        ("engine", "shell"): bool,
        ("security", "safe_mode"): bool,
        ("security", "allow_network_access"): bool,
        ("tools", "auto_discovery"): bool,
    }

    @classmethod
    def validate(cls, config: dict) -> None:
        """
        Validate a CyberAtlas configuration dictionary.

        Raises:
            ConfigurationValidationError
                If validation fails.
        """

        # Validate required sections
        for section in cls.REQUIRED_SCHEMA:

            if section not in config:
                raise ConfigurationValidationError(
                    f"Missing required section: '{section}'"
                )

        # Validate required keys
        for section, keys in cls.REQUIRED_SCHEMA.items():

            for key in keys:

                if key not in config[section]:
                    raise ConfigurationValidationError(
                        f"Missing required key: '{section}.{key}'"
                    )

        # Validate basic data types
        for (section, key), expected_type in cls.TYPE_SCHEMA.items():

            value = config[section][key]

            if not isinstance(value, expected_type):
                raise ConfigurationValidationError(
                    f"Invalid type for '{section}.{key}'. "
                    f"Expected {expected_type.__name__}."
                )
