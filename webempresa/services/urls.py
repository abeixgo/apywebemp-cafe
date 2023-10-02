from django.urls import path#creamos este archivo 
from . import views #importamos el ficher o views


urlpatterns = [
    #path del core

    path ('', views.services, name='services'),#dejamos en la raiz

]
