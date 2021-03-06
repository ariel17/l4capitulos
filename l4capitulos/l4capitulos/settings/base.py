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

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS, AUTHENTICATION_BACKENDS
from django.contrib.messages import constants as messages
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
    'django.contrib.sites'
)

THIRD_PARTY_APPS = (
    'crispy_forms',
    'raven.contrib.django.raven_compat',
    'sorl.thumbnail',
    'south',
    'social.apps.django_app.default',
)

PROJECT_APPS = (
    'account',
    'backoffice',
    'book',
    'common',
    'finance',
    'totalizer',
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

SITE_ID = 1

ROOT_URLCONF = 'l4capitulos.urls'

WSGI_APPLICATION = 'l4capitulos.wsgi.application'

LOGIN_URL = '/account/login/'

LOGIN_REDIRECT_URL = '/backoffice/home/'

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


FORMAT_MODULE_PATH = 'formats'

# Login Configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
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
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'totalizer': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'backoffice': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

# Crispy forms configuration
CRISPY_TEMPLATE_PACK = 'bootstrap3'


# Default settings for Backoffice
BACKOFFICE_PROFILE_DEFAULT_LAST_ACTIVITY_ITEMS = 10

MESSAGE_TAGS = {
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# Common application configuration
IMAGES_ROOT = 'img'
IMAGES_DEFAULT = os.path.join(IMAGES_ROOT, 'no-img.png')


# Book application configuration
BOOK_IMAGES_PATH = os.path.join(IMAGES_ROOT, 'book')

# Finance application configuration
FINANCE_INVOICE_PATH = 'invoice'


# Backoffice application configuration
BACKOFFICE_DEFAULT_CHART_SELL_DAYS = 7
BACKOFFICE_DEFAULT_RECENT_ITEMS = 5


# Base sorl thumbnail configuration
THUMBNAIL_KEY_PREFIX = 'sorl-thumbnail-l4capitulos'
THUMBNAIL_PREFIX = os.path.join(IMAGES_ROOT, 'cache/')


# Social media configuration
TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
) + AUTHENTICATION_BACKENDS

SOCIAL_AUTH_LOGIN_URL = LOGIN_URL
SOCIAL_AUTH_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL
SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'manage_pages', 'publish_actions', 'user_photos', 'publish_stream',
    'offline_access'
]

FACEBOOK_IMAGE_POST_URL = "https://www.facebook.com/photo.php?fbid="

# vim: ai ts=4 sts=4 et sw=4 ft=python
