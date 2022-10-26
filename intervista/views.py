from django.http import HttpResponse
# from .models import Intervista
from django.template import loader
from django.shortcuts import render
from utils import get_db_handle, get_collection_handle

# Mongodb connection
db = get_db_handle('crm', 'localhost', 27017, 'mongoadmin', 'mongoadmin')
collection = get_collection_handle(db, 'intervista')

# Create your views here.
def index(request):
    interviste = [
        {
            "commento": "aaa",
            "cliente": "tommaso"
        },
        {
            "commento": "bbb",
            "cliente": "michael"
        }
    ]
    template = loader.get_template('interviste.html')
    context = {
        "interviste": interviste
    }

    return HttpResponse(template.render(context, request))
