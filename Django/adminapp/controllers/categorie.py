from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from mainapp.models import ProductCategory


class CategoriesListView(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories/categories_index.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoriesListView, self).dispatch(request, *args, **kwargs)

class CategoriesUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/categories/update.html'
    fields = '__all__'
    success_url = reverse_lazy('admin:products_read')
