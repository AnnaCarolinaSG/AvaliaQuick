from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Pesquisador, Pendentes, AvaliacaoAnual
from django.db.models import Q
from .forms import FormularioPesquisador
from datetime import datetime
from django.core.mail import send_mail
import random

def login_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('/inicio')  # ou o nome da sua URL da página inicial
    return redirect('/login')

def index(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    periodos = AvaliacaoAnual.objects.filter(status="ABE")
    return render(request, 'avaliaquick/index.html', {'periodos': periodos})

def criar_avaliacao(request):
    if request.method == 'POST':
        nova_avaliacao = AvaliacaoAnual.objects.create(
            data_inicio=datetime.now(),
            status='ABE'
        )
        pesquisadores = Pesquisador.objects.all()
        pendentes = [
            Pendentes(
                pesquisador=p,
                avaliacaoAnual=nova_avaliacao,
                data_hora=datetime.now(),
                status='PEN'
            )
            for p in pesquisadores
        ]
        Pendentes.objects.bulk_create(pendentes)
    return redirect('avaliacao')

def fechar_avaliacao(request):
    if request.method == 'POST':
        avaliacao_id = request.POST.get('avaliacao_id')
        avaliacao = get_object_or_404(AvaliacaoAnual, id=avaliacao_id)
        avaliacao.status = 'FEC'
        avaliacao.data_fim = datetime.now()  # opcional
        avaliacao.save()
    return redirect('inicio')

def reabrir_avaliacao(request):
    if request.method == 'POST':
        avaliacao_id = request.POST.get('avaliacao_id')
        avaliacao = get_object_or_404(AvaliacaoAnual, id=avaliacao_id)
        avaliacao.status = 'ABE'
        avaliacao.data_fim = None  # opcional
        avaliacao.save()
    return redirect('inicio')


def adicionar_arquivos(request):
    if request.method == "POST" and request.FILES.get('arquivos'):
        arquivo = request.FILES['arquivos']

        # Se você tiver um campo de relacionamento, pode adicionar o arquivo a ele
        # Aqui estou supondo que você queira associar o arquivo à avaliação específica:
        avaliacao_id = request.POST.get('avaliacao_id')  # Você precisa garantir que o id seja passado no formulário
        avaliacao = Pendentes.objects.get(id=avaliacao_id)

        # Salva o arquivo
        avaliacao.arquivos = arquivo
        avaliacao.save()

        messages.success(request, "Arquivo adicionado com sucesso!")
        return redirect('avaliacao')  # Redirecionar para a página de avaliação ou onde for adequado
    else:
        messages.error(request, "Erro ao adicionar arquivo.")
        return redirect('avaliacao')

def avaliar_pesquisador(request, id):
    if not request.user.is_authenticated:
        raise PermissionDenied

    if request.method == 'POST':
        pendente = get_object_or_404(Pendentes, id=id)
        pendente.status = 'FIN'
        pendente.nota = random.randint(7, 10)
        pendente.save()
        messages.success(request, 'Pesquisador avaliado com sucesso!')
    return redirect('inicio')

def solicitar_novamente(request, avaliacao_id):
    if request.method == 'POST':
        avaliacao = get_object_or_404(Pendentes, id=avaliacao_id)
        email_destinatario = avaliacao.pesquisador.email

        assunto = "Solicitação de envio de documentos"
        mensagem = f"""
        Olá {avaliacao.pesquisador.nome},

        Por favor, envie os documentos pendentes relacionados à sua avaliação anual.

        Obrigado,
        AvaliaQuick
        """

        send_mail(
            assunto,
            mensagem,
            'brianhcosta@gmail.com',  # Remetente (configure no settings.py)
            [email_destinatario],
            fail_silently=False
        )

        messages.success(request, 'E-mail enviado com sucesso!')
        return redirect('avaliacao')

def avaliacao(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    if AvaliacaoAnual.objects.filter(status='ABE').exists():
        periodoAtual = AvaliacaoAnual.objects.filter(status='ABE').order_by('-data_inicio').first()
    else:
        periodoAtual = AvaliacaoAnual.objects.order_by('-data_inicio').first()
    pendentes = Pendentes.objects.filter(Q(avaliacaoAnual=periodoAtual) & Q(status='PEN') & ~(Q(arquivos='') | Q(arquivos__isnull=True))).count()
    andamento = Pendentes.objects.filter(status='AND', avaliacaoAnual=periodoAtual).count()
    finalizados = Pendentes.objects.filter(status='FIN', avaliacaoAnual=periodoAtual).count()
    pesquisadores = Pesquisador.objects.all()
    avaliacoes = Pendentes.objects.filter(avaliacaoAnual=periodoAtual)
    vazios = Pendentes.objects.filter(Q(arquivos='') | Q(arquivos__isnull=True) & Q(avaliacaoAnual=periodoAtual)).count()

    return render(request, 'avaliaquick/avaliacao.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
        'pendentes': pendentes,
        'andamento': andamento,
        'finalizados': finalizados,
        'vazios': vazios,
        'periodoAtual': periodoAtual,
    })

def editar_pesquisador(request, id):
    pesquisador = get_object_or_404(Pesquisador, id=id)
    if request.method == 'POST':
        pesquisador.nome = request.POST.get('nome')
        pesquisador.matricula = request.POST.get('matricula')
        pesquisador.email = request.POST.get('email')
        pesquisador.save()
        messages.success(request, 'Pesquisador atualizado com sucesso!')
    return redirect('lista_pesquisadores')

def lista(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    if request.method == 'POST':
        form = FormularioPesquisador(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Pesquisador cadastrado com sucesso!')
                return redirect('/lista-pesquisadores')
            except IntegrityError:
                messages.error(request, 'Já existe um pesquisador com essa matrícula.')
    else:
        form = FormularioPesquisador()

    pesquisadores = Pesquisador.objects.all()
    avaliacoes = Pendentes.objects.all()

    return render(request, 'avaliaquick/lista-pesquisadores.html', {
        'form': form,
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
    })

def deletar_pesquisador(request, id):
    if request.method == 'POST':
        pesquisador = get_object_or_404(Pesquisador, id=id)
        pesquisador.delete()
        messages.success(request, 'Pesquisador removido com sucesso!')
    return redirect('lista_pesquisadores')

def anteriores(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    anteriores = AvaliacaoAnual.objects.filter(status='FEC').order_by('-data_inicio')

    return render(request, 'avaliaquick/avaliacoes-anteriores.html', {
        'avaliacoes': anteriores,
    })

def apresentar_anteriores(request, id):
    if not request.user.is_authenticated:
        raise PermissionDenied

    finalizados = Pendentes.objects.filter(status='FIN', avaliacaoAnual=id).count()
    pesquisadores = Pesquisador.objects.all()
    avaliacoes = Pendentes.objects.filter(avaliacaoAnual=id)
    vazios = Pendentes.objects.filter(Q(arquivos='') | Q(arquivos__isnull=True) & Q(avaliacaoAnual=id)).count()

    return render(request, 'avaliaquick/avaliacao.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
        'finalizados': finalizados,
        'vazios': vazios,
        'periodoAtual': AvaliacaoAnual.objects.get(id=id),
        'anteriores': True,
    })



# Create your views here.
