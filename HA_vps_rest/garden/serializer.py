from rest_framework import serializers
from .models import EndPoint, Plant, Data

class EndPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = ('uuid', 'name', 'type' ,'description')

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields = ('uuid', 'name', 'location' ,'description')

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('endpoint', 'plant', 'temparature', 'humidity' ,'ph', 'moisture')