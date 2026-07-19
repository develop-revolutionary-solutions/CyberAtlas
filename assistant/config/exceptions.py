"""
CyberAtlas Configuration Exceptions
===================================

This module defines the custom exception hierarchy used by the
CyberAtlas configuration system.

Using custom exceptions makes error handling more precise, improves
debugging, and allows other components to respond appropriately to
different configuration failures.

Exception Hierarchy
-------------------

Exception
└── ConfigurationError
    ├── MissingConfigurationError
    ├── InvalidConfigurationError
    └── ConfigurationValidationError
"""


class ConfigurationError(Exception):
    """
    Base exception for all configuration-related errors.

    Every configuration exception in CyberAtlas should inherit from this
    class so callers can catch all configuration errors with a single
    exception handler if desired.
    """


class MissingConfigurationError(ConfigurationError):
    """
    Raised when a required configuration file cannot be found.

    Example:
        configs/default.yaml does not exist.
    """


class InvalidConfigurationError(ConfigurationError):
    """
    Raised when a configuration file contains invalid YAML syntax or
    cannot be parsed successfully.
    """


class ConfigurationValidationError(ConfigurationError):
    """
    Raised when a configuration file is syntactically valid but fails
    validation.

    Examples:
        - Required keys are missing.
        - Values have incorrect data types.
        - Unsupported configuration values are provided.
    """
