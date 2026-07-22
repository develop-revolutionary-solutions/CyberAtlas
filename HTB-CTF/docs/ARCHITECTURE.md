# CyberAtlas Architecture

Version: v0.6.0-dev

Branch: HTB-CTF

Status: Active Development

Last Updated: 2026-07-22

---

# Overview

CyberAtlas is a modular, offline-first, AI-assisted Cyber Security Assistant designed for:

- Hack The Box
- Capture The Flag (CTF)
- Bug Bounty
- Penetration Testing
- Reverse Engineering
- Digital Forensics
- Malware Analysis
- SOC Operations
- Threat Hunting

The project emphasizes modularity, maintainability, and production-quality engineering while remaining lightweight enough to run on CPU-only hardware.

---

# Architectural Principles

CyberAtlas follows these principles throughout development.

- Modular Design
- Separation of Concerns
- Offline First
- Linux First
- CPU Friendly
- Production Quality
- Test Driven
- Extensible
- Standard Library First
- Documentation Driven

---

# High-Level Architecture

```
                        CyberAtlas
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
     CLI Layer          Service Layer       Configuration
        │                    │                    │
        └──────────────┬─────┴──────────────┬─────┘
                       │                    │
                 Module Services      Shared Utilities
                       │                    │
                       └────────────┬───────┘
                                    │
                              Core Framework
                                    │
                           Logging / Config / Tests
```

---

# Repository Structure

```
CyberAtlas/

assistant/
│
├── ai/
├── cli/
├── config/
├── core/
├── database/
├── engine/
├── knowledge/
├── logging/
├── modules/
├── playbooks/
├── plugins/
├── security/
├── services/
└── utils/

configs/

docs/

tests/

assets/
```

---

# Layered Design

## 1. CLI Layer

Responsible for user interaction.

Responsibilities

- Parse command-line arguments
- Validate user input
- Invoke service layer
- Format terminal output
- Display errors gracefully

Location

```
assistant/cli/
```

Current Commands

```
doctor
inspect
workspace
decode
elf
pe
pcap
web
```

---

## 2. Service Layer

Contains all business logic.

Responsibilities

- Process requests
- Execute analysis
- Return structured results
- Avoid terminal output
- Remain reusable

Location

```
assistant/modules/
```

Example

```
assistant/modules/web/service.py
```

The service layer must never depend on the CLI.

---

## 3. Configuration Layer

Responsible for configuration loading and validation.

Location

```
assistant/config/
```

Components

- Config Loader
- Config Manager
- Config Validator

---

## 4. Logging Layer

Provides centralized logging.

Location

```
assistant/logging/
```

Responsibilities

- Console logging
- File logging
- Debug support
- Error reporting

---

## 5. Testing Layer

Ensures implementation quality.

Location

```
tests/
```

Current Status

```
29 Passing Tests
```

Every module requires

- Unit Tests
- Manual Validation
- Compile Verification

---

# Module Architecture

Every CyberAtlas module follows the same structure.

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

Documentation

Updated after module completion.

---

# Current Modules

Completed

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

Planned

```
Crypto
Networking
Linux
Forensics
Reverse Engineering Enhancements
```

---

# Data Flow

```
User

↓

CLI Command

↓

Argument Validation

↓

Module Service

↓

Processing

↓

Structured Result

↓

Rich CLI Output
```

The service layer returns structured Python objects.

The CLI is responsible for presentation.

---

# Shared Components

Current shared infrastructure includes

Configuration

- Config Loader
- Config Manager
- Config Validator

Logging

- Application Logging

Testing

- Pytest

CLI

- Typer

Output

- Rich

---

# Dependency Rules

Allowed

```
CLI

↓

Service

↓

Shared Utilities
```

Not Allowed

```
Service

↓

CLI
```

Modules must not directly depend on one another unless absolutely necessary.

Shared functionality belongs in

```
assistant/utils/

or

assistant/services/
```

---

# Development Workflow

Every implementation follows the same lifecycle.

```
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

python -m compileall assistant

↓

pytest

↓

Documentation Update

↓

Git Commit
```

No module is considered complete until every step passes.

---

# Error Handling

CyberAtlas emphasizes graceful failure.

Requirements

- Validate inputs
- Raise meaningful exceptions
- Catch expected failures
- Display concise CLI messages
- Preserve debugging information through logging

---

# Testing Strategy

Every completed module must satisfy

```
python -m compileall assistant

PASS
```

```
pytest

PASS
```

Current Result

```
29 Passed

0 Failed
```

---

# Future Architecture

As CyberAtlas evolves, the current modular architecture will expand into feature packs while preserving the same core framework.

```
CyberAtlas

├── Core Framework
│
├── HTB Toolkit
│
├── CTF Toolkit
│
├── Bug Bounty Toolkit
│
├── Malware Toolkit
│
├── DFIR Toolkit
│
├── SOC Toolkit
│
└── AI Assistant
```

Each toolkit will reuse the same:

- Configuration
- Logging
- CLI
- Testing
- Utility Libraries

This minimizes duplication and keeps the project maintainable.

---

# Current Milestone

Foundation

✅ Complete

HTB Modules

✅ Doctor

✅ Inspect

✅ Workspace

✅ Decode

✅ ELF

✅ PE

✅ PCAP

✅ Web

Quality Gate

```
python -m compileall assistant

PASS
```

```
pytest

29 Passed
```

Next Module

```
Crypto
```

---

# Architecture Goal

Maintain a clean, modular architecture that allows CyberAtlas to grow from an HTB toolkit into a comprehensive cybersecurity platform without requiring major architectural redesigns.
