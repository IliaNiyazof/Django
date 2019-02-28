from django.urls import re_path

from adminapp.views import users, categories, products
from adminapp.controllers import user, categori, product

app_name = 'adminapp'

urlpatterns = [
    re_path(r'^users/index/$', user.UserListView.as_view(), name='users_index'),
    re_path(r'^users/create/$', user.UserCreateView.as_view(), name='users_create'),
    re_path(r'^users/update/<int:pk>/$', user.UserUpdateView.as_view(), name='users_update'),
    re_path(r'^users/delete/<int:pk>/$', user.UserDeleteView.as_view(), name='users_delete'),

    # categories (CRUD)
    re_path(r'^categories/create/$', categori.ProductCategoryCreateView.as_view(), name='category_create'),
    re_path(r'^categories/read/$', categori.ProductCategoryReadView.as_view(), name='categories'),
    re_path(r'^categories/update/<int:pk>/$', categori.ProductCategoryUpdateView.as_view(), name='category_update'),
    re_path(r'^categories/delete/<int:pk>/$', categori.ProductCategoryDeleteView.as_view(), name='category_delete'),

    re_path(r'^products/create/category/<int:pk>/$', products.product_create, name='product_create'),
    re_path(r'^products/read/category/<int:pk>/$', products.products, name='products'),
    re_path(r'^products/read/<int:pk>/$', product.ProductDetailView.as_view(), name='product_read'),
    re_path(r'^products/update/<int:pk>/$', products.product_update, name='product_update'),
    re_path(r'^products/delete/<int:pk>/$', products.product_delete, name='product_delete'),
]
