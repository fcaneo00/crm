from .models import Collaboratore
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    collaboratori = Collaboratore.objects.all().values()
    template = loader.get_template('azienda.html')
    context = {
        "collaboratori": collaboratori,
    }
    return HttpResponse(template.render(context, request))
    