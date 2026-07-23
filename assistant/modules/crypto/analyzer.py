"""
CyberAtlas Crypto Analyzer.

Provides statistical analysis helpers for cryptographic
and CTF-related text analysis.
"""

from __future__ import annotations

import math
import string
from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True)
class EntropyResult:
    """
    Shannon entropy calculation result.
    """

    entropy: float
    length: int


@dataclass(slots=True)
class CharacterAnalysis:
    """
    Character distribution analysis result.
    """

    total_characters: int
    unique_characters: int
    printable_percentage: float


@dataclass(slots=True)
class LanguageScore:
    """
    Basic English language probability score.
    """

    score: float
    confidence: str


class CryptoAnalyzer:
    """
    Statistical crypto analysis utilities.

    Designed for:
    - CTF challenges
    - cipher analysis
    - encoded text inspection
    - threat analysis workflows
    """

    COMMON_ENGLISH_FREQUENCY = {
        "e": 12.70,
        "t": 9.06,
        "a": 8.17,
        "o": 7.51,
        "i": 6.97,
        "n": 6.75,
        "s": 6.33,
        "h": 6.09,
        "r": 5.99,
        "d": 4.25,
    }

    # ---------------------------------------------------------------
    # Entropy
    # ---------------------------------------------------------------

    @staticmethod
    def entropy(
        text: str,
    ) -> EntropyResult:
        """
        Calculate Shannon entropy.
        """

        if not text:
            return EntropyResult(
                entropy=0.0,
                length=0,
            )

        counter = Counter(text)

        length = len(text)

        value = 0.0

        for count in counter.values():

            probability = count / length

            value -= probability * math.log2(
                probability
            )

        return EntropyResult(
            entropy=round(value, 4),
            length=length,
        )

    # ---------------------------------------------------------------
    # Character Analysis
    # ---------------------------------------------------------------

    @staticmethod
    def character_analysis(
        text: str,
    ) -> CharacterAnalysis:
        """
        Analyze character distribution.
        """

        if not text:
            return CharacterAnalysis(
                total_characters=0,
                unique_characters=0,
                printable_percentage=0.0,
            )

        printable = sum(
            1
            for char in text
            if char in string.printable
        )

        return CharacterAnalysis(
            total_characters=len(text),
            unique_characters=len(set(text)),
            printable_percentage=round(
                (printable / len(text)) * 100,
                2,
            ),
        )

    # ---------------------------------------------------------------
    # Index of Coincidence
    # ---------------------------------------------------------------

    @staticmethod
    def index_of_coincidence(
        text: str,
    ) -> float:
        """
        Calculate Index of Coincidence.

        Useful for identifying substitution ciphers.
        """

        cleaned = "".join(
            char.lower()
            for char in text
            if char.isalpha()
        )

        length = len(cleaned)

        if length <= 1:
            return 0.0

        counts = Counter(cleaned)

        numerator = sum(
            count * (count - 1)
            for count in counts.values()
        )

        denominator = length * (length - 1)

        return round(
            numerator / denominator,
            4,
        )

    # ---------------------------------------------------------------
    # Frequency
    # ---------------------------------------------------------------

    @staticmethod
    def frequency(
        text: str,
    ) -> dict[str, float]:
        """
        Return character frequency percentages.
        """

        if not text:
            return {}

        counter = Counter(
            text.lower()
        )

        total = len(text)

        return {
            char: round(
                (count / total) * 100,
                2,
            )
            for char, count in counter.items()
        }

    # ---------------------------------------------------------------
    # English Scoring
    # ---------------------------------------------------------------

    @classmethod
    def english_score(
        cls,
        text: str,
    ) -> LanguageScore:
        """
        Estimate whether text resembles English.
        """

        if not text:
            return LanguageScore(
                score=0.0,
                confidence="unknown",
            )

        frequencies = cls.frequency(text)

        score = 0.0

        for char, expected in cls.COMMON_ENGLISH_FREQUENCY.items():

            actual = frequencies.get(
                char,
                0.0,
            )

            score += max(
                0,
                10 - abs(expected - actual),
            )

        score = round(
            (score / 100) * 100,
            2,
        )

        if score >= 70:
            confidence = "high"

        elif score >= 40:
            confidence = "medium"

        else:
            confidence = "low"

        return LanguageScore(
            score=score,
            confidence=confidence,
        )
