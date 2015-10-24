# -*- coding: utf-8 -*-

from django import forms

class NameForm(forms.Form):
    username = forms.CharField(label='Twoj login', max_length=100)
    password = forms.CharField(label='Twoje haslo', max_length=100, widget=forms.PasswordInput())