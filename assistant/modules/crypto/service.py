from __future__ import annotations

import hashlib
import string
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class HashResult:
    algorithm: str
    digest: str


@dataclass(slots=True)
class FrequencyEntry:
    character: str
    count: int
    percentage: float


class CryptoService:
    """Core cryptographic utility service for the Crypto module."""

    _SUPPORTED_HASHES = {
        "md5",
        "sha1",
        "sha224",
        "sha256",
        "sha384",
        "sha512",
        "sha3_224",
        "sha3_256",
        "sha3_384",
        "sha3_512",
        "blake2b",
        "blake2s",
    }

    # ------------------------------------------------------------------
    # Internal Helpers
    # ------------------------------------------------------------------

    @classmethod
    def _validate_algorithm(cls, algorithm: str) -> str:
        algorithm = algorithm.lower()

        if algorithm not in cls._SUPPORTED_HASHES:
            raise ValueError(
                f"Unsupported hash algorithm '{algorithm}'. "
                f"Supported: {', '.join(sorted(cls._SUPPORTED_HASHES))}"
            )

        return algorithm

    @staticmethod
    def _create_hasher(algorithm: str):
        return hashlib.new(algorithm)

    # ------------------------------------------------------------------
    # Hashing
    # ------------------------------------------------------------------

    @classmethod
    def hash_text(
        cls,
        text: str,
        algorithm: str = "sha256",
    ) -> HashResult:
        algorithm = cls._validate_algorithm(algorithm)

        hasher = cls._create_hasher(algorithm)
        hasher.update(text.encode("utf-8"))

        return HashResult(
            algorithm=algorithm,
            digest=hasher.hexdigest(),
        )

    @classmethod
    def hash_file(
        cls,
        path: Path,
        algorithm: str = "sha256",
    ) -> HashResult:
        algorithm = cls._validate_algorithm(algorithm)

        if not path.exists():
            raise FileNotFoundError(path)

        if not path.is_file():
            raise IsADirectoryError(path)

        hasher = cls._create_hasher(algorithm)

        with path.open("rb") as handle:
            while True:
                chunk = handle.read(8192)
                if not chunk:
                    break
                hasher.update(chunk)

        return HashResult(
            algorithm=algorithm,
            digest=hasher.hexdigest(),
        )

    @classmethod
    def verify_hash(
        cls,
        path: Path,
        expected: str,
        algorithm: str | None = None,
    ) -> bool:
        expected = expected.strip().lower()

        if algorithm is None:
            matches = cls.identify_hash(expected)

            if not matches:
                raise ValueError(
                    "Unable to determine hash algorithm automatically."
                )

            algorithm = matches[0]

        result = cls.hash_file(path, algorithm)

        return result.digest.lower() == expected

    # ------------------------------------------------------------------
    # Hash Identification
    # ------------------------------------------------------------------

    @staticmethod
    def identify_hash(value: str) -> list[str]:
        value = value.strip().lower()

        if not value:
            return []

        if any(c not in string.hexdigits.lower() for c in value):
            return []

        mapping = {
            32: ["md5"],
            40: ["sha1"],
            56: ["sha224"],
            64: ["sha256"],
            96: ["sha384"],
            128: ["sha512", "blake2b"],
        }

        return mapping.get(len(value), [])

    # ------------------------------------------------------------------
    # XOR
    # ------------------------------------------------------------------

    @staticmethod
    def xor_text(
        text: str,
        key: str,
    ) -> str:
        if not key:
            raise ValueError("Key cannot be empty.")

        output = []

        for index, char in enumerate(text):
            key_char = key[index % len(key)]
            output.append(chr(ord(char) ^ ord(key_char)))

        return "".join(output)

    # ------------------------------------------------------------------
    # Caesar Cipher
    # ------------------------------------------------------------------

    @staticmethod
    def caesar_encrypt(
        text: str,
        shift: int,
    ) -> str:
        shift %= 26

        result = []

        for char in text:
            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            elif char.islower():
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))
            else:
                result.append(char)

        return "".join(result)

    @classmethod
    def caesar_decrypt(
        cls,
        text: str,
        shift: int,
    ) -> str:
        return cls.caesar_encrypt(text, -shift)

    # ------------------------------------------------------------------
    # ROT13
    # ------------------------------------------------------------------

    @classmethod
    def rot13(
        cls,
        text: str,
    ) -> str:
        return cls.caesar_encrypt(text, 13)

    # ------------------------------------------------------------------
    # ROT47
    # ------------------------------------------------------------------

    @staticmethod
    def rot47(text: str) -> str:
        result = []

        for char in text:
            code = ord(char)

            if 33 <= code <= 126:
                result.append(chr(33 + ((code - 33 + 47) % 94)))
            else:
                result.append(char)

        return "".join(result)

    # ------------------------------------------------------------------
    # Frequency Analysis
    # ------------------------------------------------------------------

    @staticmethod
    def frequency(text: str) -> list[FrequencyEntry]:
        if not text:
            return []

        counter = Counter(text)
        total = len(text)

        entries = [
            FrequencyEntry(
                character=character,
                count=count,
                percentage=(count / total) * 100,
            )
            for character, count in sorted(
                counter.items(),
                key=lambda item: (-item[1], item[0]),
            )
        ]

        return entries
