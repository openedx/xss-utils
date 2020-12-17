xss-utils
=============================

Utilities to prevent possible Cross Site Scripting (XSS) attacks on Django/Mako templates.

Overview
------------------------

This repo houses utility functions to protect edx codebase (Python, Javascript and other templating
engine eg django/mako) against possible XSS attacks. Helper code include html & js escaping filters
for django and mako templates.
For more information, please read `Preventing Cross Site Scripting Vulnerabilities <https://edx.readthedocs.io/projects/edx-developer-guide/en/latest/preventing_xss/index.html>`_.

Documentation
-------------

The full documentation is in the docs directory
TODO: Publish to https://xss-utils.readthedocs.org.

License
-------

The code in this repository is licensed under the AGPL 3.0 unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

How To Contribute
-----------------

Contributions are very welcome.

Please read `How To Contribute <https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst>`_ for details.

Even though they were written with ``edx-platform`` in mind, the guidelines
should be followed for Open edX code in general.

PR description template should be automatically applied if you are sending PR from github interface; otherwise you
can find it it at `PULL_REQUEST_TEMPLATE.md <https://github.com/edx/xss-utils/blob/master/.github/PULL_REQUEST_TEMPLATE.md>`_

Issue report template should be automatically applied if you are sending it from github UI as well; otherwise you
can find it at `ISSUE_TEMPLATE.md <https://github.com/edx/xss-utils/blob/master/.github/ISSUE_TEMPLATE.md>`_

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@edx.org.

Getting Help
------------

Have a question about this repository, or about Open edX in general?  Please
refer to this `list of resources`_ if you need any assistance.

.. _list of resources: https://open.edx.org/getting-help


.. |pypi-badge| image:: https://img.shields.io/pypi/v/xss-utils.svg
    :target: https://pypi.python.org/pypi/xss-utils/
    :alt: PyPI

.. |ci-badge| image:: https://github.com/edx/xss-utils/workflows/Python%20CI/badge.svg?branch=master
    :target: https://github.com/edx/xss-utils/actions?query=workflow%3A%22Python+CI%22
    :alt: CI

.. |codecov-badge| image:: http://codecov.io/github/edx/xss-utils/coverage.svg?branch=master
    :target: http://codecov.io/github/edx/xss-utils?branch=master
    :alt: Codecov

.. |doc-badge| image:: https://readthedocs.org/projects/xss-utils/badge/?version=latest
    :target: http://xss-utils.readthedocs.io/en/latest/
    :alt: Documentation

.. |pyversions-badge| image:: https://img.shields.io/pypi/pyversions/xss-utils.svg
    :target: https://pypi.python.org/pypi/xss-utils/
    :alt: Supported Python versions

.. |license-badge| image:: https://img.shields.io/github/license/edx/xss-utils.svg
    :target: https://github.com/edx/xss-utils/blob/master/LICENSE.txt
    :alt: License
