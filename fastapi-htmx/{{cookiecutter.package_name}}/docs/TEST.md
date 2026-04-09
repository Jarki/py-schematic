# Testing

General guideline - do not test everything. Too many tests equals noise. Do not aim for coverage - aim for precision and only test the core business logic.

## Test Directory Guidelines

- **`tests/unit/`** - Fast tests with no external dependencies (database, API, filesystem)
  - Mock external services
  - Test pure functions and business logic
  - Should run in milliseconds

- **`tests/integration/`** - Tests that interact with external systems
  - Database queries
  - External API calls
  - File I/O operations
  - May take seconds to run

- **`tests/e2e/`** - Full workflow tests (optional)
  - Complete user scenarios
  - Multiple components working together
  - Slowest tests, run less frequently

- **`tests/conftest.py`** - Shared pytest fixtures
  - Session-scoped fixtures (run once)
  - Function-scoped fixtures (run per test)
  - Auto-applied markers based on directory

## Commands

```bash
uv run poe test              # Run all tests
uv run poe test-cov          # Run tests with coverage report
```

## Test Organization

### Test Markers
Tests can be marked for selective execution (defined in `pytest.ini`):
- `@pytest.mark.unit` - Fast, isolated unit tests
- `@pytest.mark.integration` - Tests with external dependencies
- `@pytest.mark.slow` - Tests that take >1 second
- `@pytest.mark.smoke` - Quick smoke tests

### Running Specific Tests
```bash
# Run only unit tests
uv run pytest tests/unit/

# Run only integration tests
uv run pytest tests/integration/

# Run tests by marker
uv run pytest -m unit
uv run pytest -m "not slow"
```

## Testing Requirements

- Tests organized by type: `tests/unit/` and `tests/integration/`
- Use pytest fixtures from `conftest.py`
- Test files must match pattern: `test_*.py` or `*_test.py`
- Maintain test coverage (see coverage reports with `uv run poe test-cov`)

## Testing Guidelines

- Write unit tests for business logic (fast, no I/O)
- Write integration tests for external dependencies (database, APIs, files)
- Use appropriate pytest markers
- Prefer parameterized tests for multiple similar cases
- Tests mirror source structure: `src/module.py` → `tests/unit/test_module.py`
- Use existing fixtures from `conftest.py` when possible

## Test Workflows

### Adding a New Feature
1. Write tests first in appropriate directory (`tests/unit/` or `tests/integration/`)
2. Implement feature in `src/`
3. Run `uv run poe check` to validate all quality checks

### Fixing a Bug
1. Add failing test that reproduces the bug
2. Fix the bug in source code
3. Verify test passes: `uv run poe test`
4. Run full quality check: `uv run poe check`
