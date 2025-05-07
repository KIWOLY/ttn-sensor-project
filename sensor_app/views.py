import os
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from .models import SensorData
from .serializers import SensorDataSerializer

@api_view(['POST'])
def ttn_webhook(request):
    WEBHOOK_SECRET = os.environ.get('WEBHOOK_SECRET')
    if request.headers.get('X-TTN-Secret') != WEBHOOK_SECRET:
        return JsonResponse({'error': 'Invalid secret'}, status=403)
    
    try:
        payload = request.data.get('uplink_message', {}).get('decoded_payload', {})
        sensor_data = SensorData(
            alcohol=payload.get('alcohol', 0.0),
            benzene=payload.get('benzene', 0.0),
            co2=payload.get('co2', 0.0),
            coord_lat=payload.get('coord_lat', 0.0),
            coord_lon=payload.get('coord_lon', 0.0),
            humidity=payload.get('humidity', 0.0),
            nox=payload.get('nox', 0.0),
            pressure=payload.get('pressure', 0.0),
            temperature=payload.get('temperature', 0.0),
        )
        sensor_data.save()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData.objects.all().order_by('-created_at')
    serializer_class = SensorDataSerializer