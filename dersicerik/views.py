from django.shortcuts import render, redirect
from django.utils import timezone
import datetime
from .forms import dersicerikFormuMezun, MesajdersMezunForm
from .models import DersIcerikMezun, MesajdersMezun
from accounts.models import Mezun, OgretimGorevlisi
from django.contrib.auth.models import Group
from django.contrib import messages


def dersicerikTalep(request):
    tarih = datetime.datetime.now(tz=timezone.utc)
    formMezun = dersicerikFormuMezun(request.POST)
    ogretimGorevlisi = OgretimGorevlisi.objects.all()
    if formMezun.is_valid():
        veriler = formMezun.save(commit=False)
        veriler.istekTarihi = timezone.now()
        veriler.ad = request.POST.get('ad')
        veriler.soyad = request.POST.get('soyad')
        if request.POST.get('ogrenciNo') != "":
            veriler.ogrenciNo = int(request.POST.get('ogrenciNo'))
        veriler.mezunYili = int(request.POST.get('mezunYili'))
        veriler.aciklama = request.POST.get('aciklama')
        veriler.dersAdi = request.POST.get('dersAdi')
        veriler.ogretimGorevlisi = request.POST.get('ogretimGorevlisi')
        veriler.mail = request.user.email
        veriler.save()
        return redirect('dersicerik:dersicerikIstek')
    else:
        return render(request, 'dersicerik/dersicerik.html',{'tarih': tarih, 'formMezun': formMezun, 'ogretimGorevlisi':ogretimGorevlisi})


def dersicerikIstekleri(request):
    for g in request.user.groups.all():
        if g.name == 'Mezun':
            mezunIstekleri = DersIcerikMezun.objects.filter(mail=request.user.email)
            return render(request, 'dersicerik/dersicerikIstekleri.html', {'mezunIstekleri': mezunIstekleri})
        if g.name == 'Öğretim Görevlisi':
            mezunIstekleri = DersIcerikMezun.objects.filter(ogretimGorevlisi=request.user.get_full_name())
            hoca = OgretimGorevlisi.objects.get(user=request.user)
            hoca.save()
            return render(request, 'dersicerik/dersicerikIstekleri.html', {'mezunIstekleri': mezunIstekleri, 'hoca': hoca})




def dersicerikIstekleriDetay(request, pk, istek):
    for g in request.user.groups.all():
        if g.name == 'Mezun' and istek == "1":
            mezunIstekleri = DersIcerikMezun.objects.get(pk=pk)
            form = MesajdersMezunForm(request.POST or None, request.FILES or None)
            tarih = datetime.datetime.now(tz=timezone.utc)
            mezun = Mezun.objects.get(user=request.user)
            mezun.oncekiGirisDersIcerik = datetime.datetime.now(tz=timezone.utc)
            mezun.gorulenDersIcerik = 0
            mezun.save()
            if form.is_valid():
                mesaj = form.save(commit=False)
                mesaj.dersicerik = mezunIstekleri
                mesaj.ad = request.user.get_full_name()
                mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                mesaj.save()
                return redirect('dersicerik:dersicerikIstekleriDetay', mezunIstekleri.pk, 1)
            return render(request, 'dersicerik/dersicerikIstekleriDetay.html', {'mezunIstekleri' :mezunIstekleri, 'form': form, 'tarih': tarih})

        if g.name == 'Öğretim Görevlisi':
            if istek == "1":
                mezunIstekleri = DersIcerikMezun.objects.get(pk=pk)
                form = MesajdersMezunForm(request.POST or None, request.FILES or None)
                tarih = datetime.datetime.now(tz=timezone.utc)
                hoca = OgretimGorevlisi.objects.get(user=request.user)
                hoca.oncekiGirisDersIcerikMezun = datetime.datetime.now(tz=timezone.utc)
                hoca.gorulenDersIcerikMezun = 0
                hoca.save()
                if form.is_valid():
                    mesaj = form.save(commit=False)
                    mesaj.dersicerik = mezunIstekleri
                    mesaj.ad = request.user.get_full_name()
                    if request.FILES.get('dersicerikleri') != None:
                        mesaj.belge = request.FILES.get('dersicerikleri')
                        mezunIstekleri.teslimTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.save()
                    return redirect('dersicerik:dersicerikIstekleriDetay', mezunIstekleri.pk, 1)
                return render(request, 'dersicerik/dersicerikIstekleriDetay.html', {'mezunIstekleri': mezunIstekleri, 'form': form, 'tarih': tarih, 'istek': istek})
            return render(request, 'dersicerik/dersicerikIstekleriDetay.html')
