"""
Unit tests for the Crypto Analyzer.
"""

from assistant.modules.crypto.analyzer import CryptoAnalyzer


def test_entropy() -> None:
    """
    Calculate Shannon entropy.
    """

    result = CryptoAnalyzer.entropy(
        "aaaaabbbbbccccc"
    )

    assert result.length == 15

    assert result.entropy > 0


def test_entropy_empty() -> None:
    """
    Empty input entropy.
    """

    result = CryptoAnalyzer.entropy("")

    assert result.length == 0

    assert result.entropy == 0.0


def test_character_analysis() -> None:
    """
    Character distribution analysis.
    """

    result = CryptoAnalyzer.character_analysis(
        "CyberAtlas123"
    )

    assert result.total_characters == 13

    assert result.unique_characters > 1

    assert result.printable_percentage == 100.0


def test_index_of_coincidence() -> None:
    """
    Index of coincidence calculation.
    """

    result = CryptoAnalyzer.index_of_coincidence(
        "AAAAABBBBB"
    )

    assert result > 0


def test_index_of_coincidence_empty() -> None:
    """
    Empty text IC.
    """

    result = CryptoAnalyzer.index_of_coincidence(
        ""
    )

    assert result == 0.0


def test_frequency() -> None:
    """
    Character frequency calculation.
    """

    result = CryptoAnalyzer.frequency(
        "aaabbc"
    )

    assert result["a"] == 50.0

    assert result["b"] == 33.33

    assert result["c"] == 16.67


def test_english_score() -> None:
    """
    English language scoring.
    """

    result = CryptoAnalyzer.english_score(
        "the quick brown fox jumps over the lazy dog"
    )

    assert result.score > 0

    assert result.confidence in {
        "high",
        "medium",
        "low",
    }


def test_english_score_empty() -> None:
    """
    Empty language score.
    """

    result = CryptoAnalyzer.english_score("")

    assert result.score == 0.0

    assert result.confidence == "unknown"
