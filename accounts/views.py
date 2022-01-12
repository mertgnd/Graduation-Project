import csv
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import UserForm, MezunForm, OgrenciForm, UserUpdateForm, MezunUpdateForm, OgrenciUpdateForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Ogrenci, Mezun, OgretimGorevlisi, BolumSekreteri
from jobs.models import stajIlani, IsIlaniEkle
import datetime
from django.utils import timezone


def loginRegister(request):
    userform = UserForm(request.POST)
    profileform = MezunForm(request.POST)
    ogrenciform = OgrenciForm(request.POST)
    if request.method == 'POST':
        if request.POST.get('submit') == 'mezun':
            userform = UserForm(request.POST)
            profileform = MezunForm(request.POST)
            mezunGrup = Group.objects.get(name='Mezun')
            if userform.is_valid() and profileform.is_valid():
                user = userform.save()
                mezunGrup.user_set.add(user)
                profile = profileform.save(commit=False)
                profile.user = user
                profile.oncekiGirisStaj = datetime.datetime.now(tz=timezone.utc)
                profile.oncekiGirisIs = datetime.datetime.now(tz=timezone.utc)
                calismaDurumu = request.POST.get('calismaDurumu')
                profile.sehir = request.POST.get('sehir')
                profile.cinsiyet = request.POST.get('cinsiyet')
                profile.calismaDurumu = request.POST.get('calismaDurumu')
                profile.ogrenimDurumu = 'Mezun'
                if calismaDurumu == 'Çalışıyorum':
                    profile.sektor = request.POST.get('sektor')
                    profile.unvanMeslek = request.POST.get('unvan')
                    profile.idariGorev = request.POST.get('idariGorev')
                    profile.maas = request.POST.get('maas')
                    profile.sirketKurumAdi = request.POST.get('sirketAdi')
                    profile.iseBaslamaTarihi = request.POST.get('iseBaslamaTarihi')
                    profile.il = request.POST.get('isIl')
                    profile.isAdresi = request.POST.get('isAdresi')

                profile.save()
                login(request, user)
                mezun = Mezun.objects.get(user=user)
                return render(request, 'anasayfa.html', {'mezun': mezun})
        elif request.POST.get('submit') == 'giris':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                for g in user.groups.all():
                    if g.name == 'Mezun':
                        ogrenciGiris = Mezun.objects.get(user=user)
                        ogrenciGiris.gorulenStajId = 0
                        ogrenciGiris.save()

                    elif g.name == 'Öğrenci':
                        ogrenciGiris = Ogrenci.objects.get(user=user)
                        ogrenciGiris.gorulenStajId = 0
                        ogrenciGiris.save()

                    elif g.name == 'Öğretim Görevlisi':
                        hocaGiris = OgretimGorevlisi.objects.get(user=user)
                        hocaGiris.gorulenDersIcerik = 0
                        hocaGiris.save()

                    elif g.name == 'Bölüm Sekreteri':
                        sekreterGiris = BolumSekreteri.objects.get(user=user)
                        sekreterGiris.gorulenTranskript = 0
                        sekreterGiris.save()

                login(request, user)
                return redirect('anasayfa')
            else:
                messages.info(request, 'Kullanıcı adı yada parola hatalı!')
                return redirect('index')



        elif request.POST.get('submit') == 'ogrenci':
            userform = UserForm(request.POST)
            ogrenciform = OgrenciForm(request.POST)
            if userform.is_valid() and ogrenciform.is_valid():
                user = userform.save()
                ogrenciGrup = Group.objects.get(name='Öğrenci')
                ogrenciGrup.user_set.add(user)
                profileOgrenci = ogrenciform.save(commit=False)
                profileOgrenci.user = user
                profileOgrenci.oncekiGirisStaj = datetime.datetime.now(tz=timezone.utc)
                profileOgrenci.oncekiGirisIs = datetime.datetime.now(tz=timezone.utc)
                profileOgrenci.save()
                login(request, user)
                ogrenci = Ogrenci.objects.get(user=user)
                return render(request, 'anasayfa.html', {'ogrenci': ogrenci})


    else:
        userform = UserForm(request.POST)
        profileform = MezunForm(request.POST)
        ogrenciform = OgrenciForm(request.POST)

    return render(request, 'accounts/index.html', {'userform': userform, 'ogrenciform': ogrenciform, 'profileform': profileform})

def logout_view(request):
    logout(request)
    return redirect('index')

