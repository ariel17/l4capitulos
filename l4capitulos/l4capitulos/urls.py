#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL dispatcher for project.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^account/', include('account.urls')),

    url(r'^backoffice/', include('backoffice.urls')),

    url(r'^mercadolibre/', include('mercadolibre.urls')),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )
