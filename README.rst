Cookiecutter PyPackage
----------------------

A Modern Cookiecutter_ template for Python packages and applications using Poetry_.


Features
========

* Poetry_: Dependency management and packaging
* Tox_: Easily run tests for different python versions
* Travis-CI_: Ready for Continous Integration testing

  * Run all tests
  * Test for PEP8_ compliance
  * Enforce the usage of black_
  * Enforce Conventional-Commits_
  * Preconfigured coveralls_

* Tests using Pytest_ including support for

  * flake8_
  * isort_
  * mypy_
  * running tests in random order (pytest-randomly_)
  * pytest-mock_ for mocking
  * code coverage using coverage.py_

* pre-commit_ hook to run

  * flake8_ validation,
  * mypy_ validation and
  * code formatting (black_)

* (optional) Preconfigured for Django_ applications

  * Support for Twelve-factor-Methodology_ using django-environ_


Quickstart
==========

Get the latest Cookiecutter_.
I recommend pipx_ for installation, but using pip_ is also possible ::

  pipx install cookiecutter

Generate a new python package ::

  cookiecutter https://github.com/escaped/cookiecutter-pypackage.git
  cd <chosen project slug>
  git init
  git add .
  git commit -m "feat: initial project structure"
  poetry install
  poetry run pre-commit install


.. _Conventional-Commits: http://conventionalcommits.org/
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Django: https://www.djangoproject.com/
.. _PEP257: https://www.python.org/dev/peps/pep-0257/
.. _PEP8: https://www.python.org/dev/peps/pep-0008/
.. _Poetry: https://poetry.eustace.io/
.. _Pytest: https://docs.pytest.org/en/latest/
.. _Tox: http://testrun.org/tox/
.. _Travis-CI: http://travis-ci.org/
.. _Twelve-factor-Methodology: https://www.12factor.net/
.. _black: https://black.readthedocs.io/en/stable/
.. _coverage.py: https://coverage.readthedocs.io/
.. _coveralls: https://coveralls.io/
.. _django-environ: https://github.com/joke2k/django-environ
.. _flake8: http://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/timothycrosley/isort
.. _mypy: http://mypy-lang.org/
.. _pip: https://pip.pypa.io/en/stable/
.. _pipx: https://github.com/pipxproject/pipx
.. _pytest-mock: https://github.com/pytest-dev/pytest-mock/
.. _pytest-randomly: https://github.com/pytest-dev/pytest-randomly
