from django.contrib import admin
from .models import Category, Size, Product, Cart, Color

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Color)