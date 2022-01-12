"""obs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from jobs.views import bildirimIcin
from django.contrib.auth import views as auth_views
from accounts.views import *
from grafik.views import HomeView, ChartData, get_data




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', loginRegister, name='index'),
    url(r'^anasayfa/', bildirimIcin, name='anasayfa'),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^jobs/', include('jobs.urls')),
    url(r'^jobs/', include('django.contrib.auth.urls')),
    url(r'^dersNotlari/', include('dersNotu.urls')),
    url(r'^dersNotlari/', include('django.contrib.auth.urls')),
    url(r'^belgeler/', include('belgeler.urls')),
    url(r'^belgeler/', include('django.contrib.auth.urls')),
    url(r'^randevu/', include('randevu.urls')),
    url(r'^dersicerik/', include('dersicerik.urls')),

    url(r'^api/data/$', get_data, name='api-data'),
    url(r'^grafik/charts', HomeView.as_view(), name='charts'),
    url(r'^api/chart/data/$', ChartData.as_view()),

    path('csv/', contect_download, name='contect-download'),


    # Password reset links
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_complete'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),
         name='password_change'),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)