from django.db import models

from categorias.models import Categoria  # Ajusta según la ubicación real de tus modelos



class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    descuento = models.IntegerField(null=True)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class ProductoImagen(models.Model):
    id_imagen = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='img_producto/', default='img_producto/image_default.jpeg')

    def __str__(self):
        return f"Imagen #{self.id_imagen} - Producto #{self.id_producto}"