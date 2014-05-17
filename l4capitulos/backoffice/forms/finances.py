#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for purchase models in backoffice.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Button, Div, Field

from finance.models import Purchase


class PurchaseForm(forms.ModelForm):

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


class PurchaseSearchForm(forms.Form):

    date_from = forms.DateField(
        required=False,
    )

    date_to = forms.DateField(
        required=False,
    )

    price_from = forms.DecimalField(
        widget=forms.TextInput(attrs={"placeholder": _("Price from")}),
        required=False,
    )

    price_to = forms.DecimalField(
        widget=forms.TextInput(attrs={"placeholder": _("Price to")}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super(PurchaseSearchForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.form_class = 'form-inline'
        self.helper.layout = Layout(
            Div(
                Field("date_from"),
                Field("date_to"),
                css_class="row group-padding-12"
            ),

            Div(
                Field("price_from"),
                Field("price_to"),
                css_class="row group-padding-12"
            ),

            ButtonHolder(
                FormActions(
                    Submit('search', _('Search')),
                )
            ),
        )

    class Meta:
        model = Purchase
