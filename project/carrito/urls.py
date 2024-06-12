from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('carrito/', views.carrito_view, name='carrito'),
    path('agregar_producto/<int:producto_id>/', views.agregar_producto_carrito, name='agregar_producto'),
]


