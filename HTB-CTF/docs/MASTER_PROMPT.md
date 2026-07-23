When starting a new session:

1. Read PROJECT_STATE.md.
2. Read ROADMAP.md.
3. Read NEXT_SESSION.md.
4. Continue from the exact last completed task.
5. Update CHANGELOG.md.
6. Update PROJECT_STATE.md.
7. Update NEXT_SESSION.md before ending.

# CyberAtlas Master Prompt

## Project

CyberAtlas

AI-assisted Cyber Security Assistant

Repository:

CyberAtlas

License:

Apache-2.0

Python:

3.13+

Operating System:

Linux First (Primary Target: Kali Linux)

Development Model:

- Local First
- Offline First
- CPU Friendly
- Modular
- Open Source
- Production Quality

---

# Vision

CyberAtlas is a professional cybersecurity platform designed to assist security professionals, students, researchers, bug bounty hunters, penetration testers, SOC analysts and CTF players.

The goal is NOT to replace existing security tools.

The goal is to orchestrate them, analyze their output, automate repetitive tasks and provide actionable intelligence through a consistent interface.

CyberAtlas should become a daily driver for:

- Hack The Box
- TryHackMe
- VulnHub
- CTF competitions
- Bug Bounty
- Internal Penetration Testing
- Security Research
- SOC Operations
- Threat Hunting
- Malware Analysis
- DFIR

---

# Core Principles

Always maintain:

- Clean architecture
- Modular code
- Type hints
- Dataclasses where appropriate
- Rich CLI output
- Typer CLI framework
- Local execution
- CPU friendly implementation
- No cloud dependency
- No GPU dependency
- Beginner friendly
- Production quality code

Never sacrifice maintainability for shortcuts.

---

# Current Project Status

Current milestone completed:

Crypto Intelligence Foundation

Current validation:

pytest

Result:

105 passed

Git status:

Clean

Latest milestone:

HMAC Intelligence completed.

---

# Completed Modules

## Configuration

Completed:

- Loader
- Manager
- Validator

---

## Decode

Completed:

- Base64
- Hex
- URL
- ROT13
- Common CTF decoding

---

## Binary Analysis

Completed:

- ELF analysis
- PE analysis
- PCAP analysis

---

## Web

Completed:

- Initial web analysis module

---

## Crypto Intelligence

Completed:

### service.py

- Hash generation
- File hashing
- Hash verification
- Hash identification
- XOR cipher
- Caesar cipher
- ROT13
- ROT47
- Frequency analysis

### analyzer.py

- Shannon entropy
- Character analysis
- Index of Coincidence
- English scoring

### jwt.py

- JWT parsing
- Header decoding
- Payload decoding
- Signature analysis
- Expiration analysis
- Security warnings

### passwords.py

- Password strength analysis
- Entropy
- Password scoring
- Mutation generation

### wordlists.py

- Loading
- Cleaning
- Statistics
- Deduplication
- Filtering
- Mutation generation
- Combination generation

### hmac.py

- HMAC generation
- Verification
- Secure key generation
- Digest identification
- Key analysis

Supported algorithms:

- MD5
- SHA1
- SHA224
- SHA256
- SHA384
- SHA512

---

# Current CLI

Current CLI structure:

```
cyberatlas

├── inspect
├── workspace
├── decode
├── elf
├── pe
├── pcap
├── web
├── jwt
├── password
├── wordlist
├── hmac
│   ├── generate
│   ├── verify
│   ├── keygen
│   ├── identify
│   └── analyze-key
├── version
└── doctor
```

Typer should remain the primary CLI framework.

Rich should remain the terminal rendering library.

---

# Development Rules

Every implementation must include:

- Complete implementation
- Complete tests
- Type hints
- Meaningful docstrings
- Error handling
- Rich CLI output where applicable

Never provide pseudocode.

Never provide partial implementations.

Always provide complete copy-paste-ready files.

---

# Testing Requirements

Every new module must include:

- Unit tests
- CLI tests (if applicable)

Target:

```
pytest
```

Must pass before moving to the next milestone.

---

# Next Major Milestone

Recon Intelligence Framework

Purpose:

Integrate existing cybersecurity tools through a unified abstraction layer.

CyberAtlas should execute tools, parse their output, correlate findings and provide actionable recommendations.

CyberAtlas should orchestrate—not simply wrap—external tools.

---

# Planned Recon Architecture

```
assistant/modules/recon/

service.py
models.py
parser.py
report.py
recommendations.py

nmap.py
http.py
web.py
dns.py
osint.py
```

CLI:

```
assistant/cli/recon.py
```

---

# Planned Tool Integrations

Priority 1

- nmap
- httpx
- ffuf
- curl

Priority 2

- nuclei

Priority 3

- amass
- subfinder
- whois

Priority 4

- strings
- file
- hexdump
- binwalk

Future

- masscan
- nikto
- gobuster
- feroxbuster
- sqlmap
- wfuzz

---

# Integration Philosophy

Do NOT expose tools as simple wrappers.

Instead:

- Execute tools safely
- Parse structured output
- Normalize results
- Correlate findings
- Generate recommendations
- Produce consistent Rich reports

Example:

Instead of:

nmap

CyberAtlas should provide:

cyberatlas recon scan

which internally performs:

- Tool execution
- Parsing
- Analysis
- Recommendations

---

# Coding Standards

Maintain:

- Python 3.13+
- PEP 8
- Dataclasses
- pathlib
- subprocess safely
- XML parsing
- JSON parsing
- Rich
- Typer

Avoid unnecessary dependencies.

---

# Documentation

After every completed milestone update:

- CHANGELOG.md
- SESSION_CONTEXT.md
- NEXT_SESSION.md

Architecture documents should be updated only after significant architectural changes.

---

# Current Handoff

Current project status:

- Crypto Intelligence Foundation complete
- HMAC Intelligence complete
- CLI namespace implemented
- 105 tests passing

The next implementation begins with:

assistant/modules/recon/service.py

This becomes the execution layer for all external security tools used by CyberAtlas.

------------------------------------------------------------
GOAL
------------------------------------------------------------

Deliver a production-quality local HTB toolkit before the Hack The Box competition.
