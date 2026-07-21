# MERGE_PLAN.md

# HTB-CTF-Assistant → CyberAtlas Merge Strategy

Version: 1.0
Status: Active
Owner: Siddarudreswara S

---

# Purpose

This document defines how experimental features developed in the HTB-CTF-Assistant repository will be evaluated, refined, and merged into the main CyberAtlas project.

The objective is to keep CyberAtlas clean, modular, stable, and production-ready while allowing rapid experimentation during CTFs.

---

# Philosophy

HTB-CTF-Assistant is the laboratory.

CyberAtlas is the production platform.

Never sacrifice CyberAtlas architecture for short-term CTF speed.

Every feature must prove its value before becoming part of CyberAtlas.

---

# Merge Workflow

```
Idea
    │
    ▼
Implement in HTB-CTF-Assistant
    │
    ▼
Use During Real CTF
    │
    ▼
Evaluate Performance
    │
    ▼
Refactor
    │
    ▼
Write Tests
    │
    ▼
Write Documentation
    │
    ▼
Review Architecture
    │
    ▼
Merge into CyberAtlas
```

---

# Merge Criteria

A feature may only be merged if it satisfies all of the following.

## Functional

- Works reliably
- Solves a real problem
- Has been used successfully during CTF
- Produces consistent results

---

## Code Quality

- Follows project coding standards
- Fully type hinted
- Documented
- Readable
- No duplicated logic

---

## Testing

Must include

- Unit tests
- Edge cases
- Error handling
- Regression tests

Minimum requirement:

```
pytest
All tests passing
```

---

## Documentation

Before merging, update

- README.md
- FEATURES.md
- MODULES.md
- CHANGELOG.md
- PROJECT_STATE.md

---

## Architecture

The feature must

- Fit existing architecture
- Respect module boundaries
- Avoid tight coupling
- Remain CPU friendly
- Work offline where possible

---

# Merge Checklist

Before merging verify

- [ ] Feature completed
- [ ] Used in real HTB challenge
- [ ] Stable
- [ ] Code reviewed
- [ ] Unit tests added
- [ ] Documentation updated
- [ ] No duplicated code
- [ ] Follows coding guidelines
- [ ] No hardcoded paths
- [ ] No hardcoded secrets
- [ ] Logging implemented
- [ ] Error handling implemented

---

# Features Suitable for Merge

Examples include

- Enumeration automation
- AI prompt generation
- Report generation
- Workspace management
- Challenge templates
- Payload generation
- Notes management
- Evidence management
- File parsers
- Hash identification
- Encoding utilities
- Networking helpers
- Tool wrappers
- CTF workflow automation

---

# Features NOT Ready for Merge

Do NOT merge

- Experimental code
- Temporary scripts
- One-off exploit code
- Hardcoded payloads
- Challenge-specific hacks
- Dirty proof-of-concepts
- Unused modules
- Unmaintained dependencies

---

# Refactoring Requirements

Before merging

Replace

- duplicated code
- magic values
- large functions
- global state

With

- reusable modules
- configuration files
- helper utilities
- dependency injection where appropriate

---

# Documentation Requirements

Every merged feature must include

Purpose

How it works

Dependencies

Example usage

Limitations

Future improvements

---

# Security Review

Before merging verify

- No credentials committed
- No API keys
- No tokens
- No passwords
- No challenge flags
- No private HTB VPN information
- No personal information

---

# Performance Review

Feature should

- Minimize RAM usage
- Minimize CPU usage
- Avoid unnecessary subprocesses
- Handle failures gracefully
- Produce meaningful logs

---

# Merge Procedure

## Step 1

Create feature branch

```bash
git checkout -b feature/<feature-name>
```

---

## Step 2

Cherry-pick or copy the implementation from HTB-CTF-Assistant.

---

## Step 3

Refactor to CyberAtlas standards.

---

## Step 4

Add tests.

Run

```bash
pytest
```

---

## Step 5

Run formatting

```bash
black .
isort .
```

---

## Step 6

Run linting

```bash
ruff check .
```

---

## Step 7

Update documentation.

---

## Step 8

Commit

```bash
git add .

git commit -m "feat(<module>): <description>"
```

---

## Step 9

Merge into main

```bash
git checkout main

git merge feature/<feature-name>
```

---

# Lessons Learned

Every merged feature should answer

What problem did it solve?

What worked well?

What failed?

What should be improved?

Can this help future CTFs?

Can this help real penetration tests?

Can this help SOC analysts?

---

# Long-Term Vision

The HTB-CTF-Assistant repository exists to rapidly prototype cybersecurity ideas.

CyberAtlas exists to become a professional, modular, AI-assisted cybersecurity platform suitable for:

- Learning
- Hack The Box
- Capture The Flag competitions
- Bug Bounty
- Penetration Testing
- Red Teaming
- Blue Teaming
- SOC Operations
- Detection Engineering
- DFIR
- Threat Hunting
- Security Research

Only mature, reusable, well-tested capabilities will be promoted from HTB-CTF-Assistant into CyberAtlas.

This approach ensures CyberAtlas remains clean, maintainable, and production-ready while continuously benefiting from real-world offensive security experience.
