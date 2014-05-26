#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url


urlpatterns = patterns('',

    url(r'^login/$', 'account.views.account_login',
        name='account_login'),

    url(r'^logout/$', 'account.views.account_logout',
        name='account_logout'),
)
