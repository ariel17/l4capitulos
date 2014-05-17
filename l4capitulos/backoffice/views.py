#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render, get_object_or_404

from .forms.books import BookForm, BookSearchForm, AuthorForm, AuthorSearchForm
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
        'authors': Author.objects.all(),
        'purchases': Purchase.objects.all(),
    })


def book_author(request):
    """
    TODO
    """
    form = AuthorSearchForm(request.GET)

    if len(request.GET.keys()):
        if form.is_valid():
            authors = Author.objects.search(**form.cleaned_data)
        else:
            authors = []
    else:
        authors = []

    return render(request, 'backoffice/book_author.html', {
        'form': form,
        'authors': authors,
    })


def book_author_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm()

    return render(request, 'backoffice/book_author_add.html', {
        'form': form,
    })


def book_author_edit(request, author_id):
    """
    TODO
    """
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(authors__in=[author_id])

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
    else:
        form = AuthorForm(instance=author)

    return render(request, 'backoffice/book_author_edit.html', {
        'form': form,
        'author': author,
        'books': books,
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
    form = BookSearchForm(request.GET)

    if len(request.GET.keys()):
        if form.is_valid():
            books = Book.objects.search(**form.cleaned_data)
        else:
            books = []
    else:
        books = []

    return render(request, 'backoffice/book_book.html', {
        'form': form,
        'books': books,
    })


def book_book_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'backoffice/book_book_add.html', {
        'form': form,
    })


def book_book_edit(request, book_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
    else:
        form = BookForm(instance=book)

    return render(request, 'backoffice/book_book_edit.html', {
        'form': form,
        'book': book,
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
    form = PurchaseSearchForm(request.GET)

    if len(request.GET.keys()):
        if form.is_valid():
            purchases = Purchase.objects.search(**form.cleaned_data)
        else:
            purchases = []
    else:
        purchases = []

    return render(request, 'backoffice/finance_purchase.html', {
        'form': form,
        'purchases': purchases,
    })


def finance_purchase_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PurchaseForm()

    return render(request, 'backoffice/finance_purchase_add.html', {
        'form': form,
    })


def finance_purchase_edit(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'backoffice/finance_purchase_edit.html', {
        'form': form,
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
