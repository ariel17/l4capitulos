#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definitions about books and related data.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.db import models
from django.utils.translation import ugettext as _


class Author(models.Model):
    """
    A person that writes books.
    """
    first_name = models.CharField(
        _('First name'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("The author's first name.")
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=200,
        help_text=_("The author's last name.")
    )

    def __unicode__(self):
        return unicode(self.get_full_name())

    def get_full_name(self):
        """
        Returns the first name and last name combination.
        """
        full_name = u"%s %s" % (self.first_name, self.last_name)
        full_name.strip()
        return full_name


class Book(models.Model):
    """
    The book itself.
    """
    title = models.CharField(
        _('Title'),
        max_length=200,
        help_text=_("The book's title.")
    )

    authors = models.ManyToManyField(Author)

    summary = models.TextField(
        _('Summary'),
        blank=True,
        null=True,
        help_text=_('Book summary about its content and why should buy it.')
    )

    created_at = models.DateTimeField(
        _('Added at'),
        auto_now=True
    )

    price = models.DecimalField(
        _('Price'),
        max_digits=10,
        decimal_places=2,
        default=0,
        help_text=_('The book sell price.'),
    )

    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
        help_text=_('How many copies of this book we have.')
    )

    def __unicode__(self):
        return unicode(self.title)
