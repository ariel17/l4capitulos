#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for book model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Book description'), {
            'fields': ('title', 'authors')
        }),
        (_('Sell options'), {
            'fields': ('quantity', 'price')
        }),
    )
    list_display = ('title', 'quantity', 'price')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)