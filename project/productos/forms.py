from django import forms
from .models import Producto
from .widgets import MultipleFileField

class ProductoForm(forms.ModelForm):
    imagenes = MultipleFileField(label='Seleccionar imágenes', required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'cantidad', 'descuento', 'id_categoria', 'imagenes']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Ingrese la descripción del producto'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el precio del producto'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese la cantidad disponible'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el descuento (opcional)'}),
            'id_categoria': forms.Select(attrs={'class': 'form-control'}),
        }