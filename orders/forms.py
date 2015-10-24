# -*- coding: utf-8 -*-

from django import forms
from django.core.exceptions import ObjectDoesNotExist

from .models import Product
'''
	Form that allows to create user
'''
class CreateUserForm(forms.Form):

    class Meta:
        model = Product
        fields = ('producer', 'product_name',)

