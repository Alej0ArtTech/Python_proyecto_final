from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Categoria, Producto

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
