from django.db import models

# Create your models here.
class Sensor(models.Model):
    name = models.TextField()
    topic = models.TextField()
    type = models.TextField()

    def __str__(self):
        return self.name