from django.contrib import admin
from .models import EndPoint, Plant, Data

# Register your models here.

admin.site.register(EndPoint)
admin.site.register(Plant)
admin.site.register(Data)