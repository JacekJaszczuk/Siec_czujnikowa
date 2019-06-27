from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    
    #path('<int:sensor_id>/', views.detail, name='detail'),
    #path('<int:sensor_id>/results/', views.results, name='results'),
    #path('<int:sensor_id>/vote/', views.vote, name='vote'),
    #path('dodaj/', views.dodaj, name="dodaj"),
    #path('generyczny/', views.IndexView.as_view(), name='generyczny'),
    #path('alicja_login/', views.alicja_login, name="alicja_login"),
    #path('alicja_logout/', views.alicja_logout, name="alicja_logout"),
    #path('wymaga_logowania/', views.wymaga_logowania, name="wymaga_logowania"),
    #path('logowanie/', LoginView.as_view(template_name="aplikacja/logowanie.html"), name="logowanie"),
    
]