from django.urls import path
from . import views

urlpatterns = [
    path('api/sensor-data/', views.sensor_data, name='sensor_data'),
]