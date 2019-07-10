from django.db import models

# Create your models here.

# Klasa przedstawiająca człowieka:
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

# Widok na człowieka, ale z wiekiem, a nie z datą urodzenia:
class PersonView(models.Model):
    # Trzeba samemu dodać ID bo Djagno nie będzie samo zarzadzać tym modelem:
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    class Meta: # Konfiguracja jako widok.
        managed = False # Model niezarządzany przez Djagno.
        db_table = "aplikacja_person_view"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)