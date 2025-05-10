from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Pesquisador, Pendentes, AvaliacaoAnual, Arquivo, CustomUser
from django.db.models import Q, Avg, Count
from .forms import FormularioPesquisador, EnvioArquivosForm
from datetime import datetime
from django.core.mail import send_mail
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate
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
        AvaliacaoAnual.objects.create(
            data_inicio=datetime.now(),
            status='ABE'
        )
        messages.success(request, 'Período de avaliação iniciada com sucesso!')
    return redirect('avaliacao')

def fechar_avaliacao(request):
    if request.method == 'POST':
        avaliacao_id = request.POST.get('avaliacao_id')
        avaliacao = get_object_or_404(AvaliacaoAnual, id=avaliacao_id)
        pendentes = Pendentes.objects.filter(avaliacaoAnual = avaliacao_id).count()
        avaliacao.status = 'FEC'
        avaliacao.qtd_avaliados = pendentes
        avaliacao.data_fim = datetime.now()  # opcional
        media = Pendentes.objects.filter(
            status='FIN',
            avaliacaoAnual=avaliacao_id
        ).aggregate(media_nota=Avg('nota'))['media_nota']
        avaliacao.media_nota = media
        avaliacao.save()
        messages.success(request, 'Período fechado com sucesso!')
    return redirect('avaliacao')

def reabrir_avaliacao(request):
    if request.method == 'POST':
        avaliacao_id = request.POST.get('avaliacao_id')
        avaliacao = get_object_or_404(AvaliacaoAnual, id=avaliacao_id)
        avaliacao.status = 'ABE'
        avaliacao.data_fim = None  # opcional
        avaliacao.save()
        messages.success(request, 'O período anterior foi reaberto!')
    return redirect('avaliacao')


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

    return redirect('avaliacao')

def solicitar_novamente(request, avaliacao_id):
    if request.method == 'POST':
        avaliacao = get_object_or_404(Pendentes, id=avaliacao_id)
        email_destinatario = avaliacao.pesquisador.email
        link = f"https://avaliaquick-production.up.railway.app/formulario-envio/{avaliacao_id}/{avaliacao.pesquisador.token}/"
        assunto = "Solicitação de envio de documentos"
        mensagem = f"""
        Olá {avaliacao.pesquisador.nome},

        Por favor, envie os documentos pendentes relacionados à sua avaliação anual.
        Link para envio: {link}

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
    vazios = Pendentes.objects.filter(Q(avaliacaoAnual=periodoAtual) & Q(arquivos='') | Q(arquivos__isnull=True)).count()
    if periodoAtual:
        media = periodoAtual.media_nota
    else:
        media = None

    return render(request, 'avaliaquick/avaliacao.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
        'pendentes': pendentes,
        'andamento': andamento,
        'finalizados': finalizados,
        'vazios': vazios,
        'periodoAtual': periodoAtual,
        'media': media,
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
    if not request.user.is_authenticated:
        raise PermissionDenied

    if request.method == 'POST':
        senha = request.POST.get('senha_confirmacao')
        user = authenticate(username=request.user.username, password=senha)

        if user is not None:
            pesquisador = get_object_or_404(Pesquisador, id=id)
            pesquisador.delete()
            messages.success(request, 'Pesquisador removido com sucesso!')
        else:
            messages.error(request, 'Senha incorreta. O pesquisador não foi removido.')

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
    avaliacao = AvaliacaoAnual.objects.get(id=id)

    return render(request, 'avaliaquick/avaliacao.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
        'finalizados': finalizados,
        'vazios': vazios,
        'periodoAtual': avaliacao,
        'anteriores': True,
    })

def enviar_arquivos_view(request, pendente_id, token):
    # Busca o registro da pendência
    pendente = get_object_or_404(Pendentes, id=pendente_id)

    # Validação do token
    #if str(pendente.token) != str(token):
        #return HttpResponseForbidden("Token inválido. Acesso não autorizado.")

    if request.method == 'POST':
        form = EnvioArquivosForm(request.POST, request.FILES)
        if form.is_valid():
            arquivos = request.FILES.getlist('arquivos')

            # Salva os arquivos no modelo Arquivo
            for arquivo in arquivos:
                Arquivo.objects.create(pendente=pendente.id, arquivo=arquivo)

            # Atualiza o status da pendência
            pendente.status = 'PEN'  # ou 'FIN' se quiser marcar como finalizado já
            pendente.save()

            # Redireciona para página de sucesso
            return render(request, 'avaliaquick/sucesso.html', {
                'pesquisador': pendente.pesquisador,
                'avaliacao': pendente.avaliacaoAnual,
            })
    else:
        form = EnvioArquivosForm()

    return render(request, 'avaliaquick/formulario_envio.html', {
        'form': form,
        'pesquisador': pendente.pesquisador,
        'avaliacao': pendente.avaliacaoAnual,
    })

def sucesso_view(request):
    return render(request, 'avaliaquick/sucesso.html')

def busca_global(request):
    termo = request.GET.get('q', '').strip()
    resultados = []

    if termo:
        pesquisadores = Pesquisador.objects.filter(nome__icontains=termo)[:]
        for p in pesquisadores:
            resultados.append({
                'label': p.nome,
                'tipo': 'Pesquisador',
                'url': reverse('detalhes_pesquisador', args=[p.id]),
                'id': p.id,
            })

        avaliacoes = AvaliacaoAnual.objects.filter(status__icontains=termo)[:]
        for a in avaliacoes:
            resultados.append({
                'label': f"Avaliação de {a.data_inicio.strftime('%d/%m/%Y')}",
                'tipo': 'Período',
                'url': reverse('detalhes_avaliacao', args=[a.id]),
                'id': a.id,
                'status': a.status,
            })

        pendentes = Pendentes.objects.filter(status__icontains=termo)[:]
        for p in pendentes:
            resultados.append({
                'label': f"Avaliação: {p.pesquisador.nome}",
                'tipo': 'Avaliação',
                'url': reverse('detalhes_pendente', args=[p.id]),
                'id': p.id,
                'status': p.status,
                'arquivos': bool(p.arquivos),
            })

    return JsonResponse({'resultados': resultados})

def perfil(request, id, tipo):
    if not request.user.is_authenticated:
        raise PermissionDenied

    if(tipo == 'pesquisador'):
        usuario = get_object_or_404(Pesquisador, id=id)
    else:
        usuario = get_object_or_404(CustomUser, id=id)
    return render(request, 'avaliaquick/perfil.html', {
        'pesquisador': usuario,
    })

def detalhes_pesquisador(request, pk):
    pesquisador = get_object_or_404(Pesquisador, pk=pk)
    return render(request, 'includes/navigation.html', {'pesquisador': pesquisador})

def detalhes_avaliacao(request, pk):
    avaliacao = get_object_or_404(AvaliacaoAnual, pk=pk)
    return render(request, 'includes/navigation.html', {'avaliacao': avaliacao})

def detalhes_pendente(request, pk):
    pendente = get_object_or_404(Pendentes, pk=pk)
    return render(request, 'includes/navigation.html', {'pendente': pendente})

# Create your views here.
