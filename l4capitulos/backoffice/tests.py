#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Test units for backoffice application.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from datetime import date

from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client

from .utils import generate_passed_dates
from book.models import Author, Book


User = get_user_model()


class UtilsTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_generate_passed_dates(self):
        today = date(2014, 5, 2)
        days = 2

        days_list = generate_passed_dates(days, today=today)

        self.assertEquals(days, len(days_list))
        self.assertEquals('2014-05-01', days_list[0])
        self.assertEquals('2014-05-02', days_list[1])


class BackofficeAuthorViewsTestCase(TestCase):
    def setUp(self):
        self._user = User.objects.create_user(
            username='admin', password='admin', email='admin@admin.com'
        )
        self._user.is_staff = True
        self._user.save()

        self._author = Author.objects.create(
            first_name='Ariel', last_name='Rios'
        )

        self.c = Client()
        self.assertTrue(self.c.login(username='admin', password='admin'))

    def tearDown(self):
        Author.objects.all().delete()
        User.objects.all().delete()

    def test_book_author_add(self):
        first_name = 'Leira'
        last_name = 'Soir'

        response = self.c.post(reverse('backoffice_book_author_add'), {
            'first_name': first_name, 'last_name': last_name
        }, follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(2, Author.objects.all().count())

        author = Author.objects.all()[1]
        self.assertEquals(first_name, author.first_name)
        self.assertEquals(last_name, author.last_name)

    def test_book_author_edit(self):
        first_name = 'Leira'
        last_name = 'Soir'

        response = self.c.post(reverse(
            'backoffice_book_author_edit', args=(self._author.pk,)
            ), {'first_name': first_name, 'last_name': last_name},
            follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, Author.objects.all().count())

        author = Author.objects.all()[0]

        self.assertEquals(first_name, author.first_name)
        self.assertEquals(last_name, author.last_name)

    def test_book_author_delete(self):
        response = self.c.post(reverse(
            'backoffice_book_author_delete', args=(self._author.pk,)
            ), follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(0, Author.objects.all().count())


class BackofficeBookViewsTestCase(TestCase):
    def setUp(self):
        self._user = User.objects.create_user(
            username='admin', password='admin', email='admin@admin.com'
        )
        self._user.is_staff = True
        self._user.save()

        self._author = Author.objects.create(
            first_name='Ariel', last_name='Rios'
        )

        self._book = Book.objects.create(
            title='Title book', quantity=1,
        )

        self.c = Client()
        self.assertTrue(self.c.login(username='admin', password='admin'))

    def tearDown(self):
        Author.objects.all().delete()
        Book.objects.all().delete()
        User.objects.all().delete()

    def test_book_book_add(self):
        title = 'Book2'
        response = self.c.post(reverse('backoffice_book_book_add'), {
            'title': title, 'quantity': 1
        }, follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(2, Book.objects.all().count())
        self.assertEquals(1, Book.objects.filter(title=title).count())

    def test_book_book_edit(self):
        title = 'New title'

        response = self.c.post(reverse(
            'backoffice_book_book_edit', args=(self._book.pk,)
            ), {'title': title, 'quantity': 1}, follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(1, Book.objects.all().count())
        self.assertEquals(1, Book.objects.filter(title=title).count())

    def test_book_book_delete(self):
        response = self.c.post(reverse(
            'backoffice_book_book_delete', args=(self._book.pk,)
            ), follow=True)

        self.assertEquals(200, response.status_code)
        self.assertEquals(0, Book.objects.all().count())

# vim: ai ts=4 sts=4 et sw=4 ft=python
