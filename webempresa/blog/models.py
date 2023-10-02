from django.db import models
from django.utils.timezone import now#importamos el tiempo
from django.contrib.auth.models import User#importamos del modelo de django los usuarios

# Create your models here.
#modelo de base de datos
class Category(models.Model):
    name_cat=models.CharField(max_length=100, verbose_name='Nombre de categoria')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    #metadotos extendidos
    class Meta:
        verbose_name='Categoria'
        verbose_name_plural='Categorias'
        ordering=['-created']

    #ver lso nombres de las categorias
    def __str__(self):
        return self.name_cat

class Post(models.Model):
    title_pos=models.CharField(max_length=150, verbose_name='Titulo del post')
    content=models.TextField(verbose_name='Contenido del post')
    published=models.DateTimeField(verbose_name='Fecha de publicacion', default=now)
    image=models.ImageField(verbose_name='Imagen para el post', upload_to='blog', null=True, blank=True )#campo opcionaal --> null=True, blank=True nulo y vacio por eso facil de migrar
    author=models.ForeignKey(User, verbose_name='Autor del post', on_delete=models.CASCADE)#importamos del modelo user de django|| cuando se borra un autor no quedara blanco borrara en cascada
    categories=models.ManyToManyField(Category, verbose_name='categorias', related_name='get_categories')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    #metadotos extendidos
    class Meta:
        verbose_name='Entrada del Post'
        verbose_name_plural='entradas de Post'
        ordering=['-created']

    #ver lso nombres de las categorias
    def __str__(self):
        return self.title_pos