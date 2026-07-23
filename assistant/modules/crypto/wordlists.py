"""
CyberAtlas Wordlist Utilities.

Provides local wordlist processing helpers for:
- CTF password attacks
- bug bounty preparation
- credential analysis
- offline security workflows

This module performs local processing only.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class WordlistStats:
    """
    Wordlist statistics result.
    """

    total_words: int
    unique_words: int
    shortest_word: int
    longest_word: int


@dataclass(slots=True)
class WordMutation:
    """
    Word mutation result.
    """

    original: str
    mutations: list[str]


class WordlistManager:
    """
    Offline wordlist processing utilities.

    Designed for:
    - HTB challenges
    - CTF workflows
    - password auditing
    - custom wordlist creation
    """

    # ---------------------------------------------------------------
    # Loading
    # ---------------------------------------------------------------

    @staticmethod
    def load(
        path: Path,
    ) -> list[str]:
        """
        Load words from a local wordlist file.
        """

        if not path.exists():
            raise FileNotFoundError(path)

        if not path.is_file():
            raise IsADirectoryError(path)

        words = []

        with path.open(
            "r",
            encoding="utf-8",
            errors="ignore",
        ) as handle:

            for line in handle:

                word = line.strip()

                if word:
                    words.append(word)

        return words

    # ---------------------------------------------------------------
    # Cleaning
    # ---------------------------------------------------------------

    @staticmethod
    def clean(
        words: list[str],
    ) -> list[str]:
        """
        Remove empty values and whitespace.
        """

        return [
            word.strip()
            for word in words
            if word.strip()
        ]

    @staticmethod
    def unique(
        words: list[str],
    ) -> list[str]:
        """
        Remove duplicate words.
        """

        return sorted(
            set(words)
        )

    # ---------------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------------

    @staticmethod
    def statistics(
        words: list[str],
    ) -> WordlistStats:
        """
        Generate wordlist statistics.
        """

        if not words:

            return WordlistStats(
                total_words=0,
                unique_words=0,
                shortest_word=0,
                longest_word=0,
            )

        lengths = [
            len(word)
            for word in words
        ]

        return WordlistStats(
            total_words=len(words),
            unique_words=len(set(words)),
            shortest_word=min(lengths),
            longest_word=max(lengths),
        )

    # ---------------------------------------------------------------
    # Filtering
    # ---------------------------------------------------------------

    @staticmethod
    def filter_length(
        words: list[str],
        minimum: int = 0,
        maximum: int | None = None,
    ) -> list[str]:
        """
        Filter words by length.
        """

        result = []

        for word in words:

            length = len(word)

            if length < minimum:
                continue

            if maximum is not None and length > maximum:
                continue

            result.append(word)

        return result

    @staticmethod
    def contains(
        words: list[str],
        keyword: str,
    ) -> list[str]:
        """
        Find words containing keyword.
        """

        keyword = keyword.lower()

        return [
            word
            for word in words
            if keyword in word.lower()
        ]

    # ---------------------------------------------------------------
    # Mutations
    # ---------------------------------------------------------------

    @staticmethod
    def mutate(
        word: str,
    ) -> WordMutation:
        """
        Generate common word mutations.
        """

        mutations = {
            word,
            word.lower(),
            word.upper(),
            word.capitalize(),
            f"{word}123",
            f"{word}!",
            f"{word}@123",
            f"{word}2026",
        }

        replacements = {
            "a": "@",
            "e": "3",
            "i": "1",
            "o": "0",
            "s": "$",
        }

        replaced = word.lower()

        for old, new in replacements.items():

            replaced = replaced.replace(
                old,
                new,
            )

        mutations.add(
            replaced
        )

        return WordMutation(
            original=word,
            mutations=sorted(
                mutations
            ),
        )

    # ---------------------------------------------------------------
    # Combination Generation
    # ---------------------------------------------------------------

    @staticmethod
    def combine(
        first: list[str],
        second: list[str],
    ) -> list[str]:
        """
        Combine two wordlists.
        """

        combinations = []

        for left in first:

            for right in second:

                combinations.append(
                    f"{left}{right}"
                )

        return combinations
