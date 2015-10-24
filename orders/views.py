from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'orders/homepage.html')
    #return HttpResponse("Hello, world. You're at the orders index.")

def create_user(request):
    return render(request, 'orders/create_user.html')

def choose_shop(request):
    return render(request, 'orders/choose_shop.html')

def show_contact(request):
    return render(request, 'orders/show_contact.html')

def show_products(request):
    products = Products.objects.all()
    return render(request, 'orders/show_products.html')

def login(request):
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