from django import forms
from .models import Producto, ProductoImagen
from .widgets import MultipleFileInput


class ProductoForm(forms.ModelForm):
    class Meta:
        imagenes = forms.FileField(widget=MultipleFileInput(), required=False)
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'descuento', 'id_categoria']
