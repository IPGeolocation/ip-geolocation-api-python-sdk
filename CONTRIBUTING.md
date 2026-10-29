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
pip-audit
python -m build
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
