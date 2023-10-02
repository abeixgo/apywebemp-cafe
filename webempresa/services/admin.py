from django.contrib import admin
from .models import Services#importamos el modelo

# Register your models here.
#mostramos el created y updated en el admin ya que por defecto django esconde
class ServicesAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

#el modelo sea visisble desde el panel del administrador
admin.site.register(Services, ServicesAdmin)