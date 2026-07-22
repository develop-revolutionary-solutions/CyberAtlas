# CyberAtlas Command Reference

Version: v0.6.0-dev

Branch: HTB-CTF

Status: Active Development

Last Updated: 2026-07-22

---

# Overview

This document lists every command currently implemented in CyberAtlas.

Only stable and tested commands are documented here.

Quality Status

```
python -m compileall assistant

PASS
```

```
pytest

29 Passed

0 Failed
```

---

# General Syntax

```
cyberatlas <command> [options]
```

Example

```
cyberatlas doctor
```

---

# Available Commands

| Command | Status |
|----------|--------|
| version | ✅ |
| doctor | ✅ |
| inspect | ✅ |
| workspace | ✅ |
| decode | ✅ |
| elf | ✅ |
| pe | ✅ |
| pcap | ✅ |
| web | ✅ |

---

# version

Display CyberAtlas version information.

## Usage

```
cyberatlas version
```

Example

```
cyberatlas version
```

---

# doctor

Perform an environment health check.

Checks may include

- Python Version
- Operating System
- Project Environment
- Dependency Availability

## Usage

```
cyberatlas doctor
```

Example

```
cyberatlas doctor
```

---

# inspect

Inspect a file and identify its basic properties.

## Usage

```
cyberatlas inspect <file>
```

Example

```
cyberatlas inspect sample.bin
```

Typical Output

- File type
- File size
- MIME type
- Extension
- Basic metadata

---

# workspace

Create a standard HTB workspace.

## Usage

```
cyberatlas workspace <directory>
```

Example

```
cyberatlas workspace HTB-Lab
```

Typical Directory Structure

```
HTB-Lab/

notes/
loot/
evidence/
screenshots/
artifacts/
```

---

# decode

Decode common encodings.

Supported

- Base64
- Hexadecimal
- URL Encoding

## Usage

```
cyberatlas decode <value>
```

Example

```
cyberatlas decode SGVsbG8=
```

---

# elf

Analyze ELF executables.

## Usage

```
cyberatlas elf <binary>
```

Example

```
cyberatlas elf ./challenge
```

Displayed Information

- ELF Class
- Architecture
- Endianness
- Entry Point
- File Type

---

# pe

Analyze Windows PE executables.

## Usage

```
cyberatlas pe malware.exe
```

Displayed Information

- Machine Type
- Sections
- Entry Point
- Timestamp
- Characteristics

---

# pcap

Analyze PCAP capture files.

## Usage

```
cyberatlas pcap capture.pcap
```

Displayed Information

- File Information
- Packet Count
- Capture Summary
- Basic Metadata

---

# web

Perform lightweight HTTP reconnaissance.

Designed for

- HTB
- CTF
- Bug Bounty
- Web Enumeration

## Usage

```
cyberatlas web <url>
```

Examples

```
cyberatlas web http://example.com
```

```
cyberatlas web https://httpbin.org
```

```
cyberatlas web https://www.google.com
```

---

## Current Features

### HTTP Request

Performs a GET request using the Python Standard Library.

---

### Summary

Displays

- Status Code
- Content-Type
- Cookie Count

Example

```
Status Code : 200
Content-Type: text/html
Cookies     : 3
```

---

### HTTP Headers

Displays all returned HTTP response headers.

Example

```
Server
Content-Type
Cache-Control
Date
Content-Length
Location
Strict-Transport-Security
```

Long header values are truncated in the CLI for readability while preserving the complete values internally.

---

### Cookie Analysis

Displays all cookies returned by the server.

Information includes

- Name
- Domain
- Path
- Secure
- HttpOnly
- Expires

Example

```
Name        : __cf_bm
Domain      : hackthebox.com
Path        : /
Secure      : Yes
HttpOnly    : Yes
Expires     : 2026-07-22 17:11:39
```

---

### robots.txt

Automatically checks

```
/robots.txt
```

Displays

- File Found
- File Missing
- Contents

Useful for

- Reconnaissance
- Hidden Directories
- Bug Bounty
- HTB Enumeration

---

## Error Handling

The command gracefully handles

- Invalid URLs
- Connection failures
- HTTP errors
- HTTPS errors
- Timeouts
- Missing robots.txt

---

# Planned Commands

The following commands are planned but not yet implemented.

| Command | Status |
|----------|--------|
| crypto | Planned |
| networking | Planned |
| linux | Planned |
| forensics | Planned |
| reversing | Planned |

---

# Standard Development Workflow

Every new command follows the same implementation process.

```
Service

↓

CLI

↓

Register Command

↓

Manual Testing

↓

Unit Tests

↓

python -m compileall assistant

↓

pytest

↓

Documentation

↓

Git Commit
```

---

# Current Test Status

```
python -m compileall assistant

PASS
```

```
pytest

29 Passed

0 Failed
```

---

# Module Progress

| Module | Status |
|----------|--------|
| Doctor | ✅ |
| Inspect | ✅ |
| Workspace | ✅ |
| Decode | ✅ |
| ELF | ✅ |
| PE | ✅ |
| PCAP | ✅ |
| Web | ✅ |
| Crypto | ⏳ |
| Networking | ⏳ |
| Linux | ⏳ |
| Forensics | ⏳ |
| Reverse Engineering | ⏳ |

---

# Notes

- All commands are designed to run on Linux, with Kali Linux as the primary target platform.
- CyberAtlas follows a Service → CLI architecture.
- Business logic resides in module service files.
- CLI commands are responsible only for argument parsing and output formatting.
- New commands must include unit tests and documentation before being considered complete.
