from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
import datetime

class Mezun(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ogrenimDurumu = models.CharField(max_length=7, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    telefonNumarasi = models.CharField(max_length=120, null=True, blank=True, unique =True)
    cinsiyet = models.CharField(max_length=7, null=True, blank=True)
    sehir = models.CharField(max_length=255, null=True, blank=True)
    adres = models.CharField(max_length=300, null=True, blank=True)
    mezuniyetYili = models.CharField(max_length=4, null=True, blank=True)
    calismaDurumu = models.CharField(max_length=12, null=True, blank=True)
    maas = models.CharField(max_length=7, null=True, blank=True)
    sektor = models.CharField(max_length=120, null=True, blank=True)
    unvanMeslek = models.CharField(max_length=120, null=True, blank=True)
    idariGorev = models.CharField(max_length=120, null=True, blank=True)
    sirketKurumAdi = models.CharField(max_length=120, null=True, blank=True)
    iseBaslamaTarihi = models.DateField(null=True, blank=True)
    il = models.CharField(max_length=255, null=True, blank=True)
    isAdresi = models.CharField(max_length=255, null=True, blank=True)
    gorulenStajId = models.IntegerField(default=0)
    gorulenIsId = models.IntegerField(default=0)
    ilanToplam = models.IntegerField(default=0)
    oncekiGirisStaj = models.DateTimeField(auto_now_add=True)
    oncekiGirisIs = models.DateTimeField(auto_now_add=True)
    gorulenTranskript = models.IntegerField(default=0)
    oncekiGirisTranskript = models.DateTimeField(auto_now_add=True)

    oncekiGirisDersIcerik = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    gorulenDersIcerik = models.IntegerField(default=0)

    gorulenRandevu = models.IntegerField(default=0)
    oncekiGirisRandevu = models.DateTimeField(auto_now_add=True , null = True , blank = True)



    def __str__(self):
        return self.user.username

class Ogrenci(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ogrenimDurumu = models.CharField(max_length=7, null=False, blank=False)
    ogrenciNo = models.IntegerField(null=False, blank=False,unique=True)
    birth_date = models.DateField(null=False, blank=False)
    telefonNumarasi = models.CharField(max_length=120, null=False, blank=False)
    cinsiyet = models.CharField(max_length=7, null=False, blank=False)
    sehir = models.CharField(max_length=255, null=False, blank=False)
    adres = models.CharField(max_length=300, null=False, blank=False)
    gorulenStajId = models.IntegerField(default=0)
    gorulenIsId = models.IntegerField(default=0)
    ilanToplam = models.IntegerField(default=0)
    oncekiGirisStaj = models.DateTimeField(auto_now_add=True)
    oncekiGirisIs = models.DateTimeField(auto_now_add=True)
    gorulenTranskript = models.IntegerField(default=0)
    oncekiGirisTranskript = models.DateTimeField(auto_now_add=True)

    oncekiGirisDersIcerik = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    gorulenDersIcerik = models.IntegerField(default=0)

    gorulenRandevu = models.IntegerField(default=0)
    oncekiGirisRandevu = models.DateTimeField(auto_now_add=True , null = True , blank = True)


    def __str__(self):
        return self.user.username

class BolumSekreteri(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gorulenTranskriptOgrenci = models.IntegerField(default=0)
    gorulenTranskriptMezun = models.IntegerField(default=0)
    gorulenTranskript = models.IntegerField(default=0)
    oncekiGirisTranskriptOgrenci = models.DateTimeField(auto_now_add=True)
    oncekiGirisTranskriptMezun = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class OgretimGorevlisi(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    gorulenRandevu = models.IntegerField(default = 0)
    gorulenRandevuOgrenci = models.IntegerField(default = 0)
    gorulenRandevuMezun = models.IntegerField(default = 0)
    oncekiGirisRandevuOgrenci = models.DateTimeField(auto_now_add=True , null = True , blank = True)
    oncekiGirisRandevuMezun = models.DateTimeField(auto_now_add=True , null = True , blank = True)

    gorulenDersIcerik = models.IntegerField(default = 0)
    gorulenDersIcerikOgrenci = models.IntegerField(default = 0)
    gorulenDersIcerikMezun = models.IntegerField(default = 0)
    oncekiGirisDersIcerikMezun = models.DateTimeField(auto_now_add=True, null = True , blank = True)
    oncekiGirisDersIcerikOgrenci = models.DateTimeField(auto_now_add=True, null=True, blank = True)

    def __str__(self):
        return self.user.username