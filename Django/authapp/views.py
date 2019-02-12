from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpRequest, HttpResponse
from django.contrib import auth
from django.urls import reverse

from .forms import LoginForm, RegisterForm, UpdateForm


# Create your views here.

def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')


def login(request):
    title = 'Войти на сайт'

    # создать форму для заполнения
    login_form = LoginForm(data=request.POST or None)

    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    # проверить данные из request
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']


        # выполнить аутентификацию
        user = auth.authenticate(username=login, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('catalog:index'))


    content = {
        'title': title,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = 'Регистарция'

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))

    else:
        register_form = RegisterForm()

    content = {
        'title': title,
        'reg_form': register_form
    }

    return render(request, 'authapp/register.html', content)


def edit(request):
    title = 'Профиль'

    if request.method == 'POST':
        edit_form = UpdateForm(request.POST, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))

    else:
        edit_form = UpdateForm(instance=request.user)

    content = {
        'title': title,
        'update_form': edit_form
    }

    return render(request, 'authapp/edit.html', content)
