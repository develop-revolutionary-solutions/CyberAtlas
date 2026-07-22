# CyberAtlas

> AI-Assisted Cyber Security Platform for Hack The Box, CTFs, Bug Bounty, DFIR, Reverse Engineering, Malware Analysis, and SOC Operations.

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-success)
![License](https://img.shields.io/badge/License-Apache--2.0-green)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange)

---

# Overview

CyberAtlas is a modular, offline-first cybersecurity platform designed to help security professionals and learners during:

- Hack The Box
- Capture The Flag (CTF)
- Bug Bounty
- Digital Forensics
- Malware Analysis
- Reverse Engineering
- Penetration Testing
- SOC Operations

CyberAtlas is **not** an automated hacking framework.

Its purpose is to:

- Automate repetitive workflows
- Organize investigations
- Analyze common cybersecurity artifacts
- Explain cybersecurity concepts
- Accelerate learning
- Build reusable security tooling

The project is designed to evolve into a long-term personal cybersecurity copilot.

---

# Current Status

Current Branch

```
HTB-CTF
```

Current Version

```
v0.6.0-dev
```

Current Quality Gate

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

# Features

## Foundation

- Configuration Loader
- Configuration Manager
- Configuration Validator
- Logging Framework
- CLI Framework
- Testing Framework

---

## HTB Toolkit

Implemented

- Doctor
- Inspect
- Workspace
- Decode
- ELF
- PE
- PCAP
- Web

---

## Planned

- Crypto
- Networking
- Linux
- Forensics
- Reverse Engineering Enhancements
- CTF Toolkit
- Bug Bounty Toolkit
- Malware Toolkit
- DFIR Toolkit
- SOC Toolkit
- AI Integration

---

# Project Structure

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

# Installation

Clone the repository

```bash
git clone https://github.com/develop-revolutionary-solutions/CyberAtlas.git
```

Enter the project

```bash
cd CyberAtlas
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate

```bash
source .venv/bin/activate
```

Install

```bash
pip install -e .
```

---

# Usage

Display version

```bash
cyberatlas version
```

Check environment

```bash
cyberatlas doctor
```

Inspect a file

```bash
cyberatlas inspect sample.bin
```

Create an HTB workspace

```bash
cyberatlas workspace HTB-Lab
```

Decode data

```bash
cyberatlas decode SGVsbG8=
```

Analyze an ELF binary

```bash
cyberatlas elf challenge
```

Analyze a PE executable

```bash
cyberatlas pe malware.exe
```

Analyze a PCAP

```bash
cyberatlas pcap capture.pcap
```

Analyze a website

```bash
cyberatlas web https://www.hackthebox.com
```

---

# Development Workflow

Every module follows the same implementation lifecycle.

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

Documentation Update

↓

Git Commit
```

---

# Testing

Compile

```bash
python -m compileall assistant
```

Run tests

```bash
pytest
```

Current Status

```
29 Passed

0 Failed
```

---

# Coding Standards

CyberAtlas follows

- PEP 8
- Type Hints
- Modular Design
- Standard Library First
- Linux First
- Offline First
- CPU Friendly
- Production Quality

Business logic resides inside

```
assistant/modules/
```

CLI commands reside inside

```
assistant/cli/
```

Reusable tests reside inside

```
tests/
```

---

# Roadmap

Current Priority

```
Crypto Module
```

Future Modules

- Networking
- Linux
- Forensics
- Reverse Engineering
- CTF Toolkit
- Bug Bounty Toolkit
- Malware Analysis
- DFIR
- SOC
- AI Assistant

See

- ROADMAP.md
- PROJECT_STATE.md
- TASKS.md

for detailed progress.

---

# Documentation

Project documentation includes

- README.md
- ARCHITECTURE.md
- CHANGELOG.md
- COMMAND_REFERENCE.md
- DEVELOPMENT_RULES.md
- LESSONS_LEARNED.md
- MASTER_BLUEPRINT.md
- MASTER_PROMPT.md
- MERGE_PLAN.md
- NEXT_SESSION.md
- PROJECT_STATE.md
- ROADMAP.md
- SESSION_CONTEXT.md
- TASKS.md
- TESTING_PLAN.md

---

# Contributing

Contributions should follow the CyberAtlas development workflow.

Every contribution should

- Follow project architecture
- Include unit tests
- Pass compilation
- Pass pytest
- Update documentation
- Keep modules modular and reusable

---

# License

Licensed under the Apache License 2.0.

See the LICENSE file for details.

---

# Author

**Siddarudreswara Somashekhar**

Founder & Developer

**Developing Revolutionary Solutions (DRS)**

GitHub

https://github.com/develop-revolutionary-solutions

---

# Vision

CyberAtlas aims to become a comprehensive, offline-capable cybersecurity platform that supports learning, investigations, automation, and professional workflows while remaining lightweight, modular, and open source.
