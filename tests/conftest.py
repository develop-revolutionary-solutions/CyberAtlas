import copy
from typing import Any

import pytest


@pytest.fixture
def valid_config() -> dict[str, Any]:
    """
    Return a fresh valid CyberAtlas configuration.

    Each test receives an independent copy to prevent
    accidental modification of shared state.
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

    return copy.deepcopy(config)
