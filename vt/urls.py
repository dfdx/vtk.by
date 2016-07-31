from django.conf.urls import url

from . import views

app_name = 'vt'
urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^news$', views.news, name='news'),
    url(r'^address$', views.address, name='address'),
    url(r'^schedule$', views.schedule, name='schedule'),
    url(r'^video$', views.video, name='video'),
    url(r'^events$', views.events, name='events'),
    url(r'^contacts$', views.contacts, name='contacts'),
    url(r'^testpage$', views.testpage, name='testpage'),
    url(r'^editpage$', views.editpage, name='editpage'),
    url(r'^savepage$', views.savepage, name='savepage'),
    url(r'^', views.viewpage, name='viewpage'),
]
