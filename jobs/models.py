from django.db import models

class IsIlaniEkle(models.Model):
    isOzeti = models.CharField(max_length=250, null=False, blank=False)
    firma = models.CharField(max_length=250, null=False, blank=False)
    konum = models.CharField(max_length=250, null=False, blank=False)
    ilanTarihi = models.DateTimeField()
    isTanimi = models.TextField(null=False, blank=False)
    nitelikler = models.TextField(null=False, blank=False)
    sektor = models.CharField(max_length=250, null=False, blank=False)
    pozisyon = models.CharField(max_length=250, null=False, blank=False)
    pozisyonSeviyesi = models.CharField(max_length=250, null=False, blank=False)
    calismaSekli = models.CharField(max_length=250, null=False, blank=False)
    adres = models.TextField(null=False, blank=False)
    basvuruSekli = models.CharField(max_length=250, null=False, blank=False)
    sonBasvuruTarihi = models.DateField()
    ilanSahibi = models.CharField(max_length=250)
    ilanSahibiMail = models.EmailField()
    class Meta:
        ordering = ["-ilanTarihi"]

    def __str__(self):
        return self.isOzeti


class stajIlani(models.Model):
    stajBaslik = models.CharField(max_length=250, null=False, blank=False)
    stajFirma = models.CharField(max_length=250, null=False, blank=False)
    stajKonum = models.CharField(max_length=250, null=False, blank=False)
    stajIlanTarihi = models.DateTimeField()
    stajBilgilendirme = models.TextField(null=False, blank=False)
    stajAdres = models.TextField(null=False, blank=False)
    stajSonBasvuruTarihi = models.DateField()
    stajIlanSahibi = models.CharField(max_length=250)
    stajIlanSahibiMail = models.EmailField()
    class Meta:
        ordering = ["-stajIlanTarihi"]

    def __str__(self):
        return self.stajBaslik
