from django.urls import path#creamos este archivo 
from . import views #importamos el ficher o views


urlpatterns = [
    #path del  blog
    #path ('', views.sample, name='sample'),
    #path otras paginas  
    path('<int:page_id>/<slug:page_slug>', views.list_page, name='list_page'),
]
