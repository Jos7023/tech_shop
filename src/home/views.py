from django.shortcuts import render

# Create your views here.

def home (request):
    return render(request, 'base.html')

def products (request):
    context = {
        'products' : [
            {'name' : 'Apple watch',
             'price' : '299.99',
             'desription' : 'Aluminium case, starlight sport' },

            {'name' : 'iphone14',
             'price' : '799.99',
             'description' : '128GB, midnight color'}
             ]
    }
    return render(request, 'home/products.html', context) 
