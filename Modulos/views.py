from django.shortcuts import render
from django.http import JsonResponse
import random
from .models import DatoSensor
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    return render(request, 'ActualData.html')

def get_potentiometer_value(request):
    last_data = DatoSensor.objects.last()
    
    if last_data:
        voltage = round((last_data.valor / 1023) * 5, 2)
        resistance = round((last_data.valor / 1023) * 10, 1)
        
        return JsonResponse({
            'value': last_data.valor,
            'voltage': voltage,
            'resistance': resistance,
            'timestamp': last_data.fecha.strftime('%Y-%m-%d %H:%M:%S')
        })
    else:
        return JsonResponse({
            'error': 'No data available'
        })
    
def get_humidity(request):
    last_data = DatoSensor.objects.last()
    if last_data:
        return JsonResponse({'value': last_data.temperatura})
    return JsonResponse({'error': 'No data available'})

def get_distance(request):
    last_data = DatoSensor.objects.last()
    if last_data:
        return JsonResponse({'value': last_data.distancia})
    return JsonResponse({'error': 'No data available'})

@csrf_exempt
def set_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            valor = data.get("valor")
            humedad = data.get("humedad")
            temperatura = data.get("temperatura")
            distancia = data.get("distancia")

            if valor is not None:
                DatoSensor.objects.create(
                    valor=valor,
                    humedad=humedad,
                    temperatura=temperatura,
                    distancia=distancia
                )
                return JsonResponse({"status": "ok", "mensaje": "Datos guardados"})
            else:
                return JsonResponse({"status": "error", "mensaje": "Valor no proporcionado"}, status=400)

        except Exception as e:
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=400)

    return JsonResponse({"mensaje": "Método no permitido"}, status=405)

def historial(request):
    datos = DatoSensor.objects.order_by('-fecha')[:50]
    historial = []

    for dato in datos:
        historial.append({
            "fecha": dato.fecha.strftime("%Y-%m-%d %H:%M:%S"),
            "valor": dato.valor
        })

    # Retorna el historial como un JSON
    return JsonResponse({"historial": historial})