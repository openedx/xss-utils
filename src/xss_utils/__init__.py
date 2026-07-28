"""
Utilities to prevent possible XSS attacks on Django/Mako templates..
"""
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version('xss-utils')
except PackageNotFoundError:  # pragma: no cover
    # Only hit if this package is imported without being installed at all
    # (e.g. run directly from a source checkout with no metadata available).
    pass
