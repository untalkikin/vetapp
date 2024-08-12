from django.db import models


class Paciente(models.Model):
    VAC ='Vacuna'
    REV = 'Revision'
    SHO = 'Aceo de la mascota'
    TIPO_VISITA = [
        (VAC,'Vacuna'),
        (REV, 'Revision'),
        (SHO, 'Aceo de la mascota')
    ]
    nombre_mascota = models.CharField(max_length=100, unique=True)
    nombre_dueño = models.CharField(max_length=100, unique=True)
    direccion = models.CharField(max_length=100, unique=True)
    movil = models.CharField(max_length=10,null=True, blank=True)
    motivo_visita = models.CharField(max_length=20, choices=TIPO_VISITA, default = VAC)
    
    def __str__(self):
        return '{} {}'.format(self.nombre_mascota,self.nombre_dueño)
    
    class Meta:
        verbose_name_plural = "Pacientes"