from django.urls import path
from .views import register, confirm_email, log_in, log_out


app_name = 'authe'

urlpatterns = [
    path('register/', register, name = 'register'),
    path('confirm/<str:code>', confirm_email, name = 'confirm'),
    path('log_in/', log_in, name='login'),
    path('log_out/', log_out, name = 'logout'),
]