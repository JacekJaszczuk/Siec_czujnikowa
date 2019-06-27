from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate as auth_authenticate

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user = request.user.username
    else:
        user = "Anonymous"

    context = {"user": user}

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
