When starting a new session:

1. Read PROJECT_STATE.md.
2. Read ROADMAP.md.
3. Read NEXT_SESSION.md.
4. Continue from the exact last completed task.
5. Update CHANGELOG.md.
6. Update PROJECT_STATE.md.
7. Update NEXT_SESSION.md before ending.


# CyberAtlas MASTER PROMPT

## Project Identity

You are working on **CyberAtlas (Cyber Security Assistant)**.

CyberAtlas is a modular, AI-assisted cybersecurity platform designed for:

- Hack The Box (HTB)
- Capture The Flag (CTF)
- Bug Bounty
- Penetration Testing
- Red Team Operations
- Blue Team Operations
- Security Operations Center (SOC)
- Threat Hunting
- Incident Response
- Digital Forensics
- Malware Analysis
- Detection Engineering
- Cybersecurity Learning

CyberAtlas is not only a CLI tool. It is designed as a long-term cybersecurity operating platform.

---

# Core Development Principles

Always maintain:

- Modular architecture
- Clean separation of concerns
- Production-quality code
- Security-first design
- Local-first operation
- Offline-first capability
- CPU-friendly implementation
- Linux-first compatibility
- Beginner-friendly learning workflow
- Professional cybersecurity standards

Primary operating environment:

- Kali Linux
- Python 3.13+

---

# Development Rules

When generating code:

- Provide complete files only.
- Never provide snippets.
- Never provide pseudocode.
- Never remove existing functionality.
- Preserve existing project architecture.
- Follow existing coding style.
- Use type hints.
- Use dataclasses where appropriate.
- Keep modules independently testable.
- Include documentation strings.
- Include tests for new functionality.

Every implementation must be:

- Copy-paste ready.
- Runnable.
- Compatible with the current repository.

---

# Repository Architecture

Current structure:

```
CyberAtlas/

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
├── tests/
├── README.md
├── CHANGELOG.md
└── pyproject.toml
```

---

# CLI Architecture

CyberAtlas CLI commands are stored under:

```
assistant/cli/
```

Current commands:

```
assistant/cli/

├── app.py
├── decode.py
├── elf.py
├── jwt.py
├── pe.py
├── pcap.py
├── web.py
├── workspace.py
├── inspect.py
├── doctor.py
└── version.py
```

Commands are registered manually in:

```
assistant/cli/app.py
```

---

# Module Architecture

CyberAtlas modules are stored:

```
assistant/modules/
```

Current modules:

```
active_directory
bugbounty
cloud
containers
crypto
ctf
forensics
linux
malware
networking
osint
reversing
soc
web
windows
```

---

# Crypto Module Status

Location:

```
assistant/modules/crypto/
```

Current implementation:

## service.py

Implemented:

- Text hashing
- File hashing
- Hash verification
- Hash identification
- XOR cipher
- Caesar cipher
- ROT13
- ROT47
- Character frequency analysis


## analyzer.py

Implemented:

- Shannon entropy calculation
- Character analysis
- Index of Coincidence
- Frequency distribution
- English language scoring


## jwt.py

Implemented:

- JWT token parsing
- Header decoding
- Payload decoding
- Algorithm detection
- Signature presence detection
- Expiration checking
- Security warning detection

Security checks:

- alg:none detection
- Missing signature detection
- Missing expiration detection
- Expired token detection


## CLI Integration

Command added:

```
cyberatlas jwt <TOKEN>
```

Features:

- JWT overview
- Algorithm display
- Header display
- Payload display
- Security warnings

---

# Testing Structure

Tests are separated by type:

```
tests/

├── modules/
│   ├── test_crypto.py
│   ├── test_crypto_analyzer.py
│   └── test_jwt.py
│
└── cli/
    └── test_jwt.py
```

Testing framework:

- pytest

---

# Current Validation

Completed:

```
pytest tests/modules/test_crypto_analyzer.py

8 passed
```

Completed:

```
pytest tests/modules/test_jwt.py

7 passed
```

---

# Next Development Priority

Continue Crypto expansion.

Next module:

```
assistant/modules/crypto/passwords.py
```

Planned features:

- Password hash identification
- bcrypt detection
- Argon2 detection
- PBKDF2 detection
- SHA crypt format detection
- Salt analysis
- Work-factor analysis
- CTF password hash intelligence


---

# Future Crypto Roadmap

Planned:

```
crypto/

├── service.py
├── analyzer.py
├── jwt.py
├── passwords.py
├── aes.py
├── rsa.py
├── certificates.py
└── hmac.py
```

---

# Security Rules

CyberAtlas must never:

- Require paid cloud services
- Depend on GPU acceleration
- Send sensitive data externally by default
- Execute dangerous actions without confirmation
- Store secrets insecurely

---

# Communication Rules

When continuing development:

- Check existing architecture first.
- Ask only when required information is missing.
- Provide complete replacement files.
- Keep implementation incremental.
- Maintain documentation after major milestones.

---

# Current Session Checkpoint

Completed:

```
Crypto Module Expansion
```

Including:

- Core cryptographic utilities
- Crypto analysis engine
- JWT security analyzer
- CLI integration
- Unit testing

Next session begins from:

```
crypto/passwords.py
```



------------------------------------------------------------
GOAL
------------------------------------------------------------

Deliver a production-quality local HTB toolkit before the Hack The Box competition.
