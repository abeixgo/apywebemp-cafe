#cremaos el archivo para craer porcesador de contexto y para que las redes socilaes se vean en todos
from .models import Link

def context_dic(request):#diccionario de contexto
    ctx={}#la clave se utiliza como variable  en cualquier template||| añadimos este en settinds-templates-context procesors
    links=Link.objects.all()#buscamos los link y almacenmoas
    for link in links:#link.key esto es la clave
        ctx[link.key]=link.url#creamos la clave del diccinario
    return ctx