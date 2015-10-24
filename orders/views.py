from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'orders/homepage.html')
    #return HttpResponse("Hello, world. You're at the orders index.")

def create_user(request, type_of_user):
	pass