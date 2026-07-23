"""
Unit tests for the Crypto Password Analyzer.
"""

from assistant.modules.crypto.passwords import (
    PasswordAnalyzer,
)


def test_password_analysis_strong_password() -> None:
    """
    Test strong password analysis.
    """

    result = PasswordAnalyzer.analyze(
        "CyberAtlas@2026"
    )

    assert result.password_length == 15

    assert result.has_lowercase is True

    assert result.has_uppercase is True

    assert result.has_digits is True

    assert result.has_symbols is True

    assert result.strength in {
        "medium",
        "strong",
    }


def test_password_analysis_empty() -> None:
    """
    Test empty password handling.
    """

    result = PasswordAnalyzer.analyze(
        ""
    )

    assert result.password_length == 0

    assert result.entropy == 0.0

    assert result.strength == "empty"

    assert "Password is empty." in result.warnings


def test_password_entropy() -> None:
    """
    Test entropy calculation.
    """

    result = PasswordAnalyzer.entropy(
        "aaaaBBBB1234!"
    )

    assert result > 0


def test_password_common_detection() -> None:
    """
    Test common password warning.
    """

    result = PasswordAnalyzer.analyze(
        "password123"
    )

    assert (
        "Password appears in common password list."
        in result.warnings
    )


def test_password_pattern_detection() -> None:
    """
    Test password pattern detection.
    """

    result = PasswordAnalyzer.detect_patterns(
        "Admin1232026"
    )

    patterns = [
        item.pattern
        for item in result
    ]

    assert "numeric_sequence" in patterns

    assert "year_pattern" in patterns


def test_passphrase_analysis() -> None:
    """
    Test passphrase analysis.
    """

    result = PasswordAnalyzer.analyze_passphrase(
        "correct horse battery staple"
    )

    assert result["word_count"] == 4

    assert result["character_count"] > 0

    assert result["entropy"] > 0


def test_password_mutation() -> None:
    """
    Test password mutations.
    """

    result = PasswordAnalyzer.mutate(
        "CyberAtlas"
    )

    assert result.original == "CyberAtlas"

    assert "CyberAtlas123" in result.mutations

    assert "CYBERATLAS" in result.mutations


def test_password_mask_creation() -> None:
    """
    Test password mask generation.
    """

    result = PasswordAnalyzer.create_mask(
        "Cyber123!"
    )

    assert result == "ULLLLDDDS"
