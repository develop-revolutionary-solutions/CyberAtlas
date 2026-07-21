# CyberAtlas

<p align="center">

<img src="assets/logo.png" alt="CyberAtlas Logo" width="180"/>

</p>

<p align="center">

<b>An Open-Source AI-Assisted Cyber Security Platform</b>

Learning • CTFs • Hack The Box • Bug Bounty • SOC • DFIR • Malware Analysis • Threat Hunting • Detection Engineering

</p>

---

# Disclaimer

> **CyberAtlas is developed exclusively for educational purposes, authorized penetration testing, defensive security operations, research, and laboratory environments.**
>
> Users are solely responsible for ensuring compliance with all applicable laws and regulations.
>
> The authors are **not responsible for any misuse** of this software.

---

# Vision

CyberAtlas aims to become a modular, AI-assisted Cyber Security Operating Platform that helps cybersecurity professionals and learners perform security operations from a single unified interface.

Rather than being another collection of scripts, CyberAtlas is designed as a scalable platform that combines:

- Learning
- Offensive Security
- Defensive Security
- Digital Forensics
- Threat Hunting
- Detection Engineering
- Knowledge Management
- AI-assisted workflows

into one extensible application.

---

# Project Goals

- Modular architecture
- Local-first operation
- Offline-friendly design
- CPU-friendly
- Linux-first (Kali Linux recommended)
- Open Source
- Production-quality code
- Beginner friendly
- Enterprise architecture
- Extensive documentation
- Unit tested

---

# Planned Features

## Offensive Security

- Hack The Box Assistant
- CTF Assistant
- Bug Bounty Toolkit
- Web Application Testing
- Active Directory Enumeration
- Privilege Escalation Helpers
- Linux Enumeration
- Windows Enumeration
- OSINT Toolkit
- Password Auditing
- Wireless Security Modules

---

## Defensive Security

- SOC Assistant
- Detection Engineering
- Threat Hunting
- Log Analysis
- Sigma Rules
- YARA Management
- IOC Management
- Wazuh Integration
- Suricata Integration
- Zeek Integration

---

## DFIR

- Incident Response
- Memory Analysis
- Disk Analysis
- Timeline Analysis
- Malware Triage
- Evidence Management

---

## AI Features

- AI-assisted investigations
- AI-generated reports
- Explain security concepts
- Explain attack techniques
- MITRE ATT&CK mapping
- Playbook generation
- Detection suggestions

---

## Knowledge Base

- Markdown knowledge library
- Attack references
- Tool documentation
- Notes
- Cheatsheets
- Learning paths

---

# Current Status

## Version

**v0.1.0 — Foundation**

The project is currently under active development.

The foundational architecture has been completed.

---

## Completed

- Project architecture
- Python packaging
- CLI entry point
- Logging subsystem
- Configuration exception hierarchy
- YAML configuration loader
- Configuration validator
- Configuration manager
- Recursive configuration merging
- Configuration caching
- Unit testing infrastructure

---

## Current Test Status

```
18 Tests
18 Passed
0 Failed
```

---

# Roadmap

| Milestone | Status |
|------------|--------|
| Foundation | ✅ Complete |
| Core Engine | 🚧 Next |
| Plugin Framework | Planned |
| Module Loader | Planned |
| Knowledge Base | Planned |
| AI Layer | Planned |
| Workspace Manager | Planned |
| Offensive Modules | Planned |
| Defensive Modules | Planned |
| DFIR Modules | Planned |
| Production Release | Planned |

---

# Project Structure

```
CyberAtlas/
│
├── assistant/
│   ├── ai/
│   ├── cli/
│   ├── config/
│   ├── core/
│   ├── database/
│   ├── engine/
│   ├── knowledge/
│   ├── logging/
│   ├── modules/
│   ├── playbooks/
│   ├── plugins/
│   ├── security/
│   ├── services/
│   └── utils/
│
├── configs/
├── docs/
├── evidence/
├── logs/
├── tests/
├── assets/
│
├── README.md
├── LICENSE
├── pyproject.toml
└── CHANGELOG.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CyberAtlas.git

cd CyberAtlas
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install CyberAtlas

```bash
pip install -e ".[dev]"
```

---

# Running

Current CLI

```bash
cyberatlas --help
```

or

```bash
python -m assistant
```

---

# Development

Run all tests

```bash
pytest
```

Expected output

```
======================
18 passed
======================
```

---

# Design Principles

CyberAtlas follows several software engineering principles:

- SOLID Principles
- Clean Architecture
- Modular Design
- Separation of Concerns
- Dependency Injection (planned)
- Test-Driven Development where practical
- Type Hints throughout the project
- Comprehensive Documentation

---

# Target Users

CyberAtlas is intended for:

- Cybersecurity Students
- SOC Analysts
- Blue Team Engineers
- Red Team Operators
- Penetration Testers
- DFIR Analysts
- Threat Hunters
- Bug Bounty Hunters
- CTF Players
- Security Researchers

---

# Development Status

Current development focus:

> **Core Engine**

Upcoming work includes:

- Application lifecycle
- Startup sequence
- Workspace initialization
- Plugin discovery
- Module discovery
- Service initialization
- Graceful shutdown

---

# Contributing

Contributions are welcome.

Before submitting changes:

- Follow the coding guidelines.
- Add tests for new functionality.
- Update documentation where applicable.
- Ensure all tests pass.

---

# License

Licensed under the **Apache License 2.0**.

See the LICENSE file for details.

---

# Author

**Siddarudreswara S**

Founder — Developing Revolutionary Services (DRS)

---

# Acknowledgements

CyberAtlas is inspired by the open-source cybersecurity community and the many projects that advance security education and defensive research.

Special thanks to everyone who contributes knowledge, tools, documentation, and ideas to make cybersecurity more accessible.

---

**Current Version:** v0.1.0 Foundation

**Status:** Active Development 🚧
