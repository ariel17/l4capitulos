#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Local settings for project.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from base import *


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}


# Sentry client configuration
RAVEN_CONFIG = {
    'dsn': 'http://0d61a2894ce9463da384e183b020cb29:'
    '3d685a797f71475bb69eb0a282ff593d@sentry.ariel17.com.ar/11',
}


SECRET_KEY = "(b-5!nc)b*x--bcx-d!d@g+l!4tmp1in*gfidq)+7ta@&9tq+&"

# vim: ai ts=4 sts=4 et sw=4 ft=python
