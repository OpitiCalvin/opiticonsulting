# opiticonsulting/urls.py
from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('demos/', views.demo, name='demos'),
    path('services/', views.service, name='services'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('about_founder/', views.aboutFounder, name='aboutFounder'),
    path('contact/', views.contact, name='contact'), 
]
