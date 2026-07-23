"""
CyberAtlas Recon Intelligence Framework

The Recon module provides a unified, local-first interface for common
reconnaissance utilities used in penetration testing, HTB, CTFs, bug bounty,
DFIR, malware analysis, and general cybersecurity workflows.

Design Principles
-----------------
- Local-first
- Offline-friendly
- CPU-friendly
- Linux-first (Kali Linux)
- Modular architecture
- Secure-by-default

Current Capabilities
--------------------
- Tool discovery
- Command execution
- File identification
- Printable string extraction
- WHOIS lookups
- HTTP retrieval

Planned Capabilities
--------------------
- Nmap Intelligence
- HTTPX Intelligence
- Amass Intelligence
- Subfinder Intelligence
- FFUF Intelligence
- Nuclei Intelligence
- Binwalk Intelligence
- Technology Fingerprinting
- Screenshot Intelligence
- Recon Report Generation
"""

from .exceptions import (
    CommandExecutionError,
    CommandTimeoutError,
    FileAnalysisError,
    InvalidTargetError,
    ReconError,
    ToolNotInstalledError,
    UnsupportedToolError,
)
from .models import (
    CommandResult,
    FileInformation,
    HttpResponse,
    ReconReport,
    ToolStatus,
    WhoisInformation,
)
from .service import ReconService

__all__ = [
    # Service
    "ReconService",

    # Models
    "ToolStatus",
    "CommandResult",
    "FileInformation",
    "WhoisInformation",
    "HttpResponse",
    "ReconReport",

    # Exceptions
    "ReconError",
    "ToolNotInstalledError",
    "CommandExecutionError",
    "CommandTimeoutError",
    "InvalidTargetError",
    "UnsupportedToolError",
    "FileAnalysisError",
]
