"""
CyberAtlas JWT Analyzer.

Provides local JWT inspection capabilities for:
- CTF challenges
- Bug bounty testing
- API security assessment
- SOC investigations
"""

from __future__ import annotations

import base64
import json
import time
from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class JWTAnalysis:
    """
    JWT inspection result.
    """

    token: str
    algorithm: str
    header: dict[str, Any]
    payload: dict[str, Any]
    signature_present: bool
    expired: bool | None
    warnings: list[str]


class JWTAnalyzer:
    """
    JSON Web Token analysis utility.

    This class performs static inspection only.
    It does not verify cryptographic signatures.
    """

    # ---------------------------------------------------------------
    # Base64URL Helpers
    # ---------------------------------------------------------------

    @staticmethod
    def _decode_base64url(
        value: str,
    ) -> bytes:
        """
        Decode Base64URL data.
        """

        padding = "=" * (
            4 - (len(value) % 4)
        )

        return base64.urlsafe_b64decode(
            value + padding
        )

    @classmethod
    def _decode_json_part(
        cls,
        value: str,
    ) -> dict[str, Any]:
        """
        Decode JWT JSON section.
        """

        decoded = cls._decode_base64url(
            value
        )

        return json.loads(
            decoded.decode("utf-8")
        )

    # ---------------------------------------------------------------
    # Token Validation
    # ---------------------------------------------------------------

    @staticmethod
    def _split_token(
        token: str,
    ) -> tuple[str, str, str]:
        """
        Split JWT token parts.
        """

        parts = token.strip().split(".")

        if len(parts) != 3:
            raise ValueError(
                "Invalid JWT format. Expected header.payload.signature"
            )

        return (
            parts[0],
            parts[1],
            parts[2],
        )

    # ---------------------------------------------------------------
    # Expiration Check
    # ---------------------------------------------------------------

    @staticmethod
    def _check_expiration(
        payload: dict[str, Any],
    ) -> bool | None:
        """
        Check JWT expiration claim.
        """

        if "exp" not in payload:
            return None

        try:
            return (
                int(payload["exp"])
                < int(time.time())
            )

        except (TypeError, ValueError):
            return None

    # ---------------------------------------------------------------
    # Analysis
    # ---------------------------------------------------------------

    @classmethod
    def analyze(
        cls,
        token: str,
    ) -> JWTAnalysis:
        """
        Analyze JWT token.
        """

        header_part, payload_part, signature = (
            cls._split_token(token)
        )

        header = cls._decode_json_part(
            header_part
        )

        payload = cls._decode_json_part(
            payload_part
        )

        algorithm = str(
            header.get(
                "alg",
                "unknown",
            )
        )

        warnings: list[str] = []

        if algorithm.lower() == "none":
            warnings.append(
                "JWT uses alg:none."
            )

        if not signature:
            warnings.append(
                "JWT signature is missing."
            )

        if "exp" not in payload:
            warnings.append(
                "JWT has no expiration claim."
            )

        expired = cls._check_expiration(
            payload
        )

        if expired:
            warnings.append(
                "JWT token has expired."
            )

        return JWTAnalysis(
            token=token,
            algorithm=algorithm,
            header=header,
            payload=payload,
            signature_present=bool(signature),
            expired=expired,
            warnings=warnings,
        )

    # ---------------------------------------------------------------
    # Helpers
    # ---------------------------------------------------------------

    @classmethod
    def decode_header(
        cls,
        token: str,
    ) -> dict[str, Any]:
        """
        Decode JWT header only.
        """

        header, _, _ = cls._split_token(
            token
        )

        return cls._decode_json_part(
            header
        )

    @classmethod
    def decode_payload(
        cls,
        token: str,
    ) -> dict[str, Any]:
        """
        Decode JWT payload only.
        """

        _, payload, _ = cls._split_token(
            token
        )

        return cls._decode_json_part(
            payload
        )
