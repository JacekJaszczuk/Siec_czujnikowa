from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Miejsca, Pacjent, Pomiar

# Create your views here.
def index(request):
    return render(request, "aplikacja/index.html")

class Zaloguj(LoginView):
    template_name = "aplikacja/zaloguj.html"
    cont = {"next": "/aplikacja/"}
    extra_context = cont

class Wyloguj(LogoutView):
    next_page = "index"

# Widok który nie używa csrf:
@csrf_exempt
def api(request):
    # Dla metody POST przetwarzaj dane i zapisz je w bazie:
    if request.method == "POST":
        pomiar = request.body
        print(pomiar)
        try:
            pomiar = json.loads(pomiar)
            miejsce = Miejsca.objects.get(id=pomiar["miejsce"])
            pacjent = Pacjent.objects.get(id=pomiar["pacjent"])
            p = Pomiar(data=pomiar["data"], miejsce=miejsce, pacjent=pacjent, typ_pomiaru=pomiar["typ_pomiaru"], wartosc=pomiar["wartosc"])
            p.save()
        except Exception as e:
            return HttpResponse(status=201)
        return HttpResponse(status=200)

    # Dla pozostałych metod zwróć stronę z informacjami jak korzystać z API:    
    return render(request, "aplikacja/api.html")

def analiza_temperatura(request):
    return render(request, "aplikacja/analiza/temperatura.html")
