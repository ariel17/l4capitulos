#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definitions for finances management.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class Purchase(models.Model):
    """
    Registers the item purchases.
    """

    date = models.DateField(
        _('Purchased at'),
        auto_now=True,
        help_text=_('The pucharse operation date.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        help_text=_('The purchase price.')
    )

    def __unicode__(self):
        return u"#%d@%s: %d item(s) at $ %s" % (
            self.pk, self.date, self.total_items, self.price
        )

    def get_unit_price(self):
        """
        Returns the price by item invidually.
        """
        total_quantity = sum([i.quantity for i in self.item_set.all()])
        return self.price / total_quantity


class Item(models.Model):
    """
    An unit in a purchase.
    """
    purchase = models.ForeignKey(Purchase)

    book = models.ForeignKey("book.Book")

    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
        help_text=_('How many items came in the purchase.')
    )

    def __unicode__(self):
        return u"Item#%d@Purchase#%d: q=%d" % (
            self.pk, self.purchase.pk, self.quantity
        )
