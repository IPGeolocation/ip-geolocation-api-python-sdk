"""Version helpers for the SDK."""

import re
from importlib import metadata
from pathlib import Path

FALLBACK_VERSION = "0.0.0"
_DISTRIBUTION_NAMES = ("ipgeolocationio", "ipgeolocation-sdk")
_PROJECT_VERSION_PATTERN = re.compile(r'^version\s*=\s*"([^"]+)"\s*$', re.MULTILINE)


def _load_local_version() -> str:
    """Read the source-tree version from ``pyproject.toml`` when package metadata is missing."""
    pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
    try:
        contents = pyproject_path.read_text(encoding="utf-8")
    except OSError:
        return FALLBACK_VERSION

    match = _PROJECT_VERSION_PATTERN.search(contents)
    if match is None:
        return FALLBACK_VERSION
    return match.group(1)


def get_version() -> str:
    """Return the installed package version, with a source-tree fallback."""
    for distribution_name in _DISTRIBUTION_NAMES:
        try:
            return metadata.version(distribution_name)
        except metadata.PackageNotFoundError:
            continue
    return _load_local_version()


__version__ = get_version()
