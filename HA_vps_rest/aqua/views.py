from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import Tank
from.serializer import TankSerializer

# Create your views here.

@api_view(['GET'])
def getData(request):
    data = Tank.objects.all()
    data_serializer = TankSerializer(data, many = True)
    return Response(data_serializer.data)
