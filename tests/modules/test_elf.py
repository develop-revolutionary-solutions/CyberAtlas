"""
Unit tests for the CyberAtlas ELF module.
"""

from __future__ import annotations

from assistant.modules.elf.service import ELFAnalyzer


def test_ls_binary():
    result = ELFAnalyzer.analyze("/bin/ls")

    assert result.bits == "ELF64"
    assert result.architecture
    assert result.entry_point.startswith("0x")
    assert result.interpreter
    assert result.stripped in {"Yes", "No"}
    assert result.relro in {"Full", "Partial", "None", "Unknown"}
    assert result.nx in {"Enabled", "Disabled", "Unknown"}
    assert result.pie in {"Enabled", "Disabled", "Unknown"}
