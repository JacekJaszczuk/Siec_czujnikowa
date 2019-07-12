from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('zaloguj', views.Zaloguj.as_view(), name='zaloguj'),
    path('wyloguj', views.Wyloguj.as_view(), name='wyloguj'),
    path('api', views.api, name='api'),
    path('analiza/temperatura', views.analiza_temperatura, name='analiza_temperatura')
]