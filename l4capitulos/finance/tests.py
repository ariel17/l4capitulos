#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for finance models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import datetime
from decimal import Decimal

from django.test import TestCase

from .models import Purchase, Item
from book.models import Book


class PurchaseTestCase(TestCase):
    def setUp(self):
        self._purchase = Purchase.objects.create(
            date=datetime.now().date(),
            price=Decimal('10.00'),
        )

        book = Book.objects.create(
            title='test title',
        )

        for i in range(10):
            Item.objects.create(
                purchase=self._purchase,
                book=book,
                quantity=1
            )

    def test_get_unit_price(self):
        self.assertEquals(Decimal('1.00'), self._purchase.get_unit_price())
