#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render

from .forms.commons import DeleteForm
from .forms.books import BookForm, BookSearchForm, AuthorForm
from .forms.finances import PurchaseForm
from book.models import Book


def home(request):
    """
    The home page.
    """
    return render(request, 'backoffice/home.html', {
        'books': Book.objects.all(),
    })


def book_author(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_author.html', {
    })


def book_author_add(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_author_add.html', {
        'form': AuthorForm(),
    })


def book_author_edit(request, author_id):
    """
    TODO
    """
    return render(request, 'backoffice/book_author_edit.html', {
        'form': AuthorForm(),
    })


def book_author_delete(request, author_id):
    """
    TODO
    """
    return render(request, 'backoffice/commons_delete.html', {
        'form': DeleteForm(),
    })


def book_book(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_book.html', {
        'form': BookSearchForm(),
        'books': Book.objects.all(),
    })


def book_book_add(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_book_add.html', {
        'form': BookForm(),
    })


def book_book_edit(request, book_id):
    """
    TODO
    """
    return render(request, 'backoffice/book_book_edit.html', {
        'form': BookForm(),
    })


def book_book_delete(request, book_id):
    """
    TODO
    """
    return render(request, 'backoffice/commons_delete.html', {
        'form': DeleteForm(),
    })


def finance_purchase(request):
    """
    TODO
    """
    return render(request, 'backoffice/finance_purchase.html', {
    })


def finance_purchase_add(request):
    """
    TODO
    """
    return render(request, 'backoffice/finance_purchase_add.html', {
        'form': PurchaseForm(),
    })


def finance_purchase_edit(request, purchase_id):
    """
    TODO
    """
    return render(request, 'backoffice/finance_purchase_edit.html', {
        'form': PurchaseForm(),
    })


def finance_purchase_delete(request, purchase_id):
    """
    TODO
    """
    return render(request, 'backoffice/commons_delete.html', {
        'form': DeleteForm(),
    })
