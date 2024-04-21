from django.contrib import admin
from .models import EndPoint, Plant, PlantAutoData, PlantUsrData

# Register your models here.

admin.site.register(EndPoint)
admin.site.register(Plant)
admin.site.register(PlantAutoData)
admin.site.register(PlantUsrData)