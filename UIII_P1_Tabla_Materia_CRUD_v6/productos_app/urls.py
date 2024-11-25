from django.urls import path
from productos_app import views

urlpatterns = [
    path("productos",views.inicio_vistaProductos,name="inicio_vistaProductos"),
    path("registrarProductos/",views.registrarProductos,name="registrarProductos"),
    path("seleccionarProductos/<id_productos>",views.seleccionarProductos,name="seleccionarProductos"),
    path("editarProductos/",views.editarProductos,name="editarProductos"),
    path("borrarProductos/<id_productos>",views.borrarProductos,name="borrarProductos")
]

