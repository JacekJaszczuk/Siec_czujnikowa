from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Sensor(models.Model):
    name = models.TextField()
    topic = models.TextField()
    type = models.TextField()

    def __str__(self):
        return self.name

# Relacja wiele do wielu:
class Publication(models.Model):
    title = models.CharField(max_length=30)

    # Sortowanie po tytule:
    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title

class Article(models.Model):
    headline = models.CharField(max_length=100)
    publication = models.ManyToManyField(Publication)

    class Meta:
        ordering = ("headline",)

    def __str__(self):
        return self.headline

class Miejsca(models.Model):
    nazwa = models.CharField(max_length=30)
    opis = models.CharField(max_length=200)
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.nazwa