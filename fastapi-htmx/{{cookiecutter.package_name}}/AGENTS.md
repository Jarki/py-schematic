# {{ cookiecutter.project_name }}

## Project Overview

{{ cookiecutter.description }}

**Python Version:** {{ cookiecutter.python_version }}

To learn about the general architecture, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
To see guidelines on testing, see [docs/TEST.md](docs/TEST.md)
To see the git branching and commit workflow, see [docs/GIT_FLOW.md](docs/GIT_FLOW.md)

## Development Setup

Use the uv skill to manage the dependencies.

## Development Commands

All tasks use `uv run poe <task>` via poethepoet. Available scripts are defined in `pyproject.toml`.

### Code Quality

**Type safety is the priority.** Ensure there are no mypy errors before each commit.

**Linting is secondary.** Ensure there are no ruff errors once a feature is complete.

Key tasks:
- `uv run poe typecheck` — type check with mypy
- `uv run poe lint` / `uv run poe lint-fix` — lint with ruff
- `uv run poe format` / `uv run poe format-check` — format with ruff
- `uv run poe check` — run all checks (format, lint, typecheck, test)

## Notes for AI Assistants

- Run `uv run poe check` before considering any task complete
- Follow the commit and branching conventions in [docs/GIT_FLOW.md](docs/GIT_FLOW.md)
- Write tests before implementing features (see [docs/TEST.md](docs/TEST.md))
- Use `uv run poe start` to run the application
