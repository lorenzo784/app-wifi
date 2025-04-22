from django.shortcuts import render
from django.http import JsonResponse
import random

def index(request):
    return render(request, 'ActualData.html')

def get_potentiometer_value(request):
    value = random.randint(0, 1023)
    return JsonResponse({
        'value': value,
        'voltage': round((value / 1023) * 5, 2),
        'resistance': round((value / 1023) * 10, 1)
    })