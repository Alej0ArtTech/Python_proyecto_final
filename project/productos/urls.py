from django.urls import path
from . import views

app_name = 'producto'

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='productocategoria_list'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='productocategoria_detail'),
    path('producto/nuevo/', views.ProductoCreateView.as_view(), name='productocategoria_create'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='productocategoria_update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='productocategoria_delete'),
]