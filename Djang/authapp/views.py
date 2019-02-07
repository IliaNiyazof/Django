from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib import auth

from .forms import LoginForm

# Create your views here.
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