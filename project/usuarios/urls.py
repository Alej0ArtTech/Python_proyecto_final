from django.urls import path
from usuarios import views

urlpatterns = [
    path('registro/', views.registro_usuario, name='registro_usuario'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('direcciones/', views.gestion_direcciones, name='gestion_direcciones'),
    path('metodos-pago/', views.gestion_metodos_pago, name='gestion_metodos_pago'),
]