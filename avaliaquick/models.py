from django.core.validators import MinValueValidator
from django.db import models

class Pesquisador(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=100)
    matricula = models.IntegerField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False, default='teste@gmail.com')


def caminho_arquivo(instance, filename):
    return f"pesquisadores/{instance.pesquisador.username}/{filename}"

class Pendentes(models.Model):
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=False, blank=False)
    arquivos = models.FileField(upload_to=caminho_arquivo)

# Create your models here.
