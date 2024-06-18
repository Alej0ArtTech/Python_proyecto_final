from django import forms
from .models import Producto
from .widgets import MultipleFileField

class ProductoForm(forms.ModelForm):
    imagenes = MultipleFileField(label='Seleccionar imágenes', required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'descuento', 'id_categoria', 'imagenes']