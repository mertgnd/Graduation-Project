from django.db import models


class randevuOgrenci(models.Model):
    randevuBaslik = models.CharField(max_length=100, null=False, verbose_name='Randevu Sebebi', blank=False)
    randevuIcerik = models.TextField(null=False, blank=False, verbose_name='Randevu İçeriği')
    randevuTarihi = models.DateField(null=False, blank=False)
    randevuTalepTarihi = models.DateTimeField(verbose_name='Randevunun Oluşturulma Tarihi', auto_now_add=True)
    randevuSender = models.CharField(max_length=250)
    mail = models.EmailField()
    ogretimGorevlisi = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        ordering = ["-randevuTalepTarihi"]

    def __str__(self):
        return self.randevuBaslik


class randevuMezun(models.Model):
    randevuBaslik = models.CharField(max_length=100, null=False, verbose_name='Randevu Sebebi', blank=False)
    randevuIcerik = models.TextField(null=False, blank=False, verbose_name='Randevu İçeriği')
    randevuTarihi = models.DateField(null=False, blank=False)
    randevuTalepTarihi = models.DateTimeField(verbose_name='Randevunun Oluşturulma Tarihi', auto_now_add=True)
    randevuSender = models.CharField(max_length=250)
    mail = models.EmailField()
    ogretimGorevlisi = models.CharField(max_length=100, null=False, blank=False)
    class Meta:
        ordering = ["-randevuTalepTarihi"]

    def __str__(self):
        return self.randevuBaslik


class MesajRandevuMezun(models.Model):

    randevu = models.ForeignKey('randevu.randevuMezun', related_name='mesajMezun', on_delete=models.CASCADE, null = True)
    ad = models.CharField(max_length=200)
    mesaj = models.TextField()
    belge = models.FileField(upload_to = 'belgeler' ,blank = True, null = True)
    mesajTarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-mesajTarihi"]

class MesajRandevuOgrenci(models.Model):

    randevu = models.ForeignKey('randevu.randevuOgrenci', related_name='mesajOgrenci', on_delete=models.CASCADE, null = True)
    ad = models.CharField(max_length=200)
    mesaj = models.TextField()
    belge = models.FileField(upload_to = 'belgeler', blank = True, null = True)
    mesajTarihi = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ["-mesajTarihi"]