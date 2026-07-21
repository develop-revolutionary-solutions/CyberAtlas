from typing import Any


import pytest


from assistant.config.exceptions import ConfigurationValidationError
from assistant.config.validator import ConfigValidator


def test_validate_valid_configuration(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigValidator should accept a valid configuration.
    """

    ConfigValidator.validate(valid_config)


def test_validate_missing_required_section(
    valid_config: dict[str, Any],
) -> None:

    """
    ConfigValidator should raise ConfigurationValidationError
    when a required section is missing.
    """

    del valid_config["application"]

    with pytest.raises(
        ConfigurationValidationError,
        match=r"Missing required section: 'application'",
    ):
        ConfigValidator.validate(valid_config)


def test_validate_missing_required_key(
    valid_config: dict[str, Any],
) -> None:

    del valid_config["logging"]["file"]

    with pytest.raises(
        ConfigurationValidationError,
        match=r"Missing required key: 'logging\.file'",
    ):
        ConfigValidator.validate(valid_config)


def test_validate_invalid_type(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigValidator should raise ConfigurationValidationError
    when a configuration value has the wrong type.
    """

    valid_config["engine"]["timeout"] = "30"

    with pytest.raises(
        ConfigurationValidationError,
        match=r"Invalid type for 'engine\.timeout'\. Expected int\.",
    ):
        ConfigValidator.validate(valid_config)
