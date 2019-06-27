from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate
from .models import Place, Device

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user.username
        place_list = request.user.place_set.all()
    else:
        user = "Anonymous"
        place_list = []

    context = {"user": user, "place_list": place_list}

    return render(request, "app/index.html", context)

def login(request):
    if request.POST:
        user = auth_authenticate(username = request.POST["user"], password = request.POST["password"])
        if user is not None:
            auth_login(request, user)
        return HttpResponseRedirect(reverse("app:index"))
    else:
        return render(request, "app/login.html")

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("app:index"))

def place_detail(request, place_id):
    user = request.user.username
    place = Place.objects.get(id=place_id)
    device_list = place.device_set.all()

    context = {"user": user, "device_list": device_list}

    return render(request, "app/place_detail.html", context)

def device_detail(request, place_id, device_id):
    user = request.user.username
    device = Device.objects.get(id=device_id)
    redisfield_list = device.redisfield_set.all()

    context = {"user": user, "redisfield_list": redisfield_list, "place_id": place_id}

    return render(request, "app/device_detail.html", context)

def redisfield_detail(request, place_id, device_id, redisfield_id):
    return HttpResponse("To już jest koniec!")
