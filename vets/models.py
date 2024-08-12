from django.db import models
from bases.models import ClaseModelo
from django.contrib.auth.models import User

class Veterinaria(ClaseModelo):
    rfc=models.CharField(
        max_length=100,
        unique=True
        )
    nombre=models.CharField(
        max_length=100,
        unique=True
        )
    descripcion=models.CharField(
        max_length=100,
        unique=True
        )
    direccion=models.CharField(
        max_length=250,
        null=True, blank=True
        )
    contacto=models.CharField(
        max_length=100
    )
    telefono=models.CharField(
        max_length=10,
        null=True, blank=True
    )
    email=models.CharField(
        max_length=250,
        null=True, blank=True
    )
    logo_vet = models.ImageField(upload_to='veterinarias/')

    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        self.nombre = self.nombre.upper()
        super(Veterinaria, self).save()

    class Meta:
        verbose_name_plural = "Veterinarias"
        
        
class PerfilVet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vet = models.ForeignKey(Veterinaria, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username
