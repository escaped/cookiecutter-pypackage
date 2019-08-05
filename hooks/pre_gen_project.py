import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
MODULE_NAME = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, MODULE_NAME):
    print(
        'ERROR: The project slug ({}) is not a valid Python module name'.format(
            MODULE_NAME,
        )
    )
    sys.exit(1)

VERSION_REGEX = r'\d\.\d'
PYTHON_VERSION = '{{ cookiecutter.python_version }}'

if not re.match(VERSION_REGEX, PYTHON_VERSION):
    print(
        'ERROR: The python version ({}) must look like 3.7'.format(
            PYTHON_VERSION,
        )
    )
    sys.exit(1)
