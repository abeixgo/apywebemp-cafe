#creamos
from django import template
from pages.models import Page

register=template.Library()#lalmamos a este metodo 

@register.simple_tag
def get_pag_list():
    pages=Page.objects.all()
    return pages

#transformanos una funcion simple en un tag simple y registramos en template library