:github_url: https://github.com/RetroArcher/RetroArcher.bundle/tree/nightly/docs/source/contributing/testing.rst

Testing
=======

Flake8
------
PlexyGlass uses `Flake8 <https://pypi.org/project/flake8/>`__ for enforcing consistent code styling. Flake is included
in the ``requirements-dev.txt``.

The config file for flake8 is ``.flake8``. This is already included in the root of the repo and should not be modified.

Test with Flake8
   .. code-block:: bash

      python -m flake8

Sphinx
------
PlexyGlass uses `Sphinx <https://www.sphinx-doc.org/en/master/>`__ for documentation building. Sphinx is included
in the ``requirements-dev.txt``.

PlexyGlass follows `numpydoc <https://numpydoc.readthedocs.io/en/latest/format.html>`__ styling and formatting in
docstrings. This will be tested when building the docs. `numpydoc` is included in the ``requirements-dev.txt``.

The config file for Sphinx is ``docs/source/conf.py``. This is already included in the root of the repo and should not
be modified.

Test with Sphinx
   .. code-block:: bash

      cd docs
      make html

   Alternatively

   .. code-block:: bash

      cd docs
      sphinx-build -b html source build

pytest
------
.. Todo:: PyTest is not yet implemented.

PlexyGlass uses `pytest <https://pypi.org/project/pytest/>`__ for unit testing. pytest is included in the
``requirements-dev.txt``.

No config is required for pytest.

Test with pytest
   .. code-block:: bash

      python -m pytest
