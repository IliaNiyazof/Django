from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest
from .models import ProductCategory, Product
from basketapp.models import Basket
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.cache import cache

from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.http import JsonResponse
from django.views.decorators.cache import never_cache


# Create your views here.
def index(request: HttpRequest):
    title = 'Главная'

    products = Product.objects.filter(is_active=True, productcategory__is_active=True).select_related('productcategory')

    return render(request, 'mainapp/layouts/layouts.html', {
        'title': title,
        'data': products

    })


@cache_page(3600)
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


def catalog_ajax(request: HttpRequest, pk=None, page=1):
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

    content = {
        'title': title,
        'provider': products_provider,
        'productcategory': product,
    }

    result = render_to_string('mainapp/includes/inc_products_list_content.html',
                              context=content,
                              request=request)

    return JsonResponse({'result': result})


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


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r',
              errors='ignore') as infile:
        return json.load(infile)


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True,
                                              category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True,
                                      category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True,
                                              category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True,
                                      category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True,
                                              category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True,
                                      category__is_active=True).order_by('price')
