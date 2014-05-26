#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url


urlpatterns = patterns('backoffice.views',

    url(r'^$', 'home', name='backoffice_home'),

    url(r'^book/author/$', 'book_author', name='backoffice_book_author'),

    url(r'^book/author/add/$', 'book_author_add',
        name='backoffice_book_author_add'),

    url(r'^book/author/(?P<author_id>\d+)/edit/$', 'book_author_edit',
        name='backoffice_book_author_edit'),

    url(r'^book/author/(?P<author_id>\d+)/delete/$', 'book_author_delete',
        name='backoffice_book_author_delete'),

    url(r'^book/category/$', 'book_category', name='backoffice_book_category'),

    url(r'^book/category/add/$', 'book_category_add',
        name='backoffice_book_category_add'),

    url(r'^book/category/(?P<category_id>\d+)/edit/$', 'book_category_edit',
        name='backoffice_book_category_edit'),

    url(r'^book/category/(?P<category_id>\d+)/delete/$',
        'book_category_delete', name='backoffice_book_category_delete'),

    url(r'^book/status/$', 'book_status', name='backoffice_book_status'),

    url(r'^book/status/add/$', 'book_status_add',
        name='backoffice_book_status_add'),

    url(r'^book/status/(?P<status_id>\d+)/edit/$', 'book_status_edit',
        name='backoffice_book_status_edit'),

    url(r'^book/status/(?P<status_id>\d+)/delete/$', 'book_status_delete',
        name='backoffice_book_status_delete'),

    url(r'^book/book/$', 'book_book', name='backoffice_book_book'),

    url(r'^book/book/add/$', 'book_book_add', name='backoffice_book_book_add'),

    url(r'^book/book/(?P<book_id>\d+)/edit/$', 'book_book_edit',
        name='backoffice_book_book_edit'),

    url(r'^book/book/(?P<book_id>\d+)/delete/$', 'book_book_delete',
        name='backoffice_book_book_delete'),

    url(r'^book/book/(?P<book_id>\d+)/image/add/', 'book_image_add',
        name='backoffice_book_image_add'),

    url(r'^book/book/(?P<book_id>\d+)/image/(?P<image_id>\d+)/edit/$',
        'book_image_edit', name='backoffice_book_image_edit'),

    url(r'^book/book/(?P<book_id>\d+)/image/(?P<image_id>\d+)/delete/$',
        'book_image_delete', name='backoffice_book_image_delete'),

    url(r'^finance/purchase/$', 'finance_purchase',
        name='backoffice_finance_purchase'),

    url(r'^finance/purchase/add/$', 'finance_purchase_add',
        name='backoffice_finance_purchase_add'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/edit/$',
        'finance_purchase_edit', name='backoffice_finance_purchase_edit'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/delete/$',
        'finance_purchase_delete', name='backoffice_finance_purchase_delete'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/item/add/$',
        'finance_purchase_item_add',
        name='backoffice_finance_purchase_item_add'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/item/(?P<item_id>\d+)/edit/$',
        'finance_purchase_item_edit',
        name='backoffice_finance_purchase_item_edit'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/item/(?P<item_id>\d+)/'
        'delete/$', 'finance_purchase_item_delete',
        name='backoffice_finance_purchase_item_delete'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/cost/add/$',
        'finance_purchase_cost_add',
        name='backoffice_finance_purchase_cost_add'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/cost/(?P<cost_id>\d+)/edit/$',
        'finance_purchase_cost_edit',
        name='backoffice_finance_purchase_cost_edit'),

    url(r'^finance/purchase/(?P<purchase_id>\d+)/cost/(?P<cost_id>\d+)/'
        'delete/$', 'finance_purchase_cost_delete',
        name='backoffice_finance_purchase_cost_delete'),

    url(r'^finance/sell/$', 'finance_sell', name='backoffice_finance_sell'),

    url(r'^finance/sell/add/$', 'finance_sell_add',
        name='backoffice_finance_sell_add'),

    url(r'^finance/sell/(?P<sell_id>\d+)/edit/$', 'finance_sell_edit',
        name='backoffice_finance_sell_edit'),

    url(r'^finance/sell/(?P<sell_id>\d+)/delete/$', 'finance_sell_delete',
        name='backoffice_finance_sell_delete'),

    url(r'^finance/sell/(?P<sell_id>\d+)/item/add/$', 'finance_sell_item_add',
        name='backoffice_finance_sell_item_add'),

    url(r'^finance/sell/(?P<sell_id>\d+)/item/(?P<item_id>\d+)/edit/$',
        'finance_sell_item_edit', name='backoffice_finance_sell_item_edit'),

    url(r'^finance/sell/(?P<sell_id>\d+)/item/(?P<item_id>\d+)/delete/$',
        'finance_sell_item_delete',
        name='backoffice_finance_sell_item_delete'),

    url(r'^finance/sell/(?P<sell_id>\d+)/cost/add/$', 'finance_sell_cost_add',
        name='backoffice_finance_sell_cost_add'),

    url(r'^finance/sell/(?P<sell_id>\d+)/cost/(?P<cost_id>\d+)/edit/$',
        'finance_sell_cost_edit', name='backoffice_finance_sell_cost_edit'),

    url(r'^finance/sell/(?P<sell_id>\d+)/cost/(?P<cost_id>\d+)/delete/$',
        'finance_sell_cost_delete',
        name='backoffice_finance_sell_cost_delete'),
)
