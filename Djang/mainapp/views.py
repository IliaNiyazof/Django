from .models import Person, Department, ProductCategory, Products
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse

from authapp.forms import LoginForm, RegisterForm, EditForm

def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auht/login')



def login(request: HttpRequest):
    title = 'title',

    login_form = LoginForm(data=request.POST)

    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=login, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {
        'title': title,
        "login_form": login_form
    }
    return render(request, 'authapp/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request: HttpRequest):
    title = 'title'

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = RegisterForm()

    content = {'title': title, 'reg_form': register_form}

    return render(request, 'authapp/register.html', content)


def edit(request: HttpRequest):
    title = 'редактирование'

    if request.method == 'POST':
            edit_form = EditForm(request.POST, instance=request.user)
            if edit_form.is_valid():
                edit_form.save()
                return HttpResponseRedirect(reverse('auth:edit'))
    else:
            edit_form = EditForm(instance=request.user)

    content = {'title': title, 'edit_form': edit_form}

    return render(request, 'authapp/edit.html', content)







def catalog(request: HttpRequest, id=None):
    users = [
                {'name': 'все'},
                {'name': 'дом'},
                {'name': 'офис'},
                {'name': 'модерн'},
                {'name': 'классика'},
            ] #пробник
    links_menu = ProductCategory.objects.all()
    products = Products.objects.all()


    return render(request, 'mainapp/child1.html', {
        'links_menu':links_menu,
        'data': users,
        'products':products
    })


def index(request: HttpRequest):
    return render(request, 'mainapp/child.html')


def contakt(request: HttpRequest):
    return render(request, 'mainapp/child2.html')


def goods1(request: HttpRequest):
    return render(request, 'mainapp/child3.html')


def view(request: HttpRequest, id=None):
    return render(request, 'mainapp/fi.html')


def company_index(request: HttpRequest):
    deps = Department.object.all()
    pass


def company_view(request: HttpRequest, id=None):
    deps = Department.object.get(id=id)
    pass



