#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for book model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin

from .models import Author, Book, Category, Status


class AuthorAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name')
    list_display = ('first_name', 'last_name')


class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'authors', 'isbn', 'published_at', 'editorial',
              'summary',)
    list_display = ('title', 'isbn', 'editorial', 'added_at')
    list_display_links = ('title', 'editorial')


class CategoryAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )


class StatusAdmin(admin.ModelAdmin):
    fields = ('name', )
    list_display = ('name', )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)

# vim: ai ts=4 sts=4 et sw=4 ft=python
