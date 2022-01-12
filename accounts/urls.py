from django.conf.urls import url
from .views import *

app_name = 'accounts'

urlpatterns = [
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^updateProfile/$',updateProfile,name='update')

]