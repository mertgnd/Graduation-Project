from django import forms
from .models import IsIlaniEkle, stajIlani

class IsIlaniEkleForm(forms.ModelForm):
    class Meta:
        model = IsIlaniEkle
        fields = ['isOzeti', 'firma', 'konum', 'isTanimi', 'nitelikler', 'sektor', 'pozisyon',
        'pozisyonSeviyesi', 'calismaSekli', 'adres', 'basvuruSekli']

class StajIlaniForm(forms.ModelForm):
    class Meta:
        model = stajIlani
        fields = ['stajBaslik', 'stajFirma', 'stajKonum', 'stajBilgilendirme', 'stajAdres']
