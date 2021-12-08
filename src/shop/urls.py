from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path("", all_products, name = 'all_products'),
    path("product_info/<int:product_id>", product_info, name = 'product_info'),
]