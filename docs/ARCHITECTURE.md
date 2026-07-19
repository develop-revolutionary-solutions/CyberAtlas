# ARCHITECTURE.md

> **Purpose**
>
> This document defines the software architecture of CyberAtlas.
>
> Every implementation must comply with the rules defined here.
>
> This document acts as the architectural contract for all future development.

---

# CyberAtlas Architecture

Version: 1.0 (Draft)

Status: Architecture Freeze (Planned)

---

# Philosophy

CyberAtlas is **NOT** just a command-line application.

CyberAtlas is designed as a **Cyber Security Operating Platform**.

The CLI is only one interface.

Future interfaces include:

- REST API
- Desktop UI
- Web UI
- Plugin SDK
- AI Workflows

All business logic must remain independent of the user interface.

---

# Architecture Goals

CyberAtlas must remain:

- Modular
- Secure
- Testable
- Maintainable
- Extensible
- Offline First
- CPU Friendly
- Linux First
- Open Source

---

# Architectural Principles

The project follows principles from:

- Clean Architecture
- Hexagonal Architecture (Ports & Adapters)
- SOLID
- Separation of Concerns
- Dependency Inversion
- Single Responsibility Principle

---

# Layered Architecture

```
                    Presentation Layer
────────────────────────────────────────────────────

CLI

REST API (Future)

Desktop UI (Future)

Web UI (Future)

────────────────────────────────────────────────────
                    ↓

                 Application Layer

────────────────────────────────────────────────────

Services

Playbooks

Workflows

AI Orchestration

────────────────────────────────────────────────────
                    ↓

                   Domain Layer

────────────────────────────────────────────────────

Networking

Web

Linux

Windows

Cloud

Containers

OSINT

SOC

Bug Bounty

CTF

Malware

Forensics

Crypto

Active Directory

Reversing

────────────────────────────────────────────────────
                    ↓

              Infrastructure Layer

────────────────────────────────────────────────────

Configuration

Logging

Execution Engine

Knowledge System

Database

Plugin Framework

Security

────────────────────────────────────────────────────
                    ↓

                 Operating System

────────────────────────────────────────────────────

Python

Linux

Filesystem

Docker

External Security Tools

```

---

# Layer Responsibilities

## Presentation Layer

Responsible for:

- User interaction
- Command parsing
- Displaying output
- User experience

Must NEVER contain:

- Business logic
- Tool execution
- Parsing logic
- Security logic

---

## Application Layer

Responsible for:

- Coordinating workflows
- Calling services
- AI orchestration
- Playbook execution

Should know:

- What to execute

Should NOT know:

- How execution happens internally

---

## Domain Layer

The heart of CyberAtlas.

Contains cybersecurity knowledge.

Examples:

Networking

Web

Linux

Windows

Malware

SOC

CTF

Bug Bounty

Every module has a single responsibility.

Modules must never depend on each other directly.

Communication happens through services.

---

## Infrastructure Layer

Responsible for:

- Logging
- Configuration
- Tool Execution
- Database
- Knowledge Storage
- Plugin Loading

Contains implementation details.

No business logic.

---

## System Layer

Responsible for interacting with:

- Linux
- Python
- External Security Tools
- Docker
- Filesystem

---

# Dependency Rules

Allowed

```
Presentation
      ↓
Application
      ↓
Domain
      ↓
Infrastructure
      ↓
System
```

Forbidden

```
Modules
     ↓
CLI
```

```
Infrastructure
      ↓
Presentation
```

```
Domain
     ↓
CLI
```

```
Module A
     ↓
Module B
```

Modules communicate through services.

---

# Package Responsibilities

## assistant/

Application root.

Contains all source code.

---

## cli/

Responsible only for:

- Commands
- Arguments
- Output

No business logic.

---

## services/

Application workflows.

Coordinates modules.

---

## engine/

Execution engine.

Responsible for:

- Safe subprocess execution
- Timeouts
- Exit codes
- stdout
- stderr
- Tool discovery

---

## modules/

Cybersecurity modules.

Every module is independent.

Examples:

- web
- networking
- linux
- malware
- soc

---

## logging/

Single logging framework.

Every package uses:

```
get_logger(__name__)
```

No package configures logging independently.

---

## config/

Single configuration manager.

Configuration loaded only once.

No hardcoded configuration.

---

## security/

Security helpers.

Examples:

- Path validation
- Command validation
- Input sanitization

---

## plugins/

Future plugin framework.

Third-party extensions.

---

## knowledge/

Knowledge Base.

Future:

- Markdown
- Vector DB
- AI Memory

---

## playbooks/

Workflow automation.

Future:

- SOC playbooks

- Incident response

- CTF workflows

---

## ai/

AI orchestration.

Future:

- Local LLM

- Prompt management

- Reasoning

- AI providers

---

# Ports & Adapters

CyberAtlas follows Ports and Adapters.

Example

```
ToolRunner

↓

LocalRunner

↓

DockerRunner

↓

RemoteRunner (Future)
```

Another example

```
KnowledgeStore

↓

SQLite

↓

ChromaDB

↓

FAISS
```

Business logic depends only on interfaces.

Never implementations.

---

# Module Contract

Every module should eventually follow:

```
module/

__init__.py

service.py

models.py

validators.py

exceptions.py

tests/
```

Additional files allowed when necessary.

---

# Coding Standards

Every implementation must:

- Have type hints
- Have docstrings
- Follow PEP8
- Follow Ruff formatting
- Use pathlib
- Use logging
- Avoid print()
- Avoid global variables

---

# Logging Rules

Single logger.

No duplicate handlers.

Console logging.

File logging.

Future:

- JSON logging

- Rotating logs

---

# Configuration Rules

Configuration comes only from:

YAML

Environment Variables (Future)

Never hardcode:

- API keys

- Paths

- Tool configuration

---

# Security Rules

Never execute shell=True.

Always validate:

- User input

- Paths

- Commands

- File operations

Never trust external input.

---

# Testing Strategy

Every feature must include:

Unit Tests

Integration Tests

Manual Verification

Expected Output

Failure Testing

---

# Documentation Requirements

Every milestone updates:

PROJECT_STATE.md

CHANGELOG.md

ROADMAP.md

NEXT_SESSION.md

Developer Guide

---

# Future Interfaces

CyberAtlas should support:

CLI

REST API

Desktop GUI

Web UI

Plugin SDK

Automation SDK

Without changing business logic.

---

# Architectural Decision Records (ADR)

Major decisions must be documented.

Examples:

ADR-001

Why Typer

ADR-002

Why YAML

ADR-003

Why SQLite

ADR-004

Why Local LLM

ADR-005

Why Apache 2.0

---

# Architecture Freeze

Before implementing major new features:

Review architecture.

Review dependencies.

Review module boundaries.

Avoid unnecessary refactoring.

Maintain backwards compatibility whenever possible.

---

# Final Rule

Every line of code added to CyberAtlas should answer three questions:

1. Does it improve maintainability?

2. Does it improve security?

3. Does it improve scalability?

If the answer is "No" to any of these, reconsider the implementation before merging it.


## Internal Package Name

The internal Python package is currently named `assistant`.

This is an implementation detail.

The public identity of the project is:

- Project: CyberAtlas
- CLI: cyberatlas
- Repository: CyberAtlas

The package name may be renamed in a future major release if there is sufficient architectural benefit.
