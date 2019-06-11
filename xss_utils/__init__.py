"""
Utilities to prevent possible XSS attacks on Django/Mako templates..
"""

from __future__ import absolute_import, unicode_literals

__version__ = '0.1.1'

default_app_config = 'xss_utils.apps.XssUtilsConfig'  # pylint: disable=invalid-name
