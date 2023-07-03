from rest_framework import serializers
from .models import Docente
from .models import Estudiante
from .models import Materia

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Docente
        fields="__all__"
        
class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields="__all__"

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Materia
        fields="__all__"