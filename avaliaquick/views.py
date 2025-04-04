from django.shortcuts import render

def index(request):
    return render(request, 'avaliaquick/index.html')

def avaliacao(request):
    return render(request, 'avaliaquick/avaliacao.html')

def perfil(request):
    return render(request, 'avaliaquick/perfil.html')

def lista(request):
    return render(request, 'avaliaquick/lista-pesquisadores.html')

def anteriores(request):
    return render(request, 'avaliaquick/avaliacoes-anteriores.html')

# Create your views here.
