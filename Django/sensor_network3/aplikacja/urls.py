from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('strona', views.strona, name='strona_fajne_to'),
    path('generyczny', views.Generyczny.as_view(), name='generyczny'),
    path('szczegoly/<int:pk>', views.Szczegoly.as_view(), name="szczegoly"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('wymaga_prawa', views.wymaga_prawa, name="wymaga_prawa")
]