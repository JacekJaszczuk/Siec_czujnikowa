from django.contrib import admin
from .models import RedisField, Device, Place

# Register your models here.
class RedisFieldAdmin(admin.ModelAdmin):
    list_display = ["key_name", "description", "device"]

class DeviceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "place"]

class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

admin.site.register(RedisField, RedisFieldAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Place, PlaceAdmin)