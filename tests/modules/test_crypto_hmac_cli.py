"""
CyberAtlas HMAC CLI Tests.

Tests:
- HMAC CLI registration
- HMAC generation command
- HMAC verification command
- HMAC key generation command
- Digest identification
- Key analysis
"""

from __future__ import annotations

from typer.testing import CliRunner

from assistant.cli.app import app


runner = CliRunner()


def test_hmac_command_available() -> None:
    """
    Test HMAC command registration.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "--help",
        ],
    )

    assert result.exit_code == 0
    assert "generate" in result.output
    assert "verify" in result.output
    assert "keygen" in result.output
    assert "identify" in result.output
    assert "analyze-key" in result.output


def test_hmac_generate_command() -> None:
    """
    Test HMAC generation command.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "generate",
            "--message",
            "CyberAtlas",
            "--key",
            "secret",
        ],
    )

    assert result.exit_code == 0
    assert "HMAC Generated Successfully" in result.output
    assert "Algorithm" in result.output
    assert "sha256" in result.output
    assert "Digest Size" in result.output


def test_hmac_verify_valid_command() -> None:
    """
    Test valid HMAC verification.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "verify",
            "--message",
            "CyberAtlas",
            "--key",
            "secret",
            "--digest",
            "415ddd50ad407a3558eb0bd80af7da81d7b887f182c888fe05eefe00492e92ad",
        ],
    )

    assert result.exit_code == 0
    assert "Valid HMAC Signature" in result.output


def test_hmac_verify_invalid_command() -> None:
    """
    Test invalid HMAC verification.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "verify",
            "--message",
            "CyberAtlas",
            "--key",
            "secret",
            "--digest",
            "invalid",
        ],
    )

    assert result.exit_code == 0
    assert "Invalid HMAC Signature" in result.output


def test_hmac_keygen_command() -> None:
    """
    Test HMAC key generation.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "keygen",
        ],
    )

    assert result.exit_code == 0
    assert "Generated HMAC Key" in result.output


def test_hmac_keygen_custom_length() -> None:
    """
    Test custom HMAC key length generation.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "keygen",
            "--length",
            "16",
        ],
    )

    assert result.exit_code == 0
    assert "Generated HMAC Key" in result.output


def test_hmac_identify_command() -> None:
    """
    Test digest identification.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "identify",
            "415ddd50ad407a3558eb0bd80af7da81d7b887f182c888fe05eefe00492e92ad",
        ],
    )

    assert result.exit_code == 0
    assert "sha256" in result.output


def test_hmac_analyze_key_command() -> None:
    """
    Test HMAC key analysis.
    """

    result = runner.invoke(
        app,
        [
            "hmac",
            "analyze-key",
            "secret",
        ],
    )

    assert result.exit_code == 0
    assert "Length Bytes" in result.output
