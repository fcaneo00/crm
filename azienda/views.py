from .models import Collaboratore, Ruolo
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    collaboratori = Collaboratore.objects.all().values()

    template = loader.get_template('collaboratori.html')
    context = {
        "collaboratori": collaboratori,
    }

    return HttpResponse(template.render(context, request))

def formAdd(request):
    template = loader.get_template('addCollaboratore.html')
    ruoli = Ruolo.objects.all().values()
    context = {
        "ruoli": ruoli
    }
    return HttpResponse(template.render(context, request))

def addRecord(request):

    collaboratore = Collaboratore(
        codiceFiscale = request.POST['codiceFiscale'],
        nome = request.POST['nome'],
        cognome = request.POST['cognome'],
        indirizzo = request.POST['indirizzo'],
        email = request.POST['email'],
        telefono = request.POST['telefono'],
        cellulare = request.POST['cellulare'],
        ruolo = Ruolo(request.POST['ruolo']),
    )

    collaboratore.save()
    
    return HttpResponseRedirect(reverse(index))

