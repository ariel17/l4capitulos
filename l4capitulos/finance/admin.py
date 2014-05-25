#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for finance model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Purchase, PurchaseItem, PurchaseCost, Sell, SellItem, SellCost


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


class SellAdmin(admin.ModelAdmin):
    fields = ('date', 'price',)
    list_display = ('date', 'price')


class SellItemAdmin(admin.ModelAdmin):
    fields = ('sell', 'book', 'quantity',)
    list_display = ('sell', 'book', 'quantity',)
    list_display_links = ('sell', 'book')


class SellCostAdmin(admin.ModelAdmin):
    fields = ('sell', 'date', 'price', 'description')
    list_display = ('sell', 'date', 'price',)
    list_display_links = ('sell',)


admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(PurchaseItem, PurchaseItemAdmin)
admin.site.register(PurchaseCost, PurchaseCostAdmin)
admin.site.register(Sell, SellAdmin)
admin.site.register(SellItem, SellItemAdmin)
admin.site.register(SellCost, SellCostAdmin)
