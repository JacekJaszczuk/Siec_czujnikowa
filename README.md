# Siec_czujnikowa
Praca magisterska na temat sieci czujnikowej. Politechnika Wrocławska 2019

## Django

1. Tworzenie nowego projektu Djagno
```
django-admin startproject sensor_network3
```

2. Migracja bazy danych:
```
python manage.py migrate
```

3. Uruchomienie serwera:
```
python manage.py runserver
```

4. Dodanie użytkownika admin:
```
python manage.py createsuperuser
```

5. Tworzenie nowej aplikacji:
```
python manage.py startapp aplikacja
```

6. Tworzenie nowego modelu aplikacji:  
W pliku "aplikacja/models.py" możemy dodać:
``` Python
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # Automatycznie dodaje się jeszcze pole "ID".
```

7. Instalacja aplikacji:  
W pliku "sensor_network3/settings.py" dodajemy naszą aplikację do INSTALLED_APPS:
``` Python
INSTALLED_APPS = [
    #...
    'aplikacja',
    #...
]
```

8. Robimy migracje oraz je implementujemy:
```
python manage.py makemigrations
python manage.py migrate
```

9. Zarejestruj swoje modele w panelu administratora:  
Modyfikujemy plik "aplikacja/admin.py"
``` Python
from aplikacja.models import Person
admin.site.register(Person)
```