from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('strona', views.strona, name='strona'),
    path('generyczny', views.Generyczny.as_view(), name='gneryczny')
]