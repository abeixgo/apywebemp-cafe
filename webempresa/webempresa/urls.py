"""
URL configuration for webempresa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #aumentamos include
#from core import views#importamos las vistas || yano para vistas ocn funciones
from  django.conf import settings#para carpeta media

urlpatterns = [
    #path core
    path('', include('core.urls')),#no se pone core

    #path services
    path('services/', include('services.urls')),#no se pone core

    #path blog
    path('blog/', include('blog.urls')),#no se pone core

    #path pages
    path('page/', include('pages.urls')),#no se pone core
    
    #path pages
    path('contact/', include('contact.urls')),#no se pone core

    #path del admin
    path('admin/', admin.site.urls),
]

#servir imagenes para desarrollo su debug=true | configuracion extendida | solo enttorno de desarrollo
if settings.DEBUG:#si debug true
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#+= está agregando elementos a la lista urlpatterns