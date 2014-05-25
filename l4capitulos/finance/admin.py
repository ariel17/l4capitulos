#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for finance model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Purchase, PurchaseItem, PurchaseCost


class PurchaseAdmin(admin.ModelAdmin):
    fields = ('date', 'price',)
    list_display = ('date', 'price')


class PurchaseItemAdmin(admin.ModelAdmin):
    fields = ('purchase', 'book', 'quantity',)
    list_display = ('purchase', 'book', 'quantity',)
    list_display_links = ('purchase', 'book')


class PurchaseCostAdmin(admin.ModelAdmin):
    fields = ('purchase', 'date', 'price', 'description')
    list_display = ('purchase', 'date', 'price',)
    list_display_links = ('purchase',)


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)
admin.site.register(PurchaseCost, PurchaseCostAdmin)
