from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'sensor-data', views.SensorDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ttn-webhook/', views.ttn_webhook, name='ttn-webhook'),
]