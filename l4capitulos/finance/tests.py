#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test cases for finance models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import datetime
from decimal import Decimal

from django.test import TestCase

from .models import Purchase, PurchaseItem, PurchaseCost, Sell, SellItem, SellCost
from book.models import Book


class PurchaseTestCase(TestCase):
    def setUp(self):
        self._purchase = Purchase.objects.create(
            date=datetime.now().date(),
            price=Decimal('100.00'),
        )

        book = Book.objects.create(
            title='test title',
        )

        for i in range(10):
            PurchaseItem.objects.create(
                purchase=self._purchase,
                book=book,
                quantity=1
            )

            PurchaseCost.objects.create(
                purchase=self._purchase,
                date=datetime.now(),
                price=Decimal('1.00'),
            )

    def test_get_total_units(self):
        self.assertEquals(10, self._purchase.get_total_units())

    def test_get_unit_price(self):
        self.assertEquals(Decimal('10.00'), self._purchase.get_unit_price())

    def test_get_total_cost(self):
        self.assertEquals(Decimal('10.00'), self._purchase.get_total_cost())

    def test_get_full_price(self):
        self.assertEquals(Decimal('110.00'), self._purchase.get_full_price())


class SellTestCase(TestCase):
    def setUp(self):
        self._sell = Sell.objects.create(
            date=datetime.now().date(),
            price=Decimal('100.00'),
        )

        book = Book.objects.create(
            title='test title',
        )

        for i in range(10):
            SellItem.objects.create(
                sell=self._sell,
                book=book,
                quantity=1
            )

            SellCost.objects.create(
                sell=self._sell,
                date=datetime.now(),
                price=Decimal('1.00'),
            )

    def test_get_total_units(self):
        self.assertEquals(10, self._sell.get_total_units())

    def test_get_total_cost(self):
        self.assertEquals(Decimal('10.00'), self._sell.get_total_cost())

    def test_get_net_price(self):
        self.assertEquals(Decimal('90.00'), self._sell.get_net_price())
