from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import re

from .models import EndPoint, Data
from .serializer import EndPointSerializer, DataSerializer

UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

# Create your views here.
@api_view(['GET'])
def getData(request):
    # endpoints = EndPoint.objects.all()
    # endpoints_serializer = EndPointSerializer(endpoints, many = True)
    # return Response(endpoints_serializer.data)
    data = Data.objects.all()
    data_serializer = DataSerializer(data, many = True)
    return Response(data_serializer.data)

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def checkConnection(request):
    try:
        uuid = request.GET["uuid"]
    except:
        uuid = None
    if uuid:
        if bool(UUID_PATTERN.match(uuid)):
            if EndPoint.objects.filter(uuid = uuid).exists():
                response = "SERVER OK"
            else:
                response = "DEVICE INVALID"
    else:
        response = "INVALID UUID"

    
    return Response(response)

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def postData(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = "SAVED"
    else:
        response = "INVALID DATA"
    return Response(response)