#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Backoffice application views.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

from datetime import datetime
import logging

from facepy import GraphAPI

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import ugettext as _

from social.apps.django_app.default.models import UserSocialAuth

from .forms.books import BookForm, BookSearchForm, AuthorForm, AuthorSearchForm, CategoryForm, StatusForm, BookImageForm, EditorialForm, EditorialSearchForm, FacebookBookPostForm
from .forms.commons import DeleteForm
from .forms.finances import PurchaseForm, PurchaseSearchForm, PurchaseItemForm, PurchaseCostForm, SellForm, SellSearchForm, SellItemForm, SellCostForm
from .utils import generate_passed_dates
from book.models import Author, Book, Category, Status, BookImage, Editorial
from finance.models import Purchase, PurchaseItem, PurchaseCost, Sell, SellItem, SellCost


logger = logging.getLogger(__name__)


@login_required
def home(request):
    """
    The home page.
    """
    days = generate_passed_dates(
        days=settings.BACKOFFICE_DEFAULT_CHART_SELL_DAYS, today=datetime.now()
    )

    sell_prices = [
        sell.get_total_price()
        for sell in Sell.objects.filter(date__gte=days[0], date__lte=days[-1])
    ]

    sell_costs = [
        sell.get_total_cost()
        for sell in Sell.objects.filter(date__gte=days[0], date__lte=days[-1])
    ]

    books = Book.objects.all()
    purchases = Purchase.objects.all()
    sells = Sell.objects.all()

    return render(request, 'backoffice/home.html', {
        'books': books,

        'recent_books':
        books.order_by('-added_at')[:settings.BACKOFFICE_DEFAULT_RECENT_ITEMS],

        'recent_sells':
        sells.order_by('-date')[:settings.BACKOFFICE_DEFAULT_RECENT_ITEMS],

        'recent_purchases':
        purchases.order_by('-date')[:settings.BACKOFFICE_DEFAULT_RECENT_ITEMS],

        'authors': Author.objects.all(),
        'purchases': {
            'objects': purchases,
            'total': purchases.count(),
            'total_items': sum([
                item.quantity for purchase in purchases
                for item in purchase.purchaseitem_set.all()
            ]),
        },
        'sells': {
            'objects': sells,
            'total': sells.count(),
            'total_items': sum([
                item.quantity for sell in sells
                for item in sell.sellitem_set.all()
            ])
        },
        'chart': {
            'days': {
                'value': settings.BACKOFFICE_DEFAULT_CHART_SELL_DAYS,
                'list': ["'%s'" % day for day in days],
            },
            'sells': {
                'values': sell_prices,
                'total': '%.2f' % sum(sell_prices),
            },
            'purchases': {
                'values': sell_costs,
                'total': '%.2f' % sum(sell_costs),
            },
            'diff': {
                'values': [
                    a - b for (a, b) in zip(sell_prices, sell_costs)
                ],
            },
        },
        'section': 'home',
    })


@login_required
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


@login_required
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


@login_required
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
            messages.info(
                request, _("Author '%s' updated :)") % author.get_full_name()
            )

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


@login_required
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
        'model': _('Author'),
        'form': DeleteForm(),
        'section': 'book_author',
    })


@login_required
def book_category(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_category.html', {
        'categories': Category.objects.all(),
        'section': 'book_category',
    })


@login_required
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


@login_required
def book_category_edit(request, category_id):
    """
    TODO
    """
    category = get_object_or_404(Category, pk=category_id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save()
            messages.info(
                request, _("Category '%s' updated :)") % category.name
            )

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


@login_required
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
        'model': _('Category'),
        'form': DeleteForm(),
        'section': 'book_category',
    })


@login_required
def book_editorial(request):
    """
    TODO
    """
    form = EditorialSearchForm(request.GET)

    if len(request.GET.keys()):
        if form.is_valid():
            editorials = Editorial.objects.search(**form.cleaned_data)
        else:
            editorials = []
    else:
        editorials = []

    return render(request, 'backoffice/book_editorial.html', {
        'form': form,
        'editorials': editorials,
        'section': 'book_editorial',
    })


@login_required
def book_editorial_add(request):
    """
    TODO
    """
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            editorial = form.save()
            messages.info(
                request, _("Editorial '%s' added :)") % editorial.name
            )

            if 'save' in request.POST:
                return redirect('backoffice_book_editorial')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_editorial_edit',
                                editorial_id=editorial.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_editorial_add')
    else:
        form = EditorialForm()

    return render(request, 'backoffice/book_editorial_add.html', {
        'form': form,
        'section': 'book_editorial',
    })


