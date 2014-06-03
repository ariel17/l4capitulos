#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Common form declarations for backoffice.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button


class AddEditFormMixin(object):
    """
    Implements customized methods for add/edit forms.
    """
    def get_button_holder(self):
        """
        Returns a holder with common buttons.
        """
        return ButtonHolder(
            Button('cancel', _('Cancel'), css_class='btn btn-default'),

            Submit('save_and_new', _('Save and new'),
                   css_class='button white'),

            Submit('save_and_edit', _('Save and edit'),
                   css_class='button white'),

            Submit('save', _('Save'), css_class='button white'),
        )


class SearchFormMixin(object):
    """
    Implements customized methods for search forms.
    """
    def get_button_holder(self):
        """
        Returns a holder with common buttons.
        """
        return ButtonHolder(
            FormActions(
                Submit('search', _('Search')),
            )
        )


class DeleteForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(DeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            ButtonHolder(
                Button('no', _('No'), css_class='btn btn-default'),
                Submit('yes', _('Yes'), css_class='button white'),
            )
        )


class PostFormMixin(object):
    """
    Implements customized methods for social media post forms.
    """
    def get_button_holder(self):
        """
        Returns a holder with common buttons.
        """
        return ButtonHolder(
            Button('cancel', _('I guess no'), css_class='btn btn-default'),
            Submit('save', _('Do it!'), css_class='button white'),
        )

# vim: ai ts=4 sts=4 et sw=4 ft=python
