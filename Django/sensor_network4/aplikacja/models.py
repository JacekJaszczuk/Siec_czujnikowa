from django.db import models

# Create your models here.

class Pacjent(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.DateField()

    def __str__(self):
        return "{} {}".format(self.imie, self.nazwisko)

class Miejsca(models.Model):
    kontynent = models.CharField(max_length=30)
    kraj = models.CharField(max_length=30)
    obszar = models.CharField(max_length=30)

    def __str__(self):
        return "{} {} {}".format(self.kontynent, self.kraj, self.obszar)

class Pomiar(models.Model):
    data = models.DateField()
    miejsce = models.ForeignKey(Miejsca, models.CASCADE)
    pacjent = models.ForeignKey(Pacjent, models.CASCADE)
    typ_pomiaru = models.CharField(max_length=30)
    wartosc = models.FloatField()

    def __str__(self):
        return "{} {}".format(self.data, self.typ_pomiaru)
