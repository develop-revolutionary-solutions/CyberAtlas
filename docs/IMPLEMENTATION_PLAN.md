# CyberAtlas Engine v1 Implementation Plan

Status: ACTIVE

Architecture Version: Engine v1

Reference:

- ENGINE_SPEC.md

---

# Goal

Complete Engine v1.

No new features.

No architecture changes.

Only implementation.

---

# Stage 1

Engine Stabilization

Status

IN PROGRESS

Tasks

- Review imports
- Fix typing
- Verify public API
- Verify lifecycle
- Verify capability validation
- Verify registry
- Verify runner
- Verify EngineResult
- Verify ExecutionContext

Deliverable

Engine builds successfully.

---

# Stage 2

Engine Tests

Directory

tests/core/engine/

Files

test_base.py

test_capabilities.py

test_context.py

test_engine.py

test_exceptions.py

test_registry.py

test_result.py

test_runner.py

Target

100% Engine coverage

Deliverable

All tests pass.

---

# Stage 3

Crypto Migration

Current Module

assistant/modules/crypto/

Objective

Convert existing services into Engine plugins.

Plugins

HashPlugin

HMACPlugin

EncodingPlugin

Future

JWTPlugin

AESPlugin

RSAPlugin

PBKDF2Plugin

Requirement

No functionality changes.

All existing Crypto tests continue passing.

---

# Stage 4

Recon Framework

Directory

assistant/modules/recon/plugins/

Initial plugins

NmapPlugin

HttpxPlugin

WhoisPlugin

CurlPlugin

StringsPlugin

FilePlugin

Second wave

SubfinderPlugin

AmassPlugin

FFUFPlugin

NucleiPlugin

Third wave

NaabuPlugin

DnsxPlugin

KatanaPlugin

HakrawlerPlugin

AssetfinderPlugin

Goal

Every tool becomes a BasePlugin.

---

# Stage 5

Malware Framework

Plugins

YARAPlugin

CAPAPlugin

BinwalkPlugin

ExifToolPlugin

Radare2Plugin

StringsPlugin

FilePlugin

Future

GhidraPlugin

VolatilityPlugin

---

# Stage 6

Web Framework

Plugins

NiktoPlugin

GobusterPlugin

DirsearchPlugin

WPScanPlugin

WhatWebPlugin

---

# Stage 7

Active Directory

Plugins

BloodHoundPlugin

NetExecPlugin

ImpacketPlugin

KerbrutePlugin

---

# Stage 8

Cloud

Plugins

AWSPlugin

AzurePlugin

GCPPlugin

---

# Stage 9

Windows

Plugins

PowerShellPlugin

RegistryPlugin

EventLogPlugin

---

# Stage 10

Linux

Plugins

JournalctlPlugin

SystemctlPlugin

AuditPlugin

---

# Stage 11

OSINT

Plugins

ShodanPlugin

CensysPlugin

TheHarvesterPlugin

SpiderFootPlugin

---

# Stage 12

AI

Capabilities

Plugin selection

Workflow orchestration

Playbook execution

Knowledge retrieval

Report generation

---

# Completion Criteria

Engine

Stable

Tested

Documented

Crypto

Migrated

Recon

Operational

Remaining modules

Follow identical architecture

No module may bypass the Engine.

Engine remains the single execution framework for CyberAtlas.
