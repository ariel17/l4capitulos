#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: Form declaration for book models.
"""
__author__ = "Ariel Gerardo Rios (ariel.gerardo.rios@gmail.com)"


from django import forms
from django.contrib import auth
from django.utils.translation import ugettext as _

from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML


class LoginForm(forms.Form):
    """
    TODO
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "username"
    }))

    password = forms.CharField(widget=forms.PasswordInput())

    helper = FormHelper()
    helper.form_class = "form-signin"
    helper.layout = Layout(
        HTML("""<h1 class="form-signin-heading">%s</h1>""" %
             _("Backoffice! u.u")),
        "username",
        "password",
        FormActions(
            Submit("signin", _("Sign in"), css_class="btn-primary btn-block"),
        )
    )

    def get_user(self):
        return self.user

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        username = cleaned_data["username"]
        password = cleaned_data["password"]

        self.user = auth.authenticate(username=username, password=password)

        if not self.user or not self.user.is_staff:
            raise forms.ValidationError(_("Username or password invalid."))

        return cleaned_data
