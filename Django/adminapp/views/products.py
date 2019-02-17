from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test
from adminapp.models.products import ProductEditForm


def create(request: HttpRequest):
    return HttpResponse('action -> create')


def list_dy_category(request: HttpRequest, category,):
    models = Product.objects.filter(pk=category)

    return render(request, 'adminapp/products/priducts_index.html', {
        'models': models,
    })

@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id):
    model = Product.objects.filter(pk=id)

    return render(request, 'adminapp/products/products_read.html', {
        'model': model,
    })


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id=None):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=id)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:products_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': edit_product.productcategory_id}

    return render(request, 'adminapp/products/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    model = get_object_or_404(ProductCategory, pk=id)

    # model.delete()
    return HttpResponseRedirect(reverse('admin:categories'))
