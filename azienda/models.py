from django.db import models

# Create your models here.
class ruolo(models.Model):
    nome = models.CharField(max_length = 50)
    
    def __str__(self):
       return self.nome


class collaboratore(models.Model):
    codiceFiscale = models.CharField(max_length = 50, primary_key = True)
    nome = models.CharField(max_length = 50)
    cognome = models.CharField(max_length = 50)
    indirizzo = models.CharField(max_length = 100)
    email = models.EmailField()
    telefono = models.CharField(max_length = 50)
    cellulare = models.CharField(max_length = 50)
    ruolo = models.ForeignKey(ruolo, on_delete = models.CASCADE)

    def __str__(self):
        return self.nome + " " + self.cognome