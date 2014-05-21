#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from .forms.books import BookForm, BookSearchForm, AuthorForm, AuthorSearchForm, CategoryForm, StatusForm, BookImageForm
from .forms.commons import DeleteForm
from .forms.finances import PurchaseForm, PurchaseSearchForm, ItemForm
from book.models import Author, Book, Category, Status, BookImage
from finance.models import Purchase, Item


def home(request):
    """
    The home page.
    """
    return render(request, 'backoffice/home.html', {
        'books': Book.objects.all(),
        'authors': Author.objects.all(),
        'purchases': Purchase.objects.all(),
        'section': 'home',
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
        'section': 'book_author',
    })


def book_author_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            messages.info(
                request, _("Author '%s' added :)") % author.get_full_name()
            )

            if 'save' in request.POST:
                return redirect('backoffice_book_author')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_author_edit',
                                author_id=author.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_author_add')
    else:
        form = AuthorForm()

    return render(request, 'backoffice/book_author_add.html', {
        'form': form,
        'section': 'book_author',
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
            messages.info(request, _('Author updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_book_author')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_author_edit',
                                author_id=author.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_author_add')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'backoffice/book_author_edit.html', {
        'form': form,
        'author': author,
        'books': books,
        'section': 'book_author',
    })


def book_author_delete(request, author_id):
    """
    TODO
    """
    author = get_object_or_404(Author, pk=author_id)

    if request.method == 'POST':
        author.delete()
        messages.warning(request, _('Author deleted.'))
        return redirect('backoffice_book_author')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': author,
        'model': author.__class__.__name__,
        'form': DeleteForm(),
        'section': 'book_author',
    })


def book_category(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_category.html', {
        'categories': Category.objects.all(),
        'section': 'book_category',
    })


def book_category_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            messages.info(
                request, _("Category '%s' added :)") % category.name
            )

            if 'save' in request.POST:
                return redirect('backoffice_book_category')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_category_edit',
                                category_id=category.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_category_add')
    else:
        form = CategoryForm()

    return render(request, 'backoffice/book_category_add.html', {
        'form': form,
        'section': 'book_category',
    })


def book_category_edit(request, category_id):
    """
    TODO
    """
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.info(request, _('Category updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_book_category')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_category_edit',
                                category_id=category.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_category_add')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'backoffice/book_category_edit.html', {
        'form': form,
        'category': category,
        'section': 'book_category',
    })


def book_category_delete(request, category_id):
    """
    TODO
    """
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        category.delete()
        messages.warning(request, _('Category deleted.'))
        return redirect('backoffice_book_category')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': category,
        'model': category.__class__.__name__,
        'form': DeleteForm(),
        'section': 'book_category',
    })


def book_status(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_status.html', {
        'statuses': Status.objects.all(),
        'section': 'book_status',
    })


def book_status_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            status = form.save()
            messages.info(request, _("Status '%s' added :)") % status.name)

            if 'save' in request.POST:
                return redirect('backoffice_book_status')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_status_edit',
                                status_id=status.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_status_add')
    else:
        form = StatusForm()

    return render(request, 'backoffice/book_status_add.html', {
        'form': form,
        'section': 'book_status',
    })


def book_status_edit(request, status_id):
    """
    TODO
    """
    status = get_object_or_404(Status, pk=status_id)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.info(request, _('Status updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_book_status')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_status_edit',
                                status_id=status.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_status_add')

    else:
        form = StatusForm(instance=status)

    return render(request, 'backoffice/book_status_edit.html', {
        'form': form,
        'status': status,
        'section': 'book_status',
    })


def book_status_delete(request, status_id):
    """
    TODO
    """
    status = get_object_or_404(Status, pk=status_id)

    if request.method == 'POST':
        status.delete()
        messages.warning(request, _('Status deleted.'))
        return redirect('backoffice_book_status')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': status,
        'model': status.__class__.__name__,
        'form': DeleteForm(),
        'section': 'book_status',
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
        'section': 'book_book',
    })


