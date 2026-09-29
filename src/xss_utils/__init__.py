"""
Utilities to prevent possible XSS attacks on Django/Mako templates..
"""
from importlib.metadata import version as get_version

__version__ = get_version('xss-utils')
