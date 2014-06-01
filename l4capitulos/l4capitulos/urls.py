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

    url(r'^account/login/$', 'account.views.account_login',
        name='account_login'),

    url(r'^backoffice/$', 'backoffice.views.home', name='backoffice_home'),

    url(r'^backoffice/book/author/$', 'backoffice.views.book_author',
        name='backoffice_book_author'),

    url(r'^backoffice/book/author/add/$', 'backoffice.views.book_author_add',
        name='backoffice_book_author_add'),

    url(r'^backoffice/book/author/(?P<author_id>\d+)/edit/$',
        'backoffice.views.book_author_edit',
        name='backoffice_book_author_edit'),

    url(r'^backoffice/book/author/(?P<author_id>\d+)/delete/$',
        'backoffice.views.book_author_delete',
        name='backoffice_book_author_delete'),

    url(r'^backoffice/book/category/$', 'backoffice.views.book_category',
        name='backoffice_book_category'),

    url(r'^backoffice/book/category/add/$',
        'backoffice.views.book_category_add',
        name='backoffice_book_category_add'),

    url(r'^backoffice/book/category/(?P<category_id>\d+)/edit/$',
        'backoffice.views.book_category_edit',
        name='backoffice_book_category_edit'),

    url(r'^backoffice/book/category/(?P<category_id>\d+)/delete/$',
        'backoffice.views.book_category_delete',
        name='backoffice_book_category_delete'),

    url(r'^backoffice/book/editorial/$', 'backoffice.views.book_editorial',
        name='backoffice_book_editorial'),

    url(r'^backoffice/book/editorial/add/$',
        'backoffice.views.book_editorial_add',
        name='backoffice_book_editorial_add'),

    url(r'^backoffice/book/editorial/(?P<editorial_id>\d+)/edit/$',
        'backoffice.views.book_editorial_edit',
        name='backoffice_book_editorial_edit'),

    url(r'^backoffice/book/editorial/(?P<editorial_id>\d+)/delete/$',
        'backoffice.views.book_editorial_delete',
        name='backoffice_book_editorial_delete'),

    url(r'^backoffice/book/status/$', 'backoffice.views.book_status',
        name='backoffice_book_status'),

    url(r'^backoffice/book/status/add/$',
        'backoffice.views.book_status_add',
        name='backoffice_book_status_add'),

    url(r'^backoffice/book/status/(?P<status_id>\d+)/edit/$',
        'backoffice.views.book_status_edit',
        name='backoffice_book_status_edit'),

    url(r'^backoffice/book/status/(?P<status_id>\d+)/delete/$',
        'backoffice.views.book_status_delete',
        name='backoffice_book_status_delete'),

    url(r'^backoffice/book/book/$', 'backoffice.views.book_book',
        name='backoffice_book_book'),

    url(r'^backoffice/book/book/add/$', 'backoffice.views.book_book_add',
        name='backoffice_book_book_add'),

    url(r'^backoffice/book/book/(?P<book_id>\d+)/edit/$',
        'backoffice.views.book_book_edit', name='backoffice_book_book_edit'),

    url(r'^backoffice/book/book/(?P<book_id>\d+)/delete/$',
        'backoffice.views.book_book_delete',
        name='backoffice_book_book_delete'),

    url(r'^backoffice/book/book/(?P<book_id>\d+)/image/add/',
        'backoffice.views.book_image_add',
        name='backoffice_book_image_add'),

    url(r'^backoffice/book/book/(?P<book_id>\d+)/image/(?P<image_id>\d+)/'
        'edit/$', 'backoffice.views.book_image_edit',
        name='backoffice_book_image_edit'),

    url(r'^backoffice/book/book/(?P<book_id>\d+)/image/(?P<image_id>\d+)/'
        'delete/$', 'backoffice.views.book_image_delete',
        name='backoffice_book_image_delete'),

    url(r'^backoffice/finance/purchase/$', 'backoffice.views.finance_purchase',
        name='backoffice_finance_purchase'),

    url(r'^backoffice/finance/purchase/add/$',
        'backoffice.views.finance_purchase_add',
        name='backoffice_finance_purchase_add'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/edit/$',
        'backoffice.views.finance_purchase_edit',
        name='backoffice_finance_purchase_edit'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/delete/$',
        'backoffice.views.finance_purchase_delete',
        name='backoffice_finance_purchase_delete'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/item/add/$',
        'backoffice.views.finance_purchase_item_add',
        name='backoffice_finance_purchase_item_add'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/item/'
        '(?P<item_id>\d+)/edit/$', 'backoffice.views.finance_purchase_item_edit',
        name='backoffice_finance_purchase_item_edit'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/item/'
        '(?P<item_id>\d+)/delete/$', 'backoffice.views.finance_purchase_item_delete',
        name='backoffice_finance_purchase_item_delete'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/cost/add/$',
        'backoffice.views.finance_purchase_cost_add',
        name='backoffice_finance_purchase_cost_add'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/cost/'
        '(?P<cost_id>\d+)/edit/$', 'backoffice.views.finance_purchase_cost_edit',
        name='backoffice_finance_purchase_cost_edit'),

    url(r'^backoffice/finance/purchase/(?P<purchase_id>\d+)/cost/'
        '(?P<cost_id>\d+)/delete/$', 'backoffice.views.finance_purchase_cost_delete',
        name='backoffice_finance_purchase_cost_delete'),

    url(r'^backoffice/finance/sell/$', 'backoffice.views.finance_sell',
        name='backoffice_finance_sell'),

    url(r'^backoffice/finance/sell/add/$',
        'backoffice.views.finance_sell_add',
        name='backoffice_finance_sell_add'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/edit/$',
        'backoffice.views.finance_sell_edit',
        name='backoffice_finance_sell_edit'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/delete/$',
        'backoffice.views.finance_sell_delete',
        name='backoffice_finance_sell_delete'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/item/add/$',
        'backoffice.views.finance_sell_item_add',
        name='backoffice_finance_sell_item_add'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/item/'
        '(?P<item_id>\d+)/edit/$', 'backoffice.views.finance_sell_item_edit',
        name='backoffice_finance_sell_item_edit'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/item/'
        '(?P<item_id>\d+)/delete/$',
        'backoffice.views.finance_sell_item_delete',
        name='backoffice_finance_sell_item_delete'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/cost/add/$',
        'backoffice.views.finance_sell_cost_add',
        name='backoffice_finance_sell_cost_add'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/cost/'
        '(?P<cost_id>\d+)/edit/$', 'backoffice.views.finance_sell_cost_edit',
        name='backoffice_finance_sell_cost_edit'),

    url(r'^backoffice/finance/sell/(?P<sell_id>\d+)/cost/'
        '(?P<cost_id>\d+)/delete/$',
        'backoffice.views.finance_sell_cost_delete',
        name='backoffice_finance_sell_cost_delete'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT
        }),
    )
