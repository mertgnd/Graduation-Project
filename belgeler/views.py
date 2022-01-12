from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .forms import TranskriptTalepFormuMezun, TranskriptTalepFormuOgrenci, MesajMezunForm, MesajOgrenciForm
from .models import TranskriptOgrenci, TranskriptMezun, MesajMezun, MesajOgrenci
from accounts.models import BolumSekreteri, Ogrenci, Mezun
from django.contrib.auth.models import Group


def transkriptTalep(request):
    tarih = datetime.datetime.now(tz=timezone.utc)
    if request.method == "POST":
        for g in request.user.groups.all():
            if g.name == 'Mezun':
                formMezun = TranskriptTalepFormuMezun(request.POST)
                if formMezun.is_valid():
                    veriler = formMezun.save(commit=False)
                    veriler.istekTarihi = timezone.now()
                    veriler.ad = request.POST.get('ad')
                    veriler.soyad = request.POST.get('soyad')
                    veriler.tc = int(request.POST.get('tc'))
                    if request.POST.get('ogrenciNo') != "":
                        veriler.ogrenciNo = int(request.POST.get('ogrenciNo'))
                    veriler.mezunYili = int(request.POST.get('mezunYili'))
                    veriler.telefon = request.POST.get('telefon')
                    veriler.adres = request.POST.get('adres')
                    veriler.mail = request.user.email
                    veriler.save()
                    return redirect('belgeler:transkriptIstek')
                else:
                    return render(request, 'belgeler/transkript.html',{'tarih': tarih, 'formMezun': formMezun})

            elif g.name == 'Öğrenci':
                formOgrenci = TranskriptTalepFormuOgrenci(request.POST)
                if formOgrenci.is_valid():
                    veriler = formOgrenci.save(commit=False)
                    veriler.istekTarihi = timezone.now()
                    veriler.ad = request.POST.get('ad')
                    veriler.soyad = request.POST.get('soyad')
                    veriler.tc = int(request.POST.get('tc'))
                    if request.POST.get('ogrenciNo') != "":
                        veriler.ogrenciNo = int(request.POST.get('ogrenciNo'))
                    veriler.telefon = request.POST.get('telefon')
                    veriler.adres = request.POST.get('adres')
                    veriler.mail = request.user.email
                    veriler.save()
                    return redirect('belgeler:transkriptIstek')
                else:
                    return render(request, 'belgeler/transkript.html', {'tarih': tarih, 'formOgrenci': formOgrenci})
    else:
        for g in request.user.groups.all():
            if g.name == 'Mezun':
                formMezun = TranskriptTalepFormuMezun(request.POST)
                return render(request, 'belgeler/transkript.html',{'tarih': tarih, 'formMezun': formMezun})
            if g.name == 'Öğrenci':
                formOgrenci = TranskriptTalepFormuOgrenci(request.POST)
                return render(request, 'belgeler/transkript.html', {'tarih': tarih, 'formOgrenci':formOgrenci})

def traskriptIstekleri(request):
    for g in request.user.groups.all():
        if g.name == 'Mezun':
            mezunIstekleri = TranskriptMezun.objects.filter(mail=request.user.email)
            return render(request, 'belgeler/transkriptIstekleri.html', {'mezunIstekleri': mezunIstekleri})
        if g.name == 'Öğrenci':
            ogrenciIstekleri = TranskriptOgrenci.objects.filter(mail=request.user.email)
            return render(request, 'belgeler/transkriptIstekleri.html', {'ogrenciIstekleri': ogrenciIstekleri})
        if g.name == 'Bölüm Sekreteri':
            ogrenciIstekleri = TranskriptOgrenci.objects.all()
            mezunIstekleri = TranskriptMezun.objects.all()
            sekreter = BolumSekreteri.objects.get(user=request.user)
            sekreter.oncekiGirisTranskript = datetime.datetime.now(tz=timezone.utc)
            sekreter.gorulenTranskript = 0
            sekreter.save()
            return render(request, 'belgeler/transkriptIstekleri.html', {'ogrenciIstekleri': ogrenciIstekleri, 'mezunIstekleri': mezunIstekleri, 'sekreter': sekreter})




