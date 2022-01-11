from django.forms.widgets import EmailInput
from django.shortcuts import render, redirect
from .models import Category, Size, Product, Cart, CartProduct, Color
from authe.views import *

def html_data():
    return {'category':Category.objects.all(), 'size':Size.objects.all(), 'color':Color.objects.all()}

def all_products(request):
    if request.user.is_authenticated:
        products = Product.objects.filter(available = True)
        return render(request, 'all_products.html', {'products':products, 'dropdown': html_data()})
    elif request.user.is_authenticated == False:
        return redirect('authe:register')

def product_info(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, "product_info.html", {"product":product, 'dropdown':html_data()})

def products_filter(request, category_id):
    products = Product.objects.filter(category__id = category_id)
    return render(request, 'products_filter.html', {'products':products, 'dropdown':html_data()})

def cart_create(request):
    cart = Cart.objects.create(
        owner = request.user,
        email = request.user.email
    )
    if cart.is_valid():
        pass
    cart.save()
    return cart_create(request)

# def cart_delete(request):
#     if log_out(request):
#         cart = Cart.objects.filter(owner = request.user)
#         cart.delete()
#         return render(request, 'index.html')

def add_to_cart(request):
    if request.method == 'POST':
        product = Product.objects.get(id = request.POST['product'])
        cart_product = CartProduct.objects.create(
            cart = request.user.cart,
            product = product,
            count = 1
        )
        cart_product.save()

def my_cart(request):
    cart = Cart.objects.get(owner = request.user)
    products = CartProduct.objects.filter(cart = cart)
    return render(request, 'my_cart.html', {'cart':cart, 'products':products, 'dropdown':html_data()})


