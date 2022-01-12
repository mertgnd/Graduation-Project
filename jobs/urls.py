from django.conf.urls import url
from .views import *

app_name = 'jobs'

urlpatterns = [
    url(r'^addjobs/$', addjobs_view, name='addjobs'),
    url(r'^ilandetay/(?P<pk>[0-9]+)/$', isİlaniDetay, name='ilandetay'),
    url(r'^ilanguncelle/(?P<pk>[0-9]+)/$', isİlaniGuncelle, name='ilanguncelle'),
    url(r'^ilansil/(?P<pk>[0-9]+)/$', isİlaniSil, name='ilansil'),
    url(r'^ilanlarim/$', ilanlarim, name='ilanlarim'),
    url(r'^ilanlar/$', isİlaniGoruntule, name='ilanlar'),
    url(r'^stajekle/$', stajIlaniEkle, name='stajekle'),
    url(r'^stajilanlari/$', stajİlaniGoruntule, name='stajilanlari'),
    url(r'^stajilanidetay/(?P<pk>[0-9]+)/$', stajİlaniDetay, name='stajilanidetay'),
    url(r'^stajilaniguncelle/(?P<pk>[0-9]+)/$', stajİlaniGuncelle, name='stajilaniguncelle'),
    url(r'^stajilanisil/(?P<pk>[0-9]+)/$', stajİlaniSil, name='stajilanisil'),
]