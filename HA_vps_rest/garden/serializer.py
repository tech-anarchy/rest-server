from rest_framework import serializers
from .models import EndPoint, Plant, PlantAutoData

class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = ('uuid', 'name', 'type' ,'description')

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = ('uuid', 'name', 'location' ,'description')

class PlantAutoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAutoData
        fields = ('endpoint', 'plant', 'temparature', 'humidity' ,'ph', 'moisture', 'time')