from django.db import models

# Create your models here.
class EndPoint(models.Model):
    uuid = models.UUIDField(unique = True)
    name = models.CharField(max_length = 140)
    type = models.CharField(max_length = 140, default="NULL")
    description = models.TextField()

    def __str__(self):
        return self.name + ":" + str(self.uuid)
    
class Plant(models.Model):
    uuid = models.UUIDField(unique = True)
    name = models.CharField(max_length = 140)
    location = models.CharField(max_length = 140, default="NULL")
    description = models.TextField()

    def __str__(self):
        return self.name + ":" + str(self.uuid)
    
class Data(models.Model):
    endpoint = models.ForeignKey(EndPoint, to_field="uuid", db_column="endpoint", on_delete=models.CASCADE, null=True, blank=True)
    plant = models.ForeignKey(Plant, to_field="uuid", db_column="plant", on_delete=models.CASCADE, null=True, blank=True)
    temparature = models.FloatField(null=True, blank=True, default=None)
    humidity = models.FloatField(null=True, blank=True, default=None)
    ph = models.FloatField(null=True, blank=True, default=None)
    moisture = models.FloatField(null=True, blank=True, default=None)
    time = models.TimeField(auto_now=True)
