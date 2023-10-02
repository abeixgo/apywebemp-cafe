from django.db import models

# Create your models here.
#modelo de base de datos
class Services(models.Model):
    title=models.CharField(max_length=100, verbose_name='titulo')
    subtitle=models.CharField(max_length=100, verbose_name='subtitulo')
    content=models.TextField(verbose_name='contenido')
    image=models.ImageField(verbose_name='imagen', upload_to='services')
    created=models.DateTimeField(auto_now_add=True, verbose_name='fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='fecha de edicion')
 
    class Meta:#añadimos los metadotos extendidos a los campos
        verbose_name='servicio'
        verbose_name_plural='servicios'
        ordering=['-created']

    def __str__(self):#ver los titulos de los proyectos en peataña admin y no nombres raros
        return self.title