#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definitions for finances management.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class PurchaseManager(models.Manager):
    """
    Custom manager for purchase operations.
    """
    def search(self, *args, **kwargs):
        """
        Searches purchases filtering by indicated parameters.
        """
        purchases = self.all()

        if 'date_from' in kwargs:
            pass  # TODO

        if 'date_to' in kwargs:
            pass  # TODO

        if 'price_from' in kwargs:
            pass  # TODO

        if 'price_to' in kwargs:
            pass  # TODO

        return purchases


class Purchase(models.Model):
    """
    Registers the item purchases.
    """

    date = models.DateField(
        _('Purchased at'),
        help_text=_('The pucharse operation date.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        help_text=_('The purchase price.')
    )

    objects = PurchaseManager()

    def __unicode__(self):
        return u"#%d@%s at $ %s" % (
            self.pk, self.date, self.price
        )

    def get_unit_price(self):
        """
        Returns the price by item invidually.
        """
        total_quantity = sum([i.quantity for i in self.item_set.all()])
        return self.price / total_quantity

    def get_total_units(self):
        """
        Counts the total units through all items.
        """
        return sum([i.quantity for i in self.purchaseitem_set.all()])


class PurchaseItem(models.Model):
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
        return u"PurchaseItem#%d@Purchase#%d: q=%d" % (
            self.pk, self.purchase.pk, self.quantity
        )


class PurchaseCost(models.Model):
    """
    An unit in a purchase.
    """
    purchase = models.ForeignKey(Purchase)

    date = models.DateField(
        _('Purchased at'),
        help_text=_('The cost operation date.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        help_text=_('The cost price.')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('The origin description for the cost.')
    )

    def __unicode__(self):
        return u"PurchaseCost#%d@Purchase#%d: p=%s" % (
            self.pk, self.purchase.pk, self.price
        )
