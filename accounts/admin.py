from django.contrib import admin
from .models import Mezun, Ogrenci, BolumSekreteri, OgretimGorevlisi

admin.site.register(Mezun)
admin.site.register(Ogrenci)
admin.site.register(BolumSekreteri)
admin.site.register(OgretimGorevlisi)
