#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Totalizes sells by category for indicated days, if indicated.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

import logging
from datetime import datetime, timedelta
import uuid

from django.core.management.base import BaseCommand, CommandError
from django.utils import formats

from finance.models import Sell
from totalizer.models import SellByCategory


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Totalizes sells for indicated days, grouped by category.'

    def handle(self, *args, **options):

        _uuid = uuid.uuid4()
        today = datetime.now()
        yesterday = today - timedelta(days=1)

        logger.info(
            '[%s] >> Initializing totalizer: %s <= range < %s' %
            (_uuid, formats.date_format(yesterday, 'DATE_FORMAT'),
             formats.date_format(today, 'DATE_FORMAT'))
        )

        totals = {}

        for sell in Sell.objects.filter(date__gte=yesterday, date__lte=today):
            date = sell.date
            totals.setdefault(date, {})

            for item in sell.sellitem_set.all():
                category = item.book.category
                totals[date].setdefault(category, 0)
                totals[date][category] += item.price * item.quantity

        total_rows = 0
        for date in totals:
            for category in totals[date]:
                logger.debug(
                    'Adding totalized row: date=%s, category=%s, total=%d' %
                    (formats.date_format(today, 'DATE_FORMAT'), category,
                     totals[date][category])
                )

                SellByCategory.objects.create(
                    date=date, category=category, total=totals[date][category]
                )
                total_rows += 1

        logger.info('[%s] >> Totalizer finished: %d rows processed' %
                    (_uuid, total_rows))
