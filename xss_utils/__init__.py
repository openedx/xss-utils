"""
Utilities to prevent possible XSS attacks on Django/Mako templates..
"""
__version__ = '0.1.4'

default_app_config = 'xss_utils.apps.XssUtilsConfig'  # pylint: disable=invalid-name
