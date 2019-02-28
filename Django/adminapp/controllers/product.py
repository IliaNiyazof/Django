from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from django.shortcuts import HttpResponseRedirect
from mainapp.models import Product

class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/products/products_read.html'

