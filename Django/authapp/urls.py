from django.urls import re_path
import authapp.views as authapp

import authapp.views as controller

app_name = 'authapp'

urlpatterns = [
    # path('', controller.login, name='index'),
    re_path(r'^$', controller.redirect_to_login, name='index'),
    re_path(r'^login/$', controller.login, name='login'),
    re_path(r'^logout/$', controller.logout, name='logout'),

    re_path(r'^register/$', controller.register, name='register'),
    re_path(r'^edit/$', controller.edit, name='edit'),
    re_path(r'^verify/(?P<email>.+)/(?P<activation_key>\w+)/$', controller.verify, name='verify'),

]
