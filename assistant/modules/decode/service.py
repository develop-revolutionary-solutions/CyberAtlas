"""
CyberAtlas Decode Service.

Detects and decodes common CTF encodings.
"""

from __future__ import annotations

import base64
import binascii
import codecs
from dataclasses import dataclass
from urllib.parse import unquote


@dataclass(slots=True)
class DecodeResult:
    encoding: str
    decoded: str


class Decoder:
    """
    Common HTB/CTF decoding helpers.
    """

    @staticmethod
    def decode(text: str) -> DecodeResult:
        text = text.strip()

        # Base64
        try:
            decoded = base64.b64decode(text, validate=True).decode("utf-8")
            return DecodeResult("Base64", decoded)
        except Exception:
            pass

        # URL Encoding
        url_decoded = unquote(text)
        if url_decoded != text:
            return DecodeResult("URL", url_decoded)

        # Binary
        try:
            if (
                set(text.replace(" ", "")) <= {"0", "1"}
                and len(text.replace(" ", "")) % 8 == 0
            ):
                binary = text.replace(" ", "")
                decoded = "".join(
                    chr(int(binary[i:i + 8], 2))
                    for i in range(0, len(binary), 8)
                )
                return DecodeResult("Binary", decoded)
        except Exception:
            pass

        # Hex
        try:
            decoded = bytes.fromhex(text).decode("utf-8")
            return DecodeResult("Hex", decoded)
        except Exception:
            pass

        # Base32
        try:
            decoded = base64.b32decode(text).decode("utf-8")
            return DecodeResult("Base32", decoded)
        except Exception:
            pass

        # Base85
        try:
            decoded = base64.b85decode(text).decode("utf-8")
            return DecodeResult("Base85", decoded)
        except Exception:
            pass

        # ROT13
        raise ValueError("Unable to detect supported encoding.")
