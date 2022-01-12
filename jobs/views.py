from django.shortcuts import render, redirect, get_object_or_404
from .forms import IsIlaniEkleForm, StajIlaniForm
from .models import IsIlaniEkle, stajIlani
from django.utils import timezone
import datetime
from accounts.models import Ogrenci, Mezun, BolumSekreteri, OgretimGorevlisi
from belgeler.models import TranskriptOgrenci, TranskriptMezun, MesajMezun, MesajOgrenci
from randevu.models import randevuMezun,randevuOgrenci,MesajRandevuMezun,MesajRandevuOgrenci
from dersicerik.models import DersIcerikMezun, MesajdersMezun

def addjobs_view(request):
    if request.method == "POST":
        form = IsIlaniEkleForm(request.POST)
        if form.is_valid():
            veri = form.save(commit=False)
            veri.ilanTarihi = timezone.now()
            veri.ilanSahibi = request.user.get_full_name()
            veri.ilanSahibiMail = request.user.email
            veri.sonBasvuruTarihi = request.POST.get('sonBasvuruTarihi')
            veri.save()
        return redirect('jobs:ilanlar')
    else:
        form = IsIlaniEkleForm(request.POST)
    return render(request, 'jobs/addjobs.html', {'form': form})

def isİlaniGoruntule(request):
    ilanlar = IsIlaniEkle.objects.all()
    bugun = datetime.datetime.now(tz=timezone.utc)

    for ilan in ilanlar:
        print(ilan.sonBasvuruTarihi.month)

    for g in request.user.groups.all():
        if g.name == 'Mezun':
            ogrenciGiris = Mezun.objects.get(user=request.user)
            ogrenciGiris.oncekiGirisIs = datetime.datetime.now(tz=timezone.utc)
            ogrenciGiris.gorulenIsId = 0
            ogrenciGiris.ilanToplam = ogrenciGiris.gorulenStajId + 0
            ogrenciGiris.save()
        if g.name == 'Öğrenci':
            ogrenciGiris = Ogrenci.objects.get(user=request.user)
            ogrenciGiris.oncekiGirisIs = datetime.datetime.now(tz=timezone.utc)
            ogrenciGiris.gorulenIsId = 0
            ogrenciGiris.ilanToplam = ogrenciGiris.gorulenStajId + 0
            ogrenciGiris.save()

    if g.name == 'Öğrenci' or g.name == 'Mezun':
        return render(request, 'jobs/isilanlari.html', {'ilanlar': ilanlar, 'ogrenci': ogrenciGiris, 'bugun': bugun})
    else:
        return render(request, 'jobs/isilanlari.html', {'ilanlar': ilanlar, 'bugun': bugun})


def isİlaniDetay(request, pk):
    ilan = IsIlaniEkle.objects.get(pk=pk)
    return render(request, 'jobs/isilanlaridetay.html', {'ilan' :ilan})

def isİlaniGuncelle(request, pk):
    ilan = get_object_or_404(IsIlaniEkle, pk=pk)
    form = IsIlaniEkleForm(instance=ilan, data=request.POST or None)

    if form.is_valid():
        veri = form.save(commit=False)
        if veri.sonBasvuruTarihi == request.POST.get('sonBasvuruTarihi'):
            veri.save()
        else:
            veri.sonBasvuruTarihi = request.POST.get('sonBasvuruTarihi')
            veri.save()

        return redirect('jobs:ilanlarim')
    return render(request, 'jobs/updatejobs.html',{'form': form, 'ilan': ilan})

def isİlaniSil(request, pk):
    ilan = get_object_or_404(IsIlaniEkle, pk=pk)
    ilan.delete()
    return redirect('jobs:ilanlarim')


def ilanlarim(request):
    ilanlar = IsIlaniEkle.objects.filter(ilanSahibiMail=request.user.email)
    stajilanlar = stajIlani.objects.filter(stajIlanSahibiMail=request.user.email)

    return render(request, 'jobs/ilanlarim.html', {'ilanlar': ilanlar, 'stajilanlar': stajilanlar})


def stajIlaniEkle(request):
    if request.method == "POST":
        form = StajIlaniForm(request.POST)
        if form.is_valid():
            veri = form.save(commit=False)
            veri.stajIlanTarihi = datetime.datetime.now(tz=timezone.utc)
            veri.stajIlanSahibi = request.user.get_full_name()
            veri.stajIlanSahibiMail = request.user.email
            veri.stajSonBasvuruTarihi = request.POST.get('sonBasvuruTarihi')
            veri.save()
        return redirect('jobs:stajilanlari')
    else:
        form = StajIlaniForm(request.POST)
    return render(request, 'jobs/stajekle.html', {'form': form})

