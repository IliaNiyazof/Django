from django.urls import path

from adminapp.views import users, categories, products
from adminapp.controllers import user, product, categorie

app_name = 'adminapp'

urlpatterns = [
    path('users/index', user.UserListView.as_view(), name='users_index'),
    path('users/create/', user.UserCreateView.as_view(), name='users_create'),
    path('users/update/<int:pk>', user.UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>', user.UserDeleteView.as_view(), name='users_delete'),

    # categories (CRUD)
    path('categories/index', categorie.CategoriesListView.as_view(), name='categories'),
    path('categories/create/', categories.create, name='categories_create'),  # admin:user_create
    path('categories/read/<int:id>', categories.read, name='category_read'),
    path('categories/update/<int:id>', categories.update, name='categories_update'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),

    # products (CRUD, list_by_category)
    path('products/create/', products.create, name='products_create'),  # admin:user_create
    path('products/read/<int:id>', products.read, name='products_read'),
    path('products/list/<int:category>', product.ProductListView.as_view(), name='products_category'),
    path('products/update/<int:id>', products.update, name='products_update'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),
]
