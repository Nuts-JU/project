# AGENTS.md

## Cursor Cloud specific instructions

This is a minimal single-file Python CLI tool (`test_accessibility.py`) that checks whether a URL is reachable and produces a JSON report.

### Running the application

```bash
python3 test_accessibility.py <url> [--timeout SECONDS] [--report PATH]
```

**Sandbox caveat:** HTTPS requests may fail with `SSL: CERTIFICATE_VERIFY_FAILED` in the Cloud Agent VM. Use `http://` URLs for testing (e.g. `http://example.com`).

### Linting

```bash
python3 -m flake8 test_accessibility.py
python3 -m pylint test_accessibility.py
```

### Dependencies

Only runtime dependency is `requests` (installed via `pip3 install requests`). Lint tools `flake8` and `pylint` are also installed.
