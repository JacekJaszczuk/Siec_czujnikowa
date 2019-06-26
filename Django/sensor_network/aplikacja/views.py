from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Sensor

# Create your views here.
def index(request):
    sensor_list = Sensor.objects.all()
    template = loader.get_template('aplikacja/index.html')
    context = { 'sensor_list': sensor_list }
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