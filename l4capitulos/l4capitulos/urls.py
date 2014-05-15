#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: The URL dispatcher for project.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'l4capitulos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^backoffice/$', 'backoffice.views.backoffice_home',
        name='backoffice_home')
)
