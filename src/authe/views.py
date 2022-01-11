from django.shortcuts import render, redirect
from authe.models import Author, ConfirmCode
from authe.forms import Register, LoginForm
from .utils import send_code_mail
from django.contrib.auth import authenticate 
from django.contrib.auth import  login as auth_login
from django.contrib.auth import logout
from shop.models import Cart
from shop.views import *

def register(request):
    form = Register()
    if request.method == 'POST':
        save_form = Register(request.POST)
        if save_form.is_valid():
            author = Author(username = request.POST['username'], email = request.POST['email'])
            author.set_password(request.POST['password'])
            author.save()
            code = ConfirmCode.objects.create(author=author)
            send_code_mail(author.email, code.code)
            message = "регистрация завершена успешно"
            return render(request,'reply.html',{"message":message})
        elif Author.objects.filter(username = request.POST['username'], verified=False) or Author.objects.filter(email = request.POST['email']):
            author = None
            if Author.objects.filter(username = request.POST['username']):
                author = Author.objects.get(username = request.POST['username'])
            elif Author.objects.filter(email = request.POST['email']):
                author = Author.objects.get(email = request.POST['email'])
            code = ConfirmCode.objects.create(author=author)
            send_code_mail(author.email, code.code)
            message = "регистрация прошла успешно"
            return render(request, 'reply.html', {'message':message})
        message = save_form.errors
        return render(request, 'reply.html', {'message':message})

    return render(request, 'register.html', {'form':form})

def confirm_email(request, code):
    code = ConfirmCode.objects.filter(code = code)
    message = 'ваш код не действителен'
    if code:
        if not code.last().confirm:
            code = code.last()
            code.confirm = True
            code.save()
            author = code.author
            author.verified = True
            author.save()
            message = 'ваша почта подтверждена'
    return render(request, 'reply.html', {'message':message})

def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        result = authentication(request)
        return render(request, 'reply.html', result)

    return render(request, 'log_in.html', {'form':form})

def authentication(request):
    user = authenticate(username = request.POST['username'], password = request.POST['password'])
    return login_result(user, request)       


def login_result(user, request):
    if user:
        auth_login(request, user)
        cart_create(request)
        return {'message':'вы вошли', 'success':True}

    return {'message':'не удалось войти в аккаунт', 'success':False}


    

def log_out(request):
    logout(request)
    return redirect('shop:all_products')

