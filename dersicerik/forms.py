from django import forms
from .models import DersIcerikMezun, MesajdersMezun



class dersicerikFormuMezun(forms.ModelForm):
    class Meta:
        model = DersIcerikMezun
        fields = ['ad', 'soyad', 'dersAdi', 'aciklama' ]

class MesajdersMezunForm(forms.ModelForm):
    class Meta:
        model = MesajdersMezun
        fields = ['mesaj']
