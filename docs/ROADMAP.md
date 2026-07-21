# ROADMAP.md

> **Purpose**
>
> This document defines the long-term development roadmap for CyberAtlas.
>
> It outlines completed milestones, current priorities, future phases, and the project's strategic direction.
>
> This roadmap is a living document and should be updated after each completed milestone.

---

# CyberAtlas Development Roadmap

Project: CyberAtlas

Version: v0.1.0 (Development)

Status: Active Development

License: Apache License 2.0

---

# Vision

CyberAtlas aims to become a complete, modular, AI-assisted Cyber Security Platform that runs locally and empowers cybersecurity professionals, students, researchers, and organizations through automation, education, and practical tooling.

The project will support:

- Cyber Security Learning
- Hack The Box
- CTF Competitions
- Bug Bounty Hunting
- Penetration Testing
- Red Team Operations
- Blue Team Operations
- SOC Operations
- Threat Hunting
- Detection Engineering
- Malware Analysis
- Digital Forensics
- Incident Response
- AI-assisted Security Workflows

---

# Development Philosophy

Every milestone should:

- Deliver working functionality
- Improve the architecture
- Improve maintainability
- Improve security
- Improve scalability
- Improve documentation
- Improve the developer experience

No milestone should compromise the architectural principles defined in `ARCHITECTURE.md`.

---

# Current Status

| Phase | Status |
|--------|--------|
| Foundation | 🟡 In Progress |
| Current Completion | ~30% |
| Current Milestone | Architecture Freeze v1.0 |

---

# Phase 0 — Project Planning

Status: ✅ Completed

Objectives:

- Define project vision
- Select license
- Define technology stack
- Define development workflow
- Create documentation structure

Deliverables:

- Project vision
- Software requirements
- Coding guidelines
- Git strategy
- Initial documentation

---

# Phase 1 — Foundation

Status: 🟡 In Progress

Goal:

Build the core infrastructure that every future component depends on.

---

## Milestone 1 — Project Foundation

Status: ✅ Completed

Completed:

- Modern project layout
- Virtual environment
- Git repository
- Apache License 2.0
- README
- pyproject.toml
- requirements.txt

---

## Milestone 2 — Modular CLI

Status: ✅ Completed

Completed:

- Typer CLI
- Modular command registration
- Version command
- Doctor command

Commands:

```bash
python -m assistant version show

python -m assistant doctor run
```

---

## Milestone 3 — Logging Framework

Status: ✅ Completed

Completed:

- Centralized logger
- Console logging
- File logging
- Automatic log directory creation
- UTF-8 log files
- Shared logger helper
- Doctor command logging integration

Future Improvements:

- Log rotation
- JSON logging
- Configurable log levels
- Colored console output

---

## Milestone 3.5 — Architecture Freeze v1.0

Status: 🔄 Planned (Immediate Next Milestone)

Goal:

Freeze the core architecture before implementing additional features.

Deliverables:

- Package hierarchy
- Layer responsibilities
- Dependency rules
- Module contracts
- Service contracts
- Plugin architecture
- AI architecture
- Data flow
- Coding standards
- ADR structure

Expected Outcome:

A stable architectural foundation that minimizes future refactoring.

---

## Milestone 4 — Configuration System

Status: Planned

Objectives:

- YAML configuration
- Configuration manager
- Singleton pattern
- Validation
- Environment profiles
- Default values

Future Enhancements:

- Environment variables
- Secret management
- Configuration migration

---

## Milestone 5 — Execution Engine

Status: Planned

Objectives:

- Safe subprocess wrapper
- Tool execution
- stdout capture
- stderr capture
- Timeout handling
- Exit code handling
- Tool discovery
- Shell injection prevention

Future Supported Tools:

- nmap
- ffuf
- nuclei
- amass
- subfinder
- httpx
- curl
- whois
- grep
- strings
- file
- binwalk
- hexdump

---

## Milestone 6 — Testing Framework

Status: Planned

Objectives:

