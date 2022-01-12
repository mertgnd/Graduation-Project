from django.contrib import admin
from .models import TranskriptOgrenci, TranskriptMezun, MesajMezun, MesajOgrenci

admin.site.register(TranskriptOgrenci)
admin.site.register(TranskriptMezun)
admin.site.register(MesajMezun)
admin.site.register(MesajOgrenci)

