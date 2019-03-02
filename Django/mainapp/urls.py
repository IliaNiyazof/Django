from django.urls import re_path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', controller.catalog, name='index'),
    re_path(r'^category/page/(?P<page>\d+)/$', controller.catalog, name='page'),
    re_path(r'^product/(?P<pk>\d+)/$', controller.catalog, name='productcategory'),
    re_path(r'^details/(?P<pk>\d+)/$', controller.product_detail, name='details'),

]
