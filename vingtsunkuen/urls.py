"""vingtsunkuen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
import vt.views as vtviews

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^uploadimage$', views.upload_image, name='uploadimage'),
    url(r'^photogallery$', views.photo_gallery, name='photogallery'),
    url(r'^vt/', include('vt.urls')),
    url(r'^sr/', include('sr.urls')),
    url(r'^admin/', admin.site.urls),
]
