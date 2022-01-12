from django import forms
from .models import TranskriptMezun, TranskriptOgrenci, MesajMezun, MesajOgrenci

class TranskriptTalepFormuMezun(forms.ModelForm):
    class Meta:
        model = TranskriptMezun
        fields = ['ad', 'soyad', 'tc', 'mezunYili', 'telefon', 'adres' ]

class TranskriptTalepFormuOgrenci(forms.ModelForm):
    class Meta:
        model = TranskriptOgrenci
        fields = ['ad', 'soyad', 'tc', 'telefon', 'adres' ]

class MesajMezunForm(forms.ModelForm):
    class Meta:
        model = MesajMezun
        fields = ['mesaj']

class MesajOgrenciForm(forms.ModelForm):
    class Meta:
        model = MesajOgrenci
        fields = ['mesaj']


