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
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


SECRET_KEY = "(b-5!nc)b*x--bcx-d!d@g+l!4tmp1in*gfidq)+7ta@&9tq+&"


THUMBNAIL_DEBUG = True


# Sentry client configuration
RAVEN_CONFIG = {
    'dsn': 'http://7ab53ea775ce4a25abf4fff81189ba93:'
    'e4319772508648e0b206ff863d85d411@sentry.ariel17.com.ar/9',
}


# vim: ai ts=4 sts=4 et sw=4 ft=python
