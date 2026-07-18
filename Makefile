.PHONY: help install run test clean tree doctor

help:
	@echo "CyberAtlas Development Commands"
	@echo ""
	@echo "make install   - Install project"
	@echo "make run       - Run CyberAtlas"
	@echo "make test      - Run tests"
	@echo "make clean     - Remove caches"
	@echo "make tree      - Show project tree"
	@echo "make doctor    - Verify installation"

install:
	pip install -e .

run:
	python -m assistant

test:
	pytest

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

tree:
	tree -L 2

doctor:
	python -m assistant --help
