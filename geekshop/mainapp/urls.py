from django.urls import re_path
from django.views.decorators.cache import cache_page

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    re_path(r'^$', controller.catalog, name='index'),
    re_path(r'^category/page/(?P<page>\d+)/$', controller.catalog, name='page'),
    re_path(r'^category/(?P<pk>\d+)/ajax/$',
            cache_page(3600)(controller.catalog_ajax)),
    re_path(r'^category/(?P<pk>\d+)/page/(?P<page>\d+)/ajax/$',
            cache_page(3600)(controller.catalog_ajax)),
    re_path(r'^product/(?P<pk>\d+)/$', controller.catalog, name='productcategory'),
    re_path(r'^details/(?P<pk>\d+)/$', controller.product_detail, name='details'),

]
