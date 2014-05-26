#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from decimal import Decimal
import json
import logging
import uuid

import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from mercadolibre.models import Item


logger = logging.getLogger(__name__)

MERCADOLIBRE_API_URL = 'https://api.mercadolibre.com/sites/MLA/search'\
                       '?seller_id=%s' % settings.MERCADOLIBRE_SELLER_ID

class Command(BaseCommand):
    args = '<item-id-1 item-id-2 ...>'
    help = ''  # TODO

    def handle(self, *args, **options):
        _uuid = uuid.uuid4()

        logger.info(">> Syncing published items on MercadoLibre")

        response = requests.get(MERCADOLIBRE_API_URL)

        if response.status_code != 200:
            raise CommandError("Bad status code from MercadoLibre API")

        json_items = json.loads(response.content)

        logger.info("%d items to sync.", len(json_items['results']))

        for json_item in json_items['results']:
            item, created = Item.objects.get_or_create(
                id=json_item['id'], defaults={
                    'title': json_item['title'],
                    'subtitle': json_item['subtitle'],
                    'price': Decimal(json_item['price']),
                    'available_quantity': int(json_item['available_quantity']),
                    'condition': json_item['condition'],
                    'permalink': json_item['permalink'],
                    'thumbnail': json_item['thumbnail'],
                    'accepts_mercadopago': json_item['accepts_mercadopago'] == 'true',
                    'category_id': json_item['category_id'],
                }
            )
            logger.debug("Item=%r, created=%r", item, created)

# vim: ai ts=4 sts=4 et sw=4 ft=python
