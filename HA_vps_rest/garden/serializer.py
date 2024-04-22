from rest_framework import serializers
from .models import EndPoint, Plant, PlantAutoData, PlantUsrData

class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = ('uuid', 'name', 'type' ,'description')

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ('uuid', 'name', 'location' ,'description')

class PlantAutoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantAutoData
        fields = ('endpoint', 'plant', 'temparature', 'humidity' ,'ph', 'moisture', 'time')

class PlantUsrDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantUsrData
        fields = ('user', 'plant', 'fertilizer', 'notes', 'time')