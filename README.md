# Siec_czujnikowa
Praca magisterska na temat sieci czujnikowej. Politechnika Wrocławska 2019

## Django

### Stworzenie nowego projektu:

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
### Dodanie admina i aplikacji:

4. Dodanie użytkownika admin:
```
python manage.py createsuperuser
```

5. Tworzenie nowej aplikacji:
```
python manage.py startapp aplikacja
```

### Stworzenie modelu:

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

10. Cofnięcie migracji i jej usunięcie:  
Dzięki temu można bez problemu zmodyfikować model danych:
```
python manage.py migrate aplikacja zero
rm aplikacja/migrations/0001_initial.py
```

11. Podgląd stworzonego SQLa:
```
python manage.py sqlmigrate aplikacja 0001
```

12. Uruchomienie Shella Pythonowego w Django:
```
python manage.py shell
```

13. Dodawanie nowego człowieka do bazy z poziomu Shella:
``` Python
from aplikacja.models import Person
Person.objects.all()                                     
#<QuerySet [<Person: Aleksander Kowal>]>
p = Person(first_name="Alicja", last_name="Kot", birth_date="1998-03-19")
p.save()
Person.objects.all()
#<QuerySet [<Person: Aleksander Kowal>, <Person: Alicja Kot>]>
```

### Bazodanowe widoki w Django:

14. Dodawanie bazodanowego widoku do Django:  
[Tutorial WWW](https://resources.rescale.com/using-database-views-in-django-orm/). W pliku "aplikacja/models.py" dodajemy:
``` Python
class PersonView(models.Model):
    # Trzeba samemu dodać ID bo Djagno nie będzie samo zarzadzać tym modelem:
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    
    class Meta: # Konfiguracja jako widok.
        managed = False # Model niezarządzany przez Djagno.
        db_table = "aplikacja_person_view"

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
```

15. Zrobienie migracji:
```
python manage.py makemigrations
```

16. Modyfikacja migracji polegająca na dodanie kodu SQL do stworzenia widoku:  
Modyfikujemy plik "aplikacja/migrations/0002_personview.py":
``` Python
migrations.RunSQL(
"""
CREATE VIEW aplikacja_person_view AS
SELECT
row_number() OVER () AS id,
p.first_name,
p.last_name,
date("now") - date(p.birth_date) AS age
FROM aplikacja_person AS p;
"""
```

17. Sprawdzamy czy generuje się dobry kod SQL:
```
python manage.py sqlmigrate aplikacja 0002
```

18. W odpowiedzi powinniśmy otrzymać:
``` SQL
BEGIN;
--
-- Create model PersonView
--
--
-- Raw SQL operation
--
CREATE VIEW aplikacja_person_view AS
SELECT
row_number() OVER () AS id,
p.first_name,
p.last_name,
date("now") - date(p.birth_date) AS age
FROM aplikacja_person AS p;
COMMIT;
```

19. Dokonujemy migracji:
```
python manage.py migrate
```

### Tworzenie widoków Django:

20. Tworzymy nasz pierwszy widok:  
W pliku "aplikacja/views.py" dodajemy:
``` Python
from django.http import HttpResponse
def index(request):
    return HttpResponse("Witaj, tu aplikacja WWW sieci czujnikowej!")
```

21. Dodajemy URLsa do naszego widoku:  
Robimy to w pliku "aplikacja/urls.py":
``` Python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

22. Dodajemy URLsa aplikacji, do głównego URLsa:  
Robimy to w pliku "sensor_network3/urls.py":
``` Python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("aplikacja/", include("aplikacja.urls"))
]
```

23. Tworzymy szablon HTML dla naszej strony:  
W pliku "aplikacja/templates/aplikacja/strona.html" dajemy:
``` HTML
<h1>To nasza strona WWW!</h1>
<h2>O tak!</h2>
```

24. Dodajemy w URLs:
``` Python
path('strona', views.strona, name="strona")
```

25. A widoku dodajemy:
``` Python
from django.shortcuts import render

def strona(request):
    return render(request, "aplikacja/strona.html")
```

### Widoki generyczne

26. Widoki generyczne:  
W pliku "aplikacja/urls.py" dodajemy:
``` Python
path('generyczny', views.Generyczny.as_view(), name='gneryczny')
```

27. W pliku "aplikacja/views.py" dodajemy widok generyczny:
``` Python
class Generyczny(generic.ListView):
    template_name = "aplikacja/generyczny.html"
    context_object_name = "fajna_lista"

    def get_queryset(self):
        # Zwróć wszystkich Pacjentów:
        return PersonView.objects.all()
```

28. Tworzymy szablon dla widoku generycznego:  
Tworzymy plik "aplikacja/templates/aplikacja/generyczny.html" i zapisujemy:
``` HTML
<h1>Lista pacjentów</h1>
{% for p in fajna_lista %}
    <li>{{ p }} Wiek: {{ p.age }}</li>
{% endfor %}
```

29. Dodanie plików statycznych:  
Pliki statyczne należy dodać do "aplikacja/static/aplikacja".

30. Stworzenie szablonu bazowego:
W pliku "aplikacja/template/aplikacja/base.html" tworzymy szablon bazowy:
``` HTML
<h1>Hej! Witaj w naszej aplikacji!</h1>
{% block content %}{% endblock %}
```

31. Następnie należy rozszerzyć stronę:
``` HTML
{% extends "aplikacja/base.html" %}
{% block content %}
<h1>To nasza strona WWW!</h1>
<h2>O tak!</h2>
{% endblock %}
```

32. Tworzenie widoku LoginView:  
W pliku "aplikacja/views.py" definiujemy widok logowania:
``` Python
from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name = "aplikacja/login.html"
    cont = {"next": "strona"}
    extra_context = cont
```

33. Tworzymy templatkę widoku wylogowania:  
Dodajemy plik "aplikacja/templates/aplikacja/login.html":
``` HTML
<h1>Zaloguj się!</h1>
<h2>Witaj {{ user }}!</h2>
<h3>Twój next: {{ next }}</h3>

{% if form.errors %}
<p>Your username and password didn't match. Please try again.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}
    <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
    </table>
    
    <input type="submit" value="login">
    <input type="hidden" name="next" value="{{ next }}">
</form>
```

34. Tworzenie widoku LogoutView:  
W pliku "aplikacja/views.py" definiujemy widok wylogowania:
``` Python
from django.contrib.auth.views import LogoutView
class Logout(LogoutView):
    # Ale można też zrobić specjalny widok dla wylogowanych:
    #template_name = "aplikacja/strona.html"
    #cont = {"next": "strona"}
    #extra_context = cont
    # Można dać też samo next_page, wtedy nie dajemy strony pośredniej:
    next_page = "strona_fajne_to"
```

35. Dodawanie praw dostępu do części serwisu:  
Można dodać dekorator do widoku:
``` Python
from django.contrib.auth.decorators import permission_required
@permission_required("aplikacja.view_personview", login_url="login")
def wymaga_prawa(request):
    return render(request, "aplikacja/wymaga_prawa.html")
```

36. Albo sprawdzanie w szablonie:
``` HTML
{% if perms.aplikacja.view_personview %}
<h4>Ach to Ty! Pewnie jesteś analitykiem!</h4>
{% endif %}
```
