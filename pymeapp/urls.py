from django.urls import path
from .views import pymeapp, plantilla

urlpatterns= [
    path("", pymeapp, name="pymeapp"),
    path("plantilla", plantilla, name="plantilla"),
    
]