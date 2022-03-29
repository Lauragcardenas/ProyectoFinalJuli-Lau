from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

#from pymeapp.forms import NuestroUserForm
from .forms import NuestroUserForm

def pymeapp(request):
    return render(request, "pymeapp/index.html", {})

def plantilla(request): 
    datos= {
        "lista":["primero", "segundo", "tercero"]
    }
        
    return render(request, "pymeapp/plantilla.html", datos)

def mi_login(request):
    
    if request.method== "POST":
        login_form= AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username= login_form.cleaned_data["username"]
            password= login_form.cleaned_data["password"]
            user= authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                # return render(request, "pymeapp/login.html", {"login_form": login_form})
                return redirect("pymeapp")
            else: 
                return render(request, "pymeapp/login.html", {"login_form": login_form, "msj": "El usuario no se pudo autenticar"})
        else: 
            return render(request, "pymeapp/login.html", {"login_form": login_form, "msj": "El formulario no es valido"})
    
    
    login_form= AuthenticationForm()
    return render(request, "pymeapp/login.html", {"login_form": login_form})

def registrarse(request):
    
    if request.method == "POST":
        form= NuestroUserForm(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data["username"]
            form.save()
            #return render(request, "pymeapp/index.html", {"msj": f"Se crea correctamente al usuario {username}"})
            return redirect("login")
        else:
            return render(request, "pymeapp/registrarse.html", {"form": form, "msj": "El formulario no es valido"})
    
    
    form = NuestroUserForm()
    return render(request, "pymeapp/registrarse.html", {"form": form})