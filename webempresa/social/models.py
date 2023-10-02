from django.db import models

# Create your models here.
#creamos un modelos de BD
class Link(models.Model):
    key=models.SlugField(verbose_name='Nombre clave', max_length=100, unique=True)#unico
    name_lin=models.CharField(verbose_name='Red social', max_length=100,   )
    url=models.URLField(verbose_name='Enlace',  max_length=100, null=True, blank=True)#no es necesario que pongan link algunas puedan dejar en blanco
    created=models.DateTimeField(verbose_name='Fecha de creacion', auto_now_add=True)
    updated=models.DateTimeField(verbose_name='Fecha de edicion', auto_now=True)

        #metadotos extendidos
    class Meta:
        verbose_name='enlace'
        verbose_name_plural='enlaces'
        ordering=['-name_lin']

    #ver lso nombres de las categorias
    def __str__(self):
        return self.name_lin