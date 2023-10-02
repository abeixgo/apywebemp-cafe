from django.urls import path#creamos este archivo 
from . import views #importamos el ficher o views


urlpatterns = [
    #path del  blog
    path ('', views.blog, name='blog'),
    #path category  
    path('category/<int:category_id>/', views.list_category, name='list_category'),
]
