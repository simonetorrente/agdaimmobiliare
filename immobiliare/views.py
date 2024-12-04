from django.shortcuts import render, HttpResponse
from .models import Agenti, Immobili
def home(request):
    return render(request, 'home.html')
# Create your views here.

def agenti(request):
    items = Agenti.objects.all()
    return render(request, 'agenti.html', {"agenti":items})

def immobili(request):
    items = Immobili.objects.all()
    return render(request, 'immobili.html', {"immobili":items})

def immobile(request, pk):
    immobile = Immobili.objects.get(riferimento=pk)
    return render(request, 'immobile.html', {"immobile":immobile})

