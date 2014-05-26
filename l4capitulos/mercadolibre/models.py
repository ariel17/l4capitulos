#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: MercadoLibre API models implementation.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from django.db import models
from django.utils.translation import ugettext as _


class Item(models.Model):
    """
    Item published on MercadoLibre.
    """
    id = models.CharField(
        _('MercadoLibre IID'),
        primary_key=True,
        max_length=20,
    )

    title = models.CharField(
        _('Title'),
        max_length=200,
    )

    subtitle = models.CharField(
        _('Subtitle'),
        max_length=200,
        blank=True,
        null=True
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
    )

    available_quantity = models.PositiveIntegerField(
        _('Available quantity')
    )

    condition = models.CharField(
        _('Condition'),
        max_length=20,
    )

    permalink = models.URLField(
        _('Permalink'),
    )

    thumbnail = models.URLField(
        _('Thumbnail URL'),
    )

    accepts_mercadopago = models.BooleanField(
        _('Accepts MercadoPago')
    )

    category_id = models.CharField(
        _('Category ID'),
        max_length=20,
    )

# vim: ai ts=4 sts=4 et sw=4 ft=python
