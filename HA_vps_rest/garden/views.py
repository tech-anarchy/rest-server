from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

import re
import json
import uuid
from datetime import datetime

from django.contrib.auth.models import User
from .models import EndPoint, PlantAutoData, Plant, PlantUsrData
from .serializer import EndPointSerializer, PlantAutoDataSerializer, PlantSerializer, PlantUsrDataSerializer

UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

# Create your views here.
@api_view(['GET'])
def getData(request):
    data = Plant.objects.all()
    data_serializer = PlantSerializer(data, many = True)
    return Response(data_serializer.data)

@api_view(['GET'])
def getPlant(request, uuid):
    if bool(UUID_PATTERN.match(uuid)):
        try:
            plant = Plant.objects.get(uuid = uuid)
        except:
            return Response('INVALID PLANT')
    else:
        return Response('INVALID QUERY')
    
    usr_data = PlantUsrData.objects.filter(plant = plant).order_by('-date')
    # auto_data = PlantAutoData.objects.filter(plant = plant)

    plant_serializer = PlantSerializer(plant)
    usr_data_serializer  = PlantUsrDataSerializer(usr_data, many = True)

    response = {
        "plant" : plant_serializer.data,
        "usr_data" : usr_data_serializer.data
    }

    return Response(response)

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
    serializer = PlantAutoDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = "SAVED"
    else:
        response = "INVALID DATA"
    return Response(response)


@api_view(['POST'])
def postFertilizer(request):
    
    msg = []
    try:
        username = request.data['user']
        user = User.objects.get(username = username)
    except:
        msg.append("Invalid User")

    plants = []
    try:
        # plants = filter(None, request.data['plants'].split(","))
        plants = request.data['plants']
    except:
        msg.append("No Plants provided")

    try:
        fertilizer = request.data['fertilizer']
    except:
        fertilizer = None

    try:
        comments = request.data['comments'] 
    except:
        comments = None

    if (fertilizer is None or fertilizer == "") and (comments is None or comments == ""):
        msg.append("Invalid Fertilizer/Notes")

    try:
        rawDate = request.data['date']
        date = datetime.strptime(rawDate[0], "%d-%b-%Y").date()
    except:
        msg.append("No Date provided")

    if plants:
        for plant_id in plants:
            save = False
            if bool(UUID_PATTERN.match(plant_id)):
                try:
                    plant = Plant.objects.get(uuid = plant_id)
                    save = True
                except:
                    msg.append("Invalid Plant : " + str(plant_id))
            else:
                msg.append("Invalid Plant ID : " + str(plant_id))


            if save and msg == []:
                data = {
                    "user": user.pk,
                    "plant": plant_id,
                    "fertilizer": fertilizer,
                    "date": date,
                    "notes": comments
                }
                serializer = PlantUsrDataSerializer(data = data)
                if serializer.is_valid():
                    serializer.save()
                    msg.append("Saved : " + str(plant.name))
                else:
                    msg.append("Invalid Data : " + str(plant.name))

    return Response(msg)

@api_view(['POST'])
def addPlant(request):
    msg = []
    try:
        plant = request.data['plant']
        if plant is None or plant == "":
            msg.append("Invalid Plant")
    except:
        msg.append("No Fertilizer provided")

    try:
        plantType = request.data['type']
        if plantType is None or plantType == "":
            msg.append("Invalid Type")
    except:
        msg.append("No Type provided")

    try:
        location = request.data['location']
        if location is None or location == "":
            msg.append("Invalid Location")
    except:
        msg.append("No Location provided")

    try:
        description = request.data['description']
        if description is None or description == "":
            description = json.dumps('NA')
    except:
        msg.append("No Description provided")

    if msg == []:

        data = {
            'uuid' : uuid.uuid4(),
            'name' : plant,
            'location' : location,
            'type' : plantType,
            'description' : description
        }
        serializer = PlantSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            msg.append("Saved")
        else :
            msg.append("Invalid Data")

    return Response(msg)
