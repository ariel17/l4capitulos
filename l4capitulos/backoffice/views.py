#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render

from book.models import Book
from .forms.books import BookForm
from .forms.finances import PurchaseForm


def home(request):
    """
    The home page.
    """
    return render(request, 'backoffice/home.html', {
        'books': Book.objects.all(),
    })


def book(request):
    """
    TODO
    """
    pass


def book_add(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_add.html', {
        'form': BookForm(),
    })


def book_edit(request, book_id):
    """
    TODO
    """
    return render(request, 'backoffice/book_edit.html', {
        'form': BookForm(),
    })


def book_delete(request, book_id):
    """
    TODO
    """
    pass


def purchase(request):
    """
    TODO
    """
    pass


def purchase_add(request):
    """
    TODO
    """
    return render(request, 'backoffice/purchase_add.html', {
        'form': PurchaseForm(),
    })


def purchase_edit(request, purchase_id):
    """
    TODO
    """
    return render(request, 'backoffice/purchase_edit.html', {
        'form': PurchaseForm(),
    })


def purchase_delete(request, purchase_id):
    """
    TODO
    """
    pass
