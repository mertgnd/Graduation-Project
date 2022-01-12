from django.db import models
from django.urls import reverse

# Create your models here.
class Ders(models.Model):
    published_time = models.DateField(auto_now_add=True)
    Ders = models.CharField(max_length=120, default='', verbose_name='Ders')
    Not = models.TextField (default='', verbose_name='Not')
    Sınıf = models.CharField(max_length=120, default='', verbose_name='Sınıf')
    Yükleyen = models.CharField(max_length=150, default='', verbose_name='Yükleyen')
    pdf = models.FileField(blank=True, null=True)
    yukleyenId = models.EmailField()

    def __str__(self):
        return self.Ders

    def get_absolute_url(self):
        return reverse('dersNotu:detail', kwargs={'id': self.id})

    def get_create_url(self):
        return reverse('dersNotu:create')

    def get_update_url(self):
        return reverse('dersNotu:update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('dersNotu:delete', kwargs={'id': self.id})

    class Meta:
        ordering = ['-published_time', 'id']