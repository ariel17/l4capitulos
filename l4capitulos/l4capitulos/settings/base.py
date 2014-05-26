#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Django settings for l4capitulos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), '..')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = ('templates',)

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'raven.contrib.django.raven_compat',
    'sorl.thumbnail',
    'south',
)

PROJECT_APPS = (
    'account',
    'backoffice',
    'book',
    'common',
    'finance',
    'mercadolibre',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'l4capitulos.urls'

WSGI_APPLICATION = 'l4capitulos.wsgi.application'

LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/backoffice/home/'


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['sentry'],
            'level': 'ERROR',
            'propagate': True,
        },
        'mercadolibre': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}
########## END LOGGING CONFIGURATION


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.normpath(os.path.join(BASE_DIR, 'assets')),
)


# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-MEDIA_ROOT
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-MEDIA_URL
MEDIA_URL = '/media/'


# Crispy forms configuration
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Default settings for Backoffice
BACKOFFICE_PROFILE_DEFAULT_LAST_ACTIVITY_ITEMS = 10


from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# Common application configuration
IMAGES_ROOT = "img"
IMAGES_DEFAULT = os.path.join(IMAGES_ROOT, 'no-img.png')


# Book application configuration
BOOK_IMAGES_PATH = os.path.join(IMAGES_ROOT, 'book')


# Base sorl thumbnail configuration
THUMBNAIL_KEY_PREFIX = 'sorl-thumbnail-l4capitulos'
THUMBNAIL_PREFIX = os.path.join(IMAGES_ROOT, 'cache/')

########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')
########## END SECRET CONFIGURATION

# MercadoLibre integration configuration
MERCADOLIBRE_SELLER_ID = get_env_setting('MERCADOLIBRE_SELLER_ID')
MERCADOLIBRE_APP_ID = get_env_setting('MERCADOLIBRE_SELLER_ID')
MERCADOLIBRE_SECRET_KEY = get_env_setting('MERCADOLIBRE_SECRET_KEY')

# vim: ai ts=4 sts=4 et sw=4 ft=python
