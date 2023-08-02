# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailsSerializer

#добавить датчик и получить список всех датчиков
class CreateSensorView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

#получить данные конкретного датчика с температурами
class SensorChange(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailsSerializer

#добавить измерение и получить список всех измерений
class CreateMeasurement(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = MeasurementSerializer