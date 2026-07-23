# CyberAtlas Next Session

## Current Project State

Project:
CyberAtlas


Current milestone:


Crypto Intelligence Foundation Expansion Completed


Latest validation:

pytest

Result:

105 passed


# Completed In Previous Session

## HMAC Intelligence Module

Completed:

assistant/modules/crypto/hmac.py

Implemented:

HMAC generation
HMAC verification
Secure key generation
Digest identification
HMAC key analysis

Supported:

MD5
SHA1
SHA224
SHA256
SHA384
SHA512


## HMAC CLI Integration

Completed:

assistant/cli/hmac.py

Architecture:

Typer grouped command namespace.

Available commands:

cyberatlas hmac generate

cyberatlas hmac verify

cyberatlas hmac keygen

cyberatlas hmac identify

cyberatlas hmac analyze-key

Registered through:

assistant/cli/app.py

Implementation:

app.add_typer(
    hmac_app,
    name="hmac",
)


# Current CLI Architecture

Current:

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

# Immediate Next Task

## Create Crypto Parent Namespace

Goal:

Improve scalability before adding more cryptographic modules.

Target command:

cyberatlas crypto

Future structure:

cyberatlas crypto

├── hash
├── cipher
├── hmac
├── encoding
├── certificate
├── aes
├── rsa
└── tls

Reason:

The crypto subsystem will continue expanding. A parent namespace avoids dozens of top-level commands.


## Planned Refactor

Move:

Current:

cyberatlas hmac

Target:

cyberatlas crypto hmac

Future examples:

cyberatlas crypto hash

cyberatlas crypto cipher

cyberatlas crypto aes

cyberatlas crypto rsa

cyberatlas crypto certificate



# Next Implementation Steps

## Step 1

Create:

assistant/cli/crypto.py

Purpose:

Crypto command namespace.


## Step 2

Move HMAC registration:

Before:

app.add_typer(
    hmac_app,
    name="hmac",
)

After:

crypto
 |
 └── hmac


## Step 3

Update CLI tests:

Create:

tests/modules/test_crypto_cli.py

Validate:

crypto namespace exists
hmac is available under crypto
existing HMAC commands work


## Step 4

Run:

pytest

Expected:

105+ passed


# After CLI Refactor

Continue Crypto Expansion:

Priority:

AES module
RSA module
Certificate analysis
TLS inspection
Encoding intelligence


# Development Requirements

Always maintain:

Python 3.13+
Typer CLI style
Rich terminal output
Local-first execution
CPU-friendly implementation
Modular architecture
Complete unit tests
Documentation updates after milestones


# Current Handoff Point

The next session should start with:

Create assistant/cli/crypto.py

Then migrate:

cyberatlas hmac

to:

cyberatlas crypto hmac

without breaking existing functionality.



