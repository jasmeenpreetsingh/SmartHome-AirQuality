from django.http import JsonResponse
from .models import SensorData

def sensor_data(request):
    latest_data = SensorData.objects.last()
    data = {
        'co2': latest_data.co2,
        'particulate_matter': latest_data.particulate_matter,
        'voc': latest_data.voc
    }
    return JsonResponse(data)