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
    url(r'^backoffice/$', 'backoffice.views.home', name='backoffice_home'),

    url(r'^backoffice/book/$', 'backoffice.views.book',
        name='backoffice_book'),

    url(r'^backoffice/book/add/$', 'backoffice.views.book_add',
        name='backoffice_book_add'),

    url(r'^backoffice/book/edit/(?P<book_id>\d+)/$',
        'backoffice.views.book_edit', name='backoffice_book_edit'),

    url(r'^backoffice/book/delete/(?P<book_id>\d+)/$',
        'backoffice.views.book_delete', name='backoffice_book_delete'),
)
