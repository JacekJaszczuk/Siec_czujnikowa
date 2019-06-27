from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('<int:place_id>/', views.place_detail, name="place_detail"),
    path('<int:place_id>/<int:device_id>', views.device_detail, name="device_detail"),
    path('<int:place_id>/<int:device_id>/<int:redisfield_id>', views.redisfield_detail, name="redisfield_detail"),  
]