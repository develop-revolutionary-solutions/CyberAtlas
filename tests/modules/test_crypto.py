"""
Unit tests for the Crypto module.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import pytest

from assistant.modules.crypto.service import CryptoService


def test_hash_text_sha256() -> None:
    """
    SHA256 hashing of text.
    """

    result = CryptoService.hash_text("CyberAtlas")

    assert result.algorithm == "sha256"
    assert (
        result.digest
        == hashlib.sha256(b"CyberAtlas").hexdigest()
    )


def test_hash_text_md5() -> None:
    """
    MD5 hashing of text.
    """

    result = CryptoService.hash_text(
        "CyberAtlas",
        "md5",
    )

    assert result.algorithm == "md5"
    assert (
        result.digest
        == hashlib.md5(b"CyberAtlas").hexdigest()
    )


def test_hash_file(tmp_path: Path) -> None:
    """
    Hash a file.
    """

    sample = tmp_path / "sample.txt"
    sample.write_text("CyberAtlas", encoding="utf-8")

    result = CryptoService.hash_file(sample)

    expected = hashlib.sha256(
        b"CyberAtlas"
    ).hexdigest()

    assert result.digest == expected


def test_verify_hash() -> None:
    """
    Verify a file hash.
    """

    sample = Path("crypto_test.txt")
    sample.write_text(
        "CyberAtlas",
        encoding="utf-8",
    )

    digest = hashlib.sha256(
        b"CyberAtlas"
    ).hexdigest()

    assert CryptoService.verify_hash(
        sample,
        digest,
    )

    sample.unlink()


def test_identify_md5() -> None:
    """
    Detect MD5 hash.
    """

    algorithms = CryptoService.identify_hash(
        "5d41402abc4b2a76b9719d911017c592"
    )

    assert "md5" in algorithms


def test_identify_sha1() -> None:
    """
    Detect SHA1 hash.
    """

    algorithms = CryptoService.identify_hash(
        "2aae6c35c94fcfb415dbe95f408b9ce91ee846ed"
    )

    assert "sha1" in algorithms


def test_identify_sha256() -> None:
    """
    Detect SHA256 hash.
    """

    algorithms = CryptoService.identify_hash(
        hashlib.sha256(b"CyberAtlas").hexdigest()
    )

    assert "sha256" in algorithms


def test_identify_unknown() -> None:
    """
    Unknown hash.
    """

    assert CryptoService.identify_hash("abc") == []


def test_xor_roundtrip() -> None:
    """
    XOR encryption/decryption.
    """

    plaintext = "CyberAtlas"

    encrypted = CryptoService.xor_text(
        plaintext,
        "key",
    )

    decrypted = CryptoService.xor_text(
        encrypted,
        "key",
    )

    assert decrypted == plaintext


def test_xor_empty_key() -> None:
    """
    Empty XOR key should fail.
    """

    with pytest.raises(ValueError):
        CryptoService.xor_text(
            "hello",
            "",
        )


def test_caesar_encrypt() -> None:
    """
    Caesar encryption.
    """

    assert (
        CryptoService.caesar_encrypt(
            "ABC",
            3,
        )
        == "DEF"
    )


def test_caesar_decrypt() -> None:
    """
    Caesar decryption.
    """

    assert (
        CryptoService.caesar_decrypt(
            "DEF",
            3,
        )
        == "ABC"
    )


def test_rot13() -> None:
    """
    ROT13.
    """

    assert (
        CryptoService.rot13(
            "Hello"
        )
        == "Uryyb"
    )


def test_rot47() -> None:
    """
    ROT47.
    """

    encrypted = CryptoService.rot47("CyberAtlas")

    assert encrypted != "CyberAtlas"

    assert (
        CryptoService.rot47(encrypted)
        == "CyberAtlas"
    )


def test_frequency() -> None:
    """
    Frequency analysis.
    """

    entries = CryptoService.frequency("aaabbc")

    assert entries[0].character == "a"
    assert entries[0].count == 3
    assert round(entries[0].percentage, 2) == 50.00


def test_invalid_algorithm() -> None:
    """
    Unsupported hash algorithm.
    """

    with pytest.raises(ValueError):
        CryptoService.hash_text(
            "CyberAtlas",
            "invalid",
        )


def test_missing_file() -> None:
    """
    Missing file should raise FileNotFoundError.
    """

    with pytest.raises(FileNotFoundError):
        CryptoService.hash_file(
            Path("does_not_exist.txt")
        )
