from django.shortcuts import render, redirect
from .models import Category, Size, Product, Cart, CartProduct, Color
from authe.views import *

def html_data():
    return {'category':Category.objects.all(), 'size':Size.objects.all(), 'color':Color.objects.all()}

def all_products(request):
    return render(request, 'all_products.html', {'products':Product.objects.filter(available = True), 'dropdown': html_data()})

def product_info(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, "product_info.html", {"product":product, 'dropdown':html_data()})

def products_filter(request, category_id):
    products = Product.objects.filter(category__id = category_id)
    return render(request, 'products_filter.html', {'products':products, 'dropdown':html_data()})

def cart_create(request):
    if request.user.is_authenticated:
        cart = Cart.objects.create(
            owner = request.user,
            email = request.user.email
        )
        cart.save()
        return redirect('shop:all_products')    

