from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
   path('', controller.catalog, name='index'),
   path('<int:id>/', controller.catalog, name='productcategory'),
   path('details/<int:id>/', controller.product_detail, name='details'),

]