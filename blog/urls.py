from django.urls import path
from .views import editar_usuario


urlpatterns = [
    #path("login/", mi_login, name="login"),
    path("editar/", editar_usuario, name="editar_usuario"),
    #path("registrarse/", registrarse, name="registrarse"),
    #path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
]