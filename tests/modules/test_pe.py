"""
Unit tests for the PE analyzer.
"""

from pathlib import Path

from assistant.modules.pe.service import PEAnalyzer


def test_pe_analyzer() -> None:
    """
    Analyze a known PE executable.
    """

    sample = Path(
        "/home/pentest/go/pkg/mod/"
        "github.com/google/pprof@v0.0.0-20240227163752-401108e1b7e7/"
        "internal/binutils/testdata/exe_windows_64.exe"
    )

    assert sample.exists()

    result = PEAnalyzer.analyze(str(sample))

    assert result.path.endswith("exe_windows_64.exe")

    assert "PE32+" in result.file_type

    assert result.architecture == "x86-64"

    assert result.bits == "PE32+ (64-bit)"

    assert result.image_base != "Unknown"

    assert result.entry_point != "Unknown"

    assert result.aslr == "Enabled"

    assert result.dep == "Enabled"

    assert ".text" in result.sections

    assert ".idata" in result.sections

    assert "KERNEL32.dll" in result.imports

    assert "msvcrt.dll" in result.imports
