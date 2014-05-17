#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for book models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, Field, HTML

from book.models import Author, Book


class AuthorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Author information',
                'first_name',
                'last_name',
            ),
            ButtonHolder(
                Button('cancel', _('Cancel'), css_class='btn btn-default'),

                Submit('save_and_close', _('Save and close'),
                       css_class='button white'),

                Submit('save_and_new', _('Save and new'),
                       css_class='button white'),

                Submit('save', _('Save'), css_class='button white'),
            )
        )

    class Meta:
        model = Author


class AuthorSearchForm(forms.Form):

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("First name")}),
        required=False,
    )

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Last name")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(AuthorSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Field("first_name"),
                Field("last_name"),
                css_class="row group-padding-12"
            ),

            ButtonHolder(
                FormActions(
                    Submit('search', _('Search')),
                )
            ),
        )

    class Meta:
        model = Author


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Book description',
                'title',
                'authors',
                'summary',
            ),
            Fieldset(
                'Publication information',
                'isbn',
                'published_at',
                'editorial',
            ),
            ButtonHolder(
                FormActions(
                    Button('cancel', _('Cancel'), css_class='btn btn-default'),

                    Submit('save_and_close', _('Save and close'),
                           css_class='button white'),

                    Submit('save_and_new', _('Save and new'),
                           css_class='button white'),

                    Submit('save', _('Save'), css_class='button white'),
                )
            )
        )

    class Meta:
        model = Book


class BookSearchForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Title")}),
        required=False,
    )

    authors = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Authors")}),
        required=False,
    )

    isbn = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("ISBN number")}),
        required=False,
    )

    added_from = forms.DateField(
        required=False,
    )

    added_to = forms.DateField(
        required=False,
    )

    published_from = forms.DateField(
        required=False,
    )

    published_to = forms.DateField(
        required=False,
    )

    editorial = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Editorial's name")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(BookSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Field("title"),
                Field("isbn"),
                Field("added_from"),
                Field("added_to"),
                css_class="row group-padding-12"
            ),

            Div(
                Field("published_from"),
                Field("published_to"),
                Field("editorial"),
                Field("authors"),
                css_class="row group-padding-12"
            ),

            ButtonHolder(
                FormActions(
                    Submit('search', _('Search')),
                )
            ),
        )

    class Meta:
        model = Book
