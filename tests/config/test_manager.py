from copy import deepcopy
from typing import Any
from unittest.mock import patch

from assistant.config.manager import ConfigManager



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



def test_mock_example() -> None:
    """
    Demonstrate how unittest.mock.patch
    replaces an object temporarily.
    """

    with patch(
        "assistant.config.manager.ConfigLoader.load"
    ) as mock_loader:

        mock_loader.return_value = {
            "application": {
                "name": "CyberAtlas",
            }
        }

        result = mock_loader("dummy.yaml")

        assert result["application"]["name"] == "CyberAtlas"

        mock_loader.assert_called_once_with("dummy.yaml")



def test_load_calls_loader_and_validator() -> None:
    """
    ConfigManager.load should load, validate,
    and cache the configuration.
    """

    ConfigManager._config = None
    ConfigManager._loaded = False

    config = {
        "application": {
            "name": "CyberAtlas",
        }
    }

    with (
        patch(
            "assistant.config.manager.ConfigLoader.load"
        ) as mock_loader,
        patch(
            "assistant.config.manager.ConfigValidator.validate"
        ) as mock_validator,
        patch(
            "pathlib.Path.exists",
            return_value=False,
        ),
    ):

        mock_loader.return_value = config

        ConfigManager.load()

        mock_loader.assert_called_once()

        mock_validator.assert_called_once_with(config)

        assert ConfigManager._config == config
        assert ConfigManager._loaded is True

    ConfigManager._config = None
    ConfigManager._loaded = False



def test_load_does_not_reload_when_already_loaded() -> None:
    """
    ConfigManager.load should immediately return
    when the configuration is already loaded.
    """

    ConfigManager._loaded = True
    ConfigManager._config = {
        "application": {
            "name": "CyberAtlas",
        }
    }

    try:
        with (
            patch(
                "assistant.config.manager.ConfigLoader.load"
            ) as mock_loader,
            patch(
                "assistant.config.manager.ConfigValidator.validate"
            ) as mock_validator,
        ):

            ConfigManager.load()

            mock_loader.assert_not_called()
            mock_validator.assert_not_called()

    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False



def test_reload_calls_load() -> None:
    """
    ConfigManager.reload should clear the cache
    and invoke load() exactly once.
    """

    ConfigManager._config = {
        "application": {
            "name": "CyberAtlas",
        }
    }
    ConfigManager._loaded = True

    try:
        with patch(
            "assistant.config.manager.ConfigManager.load"
        ) as mock_load:

            ConfigManager.reload()

            assert ConfigManager._config is None
            assert ConfigManager._loaded is False

            mock_load.assert_called_once()

    finally:
        ConfigManager._config = None
        ConfigManager._loaded = False




