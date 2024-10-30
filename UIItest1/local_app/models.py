from django.db import models

# Create your models here.

class local(models.Model):
    id_local=models.CharField(primary_key=True, max_length=6)
    direccion=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    horario=models.DateTimeField(max_length=100)
    ambiente=models.CharField(max_length=100)
    servicios=models.CharField(max_length=100)
    trabajadores=models.PositiveSmallIntegerField()

    def __str__(self):  
        return self.servicios
