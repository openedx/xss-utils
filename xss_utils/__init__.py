"""
Utilities to prevent possible XSS attacks on Django/Mako templates..
"""
__version__ = '0.2.0'

default_app_config = 'xss_utils.apps.XssUtilsConfig'  # pylint: disable=invalid-name
