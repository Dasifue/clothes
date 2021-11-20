from django.contrib.admin.sites import site
from django.shortcuts import render, redirect
from .models import Category, Size, Product, Cart, CartProduct

def html_data():
    return {'category':Category.objects.all(), 'size':Size.objects.all()}

def all_products(request):
    return render(request, 'all_products.html', {'products':Product.objects.all()})

def products_filter(request, size_id, category_id):
    products = None
    if Product.objects.filter(size = size_id):
        products = Product.objects.get(size = size_id)
    elif Product.objects.filter(category = category_id):
        products = Product.objects.get(category = category_id)
    return render(request, 'products_filter.html', {'products':products})
