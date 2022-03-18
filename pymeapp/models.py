from django.db import models

class cliente(models.Model):
    numero=models.IntegerField()
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    dni=models.IntegerField()
    email=models.EmailField()
    
class articulo(models.Model):
    productoid=models.IntegerField()
    seccion=models.CharField(max_length=50)
    marca=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    
class envio(models.Model):
    cantidad=models.IntegerField()
    direccion=models.CharField(max_length=50)
    fechaDeEntrega = models.DateField()
    entregado=models.BooleanField()