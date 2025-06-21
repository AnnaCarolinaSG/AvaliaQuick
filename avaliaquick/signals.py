from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import AvaliacaoAnual, Pesquisador, Pendentes
from .utils import enviar_link_acesso
from django.db.models import Avg

@receiver(post_save, sender=AvaliacaoAnual)
def enviar_emails_para_pesquisadores(sender, instance, created, **kwargs):
    if created:
        print("SINAL DISPARADO: Enviando e-mails")
        for pesquisador in Pesquisador.objects.filter(ativo=True):
            pendente = Pendentes.objects.create(
                usuario=pesquisador.usuario,
                pesquisador=pesquisador,
                avaliacaoAnual=instance,
                data_hora=timezone.now()
            )
            enviar_link_acesso(pendente)

def atualizar_media(avaliacao):
    media = Pendentes.objects.filter(
        status='FIN',
        avaliacaoAnual=avaliacao,
        usuario=avaliacao.usuario
    ).aggregate(media_nota=Avg('nota'))['media_nota'] or 0.0
    avaliacao.media_nota = round(media, 3)
    avaliacao.save()

@receiver(post_save, sender=Pendentes)
def atualizar_media_apos_salvar(sender, instance, **kwargs):
    if instance.status == 'FIN':
        atualizar_media(instance.avaliacaoAnual)

@receiver(post_delete, sender=Pendentes)
def atualizar_media_apos_excluir(sender, instance, **kwargs):
    if instance.status == 'FIN':
        atualizar_media(instance.avaliacaoAnual)