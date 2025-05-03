from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied
from .models import Pesquisador, Pendentes

def login_redirect_view(request):
    if request.user.is_authenticated:
        return redirect('/inicio')  # ou o nome da sua URL da página inicial
    return redirect('/login')

def index(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    pesquisadores = Pesquisador.objects.all()
    avaliacoes = Pendentes.objects.all()
    return render(request, 'avaliaquick/index.html', {
        'pesquisadores': pesquisadores,
        'avaliacoes': avaliacoes
    })

def avaliacao(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/avaliacao.html')

def perfil(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/perfil.html')

def lista(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/lista-pesquisadores.html')

def anteriores(request):
    if not request.user.is_authenticated:
        raise PermissionDenied
    return render(request, 'avaliaquick/avaliacoes-anteriores.html')


# Create your views here.
