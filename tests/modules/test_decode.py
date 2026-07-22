"""
Unit tests for the CyberAtlas Decode module.
"""

from __future__ import annotations

import pytest

from assistant.modules.decode.service import Decoder


def test_base64() -> None:
    result = Decoder.decode("SGVsbG8=")

    assert result.encoding == "Base64"
    assert result.decoded == "Hello"


def test_hex() -> None:
    result = Decoder.decode("48656c6c6f")

    assert result.encoding == "Hex"
    assert result.decoded == "Hello"


def test_binary() -> None:
    result = Decoder.decode("01001000 01101001")

    assert result.encoding == "Binary"
    assert result.decoded == "Hi"


def test_url() -> None:
    result = Decoder.decode("Hello%20World")

    assert result.encoding == "URL"
    assert result.decoded == "Hello World"


def test_base32() -> None:
    result = Decoder.decode("JBSWY3DP")

    assert result.encoding == "Base32"
    assert result.decoded == "Hello"


def test_base85() -> None:
    result = Decoder.decode("NM&qnZv")

    assert result.encoding == "Base85"
    assert result.decoded == "Hello"


def test_invalid_encoding() -> None:
    with pytest.raises(ValueError):
        Decoder.decode("asdfghjkl")
