from django.shortcuts import render
from django.http import HttpResponse,  JsonResponse

from rest_framework import viewsets
from .models import Docente
from .serializers import  DocenteSerializer

from .models import Estudiante
from .serializers import  EstudianteSerializer

from .models import Materia
from .serializers import  MateriaSerializer

from rest_framework.decorators import api_view 

def index(request):
    return HttpResponse("Hola mundo")

# Create your views here.
class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class MateriaViewSet(viewsets.ModelViewSet):
    queryset = Materia.objects.all()
    serializer_class = MateriaSerializer


## PERSONALIZADO
@api_view(["GET"])
def materia_count(request):
    try:
        cantidad = Materia.objects.count()
        return JsonResponse(
                {
                    "cantidad": cantidad
                },
                safe=False,
                status=200
            )
    except Exception as e:
        return JsonResponse({"mensaje": str(e)}, status=400)
