from django.http import HttpResponse, HttpResponseRedirect
# from .models import Intervista
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

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def addRecord(request):
    cliente = request.POST['nome']
    commento = request.POST['commento']

    intervista = {
        "cliente": cliente,
        "commento": commento,
    }

    collection.insert_one(intervista)

    return HttpResponseRedirect(reverse('index'))