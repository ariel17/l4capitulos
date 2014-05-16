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

    url(r'^backoffice/book/author/$', 'backoffice.views.book_author',
        name='backoffice_book_author'),

    url(r'^backoffice/book/author/add/$', 'backoffice.views.book_author_add',
        name='backoffice_book_author_add'),

    url(r'^backoffice/book/author/edit/(?P<author_id>\d+)/$',
        'backoffice.views.book_author_edit',
        name='backoffice_book_author_edit'),

    url(r'^backoffice/book/author/delete/(?P<author_id>\d+)/$',
        'backoffice.views.book_author_delete',
        name='backoffice_book_author_delete'),

    url(r'^backoffice/book/book/$', 'backoffice.views.book_book',
        name='backoffice_book_book'),

    url(r'^backoffice/book/book/add/$', 'backoffice.views.book_book_add',
        name='backoffice_book_book_add'),

    url(r'^backoffice/book/book/edit/(?P<book_id>\d+)/$',
        'backoffice.views.book_book_edit', name='backoffice_book_book_edit'),

    url(r'^backoffice/book/book/delete/(?P<book_id>\d+)/$',
        'backoffice.views.book_book_delete',
        name='backoffice_book_book_delete'),

    url(r'^backoffice/finance/purchase/$', 'backoffice.views.finance_purchase',
        name='backoffice_finance_purchase'),

    url(r'^backoffice/finance/purchase/add/$',
        'backoffice.views.finance_purchase_add',
        name='backoffice_finance_purchase_add'),

    url(r'^backoffice/finance/purchase/edit/(?P<purchase_id>\d+)/$',
        'backoffice.views.finance_purchase_edit',
        name='backoffice_finance_purchase_edit'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/$',
        'backoffice.views.finance_purchase_delete',
        name='backoffice_finance_purchase_delete'),
)
