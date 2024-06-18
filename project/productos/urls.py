from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='productocategoria_list'),
    path('nuevo/', views.ProductoCreateView.as_view(), name='productocategoria_create'),
    path('<int:pk>/', views.ProductoDetailView.as_view(), name='productocategoria_detail'),
    path('<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='productocategoria_update'),
    path('<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='productocategoria_delete'),
    path('crear/', views.ProductoCreateView.as_view(), name='create_product'),

]