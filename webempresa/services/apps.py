from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
      #configuracion extendida: cambiar el nombre de app Publica:
    verbose_name='Gestor de servicios'

