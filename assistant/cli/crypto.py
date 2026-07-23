"""
CyberAtlas Crypto CLI.
"""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from assistant.modules.crypto.service import CryptoService

console = Console()


def crypto(
    action: str = typer.Argument(
        ...,
        help=(
            "Action: hash, verify, identify, xor, "
            "caesar-encrypt, caesar-decrypt, rot13, "
            "rot47, frequency"
        ),
    ),
    value: str = typer.Argument(
        ...,
        help="Input text or file path depending on the action.",
    ),
    extra: str = typer.Argument(
        "",
        help="Algorithm, key, shift, or expected hash.",
    ),
    option: str = typer.Argument(
        "",
        help="Optional parameter (algorithm for verify).",
    ),
) -> None:
    """
    Perform common cryptographic operations.
    """

    action = action.lower().strip()

    try:

        # -------------------------------------------------------------
        # HASH
        # -------------------------------------------------------------
        if action == "hash":

            path = Path(value)

            if path.exists():
                result = CryptoService.hash_file(
                    path,
                    algorithm=extra or "sha256",
                )
            else:
                result = CryptoService.hash_text(
                    value,
                    algorithm=extra or "sha256",
                )

            console.print(
                Panel.fit(
                    "[bold green]Hash Generated[/bold green]",
                    title="CyberAtlas Crypto",
                )
            )

            table = Table(title="Hash Result")
            table.add_column("Field", style="cyan")
            table.add_column("Value", overflow="fold")

            table.add_row("Algorithm", result.algorithm)
            table.add_row("Digest", result.digest)

            console.print(table)
            return

        # -------------------------------------------------------------
        # VERIFY
        # -------------------------------------------------------------
        if action == "verify":

            if not extra:
                raise ValueError(
                    "Expected hash value is required."
                )

            verified = CryptoService.verify_hash(
                Path(value),
                expected=extra,
                algorithm=option or None,
            )

            if verified:
                console.print(
                    Panel.fit(
                        "[bold green]Hash Verified[/bold green]",
                        title="Verification",
                    )
                )
            else:
                console.print(
                    Panel.fit(
                        "[bold red]Hash Mismatch[/bold red]",
                        title="Verification",
                    )
                )

            return

        # -------------------------------------------------------------
        # IDENTIFY
        # -------------------------------------------------------------
        if action == "identify":

            algorithms = CryptoService.identify_hash(value)

            table = Table(title="Possible Algorithms")
            table.add_column("Algorithm")

            if algorithms:
                for algorithm in algorithms:
                    table.add_row(algorithm)
            else:
                table.add_row("Unknown")

            console.print(table)
            return

        # -------------------------------------------------------------
        # XOR
        # -------------------------------------------------------------
        if action == "xor":

            if not extra:
                raise ValueError("Key is required.")

            result = CryptoService.xor_text(
                value,
                extra,
            )

            table = Table(title="XOR Result")
            table.add_column("Output", overflow="fold")
            table.add_row(result)

            console.print(table)
            return

        # -------------------------------------------------------------
        # CAESAR ENCRYPT
        # -------------------------------------------------------------
        if action == "caesar-encrypt":

            if not extra:
                raise ValueError("Shift is required.")

            result = CryptoService.caesar_encrypt(
                value,
                int(extra),
            )

            table = Table(title="Caesar Encryption")
            table.add_column("Ciphertext", overflow="fold")
            table.add_row(result)

            console.print(table)
            return

        # -------------------------------------------------------------
        # CAESAR DECRYPT
        # -------------------------------------------------------------
        if action == "caesar-decrypt":

            if not extra:
                raise ValueError("Shift is required.")

            result = CryptoService.caesar_decrypt(
                value,
                int(extra),
            )

            table = Table(title="Caesar Decryption")
            table.add_column("Plaintext", overflow="fold")
            table.add_row(result)

            console.print(table)
            return

        # -------------------------------------------------------------
        # ROT13
        # -------------------------------------------------------------
        if action == "rot13":

            result = CryptoService.rot13(value)

            table = Table(title="ROT13")
            table.add_column("Output", overflow="fold")
            table.add_row(result)

            console.print(table)
            return

        # -------------------------------------------------------------
        # ROT47
        # -------------------------------------------------------------
        if action == "rot47":

            result = CryptoService.rot47(value)

            table = Table(title="ROT47")
            table.add_column("Output", overflow="fold")
            table.add_row(result)

            console.print(table)
            return

        # -------------------------------------------------------------
        # FREQUENCY
        # -------------------------------------------------------------
        if action == "frequency":

            entries = CryptoService.frequency(value)

            table = Table(title="Character Frequency")
            table.add_column("Character", style="cyan")
            table.add_column("Count", justify="right")
            table.add_column("Percentage", justify="right")

            for entry in entries:

                character = entry.character

                if character == " ":
                    character = "<space>"
                elif character == "\t":
                    character = "<tab>"
                elif character == "\n":
                    character = "<newline>"

                table.add_row(
                    character,
                    str(entry.count),
                    f"{entry.percentage:.2f}%",
                )

            console.print(table)
            return

        raise ValueError(
            f"Unknown crypto action: {action}"
        )

    except Exception as exc:
        console.print(
            Panel.fit(
                f"[red]{exc}[/red]",
                title="Crypto Error",
            )
        )
        raise typer.Exit(code=1)
