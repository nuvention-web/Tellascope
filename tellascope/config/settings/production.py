"""
Django settings for Tellascope project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('TELLASCOPE_DJANGO_SECRET_KEY', None)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # tools
    'tinymce',
    'storages',

    # apps
    'tellascope.landing',

    # local
    #'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'elections.urls'

WSGI_APPLICATION = 'elections.config.app.application'

ADMINS = (
    ('Alex Duner', 'asduner@gmail.com'),
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'nbn_elections',
        'USER': 'nbn_elections',
        'PASSWORD': os.environ.get('ELECTIONS_DB_PASSWORD', None),
        'HOST': '127.0.0.1'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'tellascope/templates'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

# STATIC_ROOT = '/static'
# STATIC_URL = 'http://nbn-elections.s3.amazonaws.com/static/'
# STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', None)
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', None)
# AWS_STORAGE_BUCKET_NAME = 'nbn-elections'
# AWS_QUERYSTRING_AUTH = False
# AWS_S3_URL_PROTOCOL = 'http:'
# AWS_S3_SECURE_URLS = False

# TinyMCE Setup
# TINYMCE_JS_URL = 'https://nbn-elections.s3.amazonaws.com/static/tiny_mce/tiny_mce.js'
# TINYMCE_DEFAULT_CONFIG = {
#     'plugins': "",
#     'theme': "advanced",
#     'cleanup_on_startup': True,
#     'custom_undo_redo_levels': 10,
# }

ALLOWED_HOSTS = ['*']
