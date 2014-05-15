#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render


def backoffice_home(request):
    """
    The home page.
    """
    return render(request, 'backoffice/backoffice.html', {})
