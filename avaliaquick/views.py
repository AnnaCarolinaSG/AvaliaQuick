from django.shortcuts import render

def index(request):
    return render(request, 'avaliaquick/index.html')

# Create your views here.