- Unit testing
- Integration testing
- CLI testing
- Coverage reporting
- Test fixtures
- CI-ready test suite

---

# Phase 2 — Core Security Modules

Status: Planned

Objectives:

Develop reusable cybersecurity modules.

Modules:

- Networking
- Linux
- Windows
- Web
- Cloud
- Containers
- Crypto
- OSINT
- Malware
- Digital Forensics
- Reversing
- Active Directory

Each module should:

- Follow module contracts
- Be independently testable
- Have documentation
- Support AI workflows

---

# Phase 3 — CTF & Learning Platform

Status: Planned

Objectives:

Build interactive learning capabilities.

Features:

- Hack The Box assistant
- CTF helper
- Enumeration workflows
- Challenge tracking
- Payload generation
- Notes
- Writeups
- Progress tracking

---

# Phase 4 — Bug Bounty Platform

Status: Planned

Features:

- Scope management
- Recon automation
- Subdomain enumeration
- HTTP analysis
- Vulnerability validation
- Reporting
- Evidence collection

---

# Phase 5 — Blue Team Platform

Status: Planned

Features:

- SOC workflows
- Threat hunting
- IOC analysis
- MITRE ATT&CK mapping
- Sigma rules
- Detection engineering
- Log analysis
- Alert triage
- Incident response playbooks

---

# Phase 6 — AI Platform

Status: Planned

Objectives:

Integrate AI as an assistant rather than replacing analyst judgment.

Features:

- Local LLM support
- Prompt management
- AI reasoning
- Knowledge retrieval
- AI workflows
- Context management
- AI-assisted reporting

Supported Providers (Future):

- Ollama
- llama.cpp
- OpenAI (optional)
- Anthropic (optional)
- Other local providers

---

# Phase 7 — Plugin Ecosystem

Status: Planned

Objectives:

Allow third-party developers to extend CyberAtlas.

Features:

- Plugin SDK
- Plugin discovery
- Plugin validation
- Plugin lifecycle
- Version compatibility

---

# Phase 8 — Knowledge Platform

Status: Planned

Objectives:

Build a searchable cybersecurity knowledge base.

Content:

- Notes
- Playbooks
- Cheat sheets
- MITRE mappings
- CVEs
- TTPs
- Learning material
- AI memory

---

# Phase 9 — Automation Platform

Status: Planned

Objectives:

Workflow automation.

Examples:

- Pentest automation
- SOC automation
- Recon automation
- AI-assisted workflows
- Scheduled jobs

---

# Phase 10 — Enterprise Features

Status: Future

Potential Features:

- Multi-user support
- Authentication
- RBAC
- API server
- Web dashboard
- Desktop application
- Reporting engine
- Multi-project management

---

# Definition of Done

A milestone is considered complete only when:

- Code is implemented
- Tests pass
- Documentation is updated
- CHANGELOG.md is updated
- PROJECT_STATE.md is updated
- NEXT_SESSION.md is updated
- Manual verification is complete
- Git commit is created

---

# Long-Term Goals

CyberAtlas should become:

- A cybersecurity learning platform
- A professional penetration testing assistant
- A SOC analyst toolkit
- A CTF companion
- A Bug Bounty assistant
- A local AI security platform
- A modular open-source ecosystem

---

# Success Criteria

CyberAtlas succeeds if it is:

- Easy to learn
- Easy to extend
- Easy to maintain
- Secure by default
- Well documented
- Production quality
- Community friendly
- Useful for both beginners and experienced professionals

---

# Roadmap Maintenance

This document must be reviewed:

- At the start of each major phase
- After every completed milestone
- Before introducing major architectural changes

The roadmap should evolve with the project while remaining aligned with the architecture and vision.



Foundation
██████████ 100%

Core Engine
░░░░░░░░░░

Plugin System
░░░░░░░░░░

Knowledge Base
░░░░░░░░░░

AI Layer
░░░░░░░░░░

Operational Modules
░░░░░░░░░░



