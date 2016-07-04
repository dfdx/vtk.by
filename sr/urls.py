from django.conf.urls import url

from . import views

app_name = 'sr'
urlpatterns = [
    url(r'^$', views.info, name='sr-info'),
    url(r'^info/$', views.info, name='sr-info'),
]
