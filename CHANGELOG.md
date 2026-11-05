# Changelog

## 3.0.1

- Hide the configured API key in printed settings, SDK request logs and error messages, including errors in typed bulk results.
- Keep lookup data and custom headers from being sent to a different server on a redirect.
- Read compressed responses in small chunks. Keep the HTTP status if an error response is too large or cut short.
- Check that typed bulk lookups return one result per input.
- Add Arabic (`ar`) for single and bulk lookups.
- Include CDN, proxy, bot and corporate gateway details in typed results.

## 3.0.0

- Requires Python 3.10 or newer.
- Updated HTTP, certificate, test and build dependency minimums.
- Added dependency auditing and checks across supported Python versions.

## 2.0.0

- Added the Python SDK for the IPGeolocation API unified endpoints.
- Supports typed and raw responses for single and bulk IP lookups.
- Includes response models for location, company, ASN, security, abuse, timezone, network, currency, and user-agent data.
- Bulk typed results use `result.data` for success items and `result.error.message` for error items.
- Includes validation, exception mapping, unit tests, and optional live integration and field-parity tests.
