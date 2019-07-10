from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from aplikacja.models import PersonView

# Create your views here.

def index(request):
    return HttpResponse("Witaj, tu aplikacja WWW sieci czujnikowej!")

def strona(request):
    return render(request, "aplikacja/strona.html")

class Generyczny(generic.ListView):
    template_name = "aplikacja/generyczny.html"
    context_object_name = "fajna_lista"

    def get_queryset(self):
        # Zwróć wszystkich Pacjentów:
        return PersonView.objects.all()

class Szczegoly(generic.DetailView):
    model = PersonView
    template_name = "aplikacja/szczegoly.html"
    #context_object_name = "fajny_obiekt" # A domyślna jest personview.