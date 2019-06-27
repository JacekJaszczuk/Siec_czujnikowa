from django.contrib import admin
from .models import Sensor, Article, Publication, Miejsca

# Register your models here.
class SensorAdmin(admin.ModelAdmin):
    #fields = ["type", "name", "topic"]
    fieldsets = [
        (None, {"fields": ["type", "name"]}),
        ("Inne informacje", {"fields": ["topic"]})
    ]
    list_display = ("name", "topic", "type")

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["headline"]

class MiejscaAdmin(admin.ModelAdmin):
    list_display = ["nazwa", "opis"]

admin.site.register(Sensor, SensorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Publication)
admin.site.register(Miejsca, MiejscaAdmin)