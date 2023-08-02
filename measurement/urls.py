from django.urls import path
from measurement.views import CreateSensorView, SensorChange, CreateMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', CreateSensorView.as_view()),
    path('sensors/<pk>', SensorChange.as_view()),
    path('measurements/', CreateMeasurement.as_view()),
]
