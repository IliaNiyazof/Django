from django.shortcuts import render
from django.http import HttpRequest
from .models import Person, Department


# def index(request: HttpRequest):
#    users = [
#       {'name': 'John', 'age': 10},
#       {'name': 'Artur', 'age': 20},
#       {'name': 'David', 'age': 30},
#    ]
#    return render(request, 'mainapp/index.html',{
#       'data': users
#    })


def index(request: HttpRequest):
    return render(request, 'mainapp/child.html')


def catalog(request: HttpRequest):
    return render(request, 'mainapp/child1.html')


def contakt(request: HttpRequest):
    return render(request, 'mainapp/child2.html')


def goods1(request: HttpRequest):
    return render(request, 'mainapp/child3.html')


def company_index(request: HttpRequest):
    deps = Department.object.all()
    pass


def company_view(request: HttpRequest, id=None):
    deps = Department.object.get(id=id)
    pass
