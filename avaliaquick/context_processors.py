from django.utils import timezone
from django.db.models import Avg
from .models import AvaliacaoAnual, Pendentes

def notificacoes_contexto(request):
    hoje = timezone.now().date()
    notificacoes = []
    aux = 0

    avaliacao_atual = AvaliacaoAnual.objects.filter(status='ABE').order_by('-data_inicio').first()

    if avaliacao_atual:
        pendentes = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='PEN', arquivos_prontos=False).count()
        prontos_para_avaliar = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='PEN', arquivos_prontos=True).distinct().count()
        em_andamento = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='AND').count()
        finalizados = Pendentes.objects.filter(avaliacaoAnual=avaliacao_atual, status='FIN').count()

        if pendentes:
            notificacoes.append({'texto': f"{pendentes} pendentes", 'tipo': 'pendentes'})

        if prontos_para_avaliar:
            notificacoes.append({'texto': f"{prontos_para_avaliar} prontos para avaliar", 'tipo': 'prontos'})

        if em_andamento:
            notificacoes.append({'texto': f"{em_andamento} avaliações em andamento", 'tipo': 'andamento'})

        if finalizados:
            notificacoes.append({'texto': f"{finalizados} avaliações finalizadas", 'tipo': 'finalizadas'})

        media_atual = Pendentes.objects.filter(
            avaliacaoAnual=avaliacao_atual,
            status='FIN',
            nota__isnull=False
        ).aggregate(media=Avg('nota'))['media']

        media_antiga = request.session.get('media_ultima_vista')

        if media_atual is not None:
            if media_antiga is None or media_atual != media_antiga:
                notificacoes.append({
                    'texto': f"A média atual mudou para {round(media_atual, 3)}",
                    'tipo': 'media',
                    'media_valor': round(media_atual, 3)
                })
    else:
        notificacoes.append({'texto': "Nenhuma avaliação aberta no momento", 'tipo': 'info'})
        aux = 1

    print(len(notificacoes))
    return {
        'notificacoes': notificacoes,
        'qtd_notificacoes': len(notificacoes) - aux,
    }
