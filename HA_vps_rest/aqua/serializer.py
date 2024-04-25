from rest_framework import serializers
from .models import Tank

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = ('uuid', 'name', 'description')