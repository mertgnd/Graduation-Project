from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Ders
from .forms import DersForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def ders_index(request, sinif):
    ders_list = Ders.objects.filter(Sınıf=sinif)
    query = request.GET.get("q")
    if query:
        ders_list = ders_list.filter(Ders__icontains=query)

    paginator = Paginator(ders_list, 5)

    page = request.GET.get('sayfa')
    try:
        dersler = paginator.page(page)
    except PageNotAnInteger:
        dersler = paginator.page(1)
    except EmptyPage:
        dersler = paginator.page(paginator.num_pages)

    return render(request, 'ders/notlar.html', {'dersler': dersler})


def ders_detail(request, id):
    ders = get_object_or_404(Ders, id=id)
    context = {
        'ders': ders
    }
    return render(request, 'ders/detail.html', context)


def ders_delete(request, id):
    ders = get_object_or_404(Ders, id=id)
    sinif = ders.Sınıf
    ders.delete()
    return redirect('dersNotu:index', sinif=sinif)


def ders_create(request):

    form = DersForm(request.POST, request.FILES or None)
    if form.is_valid():
        ders = form.save(commit=False)
        ders.Sınıf = request.POST.get('sinif')
        print(request.FILES.get('dosyaPdf'))
        ders.pdf = request.FILES.get('dosyaPdf')
        ders.yukleyenId = request.user.email
        ders.Yükleyen = request.user.get_full_name()
        ders.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz..', extra_tags='mesaj başarılı')
        return HttpResponseRedirect(ders.get_absolute_url())

    context = {
        'form': form,
    }
    return render(request, 'ders/form.html', context)


def ders_update(request, id):
    dersler = get_object_or_404(Ders, id=id)
    form = DersForm(request.POST or None, request.FILES or None, instance=dersler)
    if form.is_valid():
        ders = form.save(commit=False)
        ders.Sınıf = request.POST.get('sinif')
        if request.FILES.get('dosyaPdf') != None:
            dersler.pdf.delete()
            ders.pdf = request.FILES.get('dosyaPdf')
        ders.save()
        messages.success(request, 'Başarılı bir şekilde oluşturdunuz..')
        return HttpResponseRedirect(dersler.get_absolute_url())
    context = {
        'form': form,
        'dersler': dersler
    }
    return render(request, 'ders/formGuncelleme.html', context)


