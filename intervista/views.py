from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from azienda.models import Collaboratore
from django.template import loader
from django.shortcuts import render
from django.urls import reverse
from utils import get_db_handle, get_collection_handle

# Mongodb connection
db = get_db_handle('crm', 'localhost', 27017, 'mongoadmin', 'mongoadmin')
collection = get_collection_handle(db, 'intervista')

# Create your views here.

def index(request):
    interviste = collection.find()
    
    template = loader.get_template('interviste.html')
    context = {
        "interviste": interviste
    }

    return HttpResponse(template.render(context, request))


def formAdd(request):
    template = loader.get_template('addIntervista.html')
    collaboratori = Collaboratore.objects.all().values()
    context = {
        "collaboratori": collaboratori
    }
    return HttpResponse(template.render(context, request))


def addRecord(request):
    cliente = request.POST['nome']
    commento = request.POST['commento']
    collaboratore = request.POST['collaboratore']
    data = datetime.now().date()
    orario = datetime.now().time()

    intervista = {
        "cliente": cliente,
        "commento": commento,
        "collaboratore": collaboratore,
        "data": str(data),
        "orario": str(orario)
    }

    collection.insert_one(intervista)

    return HttpResponseRedirect(reverse(index))
