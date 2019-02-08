from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import ProductCategory, Product
from basketapp.models import Basket


# Create your views here.
def index(request: HttpRequest):
    title = 'Главная'

    products = Product.objects.all()

    return render(request, 'mainapp/layouts/layouts.html', {
        'title': title,
        'data': products
    })


def catalog(request: HttpRequest, id=None):
    title = 'Каталог'
    product = ProductCategory.objects.all()
    basket = Basket.objects.filter(user=request.user)


    if id is not None:
        products = Product.objects.filter(productcategory__pk=id)
    else:
        products = Product.objects.all()

    return render(request, 'mainapp/layouts/layouts1.html', {
        'title': title,
        'data': products,
        'productcategory': product,
        'basket': basket,
    })



def contakt(request: HttpRequest):
    title = 'Контакты'

    return render(request, 'mainapp/layouts/layouts2.html', {
        'title': title
    })


def goods1(request: HttpRequest):
    title = 'Товар'

    return render(request, 'mainapp/layouts/layouts3.html', {
        'title': title
    })



def product_detail(request: HttpRequest, id = None):
    if id is not None:
        # details = Product.objects.get(pk=id)
        details = get_object_or_404(Product, pk=id)
        products = Product.objects.filter(productcategory__pk=details.productcategory_id)
        product = ProductCategory.objects.all()
        basket = Basket.objects.filter(user=request.user)


    context = {
        'title':f'Товар: {details.name}',
        'product': product,
        'details': details,
        'products': products,
        'basket': basket,
    }

    return render(request, 'mainapp/details.html', context)