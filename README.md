# Cookiecutter PyPackage

A Modern [Cookiecutter] template for Python packages and applications using [Poetry].

## Features

* [Poetry]: Dependency management and packaging
* [Tox]: Easily run tests for different python versions
* Github Actions: Ready for Continous Integration testing

  * Run tests for different python versions using tox
  * Test for [PEP8] compliance
  * Enforce the usage of [black]
  * Preconfigured [coveralls]

* Tests using [Pytest] including support for

  * [pytest-mock] for mocking
  * code coverage using [coverage.py]

* [pre-commit] hook to run

  * [flake8],
  * [isort],
  * [mypy] and
  * [black]

* (optional) Preconfigured for [Django] applications

  * Support for [Twelve-factor-Methodology] using [django-environ]

* Simple pull request template with checklist

## Quickstart

Get the latest version of [Cruft] (or [Cookiecutter])
I recommend [pipx] to install it into a global isolated environment.

```sh
pipx install cruft
```

Generate a new python package

```sh
cruft create https://github.com/escaped/cookiecutter-pypackage.git
cd <chosen project slug>
git init
git add .
git commit -m "feat: initial project structure"
```

In order get automatic releases to [pypi] you need to add your pypi access token to the secrets github.
Instructions can be found here: [python.org](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/#saving-credentials-on-github).


[Conventional-Commits]: http://conventionalcommits.org/
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[Cruft]: https://github.com/cruft/cruft
[Django]: https://www.djangoproject.com/
[PEP8]: https://www.python.org/dev/peps/pep-0008/
[Poetry]: https://poetry.eustace.io/
[Pytest]: https://docs.pytest.org/en/latest/
[Tox]: http://testrun.org/tox/
[Twelve-factor-Methodology]: https://www.12factor.net/
[black]: https://black.readthedocs.io/en/stable/
[coverage.py]: https://coverage.readthedocs.io/
[coveralls]: https://coveralls.io/
[django-environ]: https://github.com/joke2k/django-environ
[flake8]: http://flake8.pycqa.org/en/latest/
[isort]: https://github.com/timothycrosley/isort
[mypy]: http://mypy-lang.org/
[pip]: https://pip.pypa.io/en/stable/
[pipx]: https://github.com/pipxproject/pipx
[pytest-mock]: https://github.com/pytest-dev/pytest-mock/
[pypi]: https://pypi.org/
