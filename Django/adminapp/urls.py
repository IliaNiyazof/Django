from django.urls import path

from adminapp.views import users, categories, products


app_name = 'adminapp'

urlpatterns = [
    # user(create, read, update, delete)
    path('users/index', users.index, name='users'),
    path('users/create/', users.create, name='users_create'),  # admin:user_create
    path('users/read/<int:id>', users.read, name='users_read'),
    path('users/update/<int:id>', users.update, name='users_update'),
    path('users/delete/<int:id>', users.delete, name='users_delete'),

    # categories (CRUD)
    path('categories/index', categories.index, name='categories'),
    path('categories/create/', categories.create, name='categories_create'),  # admin:user_create
    path('categories/read/<int:id>', categories.read, name='category_read'),
    path('categories/update/<int:id>', categories.update, name='categories_update'),
    path('categories/delete/<int:id>', categories.delete, name='categories_delete'),


    # products (CRUD, list_by_category)
    path('products/create/', products.create, name='products_create'),  # admin:user_create
    path('products/read/<int:id>', products.read, name='products_read'),
    path('products/list/<int:category>', products.list_dy_category, name='products_category'),
    path('products/update/<int:id>', products.update, name='products_update'),
    path('products/delete/<int:id>', products.delete, name='products_delete'),
]
