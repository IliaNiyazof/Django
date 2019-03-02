from django.urls import re_path

import basketapp.views as controller

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', controller.index, name='index'),
    re_path(r'^add/(?P<pk>\d+)/$', controller.add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)/$', controller.remove, name='remove'),
]
