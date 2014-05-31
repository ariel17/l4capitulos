#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Totalizer application to store purchase/sell statistics.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class SellByCategory(models.Model):
    """
    Totallizes book sells per day per category.
    """
    date = models.DateField(
        _('Date'),
        editable=False,
        auto_now=True,
    )

    category = models.ForeignKey(
        'book.Category',
        editable=False,
    )

    total = models.PositiveIntegerField(
        _('Total'),
        editable=False,
        default=0,
    )

    def __unicode__(self):
        return u"<SellByCategory date='%s' category=%s total=%d>" % (
            self.date, self.category.name, self.total
        )
