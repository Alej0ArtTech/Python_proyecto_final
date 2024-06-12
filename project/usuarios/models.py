from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    ap_paterno = models.CharField(max_length=20)
    ap_materno = models.CharField(max_length=20)
    genero = models.CharField(max_length=1)
    fec_nac = models.DateField()
    correo = models.CharField(max_length=30, null=True)
    contrasena = models.CharField(max_length=64)
    telefono = models.CharField(max_length=15)
    tipo_usuario = models.CharField(max_length=10)

class DireccionUsuario(models.Model):
    calle = models.CharField(max_length=50)
    num_ext = models.IntegerField()
    num_int = models.IntegerField(blank=True, null=True)
    colonia = models.CharField(max_length=50)
    municipio = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    cp = models.CharField(max_length=5)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class MetodoPagoUsuario(models.Model):
    tipo = models.CharField(max_length=20)
    numero_tarjeta = models.CharField(max_length=16)
    mes = models.CharField(max_length=2)
    anio = models.CharField(max_length=2)
    cvv = models.CharField(max_length=3)
    titular = models.CharField(max_length=50)
    dir_facturacion = models.TextField()
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)