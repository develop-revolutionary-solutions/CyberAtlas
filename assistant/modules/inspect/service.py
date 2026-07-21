"""
CyberAtlas Inspect Service

Performs quick triage of a file for CTF/HTB competitions.
"""

from __future__ import annotations

import hashlib
import math
import re
import subprocess
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


CHUNK_SIZE = 1024 * 1024

FLAG_PATTERNS = [
    r"HTB\{.*?\}",
    r"flag\{.*?\}",
    r"FLAG\{.*?\}",
    r"picoCTF\{.*?\}",
]

URL_REGEX = re.compile(rb"https?://[^\s\"'<>]+")
EMAIL_REGEX = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
IP_REGEX = re.compile(rb"\b(?:\d{1,3}\.){3}\d{1,3}\b")


@dataclass(slots=True)
class InspectResult:
    path: str
    size: int
    file_type: str

    md5: str
    sha1: str
    sha256: str
    sha512: str

    entropy: float

    urls: list[str]
    emails: list[str]
    ips: list[str]
    flags: list[str]

    recommendations: list[str]


class Inspector:

    @staticmethod
    def detect_file_type(path: Path) -> str:
        try:
            result = subprocess.run(
                ["file", "-b", str(path)],
                capture_output=True,
                text=True,
                check=False,
            )
            return result.stdout.strip()
        except Exception:
            return "Unknown"

    @staticmethod
    def calculate_hashes(path: Path):

        md5 = hashlib.md5()
        sha1 = hashlib.sha1()
        sha256 = hashlib.sha256()
        sha512 = hashlib.sha512()

        with path.open("rb") as f:
            while chunk := f.read(CHUNK_SIZE):
                md5.update(chunk)
                sha1.update(chunk)
                sha256.update(chunk)
                sha512.update(chunk)

        return (
            md5.hexdigest(),
            sha1.hexdigest(),
            sha256.hexdigest(),
            sha512.hexdigest(),
        )

    @staticmethod
    def entropy(path: Path) -> float:

        data = path.read_bytes()

        if not data:
            return 0.0

        counts = Counter(data)

        length = len(data)

        entropy = 0.0

        for count in counts.values():
            p = count / length
            entropy -= p * math.log2(p)

        return round(entropy, 3)

    @staticmethod
    def extract_strings(path: Path) -> bytes:

        try:
            result = subprocess.run(
                ["strings", "-a", str(path)],
                capture_output=True,
                check=False,
            )

            return result.stdout

        except Exception:
            return b""

    @staticmethod
    def recommendations(file_type: str) -> list[str]:

        ft = file_type.lower()

        if "elf" in ft:
            return [
                "Run: checksec",
                "Run: readelf -a",
                "Run: objdump -d",
                "Open in Ghidra",
            ]

        if "pe32" in ft or "windows" in ft:
            return [
                "Inspect imports",
                "Check packer",
                "Open in PEStudio",
            ]

        if "zip" in ft:
            return [
                "Extract archive",
                "Inspect contents",
            ]

        if "png" in ft or "jpeg" in ft:
            return [
                "Run exiftool",
                "Run zsteg",
                "Run binwalk",
            ]

        if "pcap" in ft:
            return [
                "Run tshark",
                "Inspect DNS",
                "Inspect HTTP",
            ]

        return []

    @classmethod
    def inspect(cls, filename: str) -> InspectResult:

        path = Path(filename)

        if not path.exists():
            raise FileNotFoundError(filename)

        file_type = cls.detect_file_type(path)

        md5, sha1, sha256, sha512 = cls.calculate_hashes(path)

        entropy = cls.entropy(path)

        strings = cls.extract_strings(path)

        urls = sorted(
            {
                m.decode(errors="ignore")
                for m in URL_REGEX.findall(strings)
            }
        )

        emails = sorted(
            {
                m.decode(errors="ignore")
                for m in EMAIL_REGEX.findall(strings)
            }
        )

        ips = sorted(
            {
                m.decode(errors="ignore")
                for m in IP_REGEX.findall(strings)
            }
        )

        decoded = strings.decode(errors="ignore")

        flags = []

        for pattern in FLAG_PATTERNS:
            flags.extend(re.findall(pattern, decoded))

        return InspectResult(
            path=str(path),
            size=path.stat().st_size,
            file_type=file_type,
            md5=md5,
            sha1=sha1,
            sha256=sha256,
            sha512=sha512,
            entropy=entropy,
            urls=urls,
            emails=emails,
            ips=ips,
            flags=flags,
            recommendations=cls.recommendations(file_type),
        )
