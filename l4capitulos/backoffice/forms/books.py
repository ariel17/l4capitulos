#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for book models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"

import logging
import uuid

from facepy import GraphAPI

from django import forms
from django.conf import settings
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field, HTML
from social.apps.django_app.default.models import UserSocialAuth

from .commons import AddEditFormMixin, SearchFormMixin, PostFormMixin
from book.models import Author, Book, Category, Status, BookImage, Editorial


logger = logging.getLogger(__name__)


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
        label=_('First name'),
        widget=forms.TextInput(attrs={"placeholder": _("First name")}),
        required=False,
    )

    last_name = forms.CharField(
        label=_('Last name'),
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
        label=_('Name'),
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
                'observations',
            ),
            Fieldset(
                _('Publication information'),
                'isbn',
                'published_at',
                'editorial',
            ),
            Fieldset(
                _('Availability and price'),
                'quantity',
                'price',
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
                            }))),
                ))

        self.helper.layout.append(
            self.get_button_holder()
        )

    class Meta:
        model = Book


class BookSearchForm(forms.Form, SearchFormMixin):
    """
    TODO
    """
    title = forms.CharField(
        label=_('Title'),
        widget=forms.TextInput(attrs={"placeholder": _("Title")}),
        required=False,
    )

    authors = forms.CharField(
        label=_('Authors'),
        widget=forms.TextInput(attrs={"placeholder": _("Authors")}),
        required=False,
    )

    isbn = forms.CharField(
        label=_('ISBN'),
        widget=forms.TextInput(attrs={"placeholder": _("ISBN number")}),
        required=False,
    )

    added_from = forms.DateField(
        label=_('Added from'),
        required=False,
    )

    added_to = forms.DateField(
        label=_('Added to'),
        required=False,
    )

    published_from = forms.DateField(
        label=_('Published from'),
        required=False,
    )

    published_to = forms.DateField(
        label=_('Published to'),
        required=False,
    )

    editorial = forms.CharField(
        label=_('Editorial'),
        widget=forms.TextInput(attrs={"placeholder": _("Editorial's name")}),
        required=False,
    )

    category = forms.CharField(
        label=_('Category'),
        widget=forms.TextInput(attrs={"placeholder": _("Category")}),
        required=False,
    )

    status = forms.CharField(
        label=_('Status'),
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


class FacebookBookPostForm(forms.Form, PostFormMixin):
    """
    Validates the book information to post.
    """
    album = forms.ChoiceField(
        label=_('Album'),
        required=False,
    )

    description = forms.CharField(
        label=_('Description'),
        widget=forms.Textarea(attrs={"placeholder": _("Description")}),
        required=True,
    )

    def __init__(self, user, book, *args, **kwargs):
        super(FacebookBookPostForm, self).__init__(*args, **kwargs)
        self.book = book
        self.user = user

        self.fields['album'].choices = self.get_album_choices(user)
        self.fields['description'].initial = render_to_string(
            'backoffice/facebook_post.txt', {
                'book': book
            }).strip()

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Field("album"),
                Field("description"),
                css_class="row group-padding-12"
            ),
            self.get_button_holder(),
        )

        self.helper.form_action = "%s?action=facebook_post" % reverse(
            'backoffice_book_book_edit',
            args=(book.pk,)
        )

    def get_album_choices(self, user):
        """
        Returns a list of tuples for album choice field.
        """
        albums = []
        try:
            provider = user.social_auth.get(provider='facebook')
        except UserSocialAuth.DoesNotExist:
            return []

        graph = GraphAPI(provider.extra_data['access_token'])
        response = graph.get(
            '%s/albums' % settings.FACEBOOK_FAN_APP_ID
        )
        logger.debug('Facebook response for album information: %r' % response)

        if 'data' not in response:
            return []

        for album in response['data']:
            albums.append((album['id'], album['name']))

        return albums

    def save(self):
        """
        Posts the content into a Facebook album.
        """
        _uuid = uuid.uuid4()

        provider = self.user.social_auth.get(provider='facebook')

        graph = GraphAPI(provider.extra_data['access_token'])

        logger.debug('[%s] Posting %d photos into album %s' % (
            _uuid, self.book.bookimage_set.all().count(),
            self.cleaned_data['album']
        ))

        page_auth = graph.get(
            "%s?fields=access_token" % settings.FACEBOOK_FAN_APP_ID
        )

        page_graph = GraphAPI(page_auth['access_token'])
        responses = []

        for image in self.book.bookimage_set.all():
            response_image = page_graph.post(
                path="%s/photos" % self.cleaned_data['album'],
                source=open(image.image.path),
                message=self.cleaned_data['description'],
            )

            logger.debug("[%s] Posting image %r to album result: %r" % (
                _uuid, image, response_image
            ))

            response_feed = page_graph.post(
                path="%s/feed" % settings.FACEBOOK_FAN_APP_ID,
                link="%s%s" % (
                    settings.FACEBOOK_IMAGE_POST_URL,
                    response_image['id']
                ))

            logger.debug("[%s] Posting image %r to feed result: %r" % (
                _uuid, image, response_feed
            ))

            responses.append({
                'image_post': response_image,
                'feed_post': response_feed,
            })

        return responses

# vim: ai ts=4 sts=4 et sw=4 ft=python
