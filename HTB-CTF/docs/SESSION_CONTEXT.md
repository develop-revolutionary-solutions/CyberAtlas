# CyberAtlas Session Context

This file provides a lightweight snapshot of the current development session.

It should be updated after every completed implementation.

---

## Project

CyberAtlas

Branch

HTB-CTF

Version

v0.6.0-dev

---

## Current Milestone

HTB Toolkit

Completed

✅ Doctor

✅ Inspect

✅ Workspace

✅ Decode

✅ ELF

✅ PE

✅ PCAP

✅ Web

---

## Current Quality

Compile

```
python -m compileall assistant

PASS
```

Testing

```
pytest

29 passed

0 failed
```

---

## Current Branch Goal

Deliver a production-quality HTB Toolkit before the Hack The Box competition.

---

## Current Module

Crypto

Status

Not Started

---

## Remaining Modules

1. Crypto
2. Networking
3. Linux
4. Forensics
5. Reverse Engineering Enhancements

---

## Standard Module Layout

```
assistant/modules/<module>/

    __init__.py
    service.py
```

CLI

```
assistant/cli/<module>.py
```

Tests

```
tests/modules/test_<module>.py
```

---

## Standard Workflow

Service

↓

CLI

↓

Register CLI

↓

Manual Testing

↓

Unit Tests

↓

Compile

↓

Pytest

↓

Documentation

↓

Git Commit

---

## Important Rules

- Do not skip tests.
- Do not break existing commands.
- Keep modules independent.
- Use Python standard library first.
- Linux-first development.
- CPU-friendly implementation.
- Production-quality code.
- Update documentation after every completed module.

---

## Current Commands

```
cyberatlas doctor

cyberatlas inspect

cyberatlas workspace

cyberatlas decode

cyberatlas elf

cyberatlas pe

cyberatlas pcap

cyberatlas web
```

---

## Current Test Summary

Configuration

- Loader
- Manager
- Validator

Modules

- Decode
- ELF
- PE
- PCAP
- Web

Result

```
29 Passed

0 Failed
```

---

## Resume Point

Continue by implementing the Crypto module.

Do not modify completed modules unless fixing bugs or improving existing functionality.

Maintain backward compatibility.

Keep all tests passing.

---

## Session Checklist

- [ ] Crypto Service
- [ ] Crypto CLI
- [ ] Register CLI
- [ ] Manual Testing
- [ ] Crypto Unit Tests
- [ ] Compile
- [ ] Pytest
- [ ] Update Documentation
- [ ] Git Commit
- [ ] Continue with Networking
