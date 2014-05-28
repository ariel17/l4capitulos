#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definitions for finances management.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from common.models import FileModel


class OperationManager(models.Manager):
    """
    Custom manager for operations.
    """
    def search(self, *args, **kwargs):
        """
        Searches purchases filtering by indicated parameters.
        """
        operations = self.all()

        if 'date_from' in kwargs:
            pass  # TODO

        if 'date_to' in kwargs:
            pass  # TODO

        if 'price_from' in kwargs:
            pass  # TODO

        if 'price_to' in kwargs:
            pass  # TODO

        return operations


class Operation(models.Model):
    """
    An abstract in/out operation.
    """
    date = models.DateField(
        _('Operation at'),
        help_text=_('The operation date.')
    )

    title = models.CharField(
        _('Title'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_('The title or short description for this operation.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        default=0,
        help_text=_('The operation price.')
    )

    objects = OperationManager()

    class Meta:
        ordering = ['date', 'title']
        abstract = True


class Item(models.Model):
    """
    An unit inside an operation.
    """
    book = models.ForeignKey("book.Book")

    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
        help_text=_('How many items came in the operation.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text=_('The item price.')
    )

    class Meta:
        abstract = True


class Cost(models.Model):
    """
    Registers a cost in an operation.
    """
    date = models.DateField(
        _('Created at'),
        help_text=_('The cost operation date.')
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        help_text=_('The cost price.')
    )

    title = models.CharField(
        _('Title'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_('The title or short description for this cost.')
    )

    description = models.TextField(
        blank=True,
        null=True,
        help_text=_('The origin description for the cost.')
    )

    class Meta:
        abstract = True


class Purchase(Operation):
    """
    Registers the a bulk book purchase.
    """
    invoice = models.FileField(
        _('Invoice'),
        upload_to=FileModel.normalize_filename(settings.FINANCE_INVOICE_PATH),
        blank=True,
        null=True,
        help_text=_('The associated invoice to this purchase.')
    )

    def __unicode__(self):
        return u"Purchase#%d@%s at $ %s" % (
            self.pk, self.date, self.price
        )

    def get_total_price(self):
        """
        Returns the total price of all items.
        """
        if self.price:
            return self.price
        return sum([i.quantity * i.price for i in self.purchaseitem_set.all()])

    def get_total_units(self):
        """
        Counts the total units through all items.
        """
        return sum([i.quantity for i in self.purchaseitem_set.all()])

    def get_total_cost(self):
        """
        Returns the summatory of all costs on this purchase.
        """
        return sum([c.price for c in self.purchasecost_set.all()])

    def get_full_price(self):
        """
        Returns the summatory of purchase price with all costs.
        """
        return self.price + self.get_total_cost()


class PurchaseItem(Item):
    """
    An unit in a purchase.
    """
    purchase = models.ForeignKey(Purchase)

    def __unicode__(self):
        return u"PurchaseItem#%d@Purchase#%d: q=%d" % (
            self.pk, self.purchase.pk, self.quantity
        )


class PurchaseCost(Cost):
    """
    Registers a cost entry for a purchase.
    """
    purchase = models.ForeignKey(Purchase)

    def __unicode__(self):
        return u"PurchaseCost#%d@Purchase#%d: p=%s" % (
            self.pk, self.purchase.pk, self.price
        )


class Sell(Operation):
    """
    Registers the sell item.
    """
    def __unicode__(self):
        return u"Sell#%d@%s at $ %s" % (
            self.pk, self.date, self.price
        )

    def get_total_price(self):
        if self.price:
            return self.price
        return sum([i.quantity * i.price for i in self.sellitem_set.all()])

    def get_total_units(self):
        """
        Counts the total units through all items.
        """
        return sum([i.quantity for i in self.sellitem_set.all()])

    def get_total_cost(self):
        """
        Returns the summatory of all costs on this sell.
        """
        return sum([c.price for c in self.sellcost_set.all()])

    def get_net_price(self):
        """
        Returns the sell price minus the summatory of all costs.
        """
        return self.price - self.get_total_cost()


class SellItem(Item):
    """
    An item inside a sell.
    """
    sell = models.ForeignKey(Sell)

    def __unicode__(self):
        return u"SellItem#%d@Sell#%d: q=%d" % (
            self.pk, self.sell.pk, self.quantity
        )


class SellCost(Cost):
    """
    A cost entry for a sell.
    """
    sell = models.ForeignKey(Sell)

    def __unicode__(self):
        return u"SellCost#%d@Sell#%d: p=%s" % (
            self.pk, self.sell.pk, self.price
        )
