from django.conf.urls import url

from . import views

app_name = 'vt'
urlpatterns = [
    url(r'^$', views.index, name='main'),
    url(r'^login$', views.loginpage, name='login'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'^signout$', views.signout, name='signout'),
    url(r'^news$', views.news, name='news'),
    url(r'^address$', views.address, name='address'),
    url(r'^schedule$', views.schedule, name='schedule'),
    url(r'^video$', views.video, name='video'),
    url(r'^events$', views.events, name='events'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^join$', views.join, name='join'),
    url(r'^shinkage$', views.shinkage, name='shinkage'),    
]
