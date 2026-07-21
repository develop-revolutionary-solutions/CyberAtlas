"""
CyberAtlas entry point.

Allows the application to be started using:

    python -m assistant
"""

from assistant.cli.app import app

if __name__ == "__main__":
    app()
