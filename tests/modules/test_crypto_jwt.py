"""
Unit tests for the JWT analyzer.
"""

import base64
import json
import time

from assistant.modules.crypto.jwt import JWTAnalyzer


def encode_part(data: dict) -> str:
    """
    Create JWT Base64URL section.
    """

    encoded = base64.urlsafe_b64encode(
        json.dumps(data).encode("utf-8")
    )

    return encoded.decode("utf-8").rstrip("=")


def create_token(
    header: dict,
    payload: dict,
    signature: str = "signature",
) -> str:
    """
    Create test JWT token.
    """

    return ".".join(
        [
            encode_part(header),
            encode_part(payload),
            signature,
        ]
    )


def test_jwt_analyze() -> None:
    """
    Analyze a normal JWT.
    """

    token = create_token(
        {
            "alg": "HS256",
            "typ": "JWT",
        },
        {
            "sub": "cyberatlas",
            "role": "admin",
            "exp": int(time.time()) + 3600,
        },
    )

    result = JWTAnalyzer.analyze(token)

    assert result.algorithm == "HS256"

    assert result.header["typ"] == "JWT"

    assert result.payload["role"] == "admin"

    assert result.signature_present is True

    assert result.expired is False

    assert result.warnings == []


def test_decode_header() -> None:
    """
    Decode JWT header.
    """

    token = create_token(
        {
            "alg": "RS256",
        },
        {
            "user": "test",
        },
    )

    header = JWTAnalyzer.decode_header(token)

    assert header["alg"] == "RS256"


def test_decode_payload() -> None:
    """
    Decode JWT payload.
    """

    token = create_token(
        {
            "alg": "HS256",
        },
        {
            "username": "admin",
        },
    )

    payload = JWTAnalyzer.decode_payload(token)

    assert payload["username"] == "admin"


def test_detect_none_algorithm() -> None:
    """
    Detect insecure alg:none.
    """

    token = create_token(
        {
            "alg": "none",
        },
        {
            "user": "admin",
        },
        signature="",
    )

    result = JWTAnalyzer.analyze(token)

    assert (
        "JWT uses alg:none."
        in result.warnings
    )

    assert (
        "JWT signature is missing."
        in result.warnings
    )


def test_detect_missing_expiration() -> None:
    """
    Detect missing exp claim.
    """

    token = create_token(
        {
            "alg": "HS256",
        },
        {
            "user": "admin",
        },
    )

    result = JWTAnalyzer.analyze(token)

    assert (
        "JWT has no expiration claim."
        in result.warnings
    )


def test_detect_expired_token() -> None:
    """
    Detect expired JWT.
    """

    token = create_token(
        {
            "alg": "HS256",
        },
        {
            "exp": int(time.time()) - 100,
        },
    )

    result = JWTAnalyzer.analyze(token)

    assert result.expired is True

    assert (
        "JWT token has expired."
        in result.warnings
    )


def test_invalid_jwt_format() -> None:
    """
    Invalid token should fail.
    """

    try:
        JWTAnalyzer.analyze(
            "invalid.token"
        )

    except ValueError as exc:

        assert (
            "Invalid JWT format"
            in str(exc)
        )

    else:
        raise AssertionError(
            "Expected ValueError"
        )
