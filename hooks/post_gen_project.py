import os
import shutil
from pathlib import Path


def remove_files(files):
    for file in files:
        try:
            os.remove(file)
        except IOError:
            pass


def prepare_django(project_root):
    uses_django = '{{ cookiecutter.uses_django }}' == 'y'
    if uses_django:
        return

    # remove django related files
    files = [
        project_root / 'tests' / 'conftest.py',
        project_root / 'tests' / 'models.py',
        project_root / 'tests' / 'urls.py',
        project_root / 'env.example',
        project_root / 'manage.py',
        project_root / '{{ cookiecutter.project_slug }}' / 'settings.py',
        project_root / '{{ cookiecutter.project_slug }}' / 'urls.py',
        project_root / '{{ cookiecutter.project_slug }}' / 'wsgi.py',
    ]
    remove_files(files)


if __name__ == '__main__':
    project_root = Path(os.path.curdir)

    prepare_django(project_root)
