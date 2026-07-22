# Development Rules

Every feature must:

- Be useful during live competitions.
- Work on Kali Linux.
- Prefer Python standard library.
- Avoid unnecessary dependencies.
- Be testable.
- Include documentation.
- Include examples.

Code Style

- PEP8
- Type hints
- Docstrings
- Rich output
- Typer CLI

Testing

Every module must include pytest tests.

Performance

Startup must remain fast.

No background services.

No database before competition.

No Docker before competition.



Service
↓
CLI
↓
Register
↓
Manual Test
↓
Unit Test
↓
compileall
↓
pytest