def stajİlaniGoruntule(request):
    ilanlar = stajIlani.objects.all()
    for g in request.user.groups.all():
        if g.name == 'Mezun':
            ogrenciGiris = Mezun.objects.get(user=request.user)
            ogrenciGiris.oncekiGirisStaj = datetime.datetime.now(tz=timezone.utc)
            ogrenciGiris.gorulenStajId = 0
            ogrenciGiris.ilanToplam = ogrenciGiris.gorulenIsId + 0
            ogrenciGiris.save()
        if g.name == 'Öğrenci':
            ogrenciGiris = Ogrenci.objects.get(user=request.user)
            ogrenciGiris.oncekiGirisStaj = datetime.datetime.now(tz=timezone.utc)
            ogrenciGiris.gorulenStajId = 0
            ogrenciGiris.ilanToplam = ogrenciGiris.gorulenIsId + 0
            ogrenciGiris.save()
        else:
            return render(request, 'jobs/stajilanlari.html', {'ilanlar': ilanlar})

    if g.name == 'Öğrenci' or g.name == 'Mezun':
        return render(request, 'jobs/stajilanlari.html', {'ilanlar': ilanlar, 'ogrenci': ogrenciGiris})
    else:
        return render(request, 'jobs/stajilanlari.html', {'ilanlar': ilanlar})

def stajİlaniDetay(request, pk):
    ilan = stajIlani.objects.get(pk=pk)
    return render(request, 'jobs/stajilanlaridetay.html', {'ilan' :ilan})

def stajİlaniGuncelle(request, pk):
    ilan = get_object_or_404(stajIlani, pk=pk)
    form = StajIlaniForm(instance=ilan, data=request.POST or None)

    if form.is_valid():
        veri = form.save(commit=False)
        if veri.stajSonBasvuruTarihi == request.POST.get('sonBasvuruTarihi'):
            veri.save()
        else:
            veri.stajSonBasvuruTarihi = request.POST.get('sonBasvuruTarihi')
            veri.save()

        return redirect('jobs:ilanlarim')
    return render(request, 'jobs/updatestajs.html',{'form': form, 'ilan': ilan})

def stajİlaniSil(request, pk):
    ilan = get_object_or_404(stajIlani, pk=pk)
    ilan.delete()
    return redirect('jobs:ilanlarim')

