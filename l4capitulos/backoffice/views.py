#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render, get_object_or_404

from .forms.books import BookForm, BookSearchForm, AuthorForm
from .forms.commons import DeleteForm
from .forms.finances import PurchaseForm, PurchaseSearchForm
from book.models import Author, Book
from finance.models import Purchase


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
        'form': None,
        'authors': Author.objects.all(),
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
    author = get_object_or_404(Author, pk=author_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': author,
        'model': author.__class__.__name__,
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
    book = get_object_or_404(Book, pk=book_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': book,
        'model': book.__class__.__name__,
        'form': DeleteForm(),
    })


def finance_purchase(request):
    """
    TODO
    """
    return render(request, 'backoffice/finance_purchase.html', {
        'form': PurchaseSearchForm(),
        'purchases': Purchase.objects.all(),
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
    purchase = get_object_or_404(Purchase, pk=purchase_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': purchase,
        'model': purchase.__class__.__name__,
        'form': DeleteForm(),
    })
