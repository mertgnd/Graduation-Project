from django.db import models

# Create your models here.

class DersIcerikMezun(models.Model):
    ad = models.CharField(max_length=250, blank=False, null=False)
    soyad = models.CharField(max_length=250, blank=False, null=False)
    ogrenciNo = models.IntegerField(blank=True, null=True)
    mezunYili = models.IntegerField(blank=False, null=False)
    dersAdi = models.CharField(max_length=250, blank=False, null=False)
    aciklama = models.TextField(max_length=250, blank=False, null=False)
    istekTarihi = models.DateTimeField()
    teslimTarihi = models.DateTimeField(blank = True, null = True)
    mail = models.EmailField()
    ogretimGorevlisi = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        ordering = ["-istekTarihi"]

class MesajdersMezun(models.Model):

    dersicerik = models.ForeignKey('dersicerik.DersIcerikMezun', related_name='mesajMezun', on_delete=models.CASCADE)
    ad = models.CharField(max_length=200)
    mesaj = models.TextField()
    belge = models.FileField(upload_to='belgeler', blank=True, null=True)
    mesajTarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-mesajTarihi"]