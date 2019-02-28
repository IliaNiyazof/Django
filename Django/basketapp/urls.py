from django.urls import re_path

import basketapp.views as controller

app_name = 'basketapp'

urlpatterns = [
    re_path(r'^$', controller.index, name='index'),
    re_path(r'^add/<int:id>/$', controller.add, name='add'),
    re_path(r'^remove/<int:id>/$', controller.remove, name='remove'),
]
