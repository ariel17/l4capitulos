#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for book models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button

from book.models import Author, Book


class BookForm(forms.Form):

    title = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Title")}),
        required=True,
    )

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
    )

    isbn = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("ISBN number")}),
    )

    published_at = forms.DateField()

    editorial = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Editorial's name")}),
    )

    summary = forms.CharField(
        widget=forms.Textarea(
            attrs={"placeholder": _("A short book summary")}
        ),
    )

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Book description',
                'title',
                'isbn',
                'published_at',
                'summary',
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
        model = Book
