from django.urls import path
from home.views import home,products,clients

urlpatterns = [
    path('', home, name = 'home'),
    path('products/', products, name = 'products'),
    path('clients/', clients, name = 'clients')
]
