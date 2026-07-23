"""
CyberAtlas Crypto Module - HMAC Intelligence

Provides:
- HMAC generation
- HMAC verification
- Supported algorithm detection
- Key analysis
- HMAC comparison helpers

CPU-friendly and local-first.
"""

from __future__ import annotations

import hashlib
import hmac as hmac_lib
import secrets
from dataclasses import dataclass
from typing import Any


SUPPORTED_ALGORITHMS = {
    "md5": hashlib.md5,
    "sha1": hashlib.sha1,
    "sha224": hashlib.sha224,
    "sha256": hashlib.sha256,
    "sha384": hashlib.sha384,
    "sha512": hashlib.sha512,
}


@dataclass
class HMACResult:
    """
    Result container for HMAC operations.
    """

    algorithm: str
    digest: str
    digest_size: int
    success: bool = True
    message: str = ""

    def to_dict(self) -> dict[str, Any]:
        """
        Convert result into dictionary format.
        """

        return {
            "algorithm": self.algorithm,
            "digest": self.digest,
            "digest_size": self.digest_size,
            "success": self.success,
            "message": self.message,
        }


class HMACService:
    """
    HMAC cryptographic utility service.
    """

    def __init__(self) -> None:
        self.algorithms = SUPPORTED_ALGORITHMS

    def supported_algorithms(self) -> list[str]:
        """
        Return available HMAC algorithms.
        """

        return sorted(self.algorithms.keys())

    def _get_algorithm(self, algorithm: str):
        """
        Resolve hashlib algorithm.
        """

        normalized = algorithm.lower().replace("-", "")

        if normalized not in self.algorithms:
            raise ValueError(
                f"Unsupported HMAC algorithm: {algorithm}"
            )

        return self.algorithms[normalized]

    def generate(
        self,
        message: str | bytes,
        key: str | bytes,
        algorithm: str = "sha256",
    ) -> HMACResult:
        """
        Generate HMAC digest.

        Args:
            message:
                Data to authenticate.

            key:
                Secret key.

            algorithm:
                Hash algorithm.
        """

        digest_module = self._get_algorithm(algorithm)

        message_bytes = self._to_bytes(message)
        key_bytes = self._to_bytes(key)

        digest = hmac_lib.new(
            key_bytes,
            message_bytes,
            digest_module,
        ).hexdigest()

        return HMACResult(
            algorithm=algorithm.lower(),
            digest=digest,
            digest_size=len(bytes.fromhex(digest)),
            message="HMAC generated successfully",
        )

    def verify(
        self,
        message: str | bytes,
        key: str | bytes,
        expected_digest: str,
        algorithm: str = "sha256",
    ) -> bool:
        """
        Verify HMAC digest.

        Uses constant-time comparison.
        """

        result = self.generate(
            message=message,
            key=key,
            algorithm=algorithm,
        )

        return hmac_lib.compare_digest(
            result.digest.lower(),
            expected_digest.lower(),
        )

    def analyze_key(
        self,
        key: str | bytes,
    ) -> dict[str, Any]:
        """
        Analyze HMAC secret key properties.
        """

        key_bytes = self._to_bytes(key)

        unique_bytes = len(set(key_bytes))

        return {
            "length_bytes": len(key_bytes),
            "length_bits": len(key_bytes) * 8,
            "unique_bytes": unique_bytes,
            "entropy_estimate_bits": round(
                len(key_bytes)
                * (unique_bytes / 256)
                * 8,
                2,
            ),
            "hex_preview": key_bytes.hex()[:32],
        }

    def generate_key(
        self,
        length: int = 32,
    ) -> str:
        """
        Generate cryptographically secure random HMAC key.

        Default:
            256-bit key.
        """

        if length <= 0:
            raise ValueError(
                "Key length must be greater than zero"
            )

        return secrets.token_hex(length)

    def identify_digest(
        self,
        digest: str,
    ) -> dict[str, Any]:
        """
        Identify possible HMAC digest algorithms
        based on length.
        """

        digest_length = len(digest)

        matches = []

        for name, algorithm in self.algorithms.items():
            if algorithm().digest_size * 2 == digest_length:
                matches.append(name)

        return {
            "digest_length": digest_length,
            "possible_algorithms": matches,
            "count": len(matches),
        }

    def compare(
        self,
        first: str,
        second: str,
    ) -> bool:
        """
        Secure constant-time digest comparison.
        """

        return hmac_lib.compare_digest(
            first,
            second,
        )

    @staticmethod
    def _to_bytes(
        value: str | bytes,
    ) -> bytes:
        """
        Convert string input into bytes.
        """

        if isinstance(value, bytes):
            return value

        return value.encode("utf-8")


def generate_hmac(
    message: str | bytes,
    key: str | bytes,
    algorithm: str = "sha256",
) -> HMACResult:
    """
    Convenience wrapper for HMAC generation.
    """

    service = HMACService()

    return service.generate(
        message=message,
        key=key,
        algorithm=algorithm,
    )


def verify_hmac(
    message: str | bytes,
    key: str | bytes,
    digest: str,
    algorithm: str = "sha256",
) -> bool:
    """
    Convenience wrapper for HMAC verification.
    """

    service = HMACService()

    return service.verify(
        message=message,
        key=key,
        expected_digest=digest,
        algorithm=algorithm,
    )
