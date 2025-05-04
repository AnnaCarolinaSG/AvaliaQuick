from django.core.validators import MinValueValidator
from django.db import models

class Pesquisador(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=100)
    matricula = models.CharField(null=False, blank=False, unique=True, max_length=15)
    email = models.EmailField(null=False, blank=False, default='')


def caminho_arquivo(instance, filename):
    return f"pesquisadores/{instance.pesquisador.nome}/{filename}"

class Pendentes(models.Model):
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=False, blank=False)
    arquivos = models.FileField(upload_to=caminho_arquivo, null=True)

    OPCOES_STATUS = [
        ('PEN', 'Pendente'),
        ('AND', 'Andamento'),
        ('FIN', 'Finalizado'),
    ]
    status = models.CharField(max_length=3, choices=OPCOES_STATUS, default='PEN')

# Create your models here.
