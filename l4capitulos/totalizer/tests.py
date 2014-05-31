#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test units for totalizer application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from datetime import datetime
from decimal import Decimal

from django.core.management import call_command
from django.test import TestCase

from book.models import Author, Book, Status, Category
from finance.models import Sell, SellItem
from totalizer.models import SellByCategory


class SellByCategoryTestCase(TestCase):
    def setUp(self):
        self.c1 = Category.objects.create(name='comic')
        self.c2 = Category.objects.create(name='novel')

        Author.objects.create(first_name='Ariel', last_name='Rios')
        Author.objects.create(first_name='Leira', last_name='Soir')

        Status.objects.create(name='new')
        Status.objects.create(name='used')

        self.b1 = Book.objects.create(title='test title', category=self.c1)
        self.b2 = Book.objects.create(title='xyz123', category=self.c2)

        self._now = datetime.now()

        sell = Sell.objects.create(date=self._now)

        sell.sellitem_set.add(SellItem.objects.create(
            sell=sell, book=self.b1, quantity=1, price=Decimal('10.00')
        ))

        sell.sellitem_set.add(SellItem.objects.create(
            sell=sell, book=self.b2, quantity=2, price=Decimal('10.00')
        ))

    def tearDown(self):
        SellByCategory.objects.all().delete()
        SellItem.objects.all().delete()
        Sell.objects.all().delete()
        Book.objects.all().delete()
        Status.objects.all().delete()
        Author.objects.all().delete()
        Category.objects.all().delete()

    def test_totalize_sell_by_category(self):
        call_command('totalize_sell_by_category')
        self.assertEquals(2, SellByCategory.objects.all().count())

        for sbc in SellByCategory.objects.all():
            if sbc.category == self.c1:
                self.assertEquals(Decimal('10.00'), sbc.total)

            if sbc.category == self.c2:
                self.assertEquals(Decimal('20.00'), sbc.total)
