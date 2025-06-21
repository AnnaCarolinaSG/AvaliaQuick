from email.policy import default

from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import uuid

class CustomUser(AbstractUser):
    matricula = models.CharField(null=False, blank=False, unique=True, max_length=16)

class AvaliacaoAnual(models.Model):
    usuario = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True)
    media_nota = models.FloatField(validators=[MinValueValidator(0.0)], null=True)
    qtd_avaliados = models.IntegerField(validators=[MinValueValidator(0)], null=True)
    OPCOES_STATUS = [
        ('ABE', 'Aberta'),
        ('FEC', 'Fechada'),
    ]
    status = models.CharField(max_length=3, choices=OPCOES_STATUS, default='ABE')

class Pesquisador(models.Model):
    usuario = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    nome = models.CharField(null=False, blank=False, max_length=100)
    matricula = models.CharField(null=False, blank=False, unique=True, max_length=15)
    email = models.EmailField(null=False, blank=False, default='')
    token = models.CharField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
    ativo = models.BooleanField(default=True)


def caminho_arquivo(instance, filename):
    return f"pesquisadores/{instance.pesquisador.nome}/{filename}"

class Pendentes(models.Model):
    usuario = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    pesquisador = models.ForeignKey(Pesquisador, on_delete=models.CASCADE)
    avaliacaoAnual = models.ForeignKey(AvaliacaoAnual, on_delete=models.CASCADE, default='')
    data_hora = models.DateTimeField(null=False, blank=False)

    OPCOES_STATUS = [
        ('PEN', 'Pendente'),
        ('AND', 'Andamento'),
        ('FIN', 'Finalizado'),
    ]
    status = models.CharField(max_length=3, choices=OPCOES_STATUS, default='PEN')
    nota = models.FloatField(validators=[MinValueValidator(0.0)], null=True)
    arquivos_prontos = models.BooleanField(default=False)



class Arquivo(models.Model):
    pendente = models.ForeignKey(Pendentes, on_delete=models.CASCADE, related_name='arquivos_enviados')
    arquivo = models.FileField(upload_to='arquivos/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def extensao_arquivo(self):
        if self.arquivo:
            nome = self.arquivo.name
            return os.path.splitext(nome)[1].lower()  # retorna tipo '.pdf', '.docx'
        return ''

    def nome_arquivo(self):
        if self.arquivo:
            nome_completo = os.path.basename(self.arquivo.name)  # ex: Documento_6Aod4oP.pdf
            nome_sem_extensao, _ = os.path.splitext(nome_completo)  # separa nome e extensão
            return nome_sem_extensao
        return ''
