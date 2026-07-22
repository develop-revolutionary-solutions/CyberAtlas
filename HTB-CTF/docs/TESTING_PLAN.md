# CyberAtlas Testing Plan

Version: v0.6.0-dev

Branch: HTB-CTF

Status: Active Development

Last Updated: 2026-07-22

---

# Purpose

This document defines the testing strategy used throughout CyberAtlas development.

Every module must satisfy the same quality gate before it is considered complete.

Testing is mandatory for all reusable functionality.

---

# Quality Gate

Every completed module must pass

```
python -m compileall assistant
```

Expected

```
PASS
```

and

```
pytest
```

Expected

```
PASS
```

No implementation is considered complete until both checks succeed.

---

# Current Test Status

Compile

```
PASS
```

Pytest

```
29 Passed

0 Failed
```

---

# Testing Workflow

Every module follows the same workflow.

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

# Test Categories

## Configuration

Tests

- Config Loader
- Config Manager
- Config Validator

Purpose

Ensure configuration loading, merging, validation, and defaults work correctly.

---

## Module Tests

Each module receives its own unit test.

Current Modules

```
Doctor
Inspect
Workspace
Decode
ELF
PE
PCAP
Web
```

---

# Manual Testing

Every command should be executed manually.

Example

```
cyberatlas doctor
```

```
cyberatlas version
```

```
cyberatlas inspect sample.bin
```

```
cyberatlas decode SGVsbG8=
```

```
cyberatlas elf challenge
```

```
cyberatlas pe malware.exe
```

```
cyberatlas pcap capture.pcap
```

```
cyberatlas web https://example.com
```

Manual verification checks

- Output formatting
- Error handling
- Invalid input
- CLI usability
- Rich rendering

---

# Automated Testing

Framework

```
pytest
```

Test Location

```
tests/
```

Naming Convention

```
test_<module>.py
```

Example

```
test_decode.py
```

---

# Test Coverage Goals

Each module should test

- Valid input
- Invalid input
- Edge cases
- Exception handling
- Return values

---

# Web Module Testing

Current coverage includes

- HTTP request
- Status code
- Headers
- Cookie extraction
- robots.txt retrieval
- Local HTTP server

Future additions

- Redirects
- HTTPS failures
- Timeout handling
- Invalid certificates
- Large headers

---

# Future Module Tests

## Crypto

- Hash generation
- Hash verification
- Base64
- Hex
- XOR
- Caesar

---

## Networking

- DNS lookup
- Reverse DNS
- CIDR
- Port scan
- Banner grabbing

---

## Linux

- Permissions
- Archives
- Strings
- Hexdump
- File helpers

---

## Forensics

- Metadata
- EXIF
- Timeline
- Hash comparison
- IOC extraction

---

## Reverse Engineering

- ELF enhancements
- PE enhancements
- Entropy
- Sections
- Imports
- Exports

---

# Continuous Verification

After every implementation

Run

```
python -m compileall assistant
```

Then

```
pytest
```

Never continue implementing new modules while tests are failing.

---

# Testing Principles

- Keep tests independent.
- Avoid external dependencies whenever possible.
- Prefer local resources.
- Test services directly.
- Keep CLI tests lightweight.
- Ensure deterministic behavior.

---

# Success Criteria

CyberAtlas maintains

- 100% passing compilation
- 100% passing unit tests
- Stable CLI commands
- Reproducible test results

No feature should be merged until these criteria are met.
