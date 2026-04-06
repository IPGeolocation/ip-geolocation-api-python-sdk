# Changelog

## 3.0.0

- Added the Python SDK for the IPGeolocation API unified endpoints.
- Supports typed and raw responses for single and bulk IP lookups.
- Includes response models for location, company, ASN, security, abuse, timezone, network, currency, and user-agent data.
- Bulk typed results use `result.data` for success items and `result.error.message` for error items.
- Includes validation, exception mapping, unit tests, and optional live integration and field-parity tests.
