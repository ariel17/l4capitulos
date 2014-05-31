#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test units for backoffice application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import date

from django.test import TestCase

from .utils import generate_passed_dates


class UtilsTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_passed_dates(self):
        today = date(2014, 5, 2)
        days = 2

        days_list = generate_passed_dates(days, today=today)

        self.assertEquals(days, len(days_list))
        self.assertEquals('2014-05-01', days_list[0])
        self.assertEquals('2014-05-02', days_list[1])
