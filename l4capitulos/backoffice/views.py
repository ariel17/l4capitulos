#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.shortcuts import render, get_object_or_404

from .forms.books import BookForm, BookSearchForm, AuthorForm, AuthorSearchForm, CategoryForm, StatusForm
from .forms.commons import DeleteForm
from .forms.finances import PurchaseForm, PurchaseSearchForm, ItemForm
from book.models import Author, Book, Category, Status
from finance.models import Purchase, Item


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
    saved = False

    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = AuthorForm()

    return render(request, 'backoffice/book_author_add.html', {
        'form': form,
        'saved': saved,
    })


def book_author_edit(request, author_id):
    """
    TODO
    """
    author = get_object_or_404(Author, pk=author_id)
    books = Book.objects.filter(authors__in=[author_id])
    saved = False

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = AuthorForm(instance=author)

    return render(request, 'backoffice/book_author_edit.html', {
        'form': form,
        'author': author,
        'books': books,
        'saved': saved,
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


def book_category(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_category.html', {
        'categories': Category.objects.all(),
    })


def book_category_add(request):
    """
    TODO
    """
    saved = False

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = CategoryForm()

    return render(request, 'backoffice/book_category_add.html', {
        'form': form,
        'saved': saved,
    })


def book_category_edit(request, category_id):
    """
    TODO
    """
    saved = False
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = CategoryForm(instance=category)

    return render(request, 'backoffice/book_category_edit.html', {
        'form': form,
        'category': category,
        'saved': saved,
    })


def book_category_delete(request, category_id):
    """
    TODO
    """
    category = get_object_or_404(Book, pk=category_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': category,
        'model': category.__class__.__name__,
        'form': DeleteForm(),
    })


def book_status(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_status.html', {
        'statuses': Status.objects.all(),
    })


def book_status_add(request):
    """
    TODO
    """
    saved = False

    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = StatusForm()

    return render(request, 'backoffice/book_status_add.html', {
        'form': form,
        'saved': saved,
    })


def book_status_edit(request, status_id):
    """
    TODO
    """
    saved = False
    status = get_object_or_404(Status, pk=status_id)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = StatusForm(instance=status)

    return render(request, 'backoffice/book_status_edit.html', {
        'form': form,
        'status': status,
        'saved': saved,
    })


def book_status_delete(request, status_id):
    """
    TODO
    """
    status = get_object_or_404(Book, pk=status_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': status,
        'model': status.__class__.__name__,
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
    saved = False

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = BookForm()

    return render(request, 'backoffice/book_book_add.html', {
        'form': form,
        'saved': saved,
    })


def book_book_edit(request, book_id):
    """
    TODO
    """
    saved = False
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = BookForm(instance=book)

    return render(request, 'backoffice/book_book_edit.html', {
        'form': form,
        'book': book,
        'saved': saved,
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
    saved = False
    purchase = None

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            saved = True
    else:
        form = PurchaseForm()

    return render(request, 'backoffice/finance_purchase_add.html', {
        'form': form,
        'saved': saved,
        'purchase': purchase,
    })


def finance_purchase_edit(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    saved = False

    if request.method == 'POST':
        form = PurchaseForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'backoffice/finance_purchase_edit.html', {
        'form': form,
        'saved': saved,
        'purchase': purchase,
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


def finance_item_add(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    saved = False
    item = Item(purchase=purchase)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            saved = True
        else:
            print form.errors
    else:
        form = ItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_add.html', {
        'form': form,
        'purchase': purchase,
        'saved': saved,
    })


def finance_item_edit(request, purchase_id, item_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(Item, pk=item_id)
    saved = False

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            saved = True
    else:
        form = ItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_edit.html', {
        'form': form,
        'purchase': purchase,
        'item': item,
        'saved': saved,
    })


def finance_item_delete(request, purchase_id, item_id):
    """
    TODO
    """
    get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(Item, pk=item_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': item,
        'model': item.__class__.__name__,
        'form': DeleteForm(),
    })
