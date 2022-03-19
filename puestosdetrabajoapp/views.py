from django.shortcuts import render

from .forms import GerenteFormulario, GerenteBusqueda, ReponedorFormulario, CajeroFormulario

from .models import gerente, reponedor, cajero

# Create your views here.

def crear_gerente(request):
    
    if request.method== "POST":
        form= GerenteFormulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            Gerente= gerente(nombre=data["nombre"], apellido=data ["apellido"], dni=data["dni"], email=data["email"])
            Gerente.save()
            return render(request, "pymeapp/index.html", {})
    
    
    form= GerenteFormulario()
    return render(request, "puestosdetrabajoapp/crear_gerente.html", {"form": form})

def crear_reponedor(request):
    
    if request.method== "POST":
        form= ReponedorFormulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            Reponedor= reponedor(nombre=data["nombre"], apellido=data ["apellido"], dni=data["dni"], email=data["email"], desempeño=data["desempeño"])
            Reponedor.save()
            return render(request, "pymeapp/index.html", {})
    
    
    form= ReponedorFormulario()
    return render(request, "puestosdetrabajoapp/crear_gerente.html", {"form": form})

def crear_cajero(request):
    
    if request.method== "POST":
        form= CajeroFormulario(request.POST)
        
        if form.is_valid():
            data= form.cleaned_data
            Cajero= cajero(nombre=data["nombre"], apellido=data ["apellido"], dni=data["dni"], email=data["email"], desempeño=data["desempeño"])
            Cajero.save()
            return render(request, "pymeapp/index.html", {})
    
    
    form= CajeroFormulario()
    return render(request, "puestosdetrabajoapp/crear_gerente.html", {"form": form})






def lista_gerentes(request):
    
    nombre_a_buscar=request.GET.get("nombre",None)
    if nombre_a_buscar is not None:
        gerentes = gerente.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        gerentes= gerente.objects.all()
    
    form= GerenteBusqueda()
    return render(request, "puestosdetrabajoapp/lista_gerentes.html", {"form": form, "gerentes": gerentes})
    