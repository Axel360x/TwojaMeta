# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from orders.models import Product, ProviderUser, Dormitory
from django.template.loader import get_template
from django.template import RequestContext
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'orders/base.html')
    #return HttpResponse("Hello, world. You're at the orders index.")

def show_contact(request, provider_name):
    context = {'provider_name': provider_name}
    return render(request, 'orders/show_contact.html', context)

def show_providers(request, dormitory_name):
    providers = ProviderUser.objects.all()
    context = {'providers': providers}
    return render(request, 'orders/show_provider.html', context)

def show_dormitories(request):
    dormitories = Dormitory.objects.all()
    context = {'dormitories': dormitories}
    return render(request, 'orders/show_dormitories.html', context)

def show_products(request, shop_name):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'orders/show_products.html', context)

####################################################################################


from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = request.POST.get('username')
            passwd = request.POST.get('password')
            user = authenticate(username=user, password=passwd)

            if user is not None:
                if user.is_active:
                    #login(request, user)
                    return HttpResponse("You're successfully logged in!")
                else:
                    return HttpResponse("Your account is not active, please contact the site admin.")
            else:
                return HttpResponse("Your username and/or password were incorrect.")

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse("pierdol sie.")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'orders/formularz.html', {'form': form})