def bildirimIcin(request):
    global dersicerikMezun
    ilanlarIs = IsIlaniEkle.objects.all()
    ilanlarStaj = stajIlani.objects.all()
    for g in request.user.groups.all():
        if g.name == 'Mezun':
            ogrenci = Mezun.objects.get(user=request.user)
            transkriptler = TranskriptMezun.objects.filter(mail=request.user.email)
            randevular = randevuMezun.objects.filter(mail=request.user.email)
            dersicerikler = DersIcerikMezun.objects.filter(mail=request.user.email)
            ogrenci.gorulenStajId = 0
            ogrenci.gorulenIsId = 0
            ogrenci.gorulenTranskript = 0
            ogrenci.gorulenRandevu = 0
            ogrenci.gorulenDersIcerik = 0
            ogrenci.save()
            for stajIlan in ilanlarStaj:
                if stajIlan.stajIlanTarihi > ogrenci.oncekiGirisStaj:
                    ogrenci.gorulenStajId += 1
                    ogrenci.save()
            for isIlan in ilanlarIs:
                if isIlan.ilanTarihi > ogrenci.oncekiGirisIs:
                    ogrenci.gorulenIsId += 1
                    ogrenci.save()
            for transkript in transkriptler:
                for mezunMesaj in MesajMezun.objects.filter(transkript=transkript):
                    if mezunMesaj.mesajTarihi > ogrenci.oncekiGirisTranskript:
                        ogrenci.gorulenTranskript += 1
                        ogrenci.save()
            for randevu in randevular:
                for mezunMesaj in MesajRandevuMezun.objects.filter(randevu=randevu):
                    if mezunMesaj.mesajTarihi > ogrenci.oncekiGirisRandevu:
                        ogrenci.gorulenRandevu += 1
                        ogrenci.save()
            for dersIcerik in dersicerikler:
                for mezunMesaj in MesajdersMezun.objects.filter(dersicerik = dersIcerik):
                    if mezunMesaj.mesajTarihi > ogrenci.oncekiGirisDersIcerik:
                        ogrenci.gorulenDersIcerik += 1
                        ogrenci.save()
            ogrenci.ilanToplam = ogrenci.gorulenIsId + ogrenci.gorulenStajId
            ogrenci.save()
        if g.name == 'Öğrenci':
            ogrenci = Ogrenci.objects.get(user=request.user)
            transkriptler = TranskriptOgrenci.objects.filter(mail=request.user.email)
            randevular = randevuOgrenci.objects.filter(mail=request.user.email)
            ogrenci.gorulenStajId = 0
            ogrenci.gorulenIsId = 0
            ogrenci.gorulenTranskript = 0
            ogrenci.gorulenRandevu = 0
            ogrenci.save()
            for stajIlan in ilanlarStaj:
                if stajIlan.stajIlanTarihi > ogrenci.oncekiGirisStaj:
                    ogrenci.gorulenStajId += 1
                    ogrenci.save()
            for isIlan in ilanlarIs:
                if isIlan.ilanTarihi > ogrenci.oncekiGirisIs:
                    ogrenci.gorulenIsId += 1
                    ogrenci.save()
            for transkript in transkriptler:
                for ogrenciMesaj in MesajOgrenci.objects.filter(transkript=transkript):
                    if ogrenciMesaj.mesajTarihi > ogrenci.oncekiGirisTranskript:
                        ogrenci.gorulenTranskript += 1
                        ogrenci.save()
            for randevu in randevular:
                for ogrenciMesaj in MesajRandevuOgrenci.objects.filter(randevu=randevu):
                    if ogrenciMesaj.mesajTarihi > ogrenci.oncekiGirisRandevu:
                        ogrenci.gorulenRandevu += 1
                        ogrenci.save()
            ogrenci.ilanToplam = ogrenci.gorulenIsId + ogrenci.gorulenStajId
            ogrenci.save()
        if g.name == 'Bölüm Sekreteri':
            sekreter = BolumSekreteri.objects.get(user=request.user)
            ogrenciTranskriptler = TranskriptOgrenci.objects.all()
            mezunTranskriptler = TranskriptMezun.objects.all()
            sekreter.gorulenTranskriptMezun = 0
            sekreter.gorulenTranskriptOgrenci = 0
            sekreter.save()
            for ogrenciTranskript in ogrenciTranskriptler:
                for ogrenciMesaj in MesajOgrenci.objects.filter(transkript=ogrenciTranskript):
                    if ogrenciMesaj.mesajTarihi > sekreter.oncekiGirisTranskriptOgrenci:
                        sekreter.gorulenTranskriptOgrenci += 1
                        sekreter.save()
                if ogrenciTranskript.istekTarihi > sekreter.oncekiGirisTranskriptOgrenci:
                        sekreter.gorulenTranskriptOgrenci += 1
                        sekreter.save()
            for mezunTranskript in mezunTranskriptler:
                for mezunMesaj in MesajMezun.objects.filter(transkript=mezunTranskript):
                    if mezunMesaj.mesajTarihi > sekreter.oncekiGirisTranskriptMezun:
                        sekreter.gorulenTranskriptMezun += 1
                        sekreter.save()
                if mezunTranskript.istekTarihi > sekreter.oncekiGirisTranskriptMezun:
                        sekreter.gorulenTranskriptMezun += 1
                        sekreter.save()
            sekreter.gorulenTranskript = sekreter.gorulenTranskriptOgrenci + sekreter.gorulenTranskriptMezun
            sekreter.save()
        if g.name == 'Öğretim Görevlisi':
            hoca = OgretimGorevlisi.objects.get(user= request.user)
            ogrenciRandevular = randevuOgrenci.objects.all()
            mezunRandevular = randevuMezun.objects.all()
            mezunDersIcerikler = DersIcerikMezun.objects.all()
            hoca.gorulenRandevuMezun = 0
            hoca.gorulenRandevuOgrenci = 0
            hoca.gorulenDersIcerikMezun = 0
            hoca.save()
            for ogrenciRandevu in ogrenciRandevular:
                for ogrenciMesaj in MesajRandevuOgrenci.objects.filter(randevu=ogrenciRandevu):
                    if ogrenciMesaj.mesajTarihi > hoca.oncekiGirisRandevuOgrenci:
                        hoca.gorulenRandevuOgrenci += 1
                        hoca.save()
                if ogrenciRandevu.randevuTalepTarihi > hoca.oncekiGirisRandevuOgrenci:
                    hoca.gorulenRandevuOgrenci += 1
                    hoca.save()
            for mezunRandevu in mezunRandevular:
                for ogrenciMesaj in MesajRandevuMezun.objects.filter(randevu=mezunRandevu):
                    if ogrenciMesaj.mesajTarihi > hoca.oncekiGirisRandevuMezun:
                        hoca.gorulenRandevuMezun += 1
                        hoca.save()
                if mezunRandevu.randevuTalepTarihi > hoca.oncekiGirisRandevuMezun:
                    hoca.gorulenRandevuMezun += 1
                    hoca.save()
            hoca.gorulenRandevu = hoca.gorulenRandevuOgrenci + hoca.gorulenRandevuMezun
            hoca.save()
            for dersicerikMezun in mezunDersIcerikler:
                for ogrenciMesajDers in MesajdersMezun.objects.filter(dersicerik=dersicerikMezun):
                    if ogrenciMesajDers.mesajTarihi > hoca.oncekiGirisDersIcerikMezun:
                        hoca.gorulenDersIcerikMezun += 1
                        hoca.save()
                if dersicerikMezun.istekTarihi > hoca.oncekiGirisDersIcerikMezun:
                    hoca.gorulenDersIcerikMezun += 1
                    hoca.save()
        if g.name == 'Öğrenci' or g.name == 'Mezun':
            return render(request, 'anasayfa.html', {'ilanlarIs': ilanlarIs, 'ilanlarStaj': ilanlarStaj, 'ogrenci': ogrenci})
        if g.name == 'Bölüm Sekreteri':
            return render(request, 'anasayfa.html', {'sekreter': sekreter})
        if g.name == 'Öğretim Görevlisi':
            return render(request, 'anasayfa.html', {'hoca':hoca})
    return render(request, 'anasayfa.html', {'ilanlarIs': ilanlarIs, 'ilanlarStaj': ilanlarStaj})


