"""
CyberAtlas Crypto Module Tests - HMAC

Tests:
- HMAC generation
- HMAC verification
- Algorithm handling
- Key analysis
- Digest identification
- Secure comparison
"""

from __future__ import annotations

import pytest

from assistant.modules.crypto.hmac import (
    HMACService,
    generate_hmac,
    verify_hmac,
)


@pytest.fixture
def service() -> HMACService:
    """
    Provide HMAC service fixture.
    """

    return HMACService()


def test_supported_algorithms(service: HMACService) -> None:
    """
    Test supported HMAC algorithms.
    """

    algorithms = service.supported_algorithms()

    assert "sha256" in algorithms
    assert "sha512" in algorithms


def test_generate_hmac(service: HMACService) -> None:
    """
    Test HMAC generation.
    """

    result = service.generate(
        message="CyberAtlas",
        key="secret-key",
        algorithm="sha256",
    )

    assert result.success is True
    assert result.algorithm == "sha256"
    assert len(result.digest) == 64
    assert result.digest_size == 32


def test_generate_wrapper() -> None:
    """
    Test convenience generation wrapper.
    """

    result = generate_hmac(
        message="hello",
        key="world",
    )

    assert result.success is True
    assert len(result.digest) == 64


def test_verify_valid_hmac(service: HMACService) -> None:
    """
    Test successful HMAC verification.
    """

    result = service.generate(
        message="data",
        key="key",
    )

    assert service.verify(
        message="data",
        key="key",
        expected_digest=result.digest,
    )


def test_verify_invalid_hmac(service: HMACService) -> None:
    """
    Test failed HMAC verification.
    """

    assert service.verify(
        message="data",
        key="key",
        expected_digest="invalid",
    ) is False


def test_verify_wrapper() -> None:
    """
    Test convenience verification wrapper.
    """

    result = generate_hmac(
        message="test",
        key="secret",
    )

    assert verify_hmac(
        message="test",
        key="secret",
        digest=result.digest,
    )


def test_invalid_algorithm(service: HMACService) -> None:
    """
    Test unsupported algorithm handling.
    """

    with pytest.raises(ValueError):
        service.generate(
            message="test",
            key="key",
            algorithm="unknown",
        )


def test_key_analysis(service: HMACService) -> None:
    """
    Test HMAC key analysis.
    """

    result = service.analyze_key(
        "secret-key",
    )

    assert result["length_bytes"] == 10
    assert result["length_bits"] == 80
    assert "entropy_estimate_bits" in result


def test_generate_key(service: HMACService) -> None:
    """
    Test secure key generation.
    """

    key = service.generate_key(
        length=32,
    )

    assert isinstance(key, str)
    assert len(key) == 64


def test_invalid_key_length(service: HMACService) -> None:
    """
    Test invalid key generation length.
    """

    with pytest.raises(ValueError):
        service.generate_key(
            length=0,
        )


def test_identify_digest(service: HMACService) -> None:
    """
    Test digest identification.
    """

    result = service.identify_digest(
        "a" * 64,
    )

    assert "sha256" in result["possible_algorithms"]


def test_secure_compare(service: HMACService) -> None:
    """
    Test secure comparison.
    """

    assert service.compare(
        "abc",
        "abc",
    )

    assert not service.compare(
        "abc",
        "xyz",
    )


def test_bytes_input(service: HMACService) -> None:
    """
    Test bytes message and key handling.
    """

    result = service.generate(
        message=b"data",
        key=b"secret",
    )

    assert result.success is True
