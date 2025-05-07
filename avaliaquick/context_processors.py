from django.utils import timezone
from django.db.models import Avg
from .models import AvaliacaoAnual, Pendentes

def notificacoes_contexto(request):
    hoje = timezone.now().date()
    notificacoes = []

    avaliacao_atual = AvaliacaoAnual.objects.filter(status='ABE').order_by('-data_inicio').first()

    if avaliacao_atual:
        prontos_para_avaliar = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='PEN').count()
        em_andamento = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='AND').count()
        finalizados = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='FIN').count()

        media = Pendentes.objects.filter(
            avaliacaoAnual=avaliacao_atual,
            status='FIN',
            nota__isnull=False
        ).aggregate(media=Avg('nota'))['media']

        notificacoes.append(f"{prontos_para_avaliar} prontos para avaliar")
        notificacoes.append(f"{em_andamento} avaliações em andamento")
        notificacoes.append(f"{finalizados} avaliações finalizadas")

        if media is not None:
            notificacoes.append(f"A média atual é {round(media, 1)}")
    else:
        notificacoes.append("Nenhuma avaliação aberta no momento")

    return {
        'notificacoes': notificacoes,
        'qtd_notificacoes': len(notificacoes),
    }
