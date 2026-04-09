# Git Flow

## Branch Strategy

This project uses a trunk-based development approach with short-lived feature branches.

### Branch Types

| Branch | Pattern | Purpose |
|--------|---------|---------|
| `main` | `main` | Production-ready code; always stable |
| Feature | `feature/<short-description>` | New features |
| Fix | `fix/<short-description>` | Bug fixes |
| Chore | `chore/<short-description>` | Maintenance, dependency updates, tooling |

## Workflow

### Starting New Work

```bash
# Always branch from main
git checkout main
git pull origin main
git checkout -b feature/my-feature
```

### During Development

```bash
# Run quality checks before committing
uv run poe check

# Commit with a clear message
git add <files>
git commit -m "feat: add workout session tracking"
```

### Commit Message Format

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>: <short description>

[optional body]
```

**Types:**
- `feat` — new feature
- `fix` — bug fix
- `refactor` — code change that neither fixes a bug nor adds a feature
- `test` — adding or updating tests
- `chore` — maintenance tasks, dependency updates
- `docs` — documentation only changes

### Merging

```bash
# Rebase onto main before merging to keep history clean
git fetch origin
git rebase origin/main

# Run checks one more time
uv run poe check

# Merge via fast-forward (or squash for messy history)
git checkout main
git merge --ff-only feature/my-feature
git push origin main
```

## Rules

- `main` must always pass `uv run poe check` (format, lint, typecheck, tests)
- No direct commits to `main` — always use a branch
- Keep branches short-lived; merge within a day or two when possible
- Delete branches after merging
- Rebase rather than merge when updating a branch from `main`
