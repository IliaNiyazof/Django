from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request: HttpRequest):
    title = 'Главная'

    products = Product.objects.all()

    return render(request, 'mainapp/layouts/layouts.html', {
        'title': title,
        'data': products

    })


def catalog(request: HttpRequest, pk=None, page=1):
    title = 'Каталог'
    product = ProductCategory.objects.all()

    if pk is not None:
        products = Product.objects.filter(productcategory__pk=pk)
    else:
        products = Product.objects.all()

    provider = Paginator(products, 1)

    try:
        products_provider = provider.page(page)
    except PageNotAnInteger:
        products_provider = provider.page(1)
    except EmptyPage:
        products_provider = provider.page(provider.num_pages)

    return render(request, 'mainapp/layouts/layouts1.html', {
        'title': title,
        'provider': products_provider,
        'productcategory': product,
    })


def contakt(request: HttpRequest):
    title = 'Контакты'

    return render(request, 'mainapp/layouts/layouts2.html', {
        'title': title,

    })


def goods1(request: HttpRequest):
    title = 'Товар'

    return render(request, 'mainapp/layouts/layouts3.html', {
        'title': title,

    })


def product_detail(request: HttpRequest, pk=None):
    if id is not None:
        # details = Product.objects.get(pk=id)
        details = get_object_or_404(Product, pk=pk)
        products = Product.objects.filter(productcategory__pk=details.productcategory_id)
        product = ProductCategory.objects.all()

    context = {
        'title': f'Товар: {details.name}',
        'product': product,
        'details': details,
        'products': products,
    }

    return render(request, 'mainapp/details.html', context)


def get_current_user(current_user):
    if current_user.is_authenticated:
        basket = Basket.objects.filter(user=current_user)
    else:
        basket = None

    return basket
