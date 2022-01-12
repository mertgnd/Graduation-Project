from django import forms
from .models import randevuMezun, randevuOgrenci, MesajRandevuMezun, MesajRandevuOgrenci


class RandevuFormMezun(forms.ModelForm):
    class Meta:
        model = randevuMezun
        fields = ['randevuBaslik', 'randevuIcerik', 'randevuTarihi', 'ogretimGorevlisi']


class RandevuFormOgrenci(forms.ModelForm):
    class Meta:
        model = randevuOgrenci
        fields = ['randevuBaslik', 'randevuIcerik', 'randevuTarihi', 'ogretimGorevlisi']

class MesajMezunForm(forms.ModelForm):
    class Meta:
        model = MesajRandevuMezun
        fields = ['mesaj']

class MesajOgrenciForm(forms.ModelForm):
    class Meta:
        model = MesajRandevuOgrenci
        fields = ['mesaj']