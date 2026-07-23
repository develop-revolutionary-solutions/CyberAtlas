# CyberAtlas Engine Specification (Engine v1)

Version: 1.0

Status: FROZEN

---

# Purpose

The CyberAtlas Engine is the common execution framework for every CyberAtlas module.

It provides a single, standardized execution model regardless of whether a plugin uses:

- Python
- Local CLI tools
- Python libraries
- Local AI
- File parsers

The Engine is completely independent of cybersecurity domains.

It contains **no Recon, Crypto, Malware, Web, AD, DFIR, or AI-specific logic**.

---

# Goals

The Engine must provide:

- Plugin registration
- Plugin discovery
- Plugin execution
- Capability validation
- Execution lifecycle
- Context creation
- Standard result objects
- Error handling

The Engine must NOT implement cybersecurity functionality.

---

# Directory Layout

assistant/core/engine/

```
__init__.py
base.py
capabilities.py
context.py
engine.py
exceptions.py
registry.py
result.py
runner.py
```

---

# Plugin Lifecycle

Every plugin follows the same lifecycle.

```
Engine.execute()

↓

Create ExecutionContext

↓

Lookup Plugin

↓

Validate Capabilities

↓

Runner.run()

↓

initialize()

↓

validate(context)

↓

execute(context)

↓

cleanup()

↓

EngineResult
```

This lifecycle is frozen for Engine v1.

---

# BasePlugin Contract

Every CyberAtlas plugin inherits from BasePlugin.

Required members:

```
name
description
category
version
```

Required methods:

```
initialize()

validate(context)

execute(context)

cleanup()

capabilities()
```

No plugin may change this interface.

---

# ExecutionContext

Plugins receive exactly one argument.

```
ExecutionContext
```

Plugins never receive **kwargs.

ExecutionContext stores:

- execution parameters
- timeout
- metadata
- environment
- tags
- working directory

---

# EngineResult

Every plugin returns:

```
EngineResult
```

No module-specific result objects are permitted.

Examples that are NOT allowed:

```
ReconResult

CryptoResult

MalwareResult

WebResult
```

The EngineResult contains:

- status
- metadata
- structured data
- warnings
- errors
- artifacts
- tags

---

# Capabilities

Plugins declare runtime requirements.

Examples:

Python plugin

```
PythonCapability()
```

Nmap plugin

```
BinaryCapability("nmap")
```

File parser

```
FilesystemCapability()
```

Capabilities are validated by the Engine.

Plugins must never validate capabilities directly.

---

# Registry Responsibilities

The registry only:

- registers plugins
- unregisters plugins
- retrieves plugins
- lists plugins

The registry never executes plugins.

---

# Runner Responsibilities

The runner:

- initializes plugins
- validates plugins
- executes plugins
- performs cleanup
- records execution timing

The runner does not discover plugins.

---

# Engine Responsibilities

The Engine:

- owns the registry
- owns the runner
- creates ExecutionContext
- validates capabilities
- executes plugins

The Engine never contains plugin-specific code.

No if/elif dispatch based on module names is permitted.

---

# Module Structure

Every CyberAtlas module follows the same layout.

Example

modules/recon/

```
plugins/
```

modules/crypto/

```
plugins/
```

modules/malware/

```
plugins/
```

Every executable component is a plugin.

---

# Public API

The Engine exposes:

```
register()

unregister()

execute()

plugins()

exists()

clear()
```

No additional public methods are added during Engine v1.

---

# Coding Rules

Every Engine file must:

- support Python 3.13+
- use type hints
- use dataclasses where appropriate
- use slots where appropriate
- avoid global mutable state
- avoid singleton patterns
- avoid circular imports

---

# Testing Requirements

Before Engine v1 is complete:

- Engine unit tests
- Registry tests
- Runner tests
- Context tests
- Capability tests
- Result tests
- Exception tests

Target:

100% Engine coverage

---

# Stability Policy

Engine v1 is frozen.

Only the following changes are allowed:

- bug fixes
- documentation improvements
- internal refactoring

No public API changes.

No lifecycle changes.

No architecture changes.

These changes are deferred to Engine v2.

---

# Future Modules

The following modules must use this Engine without modification.

- Crypto
- Recon
- Malware
- DFIR
- Web
- Windows
- Linux
- Cloud
- Containers
- Active Directory
- OSINT
- AI

Engine v1 is the foundation for the entire CyberAtlas platform.
