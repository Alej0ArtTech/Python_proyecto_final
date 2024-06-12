from django.urls import path
from . import views

app_name = 'pedidos'

urlpatterns = [
    path('detalle_pedido/<int:pedido_id>/', views.pedido_detalle, name='detalle_pedido'),
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
]