from assistant.config.manager import ConfigManager
from copy import deepcopy
from typing import Any


def test_merge_dicts_overrides_values() -> None:
    """
    ConfigManager should override values from the base dictionary
    with values from the override dictionary.
    """

    base = {
        "logging": {
            "level": "INFO",
            "file": "cyberatlas.log",
        },
    }

    override = {
        "logging": {
            "level": "DEBUG",
        },
    }

    merged = ConfigManager._merge_dicts(
        base,
        override,
    )

    assert merged == {
        "logging": {
            "level": "DEBUG",
            "file": "cyberatlas.log",
        },
    }


def test_get_returns_nested_value(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigManager.get should return a nested value
    using dot notation.
    """

    ConfigManager._config = deepcopy(valid_config)
    ConfigManager._loaded = True

    try:
        assert ConfigManager.get("logging.level") == "INFO"
    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False


def test_has_returns_true_for_existing_key(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigManager.has should return True
    when the requested key exists.
    """

    ConfigManager._config = deepcopy(valid_config)
    ConfigManager._loaded = True

    try:
        assert ConfigManager.has("logging.level") is True
    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False


def test_has_returns_false_for_missing_key(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigManager.has should return False
    when the requested key does not exist.
    """

    ConfigManager._config = deepcopy(valid_config)
    ConfigManager._loaded = True

    try:
        assert ConfigManager.has("logging.invalid_key") is False
    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False


def test_all_returns_configuration(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigManager.all should return the
    complete configuration.
    """

    ConfigManager._config = deepcopy(valid_config)
    ConfigManager._loaded = True

    try:
        config = ConfigManager.all()

        assert config == valid_config

    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False


def test_all_returns_deep_copy(
    valid_config: dict[str, Any],
) -> None:
    """
    ConfigManager.all should return
    a deep copy of the configuration.
    """

    ConfigManager._config = deepcopy(valid_config)
    ConfigManager._loaded = True

    try:
        config = ConfigManager.all()

        config["logging"]["level"] = "DEBUG"

        assert ConfigManager.get("logging.level") == "INFO"

    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False



