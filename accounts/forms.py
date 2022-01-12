from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Mezun, User, Ogrenci, BolumSekreteri, OgretimGorevlisi

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email')

class MezunForm(forms.ModelForm):
    class Meta:
        model = Mezun
        fields = ['birth_date', 'telefonNumarasi', 'cinsiyet', 'sehir',
                  'adres', 'ogrenimDurumu', 'mezuniyetYili']

class OgrenciForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['ogrenciNo', 'birth_date', 'telefonNumarasi', 'cinsiyet', 'sehir',
                  'adres', 'ogrenimDurumu']

class BolumSekreteriForm(forms.ModelForm):
    class Meta:
        model = BolumSekreteri
        fields = []

class OgretimGorevlisiForm(forms.ModelForm):
    class Meta:
        model = OgretimGorevlisi
        fields = []

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class MezunUpdateForm(forms.ModelForm):
    class Meta:
        model = model = Mezun
        fields = ['birth_date', 'telefonNumarasi', 'cinsiyet', 'sehir',
                  'adres', 'mezuniyetYili', 'calismaDurumu', 'maas', 'sektor', 'unvanMeslek', 'idariGorev', 'sirketKurumAdi',
                  'iseBaslamaTarihi', 'isAdresi', 'il']

class OgrenciUpdateForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['ogrenciNo', 'birth_date', 'telefonNumarasi', 'cinsiyet', 'sehir',
                  'adres']

