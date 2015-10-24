from django import forms

from .models import Product

class CreateUserForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('producer', 'product_name',)

