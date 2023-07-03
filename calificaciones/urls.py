from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router= DefaultRouter()
router.register(r"docentes",views.DocenteViewSet)
router.register(r"estudiantes",views.EstudianteViewSet)
router.register(r"materias",views.MateriaViewSet)

urlpatterns = [
    path("",views.index,name="index"),
    path("materias/cantidad", views.materia_count, name="materia_count"),
    path("",include(router.urls)),
    
]

