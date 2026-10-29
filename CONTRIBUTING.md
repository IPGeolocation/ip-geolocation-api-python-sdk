# Contributing

## Requirements

- Python 3.10+
- `pip`
- Node.js 24 and Postman CLI 1.73.0 for local HTTP integration tests

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
npm install --global postman-cli@1.73.0
```

## Run Tests

```bash
pytest
```

HTTP integration tests run both clients against a local Postman simulation.

## Coverage Check

```bash
pytest --cov=src/ipgeolocation --cov-report=term-missing --cov-fail-under=90
```

## Static Checks

```bash
ruff check src tests
mypy src
pyright
```

## Dependency and Build Checks

```bash
python -m build
```

Dependency audits use Python 3.11+ for the scanner and inspect the SDK's test environment:

```bash
python3.11 -m venv .venv-audit
.venv-audit/bin/python -m pip install -e '.[audit]'
.venv-audit/bin/pip-audit --skip-editable \
  --path "$(.venv/bin/python -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')"
```

## Live Tests

Live tests are disabled by default and consume API credits.

```bash
IPGEO_RUN_LIVE_TESTS=true \
IPGEO_FREE_KEY=your_free_key \
IPGEO_PAID_KEY=your_paid_key \
pytest tests/test_live_integration.py
```

Optional live field-parity hardening:

```bash
IPGEO_RUN_LIVE_HARDENING=true \
IPGEO_PAID_KEY=your_paid_key \
pytest tests/test_live_field_parity.py
```
