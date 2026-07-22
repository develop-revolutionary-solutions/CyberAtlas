# CyberAtlas Merge Plan

Version: v0.6.0-dev

Branch: HTB-CTF

Status: Active Development

Last Updated: 2026-07-22

---

# Purpose

This document defines how feature branches are developed, validated, documented, and merged into the main project.

The goal is to maintain a stable, production-quality codebase while allowing rapid feature development.

---

# Branch Strategy

```
main
```

Production-ready code only.

```
develop
```

Integration branch.

```
feature/<name>
```

Individual feature development.

Examples

```
feature/htb-web
feature/crypto
feature/networking
feature/linux
feature/forensics
feature/reversing
```

---

# Development Workflow

Every feature follows the same lifecycle.

```
Create Feature Branch

↓

Implement Service

↓

Implement CLI

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

Update Documentation

↓

Commit Changes

↓

Merge into develop

↓

Regression Testing

↓

Merge into main
```

---

# Merge Requirements

A feature may only be merged if all requirements are satisfied.

## Code

- Clean implementation
- PEP 8 compliant
- Type hints where applicable
- No unused imports
- No debug code

---

## Testing

Must pass

```
python -m compileall assistant
```

and

```
pytest
```

No failing tests are permitted.

---

## Documentation

The following files must be updated before merging.

- README.md
- CHANGELOG.md
- PROJECT_STATE.md
- TASKS.md
- ROADMAP.md
- NEXT_SESSION.md
- SESSION_CONTEXT.md
- TESTING_PLAN.md
- COMMAND_REFERENCE.md
- LESSONS_LEARNED.md
- ARCHITECTURE.md
- DEVELOPMENT_RULES.md
- MASTER_PROMPT.md

---

## Manual Verification

Each command must be executed manually.

Verify

- Output formatting
- Error handling
- Expected behavior
- Invalid inputs

---

# Commit Guidelines

Use meaningful commit messages.

Examples

```
Add HTB web analysis module
```

```
Implement crypto hash analyzer
```

```
Improve PE parser
```

```
Add networking DNS lookup
```

Avoid

```
fix
```

```
update
```

```
changes
```

---

# Pull Request Checklist

Before merging

- Feature implemented
- CLI registered
- Manual testing completed
- Unit tests added
- Documentation updated
- Compile successful
- All tests passing

---

# Regression Testing

Before merging into `main`

Run

```
python -m compileall assistant
```

```
pytest
```

Perform a quick smoke test of all implemented commands.

Current commands

```
version
doctor
inspect
workspace
decode
elf
pe
pcap
web
```

---

# Release Process

After a stable milestone

1. Merge into `develop`
2. Perform regression testing
3. Merge into `main`
4. Create Git tag
5. Update CHANGELOG
6. Publish GitHub release

---

# Versioning

Current

```
v0.6.0-dev
```

Future milestones

```
v0.7.0
Crypto Toolkit

v0.8.0
Networking Toolkit

v0.9.0
Linux Toolkit

v1.0.0
Production HTB Toolkit
```

---

# Current Merge Status

Foundation

✅ Complete

HTB Modules

- Doctor ✅
- Inspect ✅
- Workspace ✅
- Decode ✅
- ELF ✅
- PE ✅
- PCAP ✅
- Web ✅

Quality Gate

```
python -m compileall assistant

PASS
```

```
pytest

29 Passed

0 Failed
```

Next Feature

```
Crypto Module
```

---

# Merge Philosophy

Merge only complete, tested, and documented features.

Every merge should leave the repository in a releasable state, ensuring future development always begins from a stable foundation.
