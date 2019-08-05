# {{ cookiecutter.project_name }}

[![pypi](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg)](https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}) [![Build Status](https://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.png?branch=master)](http://travis-ci.org/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) [![Coverage](https://coveralls.io/repos/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.png?branch=master)](https://coveralls.io/r/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}) ![python version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }}.svg) ![Project status](https://img.shields.io/pypi/status/{{ cookiecutter.project_slug }}.svg) ![license](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}.svg)

{{ cookiecutter.short_description }}


## Requirements

* Python {{ cookiecutter.python_version }} or newer


## Development

This project uses [poetry](https://poetry.eustace.io/) for packaging and
managing all dependencies and [pre-commit](https://pre-commit.com/) to run
[flake8](http://flake8.pycqa.org/) and [black](https://github.com/python/black).

Clone this repository and run

```bash
poetry develop
```

to create a virtual enviroment containing all dependencies.
Afterwards, You can run the test suite using

```bash
poetry run pytest
```

This repository follows the [Conventional Commits](https://www.conventionalcommits.org/)
style.
