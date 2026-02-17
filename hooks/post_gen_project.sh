#!/bin/bash

set -e

echo "Project {{ cookiecutter.project_name }} successfully generated."
echo "Running initial setup..."

echo "Running uv sync..."
uv sync
echo "Installing dependencies..."
uv add python-dotenv
uv add pydantic
uv add pydantic-settings
echo "Adding development dependencies..."
uv add --group dev poethepoet
uv add --group dev mypy
uv add --group dev ruff
echo "Adding testing dependencies..."
uv add --group test pytest

echo "Setup complete. Your venv is ready at ./.venv"
