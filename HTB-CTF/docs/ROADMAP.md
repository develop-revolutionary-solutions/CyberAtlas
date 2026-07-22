# CyberAtlas Roadmap

Version: v0.6.0-dev

Branch: HTB-CTF

Status: Active Development

Last Updated: 2026-07-22

---

# Vision

CyberAtlas is a modular, offline-first, AI-assisted Cyber Security Assistant built for learning, Capture The Flag (CTF), Hack The Box (HTB), Bug Bounty, Digital Forensics, Reverse Engineering, Malware Analysis, SOC Operations, and Penetration Testing.

The long-term objective is to create a production-quality cybersecurity platform that evolves into a personal cybersecurity copilot.

---

# Design Principles

The project follows these principles throughout development.

- Offline First
- Local First
- Linux First
- CPU Friendly
- Open Source
- Modular
- Production Quality
- Secure by Design
- Beginner Friendly
- Extensible

---

# Current Development Stage

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

29 passed
0 failed
```

---

# Completed Milestones

## Foundation

Status

✅ Complete

Implemented

- Configuration Loader
- Configuration Manager
- Configuration Validator
- Logging Framework
- CLI Framework
- Testing Framework

---

## HTB Toolkit

Completed Modules

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

---

# Phase 1

## HTB Core Toolkit

Status

🟡 In Progress

Remaining Modules

### Crypto

Planned Features

- Hash Identification
- Hash Calculation
- Hash Verification
- Base Encodings
- XOR Helper
- Caesar Cipher
- ROT Variants
- Frequency Analysis
- Common CTF Helpers

---

### Networking

Planned Features

- DNS Lookup
- Reverse DNS
- WHOIS
- Port Scanner
- Banner Grabbing
- HTTP Client
- TLS Information
- IP Information
- CIDR Helper
- Socket Utilities

---

### Linux

Planned Features

- File Permissions
- Ownership
- Archive Helpers
- Strings
- Hexdump
- xxd
- File Identification
- Command Wrappers
- Common HTB Helpers

---

### Forensics

Planned Features

- File Timeline
- Metadata
- EXIF
- Hash Comparison
- IOC Extraction
- Memory Helpers
- Archive Inspection
- Evidence Collection

---

### Reverse Engineering Enhancements

Planned Features

- Extended ELF Analysis
- Extended PE Analysis
- Strings Analysis
- Section Entropy
- Symbol Detection
- Import Analysis
- Export Analysis
- Objdump Integration
- Checksec Integration
- GDB Helper

---

# Phase 2

## CTF Toolkit

Planned Features

- Challenge Tracker
- Workspace Templates
- Flag Tracker
- Notes
- Evidence Collection
- Time Tracking
- Category Management
- Difficulty Tracking

---

# Phase 3

## Bug Bounty Toolkit

Planned Features

- HTTP Enumeration
- Header Analysis
- Technology Detection
- robots.txt Analysis
- Sitemap Parser
- Parameter Discovery
- Screenshot Automation
- Recon Helpers

---

# Phase 4

## Malware Analysis

Planned Features

- Strings
- Hash Lookup
- Entropy Analysis
- File Classification
- YARA Integration
- IOC Collection
- Static Analysis Helpers

---

# Phase 5

## Digital Forensics

Planned Features

- Disk Images
- Memory Dumps
- Registry Analysis
- Timeline Generation
- Evidence Tracking
- Artifact Collection

---

# Phase 6

## SOC Toolkit

Planned Features

- Log Analysis
- Sigma Rules
- MITRE ATT&CK Mapping
- IOC Search
- Alert Investigation
- Timeline Builder
- Wazuh Integration

---

# Phase 7

## AI Integration

Planned Features

- Local Ollama Integration
- Investigation Assistant
- Command Explanation
- Malware Explanation
- Report Generation
- Investigation Summaries
- Playbook Suggestions

---

# Development Workflow

Every module follows the same implementation lifecycle.

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

↓

Next Module
```

---

# Documentation Workflow

Every completed module requires updates to:

- CHANGELOG.md
- PROJECT_STATE.md
- TASKS.md
- ROADMAP.md
- NEXT_SESSION.md
- SESSION_CONTEXT.md
- TESTING_PLAN.md
- COMMAND_REFERENCE.md
- README.md
- ARCHITECTURE.md
- LESSONS_LEARNED.md
- DEVELOPMENT_RULES.md
- MASTER_PROMPT.md

---

# Current Priority

Current Module

```
Crypto
```

Current Objective

Implement the Crypto module using the standard CyberAtlas implementation workflow while maintaining:

- Production-quality code
- Linux compatibility
- CPU efficiency
- Backward compatibility
- 100% passing tests

---

# Long-Term Vision

Version 1

HTB Toolkit

Version 2

CTF Assistant

Version 3

Bug Bounty Assistant

Version 4

SOC Assistant

Version 5

Digital Forensics Assistant

Version 6

Malware Analysis Assistant

Version 7

AI-Powered Cyber Security Copilot

---

# Success Criteria

CyberAtlas will be considered successful when it:

- Provides practical assistance during HTB and CTF challenges.
- Automates repetitive cybersecurity workflows.
- Runs efficiently on CPU-only hardware.
- Operates offline wherever practical.
- Maintains a modular architecture.
- Passes all automated tests.
- Serves as a portfolio-quality open-source project.
- Continues evolving into a comprehensive cybersecurity platform.
