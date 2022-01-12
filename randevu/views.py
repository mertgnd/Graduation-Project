from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from django.utils import timezone
import datetime
from .forms import RandevuFormMezun, RandevuFormOgrenci, MesajOgrenciForm,MesajMezunForm
from .models import randevuMezun, randevuOgrenci, MesajRandevuOgrenci, MesajRandevuMezun
from django.utils import timezone
from accounts.models import Ogrenci, Mezun, OgretimGorevlisi


def randevu_create(request):
    tarih = datetime.datetime.now(tz=timezone.utc)
    if request.method == "POST":
        for grup in request.user.groups.all():
            if grup.name == 'Öğrenci':
                form = RandevuFormOgrenci(request.POST)
                if form.is_valid():
                    veri = form.save(commit=False)
                    veri.randevuSender = request.user.get_full_name()
                    veri.mail = request.user.email
                    veri.randevuTalepTarihi = timezone.now()
                    veri.ogretimGorevlisi = request.POST.get('ogretimGorevlisi')
                    veri.save()
                    return redirect('randevu:list')
                else:
                    return render(request, 'randevu/create.html', {'tarih':tarih ,'form': form})
            if grup.name == 'Mezun':
                form = RandevuFormMezun(request.POST)
                if form.is_valid():
                    veri = form.save(commit=False)
                    veri.randevuSender = request.user.get_full_name()
                    veri.mail = request.user.email
                    veri.randevuTalepTarihi = timezone.now()
                    veri.ogretimGorevlisi = request.POST.get('ogretimGorevlisi')
                    veri.save()
                    return redirect('randevu:list')
                else:
                    return render(request, 'randevu/create.html', {'form': form, 'tarih':tarih})
    else:
        for grup in request.user.groups.all():
            ogretimGorevlisi = OgretimGorevlisi.objects.all()
            if grup.name == 'Öğrenci':
                form = RandevuFormOgrenci(request.POST)
                return render(request, 'randevu/create.html', {'tarih':tarih, 'form': form, 'ogretimGorevlisi':ogretimGorevlisi})
            if grup.name == 'Mezun':
                form = RandevuFormMezun(request.POST)
                return render(request, 'randevu/create.html', {'form': form, 'tarih':tarih , 'ogretimGorevlisi':ogretimGorevlisi})


def randevu_list(request):
    for grup in request.user.groups.all():
        if grup.name == 'Mezun':
            mezunRandevu = randevuMezun.objects.filter(mail=request.user.email)
            return render(request, 'randevu/list.html', {'mezunRandevu': mezunRandevu})
        if grup.name == 'Öğrenci':
            ogrenciRandevu = randevuOgrenci.objects.filter(mail=request.user.email)
            return render(request, 'randevu/list.html', {'ogrenciRandevu': ogrenciRandevu})
        if grup.name == 'Öğretim Görevlisi':
            hoca = OgretimGorevlisi.objects.get(user=request.user)
            mezunRandevu = randevuMezun.objects.filter(ogretimGorevlisi=request.user.get_full_name())
            ogrenciRandevu = randevuOgrenci.objects.filter(ogretimGorevlisi=request.user.get_full_name())
            hoca.oncekiGirisRandevu = datetime.datetime.now(tz=timezone.utc)
            hoca.save()
            return render(request, 'randevu/list.html',{'ogrenciRandevu': ogrenciRandevu, 'mezunRandevu': mezunRandevu})



def randevuIstekleriDetay(request, id, istek):
    global randevuMezun, randevuOgrenci
    for g in request.user.groups.all():
        if g.name == 'Mezun' and istek == "1":
            mezunRandevu = randevuMezun.objects.get(id=id)
            form = MesajMezunForm(request.POST or None, request.FILES or None)
            tarih = datetime.datetime.now(tz=timezone.utc)
            mezun = Mezun.objects.get(user=request.user)
            mezun.oncekiGirisRandevu = datetime.datetime.now(tz=timezone.utc)
            mezun.gorulenRandevu = 0
            mezun.save()
            if form.is_valid():
                mesaj = form.save(commit=False)
                mesaj.randevu = mezunRandevu
                mesaj.ad = request.user.get_full_name()
                mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                mesaj.save()
                return redirect('randevu:detay', mezunRandevu.pk, 1)
            return render(request, 'randevu/detay.html', {'randevuMezun' :mezunRandevu, 'form': form, 'tarih': tarih})

        if g.name == 'Öğrenci' and istek == "0":
            ogrenciRandevu = randevuOgrenci.objects.get(id=id)
            form = MesajOgrenciForm(request.POST or None,request.FILES or None)
            tarih = datetime.datetime.now(tz=timezone.utc)
            ogrenci = Ogrenci.objects.get(user=request.user)
            ogrenci.oncekiGirisRandevu = datetime.datetime.now(tz=timezone.utc)
            ogrenci.gorulenRandevu = 0
            ogrenci.save()
            if form.is_valid():
                mesaj = form.save(commit=False)
                mesaj.randevu = ogrenciRandevu
                mesaj.ad = request.user.get_full_name()
                mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                mesaj.save()
                return redirect('randevu:detay', ogrenciRandevu.pk, 0)
            return render(request, 'randevu/detay.html', {'randevuOgrenci' :ogrenciRandevu, 'form': form, 'tarih': tarih})

        if g.name == 'Öğretim Görevlisi':
            if istek == "0":
                ogrenciRandevu = randevuOgrenci.objects.get(id=id)
                form = MesajOgrenciForm(request.POST or None, request.FILES or None)
                tarih = datetime.datetime.now(tz=timezone.utc)
                hoca = OgretimGorevlisi.objects.get(user=request.user)
                hoca.oncekiGirisRandevuOgrenci = datetime.datetime.now(tz=timezone.utc)
                hoca.gorulenRandevuOgrenci = 0
                hoca.gorulenRandevu = hoca.gorulenRandevuOgrenci + hoca.gorulenRandevuMezun
                hoca.save()

                if form.is_valid():
                    mesaj = form.save(commit=False)
                    mesaj.randevu = ogrenciRandevu
                    mesaj.ad = request.user.get_full_name()
                    mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.save()
                    return redirect('randevu:detay', ogrenciRandevu.pk, 0)
                return render(request, 'randevu/detay.html', {'randevuOgrenci' :ogrenciRandevu, 'form': form, 'tarih': tarih, 'istek': istek})

            elif istek == "1":
                mezunRandevu = randevuMezun.objects.get(id=id)
                form = MesajMezunForm(request.POST or None, request.FILES or None)
                tarih = datetime.datetime.now(tz=timezone.utc)
                hoca = OgretimGorevlisi.objects.get(user=request.user)
                hoca.oncekiGirisRandevuMezun = datetime.datetime.now(tz=timezone.utc)
                hoca.gorulenRandevuMezun = 0
                hoca.gorulenRandevu = hoca.gorulenRandevuOgrenci + hoca.gorulenRandevuMezun
                hoca.save()
                if form.is_valid():
                    mesaj = form.save(commit=False)
                    mesaj.randevu = mezunRandevu
                    mesaj.ad = request.user.get_full_name()
                    mesaj.mesajTarihi = datetime.datetime.now(tz=timezone.utc)
                    mesaj.save()
                    return redirect('randevu:detay', mezunRandevu.pk, 1)
                return render(request, 'randevu/detay.html', {'randevuMezun': mezunRandevu, 'form': form, 'tarih': tarih, 'istek': istek})
            return render(request, 'randevu/detay.html')