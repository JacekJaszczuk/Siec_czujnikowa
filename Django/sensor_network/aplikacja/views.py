from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Sensor

# Create your views here.
def index(request):
    sensor_list = Sensor.objects.all()
    template = loader.get_template('aplikacja/index.html')
    if request.user.is_authenticated:
        lipa = "O super! Znamy Cię! Witaj {}".format(request.user.username)
    else:
        lipa = "Witaj nieznajomy!"
    context = { 'sensor_list': sensor_list, 'lipa': lipa }
    #return HttpResponse(template.render(context, request))
    return render(request, 'aplikacja/index.html', context)

def detail(request, sensor_id):
    print("HOHOHOH!")
    print(type(sensor_id))
    try:
        sensor = Sensor.objects.get(id=sensor_id)
    except Sensor.DoesNotExist:
        #return HttpResponse("Nie ma takiego czujnika! {}".format(e))
        raise Http404("Taki czujnik nie istnieje!")
    print("HIHIHI!")
    print(sensor)
    return HttpResponse("Detale dla czujnika {} {} {} {}".format(sensor_id, sensor.name, sensor.topic, sensor.type))

def results(request, sensor_id):
    s = get_object_or_404(Sensor, id=sensor_id)
    context = {"czujniki": s}
    return render(request, 'aplikacja/res.html', context)

def vote(request, sensor_id):
    return HttpResponse("O rany to jest numer %s" % sensor_id)

def dodaj(request):
    if request.POST:
        print("To POST!")
        s = Sensor(name=request.POST["name"], topic=request.POST["topic"], type=request.POST["type"])
        s.save()
        return HttpResponseRedirect(reverse("aplikacja:dodaj"))
    return render(request, "aplikacja/dodaj.html")

class IndexView(generic.ListView):
    template_name = "aplikacja/index.html"
    context_object_name = "sensor_list"

    def get_queryset(self):
        return Sensor.objects.all()

def alicja_login(request):
    u = User.objects.get(username="Alicja")
    login(request, u)
    return HttpResponse("Alicja została zalogowana!")

def alicja_logout(request):
    logout(request)
    return HttpResponse("Alicja została wylogowana!")

@login_required()
def wymaga_logowania(request):
    return HttpResponse("Ta strona wymaga logowania! Więc Cię witamy!")