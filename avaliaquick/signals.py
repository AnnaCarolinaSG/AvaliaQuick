from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import AvaliacaoAnual, Pesquisador, Pendentes
from .utils import enviar_link_acesso

@receiver(post_save, sender=AvaliacaoAnual)
def enviar_emails_para_pesquisadores(sender, instance, created, **kwargs):
    if created:
        print("SINAL DISPARADO: Enviando e-mails")
        for pesquisador in Pesquisador.objects.all():
            pendente = Pendentes.objects.create(
                pesquisador=pesquisador,
                avaliacaoAnual=instance,
                data_hora=timezone.now()
            )
            enviar_link_acesso(pendente)