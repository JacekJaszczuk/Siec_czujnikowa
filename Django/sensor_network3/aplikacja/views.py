from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from aplikacja.models import PersonView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import permission_required

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

class Login(LoginView):
    template_name = "aplikacja/login.html"
    cont = {"next": "strona"}
    extra_context = cont

class Logout(LogoutView):
    #template_name = "aplikacja/strona.html"
    #cont = {"next": "strona"}
    #extra_context = cont
    next_page = "strona_fajne_to"

@permission_required("aplikacja.view_personview", login_url="login")
def wymaga_prawa(request):
    print("Twój user: {}".format(request.user))
    return render(request, "aplikacja/wymaga_prawa.html")