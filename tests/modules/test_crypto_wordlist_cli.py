"""
Unit tests for the Crypto Wordlist CLI.
"""

from pathlib import Path

from typer.testing import CliRunner

from assistant.cli.app import app


runner = CliRunner()


def test_wordlist_cli_success(
    tmp_path: Path,
) -> None:
    """
    Test successful wordlist analysis.
    """

    wordlist = tmp_path / "test.txt"

    wordlist.write_text(
        "admin\npassword\nroot\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "wordlist",
            str(wordlist),
        ],
    )

    assert result.exit_code == 0

    assert (
        "Wordlist Analysis Complete"
        in result.stdout
    )

    assert "Total Words" in result.stdout

    assert "3" in result.stdout


def test_wordlist_cli_missing_file() -> None:
    """
    Test missing wordlist handling.
    """

    result = runner.invoke(
        app,
        [
            "wordlist",
            "missing_wordlist.txt",
        ],
    )

    assert result.exit_code == 1

    assert (
        "Wordlist Analysis Failed"
        in result.stdout
    )


def test_wordlist_cli_statistics(
    tmp_path: Path,
) -> None:
    """
    Test wordlist statistics output.
    """

    wordlist = tmp_path / "stats.txt"

    wordlist.write_text(
        "cyber\natlas\nsecurity\n",
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "wordlist",
            str(wordlist),
        ],
    )

    assert result.exit_code == 0

    assert "Unique Words" in result.stdout

    assert "Shortest Word" in result.stdout

    assert "Longest Word" in result.stdout
