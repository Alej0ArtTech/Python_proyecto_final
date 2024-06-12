from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

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
    imagen_url = models.CharField(max_length=2083)

    def __str__(self):
        return f"Imagen #{self.id_imagen} - Producto #{self.id_producto}"