@login_required
def book_editorial_edit(request, editorial_id):
    """
    TODO
    """
    editorial = get_object_or_404(Editorial, pk=editorial_id)

    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            editorial = form.save()
            messages.info(
                request, _("Editorial '%s' updated :)") % editorial.name
            )

            if 'save' in request.POST:
                return redirect('backoffice_book_editorial')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_book_editorial_edit',
                                editorial_id=editorial.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_book_editorial_add')
    else:
        form = EditorialForm(instance=editorial)

    return render(request, 'backoffice/book_editorial_edit.html', {
        'form': form,
        'editorial': editorial,
        'section': 'book_editorial',
    })


@login_required
def book_editorial_delete(request, editorial_id):
    """
    TODO
    """
    editorial = get_object_or_404(Editorial, pk=editorial_id)

    if request.method == 'POST':
        editorial.delete()
        messages.warning(request, _('Editorial deleted.'))
        return redirect('backoffice_book_editorial')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': editorial,
        'model': _('Editorial'),
        'form': DeleteForm(),
        'section': 'book_editorial',
    })


@login_required
def book_status(request):
    """
    TODO
    """
    return render(request, 'backoffice/book_status.html', {
        'statuses': Status.objects.all(),
        'section': 'book_status',
    })


@login_required
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


@login_required
def book_status_edit(request, status_id):
    """
    TODO
    """
    status = get_object_or_404(Status, pk=status_id)

    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.info(
                request, _("Status '%s' updated :)") % status.name
            )

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


@login_required
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
        'model': _('Status'),
        'form': DeleteForm(),
        'section': 'book_status',
    })


@login_required
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


@login_required
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


@login_required
def book_book_edit(request, book_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        if request.GET.get('action', '') == 'facebook_post':
            logger.debug('Processing Facebook post')

            form = BookForm(instance=book)
            facebook_form = FacebookBookPostForm(
                request.user, book, request.POST
            )

            if facebook_form.is_valid():
                logger.debug('Facebook form is ok')

                try:
                    facebook_form.save()
                except UserSocialAuth.DoesNotExist, e:
                    messages.error(
                        request,
                        _("You must be logged into Facebook to be able to "
                          "publish :(")
                    )

                messages.info(
                    request, _("Book '%s' published on Facebook :)") %
                    book.title
                )
            else:
                logger.debug('Facebook form has errors')

        else:
            form = BookForm(request.POST, instance=book)
            facebook_form = FacebookBookPostForm(request.user, book)

            if form.is_valid():
                book = form.save()

                messages.info(
                    request, _("Book '%s' updated :)") % book.title
                )

                if 'save' in request.POST:
                    return redirect('backoffice_book_book')

                if 'save_and_edit' in request.POST:
                    return redirect(
                        'backoffice_book_book_edit', book_id=book.pk
                    )

                elif 'save_and_new' in request.POST:
                    return redirect('backoffice_book_book_add')

    else:
        form = BookForm(instance=book)
        facebook_form = FacebookBookPostForm(request.user, book)

    return render(request, 'backoffice/book_book_edit.html', {
        'form': form,
        'facebook': {
            'form': facebook_form,
            'authenticated':
            request.user.social_auth.filter(provider='facebook').count() > 0
        },
        'book': book,
        'section': 'book_book',
    })


@login_required
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
        'model': _('Book'),
        'form': DeleteForm(),
        'section': 'book_book',
    })


@login_required
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


@login_required
def book_image_edit(request, book_id, image_id):
    """
    TODO
    """
    book = get_object_or_404(Book, pk=book_id)
    image = get_object_or_404(BookImage, pk=image_id)

    if request.method == 'POST':
        form = BookImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image = form.save()
            messages.info(request, _("Image #%d updated :)") % image.pk)

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

    return render(request, 'backoffice/book_image_edit.html', {
        'book': book,
        'form': form,
        'section': 'book_book',
    })


@login_required
def book_image_delete(request, book_id, image_id):
    """
    TODO
    """
    get_object_or_404(Book, pk=book_id)
    image = get_object_or_404(BookImage, pk=image_id)

    if request.method == 'POST':
        image.delete()
        messages.warning(request, _('Image deleted.'))
        return redirect('backoffice_book_book_edit', book_id=book_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': image,
        'model': _('Book image'),
        'form': DeleteForm(),
        'section': 'book_book',
    })


@login_required
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


@login_required
def finance_purchase_add(request):
    """
    TODO
    """
    purchase = None

    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
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


