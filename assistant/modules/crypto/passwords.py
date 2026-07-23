"""
CyberAtlas Password Analysis Module.

Provides local password analysis utilities for:
- CTF challenges
- password auditing
- security assessments
- credential analysis workflows

This module performs offline analysis only.
It does not perform online attacks or external lookups.
"""

from __future__ import annotations

import math
import re
import string
from collections import Counter
from dataclasses import dataclass


@dataclass(slots=True)
class PasswordAnalysis:
    """
    Password security analysis result.
    """

    password_length: int
    entropy: float
    score: int
    strength: str
    has_lowercase: bool
    has_uppercase: bool
    has_digits: bool
    has_symbols: bool
    warnings: list[str]


@dataclass(slots=True)
class PasswordPattern:
    """
    Password pattern detection result.
    """

    pattern: str
    matches: list[str]


@dataclass(slots=True)
class MutationResult:
    """
    Password mutation result.
    """

    original: str
    mutations: list[str]


class PasswordAnalyzer:
    """
    Offline password analysis utilities.

    Designed for:
    - CTF password challenges
    - security awareness training
    - password auditing
    - credential analysis
    """

    COMMON_PASSWORDS = {
        "password",
        "password123",
        "admin",
        "admin123",
        "root",
        "letmein",
        "qwerty",
        "123456",
        "12345678",
        "welcome",
        "changeme",
    }

    # ---------------------------------------------------------------
    # Character Analysis
    # ---------------------------------------------------------------

    @staticmethod
    def _character_classes(
        password: str,
    ) -> dict[str, bool]:
        """
        Detect password character classes.
        """

        return {
            "lowercase": any(
                char.islower()
                for char in password
            ),
            "uppercase": any(
                char.isupper()
                for char in password
            ),
            "digits": any(
                char.isdigit()
                for char in password
            ),
            "symbols": any(
                char in string.punctuation
                for char in password
            ),
        }

    # ---------------------------------------------------------------
    # Entropy
    # ---------------------------------------------------------------

    @staticmethod
    def entropy(
        password: str,
    ) -> float:
        """
        Calculate password entropy.

        Uses character distribution entropy.
        """

        if not password:
            return 0.0

        counter = Counter(password)

        length = len(password)

        value = 0.0

        for count in counter.values():

            probability = count / length

            value -= (
                probability
                * math.log2(probability)
            )

        return round(
            value * length,
            2,
        )

    # ---------------------------------------------------------------
    # Password Strength
    # ---------------------------------------------------------------

    @classmethod
    def analyze(
        cls,
        password: str,
    ) -> PasswordAnalysis:
        """
        Perform complete password analysis.
        """

        if not password:
            return PasswordAnalysis(
                password_length=0,
                entropy=0.0,
                score=0,
                strength="empty",
                has_lowercase=False,
                has_uppercase=False,
                has_digits=False,
                has_symbols=False,
                warnings=[
                    "Password is empty."
                ],
            )

        classes = cls._character_classes(
            password
        )

        entropy = cls.entropy(
            password
        )

        score = 0

        warnings: list[str] = []

        length = len(password)

        if length >= 8:
            score += 1
        else:
            warnings.append(
                "Password length is below 8 characters."
            )

        if length >= 12:
            score += 1

        if classes["lowercase"]:
            score += 1
        else:
            warnings.append(
                "Missing lowercase characters."
            )

        if classes["uppercase"]:
            score += 1
        else:
            warnings.append(
                "Missing uppercase characters."
            )

        if classes["digits"]:
            score += 1
        else:
            warnings.append(
                "Missing numeric characters."
            )

        if classes["symbols"]:
            score += 1
        else:
            warnings.append(
                "Missing special characters."
            )

        if password.lower() in cls.COMMON_PASSWORDS:
            score = max(
                0,
                score - 3,
            )

            warnings.append(
                "Password appears in common password list."
            )

        if len(set(password)) == 1:
            warnings.append(
                "Password uses a single repeated character."
            )

            score = max(
                0,
                score - 2,
            )

        if score <= 2:
            strength = "weak"

        elif score <= 4:
            strength = "medium"

        else:
            strength = "strong"

        return PasswordAnalysis(
            password_length=length,
            entropy=entropy,
            score=score,
            strength=strength,
            has_lowercase=classes["lowercase"],
            has_uppercase=classes["uppercase"],
            has_digits=classes["digits"],
            has_symbols=classes["symbols"],
            warnings=warnings,
        )

    # ---------------------------------------------------------------
    # Pattern Detection
    # ---------------------------------------------------------------

    @staticmethod
    def detect_patterns(
        password: str,
    ) -> list[PasswordPattern]:
        """
        Detect common password patterns.
        """

        patterns: list[PasswordPattern] = []

        checks = {
            "numeric_sequence": r"(012|123|234|345|456|567|678|789)",
            "alphabet_sequence": r"(abc|bcd|cde|xyz)",
            "repeated_characters": r"(.)\1{2,}",
            "year_pattern": r"(19\d{2}|20\d{2})",
        }

        for name, regex in checks.items():

            matches = re.findall(
                regex,
                password.lower(),
            )

            if matches:
                patterns.append(
                    PasswordPattern(
                        pattern=name,
                        matches=list(matches),
                    )
                )

        return patterns

    # ---------------------------------------------------------------
    # Passphrase Analysis
    # ---------------------------------------------------------------

    @staticmethod
    def analyze_passphrase(
        phrase: str,
    ) -> dict[str, int | float]:
        """
        Analyze passphrase characteristics.
        """

        words = [
            word
            for word in phrase.split()
            if word
        ]

        return {
            "word_count": len(words),
            "character_count": len(phrase),
            "entropy": PasswordAnalyzer.entropy(
                phrase
            ),
        }

    # ---------------------------------------------------------------
    # Password Mutation
    # ---------------------------------------------------------------

    @staticmethod
    def mutate(
        password: str,
    ) -> MutationResult:
        """
        Generate common password mutations.

        Useful for CTF wordlist preparation.
        """

        mutations = {
            password,
            password.lower(),
            password.upper(),
            password.capitalize(),
            f"{password}123",
            f"{password}!",
            f"{password}@123",
            password.replace(
                "a",
                "@",
            ),
            password.replace(
                "i",
                "1",
            ),
            password.replace(
                "e",
                "3",
            ),
        }

        return MutationResult(
            original=password,
            mutations=sorted(
                mutations
            ),
        )

    # ---------------------------------------------------------------
    # Mask Analysis
    # ---------------------------------------------------------------

    @staticmethod
    def create_mask(
        password: str,
    ) -> str:
        """
        Convert password into cracking mask format.

        Example:
        Cyber123!
        -> LuLululldddS
        """

        output = []

        for char in password:

            if char.isupper():
                output.append("U")

            elif char.islower():
                output.append("L")

            elif char.isdigit():
                output.append("D")

            elif char in string.punctuation:
                output.append("S")

            else:
                output.append("?")

        return "".join(output)
