from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, HttpResponseRedirect, reverse, get_object_or_404
from mainapp.models import ProductCategory, Product
from adminapp.models.products import ProductEditForm

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(productcategory__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products/priducts_index.html', content)


def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        # задаем начальное значение категории в форме
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title, 'update_form': product_form, 'category': category}

    return render(request, 'adminapp/products/update.html', content)


def product_update(request, pk):
    title = 'продукт/редактирование'

    edit_product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('admin:product_update', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form, 'category': edit_product.productcategory}

    return render(request, 'adminapp/products/update.html', content)


def product_delete(request, pk):
    title = 'продукт/удаление'

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('admin:products', args=[product.productcategory.pk]))

    content = {
        'title': title,
        'product_to_delete': product
    }

    return render(request, 'adminapp/products/delete.html', content)