from django.urls import re_path

from adminapp.views import users, categories, products
from adminapp.controllers import user, categori, product

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^users/index/$', user.UserListView.as_view(), name='users_index'),
    re_path(r'^users/create/$', user.UserCreateView.as_view(), name='users_create'),
    re_path(r'^users/update/(?P<pk>\d+)/$', user.UserUpdateView.as_view(), name='users_update'),
    re_path(r'^users/delete/(?P<pk>\d+)/$', users.delete, name='users_delete'),

    # categories (CRUD)
    re_path(r'^categories/create/$', categori.ProductCategoryCreateView.as_view(), name='category_create'),
    re_path(r'^categories/read/$', categories.categories, name='categories'),
    re_path(r'^categories/update/(?P<pk>\d+)/$', categori.ProductCategoryUpdateView.as_view(), name='category_update'),
    re_path(r'^categories/delete/(?P<pk>\d+)/$', categori.ProductCategoryDeleteView.as_view(), name='category_delete'),

    re_path(r'^products/create/category/<(?P<pk>\d+)/$', products.product_create, name='product_create'),
    re_path(r'^products/read/category/(?P<pk>\d+)/$', products.products, name='products'),
    re_path(r'^products/read/(?P<pk>\d+)/$', product.ProductDetailView.as_view(), name='product_read'),
    re_path(r'^products/update/(?P<pk>\d+)/$', products.product_update, name='product_update'),
    re_path(r'^products/delete/(?P<pk>\d+)/$', products.product_delete, name='product_delete'),
]
