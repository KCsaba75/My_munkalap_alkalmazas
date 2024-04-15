
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from Mymunkalap_app import views
from  . import views as  config_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/munkalapAktiv/', views. AktivMunkalapokJsonView.as_view(), name='aktiv_munkalapok_json'),
    path('api/munkalapInAktiv/', views. InAktivMunkalapokJsonView.as_view(), name='inaktiv_munkalapok_json'), 
    path('api/munkalapOsszes/', views. OsszesMunkalapokJsonView.as_view(), name='osszes_munkalapok_json'), 
    path('api/munkalapUj/', views. UjMunkalapCreateView.as_view(), name='uj_munkalap_json'), 
    path('api/gepjarmuOsszes/', views. OsszesGepjarmuJsonView.as_view(), name='osszes_gepjarmuvek_json'), 

]