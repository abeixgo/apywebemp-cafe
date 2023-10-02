from django.db import models
from ckeditor.fields import RichTextField#imporatmos el editor wisywygo

# Create your models here.
class Page(models.Model):
    title_pag=models.CharField(verbose_name='Titulo de la pagina', max_length=200)
    content=RichTextField(verbose_name='Contenido')#aqui remplazamos el editor ck
    order=models.SmallIntegerField(verbose_name='Orden', default=0)
    created=models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True)

    #configuracin extendida
    class Meta:
        verbose_name='Pagina'
        verbose_name_plural='Paginas'
        ordering=['order', 'title_pag']

    #ver los titulos de las paginas en ves de nombres raros
    def __str__(self):
        return self.title_pag