def book_book_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            messages.info(request, _("Book '%s' added :)") % book.title)

            if 'save' in request.POST:
                return redirect('backoffice_book_book')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_book_edit', book_id=book.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_book_add')

    else:
        form = BookForm()

    return render(request, 'backoffice/book_book_add.html', {
        'form': form,
        'section': 'book_book',
    })


def book_book_edit(request, book_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save()
            messages.info(request, _('Book updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_book_book')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_book_edit', book_id=book.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_book_add')

    else:
        form = BookForm(instance=book)

    return render(request, 'backoffice/book_book_edit.html', {
        'form': form,
        'book': book,
        'section': 'book_book',
    })


def book_book_delete(request, book_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        messages.warning(request, _('Book deleted.'))
        return redirect('backoffice_book_book')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': book,
        'model': book.__class__.__name__,
        'form': DeleteForm(),
        'section': 'book_book',
    })


def book_image_add(request, book_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)
    image = BookImage(book=book)

    if request.method == 'POST':
        form = BookImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image = form.save()
            messages.info(request, _("Image #%d added :)") % image.pk)

            if 'save' in request.POST:
                return redirect('backoffice_book_book_edit', book_id=book.pk)

            if 'save_and_edit' in request.POST:
                return redirect(
                    'backoffice_book_image_edit', book_id=book.pk,
                    image_id=image.pk
                )

            if 'save_and_new' in request.POST:
                return redirect('backoffice_book_image_add', book_id=book.pk)
    else:
        form = BookImageForm(instance=image)

    return render(request, 'backoffice/book_image_add.html', {
        'book': book,
        'form': form,
        'section': 'book_book',
    })


def book_image_edit(request, book_id, image_id):
    """
    TODO
    """
    pass


def book_image_delete(request, book_id, image_id):
    """
    TODO
    """
    pass


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
        'section': 'finance_purchase',
    })


def finance_purchase_add(request):
    """
    TODO
    """
    purchase = None

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save()
            messages.info(
                request, _("Purchase for '%s' added :)") % purchase.date
            )

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_add')

    else:
        form = PurchaseForm()

    return render(request, 'backoffice/finance_purchase_add.html', {
        'form': form,
        'purchase': purchase,
        'section': 'finance_purchase',
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
            messages.info(request, _('Purchase updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_add')

    else:
        form = PurchaseForm(instance=purchase)

    return render(request, 'backoffice/finance_purchase_edit.html', {
        'form': form,
        'purchase': purchase,
        'section': 'finance_purchase',
    })


def finance_purchase_delete(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)

    if request.method == 'POST':
        purchase.delete()
        messages.warning(request, _('Purchase deleted.'))
        return redirect('backoffice_finance_purchase')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': purchase,
        'model': purchase.__class__.__name__,
        'form': DeleteForm(),
        'section': 'finance_purchase',
    })


def finance_item_add(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    item = Item(purchase=purchase)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.info(request, _("Item %d added :)") % item.pk)

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_item_edit',
                                purchase_id=purchase_id, item_id=item.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_item_add',
                                purchase_id=purchase_id, item_id=item.pk)
    else:
        form = ItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_add.html', {
        'form': form,
        'purchase': purchase,
        'section': 'finance_purchase',
    })


def finance_item_edit(request, purchase_id, item_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, _('Item updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_item_edit',
                                purchase_id=purchase_id, item_id=item_id)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_item_add',
                                purchase_id=purchase_id, item_id=item_id)
    else:
        form = ItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_edit.html', {
        'form': form,
        'purchase': purchase,
        'item': item,
        'section': 'finance_purchase',
    })


def finance_item_delete(request, purchase_id, item_id):
    """
    TODO
    """
    get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(Item, pk=item_id)

    if request.method == 'POST':
        item.delete()
        messages.warning(request, _('Item deleted.'))
        return redirect('backoffice_finance_purchase', purchase_id=purchase_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': item,
        'model': item.__class__.__name__,
        'form': DeleteForm(),
        'section': 'finance_purchase',
    })
