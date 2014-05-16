#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for purchase models in backoffice.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button

from finance.models import Purchase


class PurchaseForm(forms.Form):

    date = forms.DateField(
        required=False,
    )

    price = forms.DecimalField(
        widget=forms.TextInput(attrs={"placeholder": _("Price")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(PurchaseForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Purchase information',
                'date',
                'price',
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
        model = Purchase
