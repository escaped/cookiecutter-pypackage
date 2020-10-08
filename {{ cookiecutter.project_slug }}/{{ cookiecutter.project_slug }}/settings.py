import os
import sys
from pathlib import Path

import environ

TESTING = os.path.basename(sys.argv[0]) in ('pytest', 'py.test')
PROJECT_DIR = Path(__file__).parent

# set default values and casting
env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    DEFAULT_FROM_EMAIL=(str, ''),
    MEDIA_ROOT=(str, None),
    SECRET_KEY=(str, None),
    SENTRY_DSN=(str, None),
    SITE_DOMAIN=(str, ''),
    STATIC_ROOT=(str, None),
)

# load existing `.env` file
env_file = PROJECT_DIR / '..' / '.env'
if 'ENV_CONFIG' in os.environ:
    env_file = Path(os.environ['ENV_CONFIG'])

if env_file.is_file():
    with open(env_file, encoding='utf-8') as f:
        environ.Env.read_env(f)
else:
    environ.Env.read_env()


DEBUG = env('DEBUG')

SITE_ROOT = PROJECT_DIR
SITE_DOMAIN = env('SITE_DOMAIN')
ALLOWED_HOSTS = [SITE_DOMAIN] + env('ALLOWED_HOSTS')

SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = '{{ cookiecutter.project_slug }}.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ]
        },
    }
]

WSGI_APPLICATION = '{{ cookiecutter.project_slug }}.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {'default': env.db()}

# SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
#
CACHES = {'default': env.cache()}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Berlin'

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = env('MEDIA_ROOT')

if env('STATIC_ROOT'):
    STATIC_ROOT = env('STATIC_ROOT')

STATICFILES_DIRS = (PROJECT_DIR / 'static',)


# E-Mail settings

email_config = env.email_url()
EMAIL_FILE_PATH = email_config['EMAIL_FILE_PATH']
EMAIL_HOST_USER = email_config['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = email_config['EMAIL_HOST_PASSWORD']
EMAIL_HOST = email_config['EMAIL_HOST']
EMAIL_PORT = email_config['EMAIL_PORT']
EMAIL_BACKEND = email_config['EMAIL_BACKEND']
EMAIL_USE_TLS = email_config.get('EMAIL_USE_TLS', False)

DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL')


# Debug settings

if DEBUG:
    INTERNAL_IPS = ('localhost', '127.0.0.1')

    try:
        import debug_toolbar  # NOQA
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ('debug_toolbar',)
        MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

    try:
        import django_extensions  # NOQA
    except ImportError:
        pass
    else:
        INSTALLED_APPS += ('django_extensions',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {'format': '%(levelname)s %(asctime)s %(name)s %(message)s'},
        'simple': {'format': '>>> %(levelname)s %(message)s'},
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG' if DEBUG else 'WARNING',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'WARNING',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django.db': {'handlers': ['console'], 'level': 'WARNING'},
        'factory': {'level': 'WARNING'},
        'py.warnings': {'level': 'DEBUG', 'handlers': ['console'], 'propagate': False},
        'requests': {'level': 'WARNING'},
        'raven': {'level': 'WARNING', 'handlers': ['console'], 'propagate': False},
        'flake8': {'level': 'WARNING', 'handlers': ['console'], 'propagate': False},
        '': {'handlers': ['console'], 'level': 'DEBUG'},
    },
}


if env('SENTRY_DSN'):
    CELERY_SEND_TASK_ERROR_EMAILS = False
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
    RAVEN_CONFIG = {'dsn': env('SENTRY_DSN'), 'release': '0.1'}  # __version__,

    # defined sentry handler so production works without `raven` installed
    LOGGING['handlers']['sentry'] = {
        'level': 'WARNING',
        'class': 'raven.contrib.django.handlers.SentryHandler',
        'formatter': 'verbose',
    }
    LOGGING['loggers']['']['handlers'].append('sentry')
    LOGGING['loggers']['management_commands']['handlers'].append('sentry')
