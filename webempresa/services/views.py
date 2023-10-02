from django.shortcuts import render
from .models import Services #importamos el modelo Servicios de models

# Create your views here. ||| recuepramos nustro lista de proyectocto gracias al ORM de django
def services(request):
    services=Services.objects.all()#nos devuelve y obtenemos todos los objetos de la lista de servicios |||  solo falta inyectar los datos obtenidos al template
    return render(request, 'services/services.html', {'services':services})#buscamos en services html||||| agregamos los datos del servicio al template
