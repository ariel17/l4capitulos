#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Model definitions about books and related data.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django.conf import settings
from django.db import models
from django.utils.translation import ugettext as _

from common.models import FileModel


class AuthorManager(models.Manager):
    """
    Custom manager for author model instances.
    """
    def search(self, *args, **kwargs):
        """
        Search for possible matchings on author's fields.
        """
        authors = self.all()

        if 'first_name' in kwargs:
            first_name = kwargs['first_name'].strip()
            if first_name:
                authors = authors.filter(first_name__icontains=first_name)

        if 'last_name' in kwargs:
            last_name = kwargs['last_name'].strip()
            if last_name:
                authors = authors.filter(last_name__icontains=last_name)

        return authors


class Author(models.Model):
    """
    A person that writes books.
    """
    first_name = models.CharField(
        _('First name'),
        max_length=200,
        blank=True,
        null=True,
        help_text=_("The author's first name.")
    )

    last_name = models.CharField(
        _('Last name'),
        max_length=200,
        help_text=_("The author's last name.")
    )

    objects = AuthorManager()

    class Meta:
        ordering = ['first_name', 'last_name']

    def __unicode__(self):
        return unicode(self.get_full_name())

    def get_full_name(self):
        """
        Returns the first name and last name combination.
        """
        full_name = u"%s %s" % (self.first_name, self.last_name)
        full_name.strip()
        return full_name


class BookManager(models.Manager):
    """
    Custom manager for book model instances.
    """
    def search(self, *args, **kwargs):
        """
        Searches a book in filtering by indicated parameters.
        """
        books = self.all()

        if 'title' in kwargs:
            title = kwargs['title'].strip()
            if title:
                books = books.filter(title__icontains=title)

        if 'authors' in kwargs:
            for author in kwargs['authors'].split(' '):
                author = author.strip()
                if author:
                    books = books.filter(authors__last_name__icontains=author)

        if 'isbn' in kwargs:
            isbn = kwargs['isbn'].strip()
            if isbn:
                books = books.filter(isbn__icontains=isbn)

        # added_from
        # added_to
        # published_from
        # published_to

        if 'editorial' in kwargs:
            editorial = kwargs['editorial'].strip()
            if editorial:
                books = books.filter(editorial__icontains=editorial)

        if 'category' in kwargs:
            category = kwargs['category'].strip()
            if category:
                books = books.filter(category__name__icontains=category)

        if 'status' in kwargs:
            status = kwargs['status'].strip()
            if status:
                books = books.filter(status__name__icontains=status)

        return books


class Category(models.Model):
    """
    A book category for classifition.
    """
    parent = models.ForeignKey(
        "self",
        blank=True,
        null=True
    )

    name = models.CharField(
        _('Name'),
        max_length=50,
        help_text=_('The category name.')
    )

    class Meta:
        ordering = ['name', 'parent__id']

    def get_full_name(self):
        """
        Returns the full category name with parent's names, separated by ">".
        """
        if self.parent is None:
            return self.name

        return "%s > %s" % (self.parent.get_full_name(), self.name)

    def __unicode__(self):
        return unicode(self.get_full_name())


class Status(models.Model):
    """
    A book status.
    """
    name = models.CharField(
        _('Name'),
        max_length=100,
        help_text=_('The status name.')
    )

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return unicode(self.name)


class Book(models.Model):
    """
    The book itself.
    """
    title = models.CharField(
        _('Title'),
        max_length=200,
        help_text=_("The book's title.")
    )

    authors = models.ManyToManyField(
        Author,
        blank=True,
        null=True,
    )

    isbn = models.CharField(
        _('ISBN'),
        max_length=50,
        blank=True,
        null=True,
        help_text=_("The book's ISBN number that identifies it.")
    )

    published_at = models.DateField(
        _('Published at'),
        blank=True,
        null=True,
        help_text=_("The publication date of the book.")
    )

    editorial = models.CharField(
        _('Editorial'),
        max_length=100,
        blank=True,
        null=True,
        help_text=_("The editorial that printed and released the book.")
    )

    summary = models.TextField(
        _('Summary'),
        blank=True,
        null=True,
        help_text=_('Book summary about its content and why should buy it.')
    )

    added_at = models.DateTimeField(
        _('Added at'),
        auto_now=True,
        blank=True,
        null=True,
    )

    category = models.ForeignKey(
        Category,
        blank=True,
        null=True
    )

    status = models.ForeignKey(
        Status,
        blank=True,
        null=True
    )

    objects = BookManager()

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return unicode(self.title)


class BookImage(FileModel):
    """
    A book picture or image.
    """
    book = models.ForeignKey(Book)

    image = models.ImageField(
        _(u"Book image"),
        upload_to=FileModel.normalize_filename(settings.BOOK_IMAGES_PATH),
        default=settings.IMAGES_DEFAULT,
    )

    primary = models.BooleanField(
        _(u"Is primary"),
        help_text=u"The image is the one that better describes the book.",
        default=False,
    )

    def __unicode__(self):
        return u"picture#%d@book#%d" % (self.pk, self.book.pk)


class Availability(models.Model):
    """
    TODO
    """
    book = models.ForeignKey(
        Book,
        unique=True
    )

    quantity = models.PositiveIntegerField(
        _('Quantity'),
        default=0,
        help_text=_('How many items of this book are available.')
    )
