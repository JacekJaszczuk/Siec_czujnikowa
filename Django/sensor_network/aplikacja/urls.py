from django.urls import path
from . import views

app_name = 'aplikacja'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:sensor_id>/', views.detail, name='detail'),
    path('<int:sensor_id>/results/', views.results, name='results'),
    path('<int:sensor_id>/vote/', views.vote, name='vote'),
]