from django.db import models
from usuarios.models import Usuario
from productos.models import Producto

class EstadoPedido(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.PROTECT)

class PedidoProducto(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)