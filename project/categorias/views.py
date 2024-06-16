
from django.shortcuts import render, get_object_or_404, redirect
from .models import Categoria
from .forms import CategoriaForm

def categoria_list_view(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categoria_list.html', {'categorias': categorias})

def categoria_detail_view(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'categorias/categoria_detail.html', {'categoria': categoria})

def categoria_create_view(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categoria_list')  # Redirigir a la lista de categorías después de crear una nueva
    else:
        form = CategoriaForm()
    return render(request, 'categorias/categoria_form.html', {'form': form})

def categoria_delete_view(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method == 'POST':
        categoria.delete()
        return redirect('categoria_list')  # Redirigir a la lista de categorías después de eliminar
    return render(request, 'categorias/categoria_confirm_delete.html', {'categoria': categoria})