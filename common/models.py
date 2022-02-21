from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    direccion=models.CharField(max_length=100)
    cel=models.CharField(max_length=20)
    email=models.CharField(max_length=50)
    telefono=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre+'-'+self.apellido
    
class Producto(models.Model):
    codigo=models.CharField(max_length=50)
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=500)
    precio=models.FloatField()
    stock=models.IntegerField()
    stock_min=models.IntegerField()
    stock_max=models.IntegerField() 

    def __str__(self):
        return self.codigo+'-'+self.nombre

class Dispositivo(models.Model):
    nombre=models.CharField(max_length=20)
    type=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

