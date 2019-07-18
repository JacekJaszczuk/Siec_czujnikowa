from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Miejsca, Pacjent, Pomiar
from cubes import Workspace

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
    if request.GET.get("czy_analiza", None):
        print("Super dokonaj analizy!")
        # Stwórz Workspace z pliku konfiguracyjnego:
        workspace = Workspace()
        workspace.register_default_store("sql", url="sqlite:///db.sqlite3")

        # Ładuj model:
        workspace.import_model("model.json")

        # Twórz obiekt browser:
        browser = workspace.browser("analiza_temperatura")

        # Twórz wyniki agregacji:
        if request.GET.get("wiek_pacjenta", None):
            res = browser.aggregate(drilldown=["wiek_pacjenta"])
            po_czym = "wiek_pacjenta"
        elif request.GET.get("data_pomiaru", None):
            res = browser.aggregate(drilldown=["data_pomiaru"])
            po_czym = "data_pomiaru"
        elif request.GET.get("kontynent", None):
            res = browser.aggregate(drilldown=["kontynent"])
            po_czym = "kontynent"
        elif request.GET.get("kraj", None):
            res = browser.aggregate(drilldown=["kraj"])
            po_czym = "kraj"
        elif request.GET.get("obszar", None):
            res = browser.aggregate(drilldown=["obszar"])
            po_czym = "obszar"

        # Wyświetl podsumowanie całkowite i dla grupy:
        lista = []
        print(res.summary)
        for r in res:
            print(type(r))
            print(r)
            lista.append(r)

        # Twórz kontekst:
        print(type(res))
        cont = {"agre_list": lista, "czy_analiza": True, "po_czym": po_czym}

    else:
        cont = {}
        print("Lipa")

    return render(request, "aplikacja/analiza/temperatura.html", cont)
