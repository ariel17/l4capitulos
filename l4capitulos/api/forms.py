#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Forms for API application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _


class FacebookBookPostForm(forms.Form):
    """
    Validates the book information to post.
    """
    description = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Description")}),
        required=True,
    )

# vim: ai ts=4 sts=4 et sw=4 ft=python
