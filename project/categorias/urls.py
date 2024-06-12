from django.urls import path
from categorias import views

urlpatterns = [
    path('', views.listar_categorias, name='listar_categorias'),
    path('crear/', views.crear_categoria, name='crear_categoria'),
]