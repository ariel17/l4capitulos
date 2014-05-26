#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Admin registration for mercadolibre model definitions.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    def view_permalink(obj):
        return u"<a href='%s'>%s</a>" % (obj.permalink, obj.permalink)

    view_permalink.short_description = _('Permalink')
    view_permalink.allow_tags = True

    fields = (
        'id', 'title', 'subtitle', 'price', 'available_quantity', 'condition',
        'permalink', 'thumbnail', 'accepts_mercadopago', 'category_id',
    )
    list_display = ('id', 'title', 'price', 'available_quantity', view_permalink)



admin.site.register(Item, ItemAdmin)


# vim: ai ts=4 sts=4 et sw=4 ft=python
