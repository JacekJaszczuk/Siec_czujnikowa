from django.contrib import admin
from aplikacja.models import Pacjent, Miejsca, Pomiar

# Register your models here.
admin.site.register(Pacjent)
admin.site.register(Miejsca)

class PomiarAdmin(admin.ModelAdmin):
    list_display = ("data", "typ_pomiaru", "wartosc", "miejsce", "pacjent")

admin.site.register(Pomiar, PomiarAdmin)