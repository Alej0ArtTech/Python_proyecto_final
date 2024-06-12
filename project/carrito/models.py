from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class Carrito(models.Model):
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class CarritoProducto(models.Model):
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)