from django.contrib import admin
from randevu.models import randevuMezun,randevuOgrenci,MesajRandevuMezun,MesajRandevuOgrenci

# Register your models here.

admin.site.register(randevuMezun)
admin.site.register(randevuOgrenci)
admin.site.register(MesajRandevuMezun)
admin.site.register(MesajRandevuOgrenci)