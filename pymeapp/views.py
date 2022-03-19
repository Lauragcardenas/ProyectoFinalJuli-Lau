from http.client import HTTPResponse
from django.shortcuts import render


def pymeapp(request):
    return render(request, "pymeapp/index.html", {})

def plantilla(request): 
    datos= {
        "lista":["primero", "segundo", "tercero"]
    }
        
    return render(request, "pymeapp/plantilla.html", datos)
    