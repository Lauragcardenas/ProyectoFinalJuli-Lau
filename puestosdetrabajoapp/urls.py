from django.urls import path
from . import views


urlpatterns = [
    path("gerentes/", views.lista_gerentes ,name="gerentes"),
    path("gerentes/crear/", views.crear_gerente,name="crear_gerente"),
    path("gerentes/<int:pk>", views.DetalleGerente.as_view(),name="detalle_gerente"),
    path("gerentes/<int:pk>/editar", views.EditarGerente.as_view(),name="editar_gerente"),
    path("gerentes/<int:pk>/borrar", views.BorrarGerente.as_view(),name="borrar_gerente"),
]
