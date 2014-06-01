#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for book models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, HTML

from book.models import Author, Book, Category, Status, BookImage, Editorial, Availability
from .commons import AddEditFormMixin, SearchFormMixin


class AuthorForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Author information'),
                'first_name',
                'last_name',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Author


class AuthorSearchForm(forms.Form, SearchFormMixin):
    """
    TODO
    """
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
            self.get_button_holder()
        )

    class Meta:
        model = Author


class CategoryForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Category description'),
                'name',
            ),
            Fieldset(
                _('Child of'),
                'parent',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Category


class StatusForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Status description'),
                'name',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Status


class EditorialForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(EditorialForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Editorial information'),
                'name',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Editorial


class EditorialSearchForm(forms.Form, SearchFormMixin):
    """
    TODO
    """
    name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Editorial's name")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(EditorialSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Field("name"),
                css_class="row group-padding-12"
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Editorial


class BookForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Book description'),
                'title',
                'authors',
                'summary',
                'category',
                'status',
            ),
            Fieldset(
                _('Publication information'),
                'isbn',
                'published_at',
                'editorial',
            )
        )

        if self.instance.pk:
            self.helper.layout.append(
                Layout(
                    HTML(render_to_string(
                        "backoffice/commons_add_button.html", {
                            'url': reverse(
                                'backoffice_book_image_add',
                                args=(self.instance.pk,)
                            ),
                            'text': _('Add images'),
                        })),
                    Fieldset(
                        _("Images for this book"),
                        HTML(render_to_string(
                            "backoffice/book_book_image.html", {
                                "images": self.instance.bookimage_set.all(),
                                "book": self.instance,
                            })))
                ))

        self.helper.layout.append(
            self.get_button_holder()
        )

    class Meta:
        model = Book


class AvailabilitySearchForm(forms.Form, SearchFormMixin):
    """
    TODO
    """
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

    editorial = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Editorial's name")}),
        required=False,
    )

    category = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Category")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(AvailabilitySearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Field("title"),
                Field("isbn"),
                Field("category"),
                Field("status"),
                css_class="row group-padding-12"
            ),

            Div(
                Field("editorial"),
                Field("authors"),
                css_class="row group-padding-12"
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Book


class AvailabilityForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(AvailabilityForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Availability information'),
                'book',
                'quantity',
                'price',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Availability


class BookSearchForm(forms.Form, SearchFormMixin):
    """
    TODO
    """
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

    category = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Category")}),
        required=False,
    )

    status = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": _("Status")}),
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
                Field("category"),
                Field("status"),
                css_class="row group-padding-12"
            ),

            Div(
                Field("published_from"),
                Field("published_to"),
                Field("editorial"),
                Field("authors"),
                css_class="row group-padding-12"
            ),
            self.get_button_holder()
        )

    class Meta:
        model = Book


class BookImageForm(forms.ModelForm, AddEditFormMixin):
    """
    TODO
    """
    def __init__(self, *args, **kwargs):
        super(BookImageForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                _('Image'),
                'image',
                'primary',
            ),
            self.get_button_holder()
        )

    class Meta:
        model = BookImage
        exclude = ['book']
