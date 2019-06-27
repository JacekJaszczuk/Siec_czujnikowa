from django.contrib import admin
from .models import RedisField, Device, Place

# Register your models here.
admin.site.register(RedisField)
admin.site.register(Device)
admin.site.register(Place)