#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Common form declarations for backoffice.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit, Button


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
