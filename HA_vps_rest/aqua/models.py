from django.db import models
from django.contrib.auth.models import User

from .choices import *

# Create your models here.
class Tank(models.Model):
    uuid = models.UUIDField(unique = True)
    name = models.CharField(max_length = 140)
    description = models.TextField()

    def __str__(self):
        return self.name + ":" + str(self.uuid)

class TankUsrData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tank = models.ForeignKey(Tank, to_field="uuid", db_column="tank", on_delete=models.CASCADE)

    ammonia = models.FloatField(null=True, blank=True, default=None)
    phosphate = models.FloatField(null=True, blank=True, default=None)

    calcium = models.IntegerField(null=True, blank=True, default=None)
    magnesium = models.IntegerField(null=True, blank=True, default=None)

    ph = models.FloatField(null=True, blank=True, default=None)
    dkh = models.FloatField(null=True, blank=True, default=None)

    temparature = models.FloatField(null=True, blank=True, default=None)

    nitrate = models.FloatField(null=True, blank=True, default=None)
    nitrite = models.FloatField(null=True, blank=True, default=None)

    salinity = models.FloatField(null=True, blank=True, default=None)

    b_filterCarbon = models.BooleanField(null=True, blank=True, default=False)
    b_filterAmmonia = models.BooleanField(null=True, blank=True, default=False)
    b_filterPhosphate = models.BooleanField(null=True, blank=True, default=False)
    b_filterSponges = models.BooleanField(null=True, blank=True, default=False)

    water_change = models.IntegerField(null=True, blank=True, default=None)

    dose = models.CharField(max_length=2, choices=DOSE_CHOICES, null=True, blank=True, default=None)

    comment = models.TextField(null=True, blank=True)
    time = models.TimeField(auto_now=True)


