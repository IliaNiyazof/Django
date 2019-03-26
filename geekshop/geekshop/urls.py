"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import mainapp.views as controller
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', controller.index),
    re_path(r'^index/', controller.index, name='index'),
    re_path(r'^contakt/', controller.contakt, name='contakt'),
    re_path(r'^goods1/', controller.goods1, name='goods1'),

    re_path(r'^catalog/', include('mainapp.urls', namespace='catalog')),
    re_path(r'^basket/', include('basketapp.urls', namespace='basket')),
    re_path(r'^auth/', include('authapp.urls', namespace='auth')),

    re_path(r'^admin/', include('adminapp.urls', namespace='admin')),
    # path('admin-django/', admin.site.urls),
    re_path(r'^', include('social_django.urls', namespace='social')),
    re_path(r'^order/', include('ordersapp.urls', namespace='order')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
