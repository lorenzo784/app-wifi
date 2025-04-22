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

@csrf_exempt
def set_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            valor = data.get("valor")

            if valor is not None:
                DatoSensor.objects.create(valor=valor)
                return JsonResponse({"status": "ok", "mensaje": "Valor guardado"})
            else:
                return JsonResponse({"status": "error", "mensaje": "Valor no proporcionado"}, status=400)

        except Exception as e:
            return JsonResponse({"status": "error", "mensaje": str(e)}, status=400)

    return JsonResponse({"mensaje": "Método no permitido"}, status=405)