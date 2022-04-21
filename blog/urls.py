from django.urls import path
from .views import editar_usuario, usuario_datos, crear_blog
from . import views

urlpatterns = [
    #path("login/", mi_login, name="login"),
    path("editar/", editar_usuario, name="editar_usuario"),
    path("datos/", usuario_datos, name="usuario_datos"),
    path("blog/", crear_blog ,name="crear_blog"),
    #path("registrarse/", registrarse, name="registrarse"),
    #path("logout/", LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    path("blog/", views.Detalleblog.as_view(),name="detalle_blog"),
    path("lista_blog/", views.lista_blog,name="lista_blog"),
    path("blog/editar", views.EditarBlog.as_view(),name="editar_blog"),
    path("blog/borrar", views.BorrarBlog.as_view(),name="borrar_blog"),
]