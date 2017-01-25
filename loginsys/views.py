# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from extUser.models import extUser
from django.core.mail import send_mail
import random
import string


# Create your views here.

@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect("/articles/all/")
            else:
                args[
                    'login_error'] = "Извените, Ваша учётная запись ещё не активна. Пройдите по ссылке отправленной по указанному Вами адресу электронной почты"
                return render(request, "login.html", args)
        else:
            args['login_error'] = "Пользователь не найден"
            return render(request, "login.html", args)
    else:
        return render(request, "login.html", args)


def logout(request):
    auth.logout(request)
    return redirect("/articles/all/")


@csrf_protect
def register(request):
    args = {}
    args['form'] = UserCreationForm()
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser = newuser_form.save(commit=False)
            if newuser.username.endswith("ru"):
                newuser.is_active = False
                newuser.save()
                newExtUser = extUser()
                newExtUser.user_key = newuser
                newExtUser.secret_key = ''.join(
                    random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(30))
                newExtUser.save()
                message = "//192.168.1.100:8000/auth/register/" + newExtUser.secret_key
                send_mail('Регистрация', message, 'stepan.syzganov@ya.ru', [newuser.username, ], fail_silently=False)
            else:
                args['form'] = newuser_form
                args["error"] = "Не корректный адрес электронной почты, используйте корпоративную почту"
                return render(request, 'register.html', args)

            # newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
            #                           password=newuser_form.cleaned_data['password2'])
            # auth.login(request, newuser)

            return redirect("/articles/all/")
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)


def confirm_registration(request, secret_key):
    user = (extUser.objects.get(secret_key=secret_key)).user_key
    if (user is not None) and (user.is_active == False):
        user.is_active = True
        user.save()
        return redirect("/auth/login/")
    else:
        return redirect("/auth/login/")



# def restore_passwd(request, secret_key):
#     user = (extUser.objects.get(secret_key=secret_key)).user_key
#     if (user is not None) and user.is_active:
