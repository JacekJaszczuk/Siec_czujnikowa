from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Witaj, tu aplikacja WWW sieci czujnikowej!")

def strona(request):
    return render(request, "aplikacja/strona.html")