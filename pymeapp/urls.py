from django.urls import path
from .views import pymeapp, plantilla

urlpatterns= [
    path("", pymeapp, name="pymeapp"),
    #path("login/", mi_login, name="login"),
    #path("registrarse/", registrarse, name="registrarse"),
    # path("logout/", LogoutView.as_view(template_name="pymeapp/logout.html"), name="logout"),
    path("plantilla/", plantilla, name="plantilla"),
    
]