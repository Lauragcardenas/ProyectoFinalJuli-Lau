from django.http import HttpResponse
from django.template import loader

def mi_plantilla(request):
    template = loader.get_template("plantilla.html")

    diccionario_de_datos = {

    }

    plantilla_preparada = template.render(diccionario_de_datos)
    return HttpResponse(plantilla_preparada)