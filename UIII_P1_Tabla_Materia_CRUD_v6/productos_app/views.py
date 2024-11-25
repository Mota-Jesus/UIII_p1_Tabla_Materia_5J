from django.shortcuts import render,redirect
from .models import Productos

# Create your views here.
def inicio_vistaProductos(request):
    losproductos=Productos.objects.all()
    return render(request,"gestionarProductos.html",{"misproductos":losproductos})

def registrarProductos(request):
    id_productos=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    categoria=request.POST["txtcategoria"]
    fecha_añadido=request.POST["datefecha_a"]

    guardarproductos=Productos.objects.create(
        id_productos=id_productos,nombre=nombre,descripcion=descripcion,precio=precio,stock=stock,categoria=categoria,fecha_añadido=fecha_añadido
    ) #GUARDA EL REGISTRO

    return redirect("productos")

def seleccionarProductos(request,id_productos):
    productos=Productos.objects.get(id_productos=id_productos)
    return render(request,"editarproductos.html",{"misproductos":productos})

def editarProductos(request):
    id_productos=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    descripcion=request.POST["txtdescripcion"]
    precio=request.POST["numprecio"]
    stock=request.POST["numstock"]
    categoria=request.POST["txtcategoria"]
    fecha_añadido=request.POST["datefecha_a"]
    productos=Productos.objects.get(id_productos=id_productos)
    productos.nombre=nombre
    productos.descripcion=descripcion
    productos.precio=precio
    productos.stock=stock
    productos.categoria=categoria
    productos.fecha_añadido=fecha_añadido
    productos.save() #GUARDA REGISTRO ACTUALIZADO
    return redirect("productos")

def borrarProductos(request,id_productos):
    productos=Productos.objects.get(id_productos=id_productos)
    productos.delete() #BORRA EL REGISTRO
    return redirect("productos")