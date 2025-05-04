from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Pesquisador, Pendentes
from django.db.models import Q
from .forms import FormularioPesquisador

def login_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('/inicio')  # ou o nome da sua URL da página inicial
    return redirect('/login')

def index(request):
    if not request.user.is_authenticated:
        raise PermissionDenied


    return render(request, 'avaliaquick/index.html')

def avaliacao(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    pendentes = Pendentes.objects.filter(Q(status='PEN') & ~(Q(arquivos='') | Q(arquivos__isnull=True))).count()
    andamento = Pendentes.objects.filter(status='AND').count()
    finalizados = Pendentes.objects.filter(status='FIN').count()
    pesquisadores = Pesquisador.objects.all()
    avaliacoes = Pendentes.objects.all()
    vazios = Pendentes.objects.filter(Q(arquivos='') | Q(arquivos__isnull=True)).count()

    return render(request, 'avaliaquick/avaliacao.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes,
        'pendentes': pendentes,
        'andamento': andamento,
        'finalizados': finalizados,
        'vazios': vazios
    })

def perfil(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/perfil.html')

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

def anteriores(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/avaliacoes-anteriores.html')


# Create your views here.
