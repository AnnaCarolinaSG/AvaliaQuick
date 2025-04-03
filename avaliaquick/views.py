from django.shortcuts import render

def index(request):
    return render(request, 'avaliaquick/index.html')

def avaliacao(request):
    return render(request, 'avaliaquick/avaliacao.html')

# Create your views here.
