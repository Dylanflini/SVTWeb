from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class posibleCliente(models.Model):
    idPosibleCliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    telefono = models.IntegerField(validators=[MaxValueValidator(999999999)])
    email = models.CharField(max_length=30)
    mensaje = models.TextField(max_length=350)
    copiaMensaje = models.BooleanField(null=True)

    def guardar(self):
        self.save() 

    def __str__(self):
        return self.nombre