from django.conf.urls import url

from . import views

app_name = 'vt'
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^address$', views.address, name='address'),
    url(r'^video$', views.video, name='video'),
    url(r'^events$', views.events, name='events'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^join$', views.join, name='join'),
    url(r'^shinkage$', views.shinkage, name='shinkage'),    
]
