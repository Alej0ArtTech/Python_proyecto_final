from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Producto, ProductoImagen
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/productocategoria_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'producto/productocategoria_detail.html'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/productocategoria_form.html'
    success_url = reverse_lazy('producto:productocategoria_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        for file in self.request.FILES.getlist('imagenes'):
            ProductoImagen.objects.create(id_producto=self.object, imagen=file)
        return response

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'producto/productocategoria_form.html'
    success_url = reverse_lazy('producto:productocategoria_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/confirm_delete.html'
    success_url = reverse_lazy('producto:productocategoria_list')