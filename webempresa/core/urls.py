from django.urls import path#creamos este archivo 
from . import views #importamos el ficher o views


urlpatterns = [
    #path del core
    path('', views.home, name='home' ),
    path ('about/', views.about, name='about'),
    #path ('services/', views.services, name='services'),
    path ('store/', views.store, name='store'),
    #path ('contact/', views.contact, name='contact'),
    #path ('blog/', views.blog, name='blog'),
    #path ('sample/', views.sample, name='sample'),

]
