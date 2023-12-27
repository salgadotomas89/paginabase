from django.http import JsonResponse
from django.shortcuts import redirect, render

from comunicados.models import Comunicado, Comunicados

# Create your views here.


def actualizar_seccion_comunicados(request, color):
    Comunicados.objects.filter(id=1).update(background=color)

    return redirect('home')

def guardar_comunicado(request):
    if request.method == 'POST':
        # Acceder a los datos del comunicado enviados en la solicitud
        titulo = request.POST.get('titulo')
        texto = request.POST.get('texto')
        autor = request.POST.get('autor')

        # Realizar las operaciones necesarias para guardar los datos en el modelo
        
        # Ejemplo: Crear un nuevo objeto de Comunicado y guardar los datos
        comunicado = Comunicado(titulo=titulo, texto=texto, autor=autor)
        comunicado.save()

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Método de solicitud no válido'})
    