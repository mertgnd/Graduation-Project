from django.conf.urls import url
from .views import *

app_name= 'dersNotu'

urlpatterns = [
    url(r'^notlar/(?P<sinif>[0-9]+)/$', ders_index, name='index'),
    url(r'^(?P<id>\d+)/$', ders_detail, name='detail'),
    url(r'^create$', ders_create, name='create'),
    url(r'^(?P<id>\d+)/update$', ders_update, name='update'),
    url(r'^(?P<id>\d+)/delete$', ders_delete, name='delete'),
]