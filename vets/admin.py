from django.contrib import admin
from .models import Veterinaria, PerfilVet

class VetAdmin(admin.ModelAdmin):
      list_display = ('rfc', 'nombre', 'contacto', 'direccion') #Ahora la interfaz mostrará nombre, apellido y email de cada autor.
      search_fields = ('nombre', 'descripcion')


class VetProfileAdmin(admin.ModelAdmin):
      list_display = ('user', 'vet')
      
admin.site.register(Veterinaria, VetAdmin)
admin.site.register(PerfilVet, VetProfileAdmin)