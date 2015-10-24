from django import forms

from .models import Product

'''
	Form that allows to create user
'''
class CreateUserForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('producer', 'product_name',)

'''
	Form that allows to login user
'''
class LoginUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('login', 'password',)