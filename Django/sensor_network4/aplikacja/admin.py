from django.contrib import admin
from aplikacja.models import Pacjent, Miejsca, Pomiar

# Register your models here.
class PacjentAdmin(admin.ModelAdmin):
    list_display = ("id", "data_urodzenia", "imie", "nazwisko")
admin.site.register(Pacjent, PacjentAdmin)

class MiejscaAdmin(admin.ModelAdmin):
    list_display = ("id", "kontynent", "kraj", "obszar")
admin.site.register(Miejsca, MiejscaAdmin)

class PomiarAdmin(admin.ModelAdmin):
    list_display = ("data", "typ_pomiaru", "wartosc", "miejsce", "pacjent")

admin.site.register(Pomiar, PomiarAdmin)