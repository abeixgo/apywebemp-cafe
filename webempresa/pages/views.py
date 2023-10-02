from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Page

# Create your views here.
#def sample(request):
#    return render(request, 'pages/sample.html')REVISAR SI NO FUNCA

#creamos vistas secundarias de paginas para privacidad, cokies|||VISTAS SECUNDARIAS
def list_page(request, page_id, page_slug):
    #obtener paginas con el id proprocionadp
    page=get_object_or_404(Page, id=page_id)#obtenemos todas las entradas de modeloDBpage 
    return render(request, 'pages/sample.html', {'page':page})#creamos variable de dicionario para inyectar los datos en HTML