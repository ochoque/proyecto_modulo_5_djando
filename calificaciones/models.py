from django.db import models

#validador
from .validators import validar_gestion
from .validators import validar_notas


class TipoDoc(models.TextChoices):
    TC = 'TC', 'TIEMPO COMPLETO'
    TH = 'TH', 'TIEMPO HORARIO'

class TipoMat(models.TextChoices):
    TE = 'T', 'TEORICO'
    TP = 'TP', 'TEORICO PRACTICO'
    PR = 'P', 'PRACTICO'
    
class Semestre(models.TextChoices):
    PS = 'P', '1'
    SS = 'S', '2'
    

class Docente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    tipo_doc = models.CharField(
        max_length=2,
        choices=TipoDoc.choices,
        default=TipoDoc.TC
    )
    fecha_nac = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre

class Materia(models.Model):
    sigla = models.CharField(max_length=6)
    descripcion = models.CharField(max_length=20)
    tipo_mat = models.CharField(
        max_length=2,
        choices=TipoMat.choices,
        default=TipoMat.TE
    )
    habilitado = models.BooleanField(blank=True, default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.sigla
    
class Estudiante(models.Model):
    nombree = models.CharField(max_length=30)
    fecha_nac = models.DateField(null=True)
    procedencia = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombree

class RegisNotas(models.Model):
    semestre = models.CharField(
        max_length=1,
        choices=Semestre.choices,
        default=Semestre.PS
    )
    gestion= models.PositiveIntegerField(validators=[validar_gestion,])
    parcial_1 = models.DecimalField(decimal_places=2, max_digits=5,validators=[validar_notas,])
    parcial_2 = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_notas,])
    parcial_3 = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_notas,])
    final = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_notas,])
    practicas = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_notas,])
    nota_final = models.DecimalField(decimal_places=2, max_digits=5, validators=[validar_notas,])
    id_doc = models.ForeignKey(Docente, on_delete=models.CASCADE)
    id_est = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    id_mat = models.ForeignKey(Materia, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
## Create your models here.
