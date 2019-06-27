from django.contrib import admin
from .models import Sensor

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    #fields = ["type", "name", "topic"]
    fieldsets = [
        (None, {"fields": ["type", "name"]}),
        ("Inne informacje", {"fields": ["topic"]})
    ]
    list_display = ("name", "topic", "type")

admin.site.register(Sensor, SensorAdmin)