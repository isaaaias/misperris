from django.contrib import admin
from .models import Adoptante, Region, Ciudad, Comuna, Vivienda

# Register your models here.

class AdoptanteAdmin(admin.ModelAdmin):
    #las tuplas con como arreglos pero no se pueden modificar
    list_display = ('rut', 'nombre', 'fechaNacimiento', 'email', 'telefono')
    search_fields = ['rut', 'nombre']
   
 

admin.site.register(Adoptante, AdoptanteAdmin)
admin.site.register(Vivienda)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
