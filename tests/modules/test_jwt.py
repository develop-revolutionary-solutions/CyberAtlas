"""
Unit tests for the JWT CLI.
"""

from __future__ import annotations

import base64
import json
import time

from typer.testing import CliRunner

from assistant.cli.app import app


runner = CliRunner()


def encode_part(data: dict) -> str:
    """
    Encode JWT section.
    """

    encoded = base64.urlsafe_b64encode(
        json.dumps(data).encode("utf-8")
    )

    return encoded.decode("utf-8").rstrip("=")


def create_token(
    header: dict,
    payload: dict,
    signature: str = "signature",
) -> str:
    """
    Create test JWT.
    """

    return ".".join(
        [
            encode_part(header),
            encode_part(payload),
            signature,
        ]
    )


def test_jwt_cli_success() -> None:
    """
    Test valid JWT analysis command.
    """

    token = create_token(
        {
            "alg": "HS256",
            "typ": "JWT",
        },
        {
            "sub": "cyberatlas",
            "role": "admin",
            "exp": int(time.time()) + 3600,
        },
    )

    result = runner.invoke(
        app,
        [
            "jwt",
            token,
        ],
    )

    assert result.exit_code == 0

    assert "JWT Analysis Complete" in result.stdout

    assert "HS256" in result.stdout

    assert "admin" in result.stdout


def test_jwt_cli_invalid_token() -> None:
    """
    Test invalid JWT handling.
    """

    result = runner.invoke(
        app,
        [
            "jwt",
            "invalid.token",
        ],
    )

    assert result.exit_code == 1

    assert "JWT Analysis Failed" in result.stdout


def test_jwt_cli_security_warning() -> None:
    """
    Test insecure JWT detection.
    """

    token = create_token(
        {
            "alg": "none",
            "typ": "JWT",
        },
        {
            "user": "admin",
        },
        signature="",
    )

    result = runner.invoke(
        app,
        [
            "jwt",
            token,
        ],
    )

    assert result.exit_code == 0

    assert "alg:none" in result.stdout

    assert "signature" in result.stdout
