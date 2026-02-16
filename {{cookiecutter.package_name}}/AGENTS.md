# {{ cookiecutter.project_name }}

## Project Overview

{{ cookiecutter.description }}

**Python Version:** {{ cookiecutter.python_version }}

To learn about the general architecture, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
To see guidelines on testing, see [docs/TEST.md](docs/TEST.md)

## Development Setup

```bash
# Install dependencies
uv sync

# Run the application
uv run python -m src
```

## Development Commands

All tasks use `uv run poe <task>` via poethepoet:

### Code Quality
```bash
uv run poe format            # Format code with ruff
uv run poe format-check      # Check formatting without changes
uv run poe lint              # Lint code with ruff
uv run poe lint-fix          # Lint and auto-fix issues
uv run poe typecheck         # Type check with mypy
```

### Combined Checks
```bash
uv run poe check             # Run all checks (format, lint, typecheck, test)
uv run poe clean             # Clean build artifacts and caches
```

### Manual Tool Usage
```bash
uv run ruff check .          # Lint directly
uv run ruff format .         # Format directly
uv run mypy src              # Type check directly
uv run pytest                # Test directly
```

## Code Standards

### Style & Formatting
- **Line length:** 88 characters (Black-compatible)
- **Quote style:** Double quotes

### Linting Rules
- Ruff with strict rule sets enabled (see `ruff.toml`)
- Auto-fix available for most issues via `uv run poe lint-fix`

### Type Checking
- mypy in strict mode
- Check against mypy strict mode

## Common Workflows

### Adding a New Feature
1. Create feature branch
2. Write tests first (see [docs/TEST.md](docs/TEST.md))
3. Implement feature in `src/`
4. Run `uv run poe check` to validate all quality checks
5. Commit changes

### Adding Dependencies
```bash
# Add runtime dependency
uv add package-name

# Add development dependency
uv add --dev package-name

# Sync dependencies (after manual pyproject.toml edits)
uv sync
```

### Before Committing
```bash
# Run all quality checks
uv run poe check

# This runs: format-check → lint → typecheck → test
```

## Notes for AI Assistants

### Quality Standards
- **Always** run `uv run poe check` before considering a task complete
- All code must pass: formatting, linting, type checking, and tests
- Match existing code style and patterns in the project

### Common Patterns
- Use `uv run python -m src` to run the application
- Use `uv run poe <task>` for development tasks
- Configuration via environment variables or config files
- Follow existing patterns in the codebase for consistency
