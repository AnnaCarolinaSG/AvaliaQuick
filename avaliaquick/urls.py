from django.urls import path
from avaliaquick.views import index, avaliacao, perfil, lista, anteriores

urlpatterns = [
    path('', index),
    path('avaliacao/', avaliacao),
    path('perfil', perfil),
    path('lista-pesquisadores', lista),
    path('avaliacoes-anteriores', anteriores)
]