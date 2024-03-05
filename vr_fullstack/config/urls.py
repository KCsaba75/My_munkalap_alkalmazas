
from django.contrib import admin
from django.urls import path

from mymunkalap_app import views
from  . import views as  config_views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', config_views.home, name='home'),
    path('login/', config_views.login_page, name='login_page'),
    path('register/', config_views.register_page, name='register_page'),
    path('logout/', config_views.logout_page, name='logout_page'),
    path('gepjarmuvek/', views.GepjarmuListView.as_view()),
    path('megrendelok-gepjarmuvekkel/', views.MegrendeloListWithGepjarmuView.as_view()),






    

   
    
]
