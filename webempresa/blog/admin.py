from django.contrib import admin
#importamos los modelos
from .models import Category, Post

# Register your models here.
#mostramos el created y updated en el admin ya que por defecto django esconde
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

#mostrmos el campo de usated y created
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')#mostamos el field createdy updated
    list_display=('title_pos', 'author', 'published', 'post_categories')#mostramos las columnas |||| categories no funciona porque es manytomany
    ordering=('author', 'published')#ordenamos primero por autor y despues pr fecha de publlicacion ||| si es uno solo se deja con coma al final
    search_fields=('title_pos', 'content', 'author__username',  'categories__name_cat')#Agregamos el  campos de busqueda
    date_hierarchy='published'#mostramos jerarquia de fechas para navegar en las disntinaas fechas
    list_filter=('author__username', 'categories__name_cat')#Mostrart filtrar campos 

    #categories no funciona porque es manytomany--- creamos nuestro propio campo Metodo
    def post_categories(self, obj):
        return ', '.join([c.name_cat for c in obj.categories.all().order_by('name_cat')])
    post_categories.short_description='categorias'#asiganmos el nombe de categoias

#el modelo sea visisble desde el panel del administrador
admin.site.register(Category, CategoryAdmin, )
admin.site.register(Post, PostAdmin)