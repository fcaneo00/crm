from .models import Collaboratore
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
    collaboratori = Collaboratore.objects.all().values()
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def addRecord(request):
    
    return HttpResponseRedirect(reverse('index'))

