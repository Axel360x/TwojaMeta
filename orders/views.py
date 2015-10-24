# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from orders.models import Product, ProviderUser, Dormitory

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

def login_view(request):
	return render(request, 'orders/login.html')

def login_attempt(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/orders/")
    else:
        form = UserCreationForm()
    return render(request, "orders/register.html", {
        'form': form,
    })