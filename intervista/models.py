import string
from django.db import models

# Create your models here.
class Cliente(models.Model):
    codiceFiscale = models.CharField(max_length = 50, primary_key = True)
    nome = models.CharField(max_length = 50)
    cognome = models.CharField(max_length = 50)

    def __str__(self):
        return self.nome + " " + self.cognome

class Intervista(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    collaboratore = models.ForeignKey('azienda.Collaboratore', on_delete = models.CASCADE)
    commento = models.CharField(max_length = 1000)
    data = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return "Commento del cliente " + str(self.cliente) + " per il collaboratore " + str(self.collaboratore) + " | " + str(self.data)