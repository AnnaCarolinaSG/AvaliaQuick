from django.core.validators import MinValueValidator
from django.db import models

class Pesquisador(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=100)
    matricula = models.IntegerField(null=False, blank=False)

# Create your models here.
