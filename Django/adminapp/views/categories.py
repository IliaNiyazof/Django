from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse
from mainapp.models import ProductCategory
from django.contrib.auth.decorators import user_passes_test
from adminapp.models.categories import CategoryEditForm


@user_passes_test(lambda user: user.is_superuser)
def index(request: HttpRequest):
    models = ProductCategory.objects.all()

    return render(request, 'adminapp/categories/categories_index.html', {
        'models': models,
    })


@user_passes_test(lambda user: user.is_superuser)
def create(request: HttpRequest):
    return HttpResponse('action -> create')


@user_passes_test(lambda user: user.is_superuser)
def read(request: HttpRequest, id=None):
    # model = ProductCategory.objects.get(pk=id)
    model = get_object_or_404(ProductCategory, pk=id)
    products = model.products.all()  # only 5 last

    return render(request, 'adminapp/categories/read.html', {
        'model': model,
        'products': products
    })


@user_passes_test(lambda user: user.is_superuser)
def update(request: HttpRequest, id):
    title = 'категории/редактирование'

    edit_category = get_object_or_404(ProductCategory, pk=id)
    if request.method == 'POST':
        edit_form = CategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:categories_update', args=[edit_category.pk]))
    else:
        edit_form = CategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}

    return render(request, 'adminapp/categories/update.html', content)


@user_passes_test(lambda user: user.is_superuser)
def delete(request: HttpRequest, id):
    model = get_object_or_404(ProductCategory, pk=id)

    # model.delete()
    return HttpResponseRedirect(reverse('admin:categories'))
