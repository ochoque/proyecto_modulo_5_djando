from django.contrib import admin
from .models import Docente
from .models import Estudiante
from .models import Materia
from .models import RegisNotas


class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'tipo_doc', 'fecha_nac')
    list_filter = ('nombre', 'tipo_doc')
    search_fields = ('nombre','tipo_doc')
    ordering = ('nombre', 'tipo_doc')
admin.site.register(Docente, DocenteAdmin)

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombree', 'fecha_nac', 'procedencia')
  
admin.site.register(Estudiante,EstudianteAdmin)

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'descripcion', 'tipo_mat', 'habilitado')
    list_filter = ('tipo_mat', 'habilitado')
    ordering = ('sigla', 'tipo_mat')
admin.site.register(Materia,MateriaAdmin)

class RegisNotasAdmin(admin.ModelAdmin):
    list_display = ('semestre','gestion','id_mat','id_est','id_doc','parcial_1','parcial_2','parcial_3','practicas','final','nota_final')
    
admin.site.register(RegisNotas,RegisNotasAdmin)

# Register your models here.
