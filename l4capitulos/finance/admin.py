#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for finance model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Purchase, Item


class PurchaseAdmin(admin.ModelAdmin):
    fields = ('date', 'price',)
    list_display = ('date', 'price')


admin.site.register(Purchase, PurchaseAdmin)
