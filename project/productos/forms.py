from django import forms
from .models import Producto, ProductoImagen
from .widgets import MultipleFileInput
from categorias.models import Categoria


class ProductoForm(forms.ModelForm):
    imagenes = forms.FileField(widget=MultipleFileInput(), required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'descuento', 'id_categoria', 'imagenes']



