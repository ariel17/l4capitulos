#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Views implementation for MercadoLibre integration.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


import logging
import uuid

from django.shortcuts import render


logger = logging.getLogger(__name__)


def callback(request):
    """
    Receives a callback request from MercadoLibre API.
    """
    _uuid = uuid.uuid4()

    logger.info(
        '[%s] >> MercadoLibre callback received. GET=%r, POST=%r', _uuid,
        request.GET, request.POST
    )
    pass
