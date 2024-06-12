from django.shortcuts import render

def registro_usuario(request):
    # Lógica para registrar un nuevo usuario
    return render(request, 'usuarios/registro.html')

def inicio_sesion(request):
    # Lógica para iniciar sesión de un usuario
    return render(request, 'usuarios/inicio_sesion.html')

def perfil_usuario(request):
    # Lógica para mostrar el perfil de usuario
    return render(request, 'usuarios/perfil.html')

def gestion_direcciones(request):
    # Lógica para gestionar las direcciones de usuario
    return render(request, 'usuarios/gestion_direcciones.html')

def gestion_metodos_pago(request):
    # Lógica para gestionar los métodos de pago del usuario
    return render(request, 'usuarios/gestion_metodos_pago.html')