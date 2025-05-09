from django.utils import timezone
from django.db.models import Avg
from .models import AvaliacaoAnual, Pendentes

def notificacoes_contexto(request):
    hoje = timezone.now().date()
    notificacoes = []
    aux = 0

    avaliacao_atual = AvaliacaoAnual.objects.filter(status='ABE').order_by('-data_inicio').first()

    if avaliacao_atual:
        pendentes = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='PEN', arquivos='').count()
        prontos_para_avaliar = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='PEN').exclude(arquivos='').count()
        em_andamento = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='AND').count()
        finalizados = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='FIN').count()

        media = Pendentes.objects.filter(
            avaliacaoAnual=avaliacao_atual,
            status='FIN',
            nota__isnull=False
        ).aggregate(media=Avg('nota'))['media']

        if pendentes:
            notificacoes.append(f"{pendentes} pendentes")

        if prontos_para_avaliar:
            notificacoes.append(f"{prontos_para_avaliar} prontos para avaliar")

        if em_andamento:
            notificacoes.append(f"{em_andamento} avaliações em andamento")

        if finalizados:
            notificacoes.append(f"{finalizados} avaliações finalizadas")

        if media is not None:
            notificacoes.append(f"A média atual é {round(media, 1)}")
    else:
        notificacoes.append("Nenhuma avaliação aberta no momento")
        aux = 1

    return {
        'notificacoes': notificacoes,
        'qtd_notificacoes': len(notificacoes) - aux,
    }
