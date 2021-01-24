# Cookiecutter PyPackage

A modern opinionated [Cookiecutter] template for Python packages and applications using [Poetry].

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

* [pre-commit] hook to automatically run

  * [autoflake] - automatically removes unused imports and variables,
  * [isort] - automatically sorts imports alphabetically, and automatically separated into sections and by type,
  * [black] - automatically formats your code,
  * [flake8] - checks code against code style (PEP8), programming errors and complexity,
    * [flake8-bugbear] - finds likely bugs and design problems in your program,
    * [flake8-builtins] - Checks for python builtins being used as variables or parameters,
    * [flake8-debugger] - Checks for `pdb` statements,
    * [pep8-naming] - Checks code against PEP 8 naming conventions,
    * [flake8-comprehensions] - helps you write better list/set/dict comprehensions,
  * [mypy] - static type checker,

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

### Publish releases to pypi

In order get automatic releases to [pypi] you need to add your pypi access token to the github secrets (named `PYPI_TOKEN`).
Instructions can be found here: [python.org](https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/#saving-credentials-on-github).

### Autoupdate template

This cookiecutter template comes with an auto update feature if the project was created using [cruft].
A GitHub action automatically checks for updates and creates a pull request.

It is required to add a [personal access token](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token)
as github secret to the repository (named `AUTO_UPDATE_GITHUB_TOKEN`).
While creating the access token, the following permissions have to be granted

* repo
* workflow

[autoflake]: https://pypi.org/project/autoflake/
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
[flake8-bugbear]: https://pypi.org/project/flake8-bugbear/
[flake8-builtins]: https://pypi.org/project/flake8-builtins/
[flake8-comprehensions]: https://pypi.org/project/flake8-comprehensions/
[flake8-debugger]: https://pypi.org/project/flake8-debugger/
[isort]: https://github.com/timothycrosley/isort
[mypy]: http://mypy-lang.org/
[pep8-naming]: https://pypi.org/project/pep8-naming/
[pip]: https://pip.pypa.io/en/stable/
[pipx]: https://github.com/pipxproject/pipx
[pre-commit]: https://pre-commit.com/
[pytest-mock]: https://github.com/pytest-dev/pytest-mock/
[pypi]: https://pypi.org/
