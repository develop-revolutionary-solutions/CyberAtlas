from pathlib import Path

import pytest

from assistant.config.exceptions import (
    InvalidConfigurationError,
    MissingConfigurationError,
)
from assistant.config.loader import ConfigLoader


def test_load_valid_yaml(tmp_path: Path) -> None:
    """
    ConfigLoader should return a dictionary
    when given a valid YAML file.
    """

    # Arrange
    config_file = tmp_path / "config.yaml"

    config_file.write_text(
        """
logging:
  level: INFO
""",
        encoding="utf-8",
    )

    # Act
    config = ConfigLoader.load(config_file)

    # Assert
    assert config == {
        "logging": {
            "level": "INFO",
        }
    }


def test_load_missing_file(tmp_path: Path) -> None:
    """
    ConfigLoader should raise MissingConfigurationError
    when the configuration file does not exist.
    """

    # Arrange
    missing_file = tmp_path / "missing.yaml"

    # Act / Assert
    with pytest.raises(MissingConfigurationError, match="Configuration file not found"):
        ConfigLoader.load(missing_file)


def test_load_invalid_yaml(tmp_path: Path) -> None:
    """
    ConfigLoader should raise InvalidConfigurationError
    when the YAML syntax is invalid.
    """

    # Arrange
    config_file = tmp_path / "invalid.yaml"

    config_file.write_text(
        """
logging:
  level: INFO
  invalid: [1, 2,
""",
        encoding="utf-8",
    )

    # Act / Assert
    with pytest.raises(InvalidConfigurationError):
        ConfigLoader.load(config_file)


def test_load_empty_yaml(tmp_path: Path) -> None:
    """
    ConfigLoader should return an empty dictionary
    when the YAML file is empty.
    """

    # Arrange
    config_file = tmp_path / "empty.yaml"

    config_file.write_text(
        "",
        encoding="utf-8",
    )

    # Act
    config = ConfigLoader.load(config_file)

    # Assert
    assert config == {}
