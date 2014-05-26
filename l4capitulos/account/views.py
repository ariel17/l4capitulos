#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: TODO
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib.auth import login
from django.shortcuts import render, redirect

from forms import LoginForm


def account_login(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('backoffice_home')

    else:
        form = LoginForm()

    return render(request, 'account/login.html', {
        'form': form,
    })


def account_logout(request):
    """
    TODO
    """
    pass
