import pytest

from assistant.config.exceptions import ConfigurationValidationError
from assistant.config.validator import ConfigValidator


def test_validate_valid_configuration() -> None:
    """
    ConfigValidator should accept a valid configuration.
    """

    config = {
        "application": {
            "name": "CyberAtlas",
            "version": "0.1.0",
            "environment": "development",
        },
        "logging": {
            "level": "INFO",
            "file": "cyberatlas.log",
        },
        "engine": {
            "timeout": 30,
            "shell": False,
        },
        "security": {
            "safe_mode": True,
            "allow_network_access": False,
        },
        "workspace": {
            "evidence_directory": "evidence",
            "reports_directory": "reports",
            "notes_directory": "notes",
        },
        "tools": {
            "auto_discovery": True,
        },
    }

    ConfigValidator.validate(config)


def test_validate_missing_required_section() -> None:
    """
    ConfigValidator should raise ConfigurationValidationError
    when a required section is missing.
    """

    # Arrange
    config = {
        "logging": {
            "level": "INFO",
            "file": "cyberatlas.log",
        },
        "engine": {
            "timeout": 30,
            "shell": False,
        },
        "security": {
            "safe_mode": True,
            "allow_network_access": False,
        },
        "workspace": {
            "evidence_directory": "evidence",
            "reports_directory": "reports",
            "notes_directory": "notes",
        },
        "tools": {
            "auto_discovery": True,
        },
    }

    # Act / Assert
    with pytest.raises(
        ConfigurationValidationError,
        match=r"Missing required section: 'application'",
    ):
        ConfigValidator.validate(config)


def test_validate_missing_required_key() -> None:
    """
    ConfigValidator should raise ConfigurationValidationError
    when a required key is missing.
    """

    # Arrange
    config = {
        "application": {
            "name": "CyberAtlas",
            "version": "0.1.0",
            "environment": "development",
        },
        "logging": {
            "level": "INFO",
            # "file" intentionally omitted
        },
        "engine": {
            "timeout": 30,
            "shell": False,
        },
        "security": {
            "safe_mode": True,
            "allow_network_access": False,
        },
        "workspace": {
            "evidence_directory": "evidence",
            "reports_directory": "reports",
            "notes_directory": "notes",
        },
        "tools": {
            "auto_discovery": True,
        },
    }

    # Act / Assert
    with pytest.raises(
        ConfigurationValidationError,
        match=r"Missing required key: 'logging\.file'",
    ):
        ConfigValidator.validate(config)


def test_validate_invalid_type() -> None:
    """
    ConfigValidator should raise ConfigurationValidationError
    when a configuration value has the wrong type.
    """

    # Arrange
    config = {
        "application": {
            "name": "CyberAtlas",
            "version": "0.1.0",
            "environment": "development",
        },
        "logging": {
            "level": "INFO",
            "file": "cyberatlas.log",
        },
        "engine": {
            "timeout": "30",  # Should be int
            "shell": False,
        },
        "security": {
            "safe_mode": True,
            "allow_network_access": False,
        },
        "workspace": {
            "evidence_directory": "evidence",
            "reports_directory": "reports",
            "notes_directory": "notes",
        },
        "tools": {
            "auto_discovery": True,
        },
    }

    # Act / Assert
    with pytest.raises(
        ConfigurationValidationError,
        match=r"Invalid type for 'engine\.timeout'\. Expected int\.",
    ):
        ConfigValidator.validate(config)
