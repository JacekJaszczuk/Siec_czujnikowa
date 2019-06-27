from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    user = models.ManyToManyField(User)

class Device(models.Model):
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    place = models.ForeignKey(Place, on_delete = models.CASCADE)

class RedisField(models.Model):
    key_name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 200)
    device = models.ForeignKey(Device, on_delete = models.CASCADE)