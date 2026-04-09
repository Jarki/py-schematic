# Architecture

## Project Structure

```
{{ cookiecutter.project_name }}/
├── src/                              # Main source code
│   ├── __init__.py
│   └── __main__.py
├── tests/                            # Test suite
│   ├── unit/                         # Fast, isolated unit tests
│   │   ├── __init__.py
│   │   └── test_*.py
│   ├── integration/                  # Tests with external dependencies
│   │   ├── __init__.py
│   │   └── test_*.py
│   ├── e2e/                          # End-to-end tests (optional)
│   │   ├── __init__.py
│   │   └── test_*.py
│   └── conftest.py                   # Shared fixtures for all tests
├── pyproject.toml                    # Dependencies & tool config
├── ruff.toml                         # Linting & formatting rules
├── pytest.ini                        # Test configuration
└── AGENTS.md                         # AI assistant instructions
```

## Code Organization

- New modules go in `src/`
- Tests mirror source structure: `src/module.py` → `tests/unit/test_module.py`
- Follow the import style: absolute imports from `src`
- Use `uv run python -m src` to run the application
- Configuration via environment variables or config files
- Follow existing patterns in the codebase for consistency

## Configuration Files

- **pyproject.toml** - Project metadata, dependencies, Poe tasks, tool configurations
- **ruff.toml** - Ruff linting and formatting rules
- **pytest.ini** - Pytest configuration (test discovery, markers, options)
- **mypy.ini** - mypy type checking configuration (if exists)
