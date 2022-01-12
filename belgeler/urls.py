from django.conf.urls import url
from .views import *

app_name= 'belgeler'

urlpatterns = [
    url(r'^transkriptTalep/$', transkriptTalep, name='transkriptTalep'),
    url(r'^transkriptIstek/$', traskriptIstekleri, name='transkriptIstek'),
    url(r'^transkriptIstekleriDetay/(?P<pk>[0-9]+)/(?P<istek>[0-9]+)/$', transkriptIstekleriDetay, name='transkriptIstekleriDetay'),

]