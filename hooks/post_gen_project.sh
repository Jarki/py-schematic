#!/bin/bash

set -e

echo "Project {{ cookiecutter.project_name }} successfully generated."
echo "Running initial setup..."

echo "Running uv sync..."
uv sync

echo "Setup complete. Your venv is ready at ./.venv"