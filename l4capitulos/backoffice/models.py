#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice models declaration.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth import get_user_model


class Profile(models.Model):
    """
    Profile settings for each staff user.
    """
    user = models.OneToOneField(
        get_user_model()
    )

    last_activity_items = models.PositiveIntegerField(
        _('Last activity items'),
        default=settings.BACKOFFICE_PROFILE_DEFAULT_LAST_ACTIVITY_ITEMS,
        help_text=_('How many last activity items to show.')
    )
