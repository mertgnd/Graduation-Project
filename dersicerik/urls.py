from django.conf.urls import url
from .views import *

app_name= 'dersicerik'

urlpatterns = [
    url(r'^dersicerikTalep/$', dersicerikTalep, name='dersicerikTalep'),
    url(r'^dersicerikIstek/$', dersicerikIstekleri, name='dersicerikIstek'),
    url(r'^dersicerikIstekleriDetay/(?P<pk>[0-9]+)/(?P<istek>[0-9]+)/$', dersicerikIstekleriDetay, name='dersicerikIstekleriDetay'),

]