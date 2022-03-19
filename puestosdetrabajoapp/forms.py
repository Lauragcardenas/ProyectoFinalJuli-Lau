from django import forms


class GerenteFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    email=forms.EmailField()
 
class GerenteBusqueda(forms.Form):
    nombre=forms.CharField(max_length=50)
    
    
class ReponedorFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    email=forms.EmailField()
    desempeño=forms.BooleanField(required=False)
 
class CajeroFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    dni=forms.IntegerField()
    email=forms.EmailField()
    desempeño=forms.BooleanField(required=False)
