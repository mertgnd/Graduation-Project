from django.conf.urls import url

from .views import randevu_create, randevu_list, randevuIstekleriDetay

app_name = 'randevu'

urlpatterns = [

    url(r'^list/', view=randevu_list, name='list'),
    url(r'^create/', view=randevu_create, name='create'),
    url(r'^detay/(?P<id>[0-9]+)/(?P<istek>[0-9]+)/$', randevuIstekleriDetay, name='detay'),
]