#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Utillity module for backoffice application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from datetime import datetime, timedelta

from django.utils import formats


def generate_passed_dates(days, today=datetime.now()):
    """
    Returns a list of length=days with each element as string date formatted.
    """
    days_list = []

    for day in range(days):
        new_day = today - timedelta(days=day)
        days_list.append(formats.date_format(new_day, 'DATE_FORMAT'))

    days_list.sort()
    return days_list