@login_required
def finance_purchase_edit(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)

    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES, instance=purchase)
        if form.is_valid():
            form.save()
            messages.info(
                request, _("Purchase for '%s' updated :)") % purchase.date
            )

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


@login_required
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
        'model': _('Purchase'),
        'form': DeleteForm(),
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_item_add(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    item = PurchaseItem(purchase=purchase)

    if request.method == 'POST':
        form = PurchaseItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.info(request, _("Purchase item %d added :)") % item.pk)

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_item_edit',
                                purchase_id=purchase_id, item_id=item.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_item_add',
                                purchase_id=purchase_id)
    else:
        form = PurchaseItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_add.html', {
        'form': form,
        'purchase': purchase,
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_item_edit(request, purchase_id, item_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(PurchaseItem, pk=item_id)

    if request.method == 'POST':
        form = PurchaseItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, _('Purchase item updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_item_edit',
                                purchase_id=purchase_id, item_id=item_id)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_item_add',
                                purchase_id=purchase_id, item_id=item_id)
    else:
        form = PurchaseItemForm(instance=item)

    return render(request, 'backoffice/finance_purchase_item_edit.html', {
        'form': form,
        'purchase': purchase,
        'item': item,
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_item_delete(request, purchase_id, item_id):
    """
    TODO
    """
    get_object_or_404(Purchase, pk=purchase_id)
    item = get_object_or_404(PurchaseItem, pk=item_id)

    if request.method == 'POST':
        item.delete()
        messages.warning(request, _('Purchase item deleted.'))
        return redirect('backoffice_finance_purchase_edit', purchase_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': item,
        'model': _('Purchase item'),
        'form': DeleteForm(),
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_cost_add(request, purchase_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    cost = PurchaseCost(purchase=purchase)

    if request.method == 'POST':
        form = PurchaseCostForm(request.POST, instance=cost)
        if form.is_valid():
            cost = form.save()
            messages.info(request, _("Purchase cost %d added :)") % cost.pk)

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_cost_edit',
                                purchase_id=purchase_id, cost_id=cost.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_cost_add',
                                purchase_id=purchase_id, cost_id=cost.pk)
    else:
        form = PurchaseCostForm(instance=cost)

    return render(request, 'backoffice/finance_purchase_cost_add.html', {
        'form': form,
        'purchase': purchase,
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_cost_edit(request, purchase_id, cost_id):
    """
    TODO
    """
    purchase = get_object_or_404(Purchase, pk=purchase_id)
    cost = get_object_or_404(PurchaseCost, pk=cost_id)

    if request.method == 'POST':
        form = PurchaseCostForm(request.POST, instance=cost)
        if form.is_valid():
            form.save()
            messages.info(request, _('Purchase cost updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_purchase_edit',
                                purchase_id=purchase_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_purchase_cost_edit',
                                purchase_id=purchase_id, cost_id=cost_id)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_purchase_cost_add',
                                purchase_id=purchase_id, cost_id=cost_id)
    else:
        form = PurchaseCostForm(instance=cost)

    return render(request, 'backoffice/finance_purchase_cost_edit.html', {
        'form': form,
        'purchase': purchase,
        'cost': cost,
        'section': 'finance_purchase',
    })


@login_required
def finance_purchase_cost_delete(request, purchase_id, cost_id):
    """
    TODO
    """
    get_object_or_404(Purchase, pk=purchase_id)
    cost = get_object_or_404(PurchaseCost, pk=cost_id)

    if request.method == 'POST':
        cost.delete()
        messages.warning(request, _('Purchase cost deleted.'))
        return redirect('backoffice_finance_purchase_edit', purchase_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': cost,
        'model': _('Purchase cost'),
        'form': DeleteForm(),
        'section': 'finance_purchase',
    })


@login_required
def finance_sell(request):
    """
    TODO
    """
    form = SellSearchForm(request.GET)

    if len(request.GET.keys()):
        if form.is_valid():
            sells = Sell.objects.search(**form.cleaned_data)
        else:
            sells = []
    else:
        sells = []

    return render(request, 'backoffice/finance_sell.html', {
        'form': form,
        'sells': sells,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_add(request):
    """
    TODO
    """
    sell = None

    if request.method == 'POST':
        form = SellForm(request.POST)
        if form.is_valid():
            sell = form.save()
            messages.info(
                request, _("Sell for '%s' added :)") % sell.date
            )

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_add')

    else:
        form = SellForm()

    return render(request, 'backoffice/finance_sell_add.html', {
        'form': form,
        'sell': sell,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_edit(request, sell_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)

    if request.method == 'POST':
        form = SellForm(request.POST, instance=sell)
        if form.is_valid():
            form.save()
            messages.info(
                request, _("Sell for '%s' updated :)") % sell.date
            )

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell')

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_add')

    else:
        form = SellForm(instance=sell)

    return render(request, 'backoffice/finance_sell_edit.html', {
        'form': form,
        'sell': sell,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_delete(request, sell_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)

    if request.method == 'POST':
        sell.delete()
        messages.warning(request, _('Sell deleted.'))
        return redirect('backoffice_finance_sell')

    return render(request, 'backoffice/commons_delete.html', {
        'obj': sell,
        'model': _('Sell'),
        'form': DeleteForm(),
        'section': 'finance_sell',
    })


@login_required
def finance_sell_item_add(request, sell_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    item = SellItem(sell=sell)

    if request.method == 'POST':
        form = SellItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            messages.info(request, _("Sell item %d added :)") % item.pk)

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_item_edit',
                                sell_id=sell_id, item_id=item.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_item_add',
                                sell_id=sell_id, item_id=item.pk)
    else:
        form = SellItemForm(instance=item)

    return render(request, 'backoffice/finance_sell_item_add.html', {
        'form': form,
        'sell': sell,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_item_edit(request, sell_id, item_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    item = get_object_or_404(SellItem, pk=item_id)

    if request.method == 'POST':
        form = SellItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, _('Sell item updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_item_edit',
                                sell_id=sell_id, item_id=item_id)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_item_add',
                                sell_id=sell_id, item_id=item_id)
    else:
        form = SellItemForm(instance=item)

    return render(request, 'backoffice/finance_sell_item_edit.html', {
        'form': form,
        'sell': sell,
        'item': item,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_item_delete(request, sell_id, item_id):
    """
    TODO
    """
    get_object_or_404(Sell, pk=sell_id)
    item = get_object_or_404(SellItem, pk=item_id)

    if request.method == 'POST':
        item.delete()
        messages.warning(request, _('Sell item deleted.'))
        return redirect('backoffice_finance_sell_edit', sell_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': item,
        'model': _('Sell item'),
        'form': DeleteForm(),
        'section': 'finance_sell',
    })


@login_required
def finance_sell_cost_add(request, sell_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    cost = SellCost(sell=sell)

    if request.method == 'POST':
        form = SellCostForm(request.POST, instance=cost)
        if form.is_valid():
            item = form.save()
            messages.info(request, _("Sell cost %d added :)") % item.pk)

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_cost_edit',
                                sell_id=sell_id, cost_id=cost.pk)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_cost_add',
                                sell_id=sell_id, cost_id=cost.pk)
    else:
        form = SellCostForm(instance=cost)

    return render(request, 'backoffice/finance_sell_cost_add.html', {
        'form': form,
        'sell': sell,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_cost_edit(request, sell_id, cost_id):
    """
    TODO
    """
    sell = get_object_or_404(Sell, pk=sell_id)
    cost = get_object_or_404(SellCost, pk=cost_id)

    if request.method == 'POST':
        form = SellCostForm(request.POST, instance=cost)
        if form.is_valid():
            form.save()
            messages.info(request, _('Sell cost updated :)'))

            if 'save' in request.POST:
                return redirect('backoffice_finance_sell_edit',
                                sell_id=sell_id)

            if 'save_and_edit' in request.POST:
                return redirect('backoffice_finance_sell_cost_edit',
                                sell_id=sell_id, cost_id=cost_id)

            elif 'save_and_new' in request.POST:
                return redirect('backoffice_finance_sell_cost_add',
                                sell_id=sell_id, cost_id=cost_id)
    else:
        form = SellCostForm(instance=cost)

    return render(request, 'backoffice/finance_sell_cost_edit.html', {
        'form': form,
        'sell': sell,
        'cost': cost,
        'section': 'finance_sell',
    })


@login_required
def finance_sell_cost_delete(request, sell_id, cost_id):
    """
    TODO
    """
    get_object_or_404(Sell, pk=sell_id)
    cost = get_object_or_404(SellCost, pk=cost_id)

    if request.method == 'POST':
        cost.delete()
        messages.warning(request, _('Sell cost deleted.'))
        return redirect('backoffice_finance_sell_edit', sell_id)

    return render(request, 'backoffice/commons_delete.html', {
        'obj': cost,
        'model': _('Sell cost'),
        'form': DeleteForm(),
        'section': 'finance_sell',
    })


# vim: ai ts=4 sts=4 et sw=4 ft=python
