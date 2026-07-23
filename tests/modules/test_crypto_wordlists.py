
"""
Unit tests for the Crypto Wordlist Manager.
"""

from pathlib import Path

import pytest

from assistant.modules.crypto.wordlists import (
    WordlistManager,
)


def test_wordlist_load(tmp_path: Path) -> None:
    """
    Test loading a wordlist file.
    """

    wordlist = tmp_path / "words.txt"

    wordlist.write_text(
        "admin\npassword\nroot\n",
        encoding="utf-8",
    )

    result = WordlistManager.load(
        wordlist
    )

    assert result == [
        "admin",
        "password",
        "root",
    ]


def test_wordlist_load_missing_file() -> None:
    """
    Test missing wordlist handling.
    """

    with pytest.raises(
        FileNotFoundError
    ):

        WordlistManager.load(
            Path(
                "missing_wordlist.txt"
            )
        )


def test_wordlist_clean() -> None:
    """
    Test word cleanup.
    """

    result = WordlistManager.clean(
        [
            " admin ",
            "",
            " root ",
        ]
    )

    assert result == [
        "admin",
        "root",
    ]


def test_wordlist_unique() -> None:
    """
    Test duplicate removal.
    """

    result = WordlistManager.unique(
        [
            "admin",
            "root",
            "admin",
        ]
    )

    assert result == [
        "admin",
        "root",
    ]


def test_wordlist_statistics() -> None:
    """
    Test wordlist statistics.
    """

    result = WordlistManager.statistics(
        [
            "a",
            "admin",
            "password",
        ]
    )

    assert result.total_words == 3

    assert result.unique_words == 3

    assert result.shortest_word == 1

    assert result.longest_word == 8


def test_wordlist_length_filter() -> None:
    """
    Test length filtering.
    """

    result = WordlistManager.filter_length(
        [
            "a",
            "admin",
            "password",
        ],
        minimum=5,
    )

    assert result == [
        "admin",
        "password",
    ]


def test_wordlist_contains() -> None:
    """
    Test keyword search.
    """

    result = WordlistManager.contains(
        [
            "administrator",
            "root",
            "admin123",
        ],
        "admin",
    )

    assert result == [
        "administrator",
        "admin123",
    ]


def test_word_mutation() -> None:
    """
    Test word mutations.
    """

    result = WordlistManager.mutate(
        "CyberAtlas"
    )

    assert result.original == "CyberAtlas"

    assert "CyberAtlas123" in result.mutations

    assert "CYBERATLAS" in result.mutations


def test_word_combination() -> None:
    """
    Test word combination generation.
    """

    result = WordlistManager.combine(
        [
            "cyber",
        ],
        [
            "atlas",
            "2026",
        ],
    )

    assert result == [
        "cyberatlas",
        "cyber2026",
    ]
