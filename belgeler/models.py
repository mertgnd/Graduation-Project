from django.db import models

class TranskriptMezun(models.Model):
    ad = models.CharField(max_length=250, blank=False, null=False)
    soyad = models.CharField(max_length=250, blank=False, null=False)
    tc = models.CharField(max_length=11, blank=False, null=False)
    ogrenciNo = models.IntegerField(blank=True, null=True)
    mezunYili = models.IntegerField(blank=False, null=False)
    telefon = models.CharField(max_length=11, blank=False, null=False)
    adres = models.TextField(max_length=250, blank=False, null=False)
    istekTarihi = models.DateTimeField()
    teslimTarihi = models.DateTimeField(blank = True, null = True)
    mail = models.EmailField()
    class Meta:
        ordering = ["-istekTarihi"]


class TranskriptOgrenci(models.Model):
    ad = models.CharField(max_length=250)
    soyad = models.CharField(max_length=250)
    tc = models.CharField(max_length=11)
    ogrenciNo = models.IntegerField()
    telefon = models.CharField(max_length=11)
    adres = models.TextField(max_length=250)
    istekTarihi = models.DateTimeField()
    teslimTarihi = models.DateTimeField(blank = True , null = True)
    mail = models.EmailField()
    class Meta:
        ordering = ["-istekTarihi"]


class MesajMezun(models.Model):

    transkript = models.ForeignKey('belgeler.TranskriptMezun', related_name='mesajMezun', on_delete=models.CASCADE)
    ad = models.CharField(max_length=200)
    mesaj = models.TextField()
    belge = models.FileField(upload_to = 'belgeler', blank=True, null=True)
    mesajTarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-mesajTarihi"]

class MesajOgrenci(models.Model):

    transkript = models.ForeignKey('belgeler.TranskriptOgrenci', related_name='mesajOgrenci', on_delete=models.CASCADE)
    ad = models.CharField(max_length=200)
    mesaj = models.TextField()
    belge = models.FileField(upload_to = 'belgeler', blank=True, null=True)
    mesajTarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-mesajTarihi"]





