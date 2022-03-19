from django.db import models

# Create your models here.

class gerente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni} {self.email}"
    
class reponedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    desempeño= models.BooleanField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni} {self.email} {self.desempeño}"

    
class cajero(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    desempeño= models.BooleanField()
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni} {self.email} {self.desempeño}"   
