#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf.urls import patterns, url


urlpatterns = patterns('mercadolibre.views',

    url(r'^callback/$', 'callback', name='mercadolibre_callback'),
)
