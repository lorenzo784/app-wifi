from django.shortcuts import render
from django.http import JsonResponse
from .models import DispositivoIoT

# Create your views here.
def index(request):
    dispositivo = DispositivoIoT.objects.first()
    return render(request, 'Index.html', {'dispositivo': dispositivo})

def cambiar_estado(request):
    dispositivo = DispositivoIoT.objects.first()

    if dispositivo:
        dispositivo.encendido = not dispositivo.encendido
        dispositivo.save()

        return JsonResponse({'encendido': dispositivo.encendido})
    return JsonResponse({'error': 'Dispositivo no encontrado'}, status=404)

def obtener_estado(request):
    dispositivo = DispositivoIoT.objects.first()

    if dispositivo:
        return JsonResponse({'encendido': dispositivo.encendido})
    
    return JsonResponse({'error': 'Dispositivo no encontrado'}, status=404)