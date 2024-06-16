from django.urls import path
from categorias import views

urlpatterns = [
    path('', views.categoria_list_view, name='categoria_list'),
    path('<int:pk>/', views.categoria_detail_view, name='categoria_detail'),
    path('crear/', views.categoria_create_view, name='categoria_create'),
    path('<int:pk>/eliminar/', views.categoria_delete_view, name='categoria_delete'),
]