def transkriptIstekleriDetay(request, pk, istek):
    for g in request.user.groups.all():
        if g.name == 'Mezun' and istek == "1":
            mezunIstekleri = TranskriptMezun.objects.get(pk=pk)
            form = MesajMezunForm(request.POST or None, request.FILES or None)
            tarih = datetime.datetime.now(tz=timezone.utc)
            mezun = Mezun.objects.get(user=request.user)
            mezun.oncekiGirisTranskript = datetime.datetime.now(tz=timezone.utc)
            mezun.gorulenTranskript = 0
            mezun.save()
            if form.is_valid():
                mesaj = form.save(commit=False)
                mesaj.transkript = mezunIstekleri
                mesaj.ad = request.user.get_full_name()
                mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                mesaj.save()
                return redirect('belgeler:transkriptIstekleriDetay', mezunIstekleri.pk, 1)
            return render(request, 'belgeler/transkriptIstekleriDetay.html', {'mezunIstekleri' :mezunIstekleri, 'form': form, 'tarih': tarih})

        if g.name == 'Öğrenci' and istek == "0":
            ogrenciIstekleri = TranskriptOgrenci.objects.get(pk=pk)
            form = MesajOgrenciForm(request.POST or None, request.FILES or None)
            tarih = datetime.datetime.now(tz=timezone.utc)
            ogrenci = Ogrenci.objects.get(user=request.user)
            ogrenci.oncekiGirisTranskript = datetime.datetime.now(tz=timezone.utc)
            ogrenci.gorulenTranskript = 0
            ogrenci.save()
            if form.is_valid():
                mesaj = form.save(commit=False)
                mesaj.transkript = ogrenciIstekleri
                mesaj.ad = request.user.get_full_name()
                mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                mesaj.save()
                return redirect('belgeler:transkriptIstekleriDetay', ogrenciIstekleri.pk, 0)
            return render(request, 'belgeler/transkriptIstekleriDetay.html', {'ogrenciIstekleri' :ogrenciIstekleri, 'form': form, 'tarih': tarih})

        if g.name == 'Bölüm Sekreteri':
            if istek == "0":
                ogrenciIstekleri = TranskriptOgrenci.objects.get(pk=pk)
                form = MesajOgrenciForm(request.POST or None, request.FILES or None)
                tarih = datetime.datetime.now(tz=timezone.utc)
                sekreter = BolumSekreteri.objects.get(user=request.user)
                sekreter.oncekiGirisTranskriptOgrenci = datetime.datetime.now(tz=timezone.utc)
                sekreter.gorulenTranskriptOgrenci = 0
                sekreter.save()

                if form.is_valid():
                    mesaj = form.save(commit=False)
                    mesaj.transkript = ogrenciIstekleri
                    mesaj.ad = request.user.get_full_name()
                    if request.FILES.get('transkriptler') != None:
                        mesaj.belge = request.FILES.get('transkriptler')
                        ogrenciIstekleri.teslimTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.save()
                    return redirect('belgeler:transkriptIstekleriDetay', ogrenciIstekleri.pk, 0)
                return render(request, 'belgeler/transkriptIstekleriDetay.html', {'ogrenciIstekleri' :ogrenciIstekleri, 'form': form, 'tarih': tarih, 'istek': istek})

            elif istek == "1":
                mezunIstekleri = TranskriptMezun.objects.get(pk=pk)
                form = MesajMezunForm(request.POST or None, request.FILES or None)
                tarih = datetime.datetime.now(tz=timezone.utc)
                sekreter = BolumSekreteri.objects.get(user=request.user)
                sekreter.oncekiGirisTranskriptMezun = datetime.datetime.now(tz=timezone.utc)
                sekreter.gorulenTranskriptMezun = 0
                sekreter.save()
                if form.is_valid():
                    mesaj = form.save(commit=False)
                    mesaj.transkript = mezunIstekleri
                    mesaj.ad = request.user.get_full_name()
                    if request.FILES.get('transkriptler') != None:
                        mesaj.belge = request.FILES.get('transkriptler')
                        mezunIstekleri.teslimTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.save()
                    return redirect('belgeler:transkriptIstekleriDetay', mezunIstekleri.pk, 1)
                return render(request, 'belgeler/transkriptIstekleriDetay.html', {'mezunIstekleri': mezunIstekleri, 'form': form, 'tarih': tarih, 'istek': istek})
            return render(request, 'belgeler/transkriptIstekleriDetay.html')