def updateProfile(request):

        if request.method == 'POST':
            for g in request.user.groups.all():
                if g.name == 'Mezun':
                    userform = UserUpdateForm(data=request.POST, instance=request.user)
                    profileform = MezunUpdateForm(data=request.POST, instance=request.user.mezun)
                    if userform.is_valid() and profileform.is_valid():
                        user = userform.save()
                        profile = profileform.save(commit=False)
                        profile.user = user
                        calismaDurumu = request.POST.get('calismaDurumu')
                        profile.sehir = request.POST.get('sehir')
                        profile.cinsiyet = request.POST.get('cinsiyet')
                        profile.calismaDurumu = request.POST.get('calismaDurumu')
                        if calismaDurumu == 'Çalışıyorum':
                            profile.sektor = request.POST.get('sektor')
                            profile.unvanMeslek = request.POST.get('unvan')
                            profile.idariGorev = request.POST.get('idariGorev')
                            profile.maas = request.POST.get('maas')
                            profile.sirketKurumAdi = request.POST.get('sirketAdi')
                            profile.iseBaslamaTarihi = request.POST.get('iseBaslamaTarihi')
                            profile.il = request.POST.get('isIl')
                            profile.isAdresi = request.POST.get('isAdresi')
                        elif calismaDurumu == 'Çalışmıyorum':
                            profile.sektor = ""
                            profile.unvanMeslek = ""
                            profile.idariGorev = ""
                            profile.maas = ""
                            profile.sirketKurumAdi = ""
                            profile.iseBaslamaTarihi = None
                            profile.il = ""
                            profile.isAdresi = ""

                        profile.save()
                        return redirect('anasayfa')


                elif g.name == 'Öğrenci':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    ogrenciform = OgrenciUpdateForm(request.POST, instance=request.user.ogrenci)
                    if userform.is_valid() and ogrenciform.is_valid():
                        user = userform.save()
                        profileOgrenci = ogrenciform.save(commit=False)
                        profileOgrenci.user = user
                        profileOgrenci.save()
                        return redirect('anasayfa')

                elif g.name == 'Öğretim Görevlisi':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    if userform.is_valid():
                        userform.save()
                        return redirect('anasayfa')

                elif g.name == 'Bölüm Sekreteri':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    if userform.is_valid():
                        userform.save()
                        return redirect('anasayfa')

                else:
                    for g in request.user.groups.all():
                        if g.name == 'Mezun':
                            userform = UserUpdateForm(request.POST, instance=request.user)
                            profileform = MezunUpdateForm(request.POST, instance=request.user.mezun)
                            return render(request, 'accounts/userUpdate.html',
                                          {'userform': userform, 'profileform': profileform})
                        elif g.name == 'Öğrenci':
                            userform = UserUpdateForm(request.POST, instance=request.user)
                            ogrenciform = OgrenciUpdateForm(request.POST, instance=request.user.ogrenci)
                            return render(request, 'accounts/userUpdate.html',
                                          {'userform': userform, 'ogrenciform': ogrenciform})
                        elif g.name == 'Öğretim Görevlisi':
                            userform = UserUpdateForm(request.POST, instance=request.user)
                            return render(request, 'accounts/userUpdate.html',
                                          {'userform': userform})
                        elif g.name == 'Bölüm Sekreteri':
                            userform = UserUpdateForm(request.POST, instance=request.user)
                            return render(request, 'accounts/userUpdate.html',
                                          {'userform': userform})
        else:
            for g in request.user.groups.all():
                if g.name == 'Mezun':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    profileform = MezunUpdateForm(request.POST, instance=request.user.mezun)
                    return render(request, 'accounts/userUpdate.html', {'userform': userform, 'profileform':profileform})
                elif g.name == 'Öğrenci':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    ogrenciform = OgrenciUpdateForm(request.POST, instance=request.user.ogrenci)
                    return render(request, 'accounts/userUpdate.html', {'userform': userform, 'ogrenciform': ogrenciform})
                elif g.name == 'Öğretim Görevlisi':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    return render(request, 'accounts/userUpdate.html',
                                  {'userform': userform})
                elif g.name == 'Bölüm Sekreteri':
                    userform = UserUpdateForm(request.POST, instance=request.user)
                    return render(request, 'accounts/userUpdate.html',
                                  {'userform': userform})

def staff_required(login_url=None):
    return user_passes_test(lambda u: u.is_staff, login_url=login_url)


@permission_required('admin.can_add_log_entry')
def contect_download(request):
    items = Mezun.objects.filter(calismaDurumu = 'Çalışıyorum')

    response = HttpResponse(content_type='text/pkl')
    response['Content-Disposition'] = 'attachment; filename="Mezun.csv"'

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['mezuniyetYili','maas','il'])

    for obj in items:
        writer.writerow([obj.mezuniyetYili,obj.maas,obj.il])

    return response
