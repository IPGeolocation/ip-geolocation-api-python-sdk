# Contributing

## Requirements

- Python 3.8+
- `pip`

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run Tests

```bash
pytest
```

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
