from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Producto, ProductoImagen
from .forms import ProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'productos/productocategoria_list.html'

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/productocategoria_detail.html'

class ProductoCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/productocategoria_form.html'  # Aquí está el nombre correcto de la plantilla
    success_url = reverse_lazy('productos:productocategoria_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        for file in self.request.FILES.getlist('imagenes'):
            ProductoImagen.objects.create(id_producto=self.object, imagen=file)
        return response

    def test_func(self):
        return self.request.user.is_superuser

class ProductoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'productos/productocategoria_form.html'  # Aquí está el nombre correcto de la plantilla
    success_url = reverse_lazy('productos:productocategoria_list')

    def test_func(self):
        return self.request.user.is_superuser

class ProductoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Producto
    template_name = 'productos/confirm_delete.html'
    success_url = reverse_lazy('productos:productocategoria_list')

    def test_func(self):
        return self.request.user.is_superuser