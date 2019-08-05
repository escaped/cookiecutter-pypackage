{% if cookiecutter.uses_django == "y" %}
import django
from django.conf import settings


def pytest_configure():
    """
    Basic configuration of django for testing a django module.
    """
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        ROOT_URLCONF='tests.urls',
        INSTALLED_APPS=(
            'tests',
        ),
    )

    django.setup()
{% endif %}
