from django.core.exceptions import ValidationError

def validar_gestion(value):
    if not(2022 < value <2050):
        raise ValidationError(
            'la gestion %(value) debe estar entre 2020 y 2050',
            params={'value':value}
        )

def validar_notas(value):
    if not(0 <= value <= 100):
        raise ValidationError(
            'la nota  %(value) debe estar entre 0 .. 100',
            params={'value':value}
        )