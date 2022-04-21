from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone

class UserExtension(models.Model):
    avatar= models.ImageField(upload_to="avatar",blank=True, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    link= models.URLField(null=True)
    more_description= models.CharField(max_length=100)
    
class Blog(models.Model):
    titulo=models.CharField(max_length=100)
    subtitulo=models.CharField(max_length=100)
    cuerpo=RichTextField(blank=True, null=True)
    autor=models.CharField(max_length=100)
    fecha_creacion= models.DateTimeField(default=timezone.now)
    imagen= models.ImageField(upload_to="imagen",blank=True, null=True)
    
