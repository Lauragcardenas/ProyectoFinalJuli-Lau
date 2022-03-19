from django.db import models

# Create your models here.

class gerente(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    
class reponedor(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    desempeño= models.BooleanField()
    
class cajero(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    desempeño= models.BooleanField()