#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Production settings and globals.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import os
from os import environ

from base import *


# Allowed hosts configuration
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']

# Database configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'l4capitulos',
        'USER': 'l4capitulos',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Cache configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
        'KEY_PREFIX': 'production-',
    },
}

# Installed apps configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS += ('gunicorn',)

# Sentry client configuration
RAVEN_CONFIG = {
    'dsn': 'http://ca12a551a6d24cd68ae2fd7ff8cdf402:'
    '15ff77ecb7734f9bac1b8b614c03de31@sentry.ariel17.com.ar/8',
}

# Secret key configuration
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')

# Social media configuration

SOCIAL_AUTH_FACEBOOK_KEY = get_env_setting('FACEBOOK_APP_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = get_env_setting('FACEBOOK_APP_SECRET')
FACEBOOK_FAN_APP_ID = get_env_setting('FACEBOOK_FAN_APP_ID')

# vim: ai ts=4 sts=4 et sw=4 ft=python
