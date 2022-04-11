from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextFormField
from django.utils import timezone


class EditFullUser(forms.Form):
    email= forms.EmailField()
    password1= forms.CharField(label="Contraseña", widget= forms.PasswordInput,required=False)
    password2= forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput,required=False)
    first_name= forms.CharField(label="Nombre", max_length=20)
    last_name= forms.CharField(label="Apellido", max_length=20)
    avatar= forms.ImageField(required=False)
    link= forms.URLField(required=False)
    more_description=forms.CharField(max_length=100, required=False)
  
    
class BlogFormulario(forms.Form):
    titulo=forms.CharField(max_length=100)
    subtitulo=forms.CharField(max_length=100)
    cuerpo=RichTextFormField(required=False)
    autor=forms.CharField(max_length=100)
    imagen=forms.ImageField(required=False)
    fecha_creacion=forms.DateTimeField(required=False)

class BlogBusqueda(forms.Form):
    nombre=forms.CharField(max_length=50)