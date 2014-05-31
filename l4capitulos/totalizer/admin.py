#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for totalizer model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import SellByCategory


class SellByCategoryAdmin(admin.ModelAdmin):
    fields = ('date', 'category', 'total')
    list_display = ('date', 'category', 'total')
    list_display_links = ('category',)


admin.site.register(SellByCategory, SellByCategoryAdmin)
