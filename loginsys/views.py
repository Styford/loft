# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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
                args['login_error'] = "Извените, Ваша учётная запись ещё не активна. Пройдите по ссылке отправленной по указанному Вами адресу электронной почты"
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
            newuser.is_active = False
            newuser.save()

            # newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
            #                           password=newuser_form.cleaned_data['password2'])
            # auth.login(request, newuser)

            return redirect("/articles/all/")
        else:
            args['form'] = newuser_form
    return render(request, 'register.html', args)
