from django.shortcuts import render
from .models import product

# Create your views here.

def home (request):
    return render(request, 'home/home.html')

def products (request):
    products = product.objects.all()
    context = {
        'products' : products,
    }
 
    return render(request, 'home/products.html', context) 

def clients (request):

    return render(request, 'home/clients.html')