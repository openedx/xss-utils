Change Log
----------

..
   All enhancements and patches to xss_utils will be documented
   in this file.  It adheres to the structure of http://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (http://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
~~~~~~~~~~

[0.8.0] - 2025-04-17
~~~~~~~~~~~~~~~~~~~~

* Add support for django 5.2.

[0.7.1] - 2025-02-28
~~~~~~~~~~~~~~~~~~~~

* Fix to PyPI publishing workflow.

[0.7.0] - 2025-02-28
~~~~~~~~~~~~~~~~~~~~

* Drop support for Python 3.8

[0.6.0] - 2024-04-22
~~~~~~~~~~~~~~~~~~~~

* Test and declare Python 3.11 and 3.12 compatibility.

[0.5.0] - 2023-08-01
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Switch from ``edx-sphinx-theme`` to ``sphinx-book-theme`` since the former is
  deprecated.  See https://github.com/openedx/edx-sphinx-theme/issues/184 for
  more details.
* Added supportt for Django 4.2

[0.4.0] - 2022-01-20
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* Added Support for Django40

Dropped
_______

* Dropped Django22, 30, 31 from CI

[0.3.0] - 2021-07-07
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* Support for django3.0, 3.1, 3.2

[0.1.0] - 2018-08-17
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* Utilities to enable html escaping, preventing Cross Site Scripting (XSS) attacks in Django templates.
