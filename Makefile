.PHONY: help install dev test lint format type-check clean setup pre-commit docs

# Default target
help:
	@echo "AERI - Development Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help         Show this help message"
	@echo "  setup        Set up development environment"
	@echo "  install      Install production dependencies"
	@echo "  dev          Install development dependencies"
	@echo "  test         Run all tests"
	@echo "  test-cov     Run tests with coverage"
	@echo "  lint         Check code style with flake8"
	@echo "  format       Format code with black"
	@echo "  type-check   Run type checking with mypy"
	@echo "  check        Run all checks (lint, format, type-check)"
	@echo "  pre-commit   Install pre-commit hooks"
	@echo "  clean        Clean up temporary files"
	@echo "  docs         Build documentation"
	@echo "  run          Run AERI in development mode"

# Environment setup
setup:
	@echo "Setting up AERI development environment..."
	python -m venv venv || python3 -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "  source venv/bin/activate  # Linux/macOS"
	@echo "  venv\Scripts\activate     # Windows"

# Install dependencies
install:
	pip install --upgrade pip
	pip install -e .

dev:
	pip install --upgrade pip
	pip install -e ".[dev]"

# Testing
test:
	pytest tests/ -v

test-cov:
	pytest tests/ --cov=aeri --cov-report=term-missing --cov-report=html

# Code quality
lint:
	flake8 src/ tests/ --count --select=E9,F63,F7,F82 --show-source --statistics
	flake8 src/ tests/ --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics

format:
	black src/ tests/

format-check:
	black --check src/ tests/

type-check:
	mypy src/

check: lint format-check type-check

# Pre-commit
pre-commit:
	pre-commit install
	pre-commit autoupdate

# Cleanup
clean:
	@echo "Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".coverage" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "build" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "dist" -exec rm -rf {} + 2>/dev/null || true
	@echo "Done!"

# Documentation
docs:
	@echo "Building documentation..."
	cd docs && make html
	@echo "Documentation built in docs/_build/html/"

# Run AERI
run:
	python -m aeri.cli

# Development session
session:
	python src/scripts/run_teaching_session.py --stage 0

# Data export
export:
	python src/scripts/export_learning_data.py

# Visualization
visualize:
	python src/scripts/visualize_progress.py

# Database operations
db-init:
	@echo "Initializing database..."
	# Add database initialization commands here

db-reset: clean db-init
	@echo "Database reset complete"

# Docker
docker-build:
	docker build -t aeri:latest .

docker-run:
	docker run -p 8000:8000 aeri:latest

# Release
bump-patch:
	bumpversion patch

bump-minor:
	bumpversion minor

bump-major:
	bumpversion major

# Git helpers
git-clean:
	git fetch --all --prune
	git branch -vv | grep ': gone]' | awk '{print $$1}' | xargs git branch -d

# Profile
profile:
	python -m cProfile -o profile.stats src/scripts/run_teaching_session.py
	snakeviz profile.stats