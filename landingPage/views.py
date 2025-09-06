from django.shortcuts import render,get_object_or_404
from .models import Products

def home(request):
    products = Products.objects.all() 
    context = {
        "products": products,
    }
    return render(request, "home.html", context)

def product_details(request, pk):
    product = get_object_or_404(Products, pk=pk)
    context = {
        "product": product,
    }
    return render(request, 'product_details.html', context)
