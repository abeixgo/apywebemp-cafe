from django.contrib import admin
from .models import Link# el modelo de DB Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')#solo lectura de estos campos en admin para todos

    #crear solo vista de algunos campos dependiendo si es superusuario o un personal
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('created', 'updated', 'key', 'name_lin')
        else:
            return ('created', 'updated')

admin.site.register(Link, LinkAdmin)