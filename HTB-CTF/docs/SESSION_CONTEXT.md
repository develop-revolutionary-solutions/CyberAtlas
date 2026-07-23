# CyberAtlas Session Context

## Project

**CyberAtlas**

AI-assisted Cyber Security Assistant.

Repository:
CyberAtlas


Purpose:

A modular, local-first cybersecurity platform supporting:

- Cybersecurity learning
- Hack The Box workflows
- CTF solving
- Penetration testing assistance
- SOC operations
- Threat hunting
- Security automation


---

# Current Development Status

## Version

0.1.0 Development Release




## Environment

Operating System:
Kali Linux


Python:
3.13+


Execution model:

- Local-first
- CPU-friendly
- No cloud dependency
- No GPU requirement


---

# Completed Components


## Core Framework

Completed:

- Project structure
- CLI framework
- Configuration system
- Logging system
- Environment validation


Location:
assistant/




---

# Crypto Intelligence Foundation

Status:
COMPLETED

Location:
assistant/modules/crypto/




## Crypto Service

Completed:
service.py


Capabilities:

- Hash generation
- File hashing
- Hash verification
- Hash identification
- XOR cipher
- Caesar cipher
- ROT13
- ROT47
- Frequency analysis


---

## Crypto Analyzer

Completed:
analyzer.py


Capabilities:

- Shannon entropy
- Character analysis
- Index of Coincidence
- Frequency analysis
- English scoring


---

## JWT Intelligence

Completed:
jwt.py


Capabilities:

- JWT parsing
- Header decoding
- Payload decoding
- Algorithm detection
- Signature analysis
- Expiration analysis
- Security warnings


CLI:

cyberatlas jwt <TOKEN>


## Password Intelligence
Completed:
passwords.py

Capabilities:

Password strength analysis
Entropy calculation
Character class analysis
Password scoring
Pattern detection
Mutation generation
Password masking

CLI:

cyberatlas password <PASSWORD>



# Wordlist Intelligence

Completed:

wordlists.py

Capabilities:

Wordlist loading
Cleaning
Deduplication
Statistics
Length filtering
Keyword searching
Mutation generation
Combination generation

CLI:

cyberatlas wordlist <FILE>


# HMAC Intelligence

Status:

COMPLETED

Backend:

assistant/modules/crypto/hmac.py

Capabilities:

HMAC generation
HMAC verification
Secure key generation
Digest identification
Key strength analysis

Supported algorithms:

MD5
SHA1
SHA224
SHA256
SHA384
SHA512


# HMAC CLI

Completed:

assistant/cli/hmac.py

Architecture:

Typer grouped command namespace.

Commands:

cyberatlas hmac generate

cyberatlas hmac verify

cyberatlas hmac keygen

cyberatlas hmac identify

cyberatlas hmac analyze-key

Registration:

assistant/cli/app.py

Implemented:

app.add_typer(
    hmac_app,
    name="hmac",
)


# Testing Status

Current test count:

105 passed

Validated:

Crypto services
Crypto analysis
JWT module
Password module
Wordlist module
HMAC module
CLI integration

Command:

pytest

Result:

105 passed


# Current Repository Structure

Important paths:

assistant/

├── cli/
│   ├── app.py
│   ├── jwt.py
│   ├── password.py
│   ├── wordlist.py
│   └── hmac.py
│
├── modules/
│   └── crypto/
│       ├── service.py
│       ├── analyzer.py
│       ├── jwt.py
│       ├── passwords.py
│       ├── wordlists.py
│       └── hmac.py



# Current Development Decision

Next architecture improvement:

Create Crypto command namespace.

Target:

cyberatlas crypto

Structure:

cyberatlas crypto

├── hash
├── cipher
├── hmac
├── encoding
├── certificate
└── future crypto modules

Reason:

Avoid CLI fragmentation as Crypto capabilities expand.


Next Planned Work

Priority order:

Create crypto CLI parent namespace
Move HMAC under crypto namespace
Add AES intelligence module
Add RSA intelligence module
Add certificate analysis
Add TLS inspection
Development Rules

Maintain:

Python 3.13+
Modular architecture
CPU-friendly solutions
Local-first execution
Open-source approach
Secure coding practices
Complete tests for every module
Documentation updates after milestones



