from django.urls import path
from avaliaquick.views import index, avaliacao, perfil, lista, anteriores, login_redirect_view, deletar_pesquisador, criar_avaliacao, fechar_avaliacao, reabrir_avaliacao, adicionar_arquivos

urlpatterns = [
    path('', login_redirect_view, name="login_redirect"),
    path('inicio/', index, name="inicio"),
    path('avaliacao/', avaliacao, name="avaliacao"),
    path('perfil', perfil),
    path('lista-pesquisadores', lista, name='lista_pesquisadores'),
    path('avaliacoes-anteriores', anteriores),
    path('pesquisador/deletar/<int:id>/', deletar_pesquisador, name='deletar_pesquisador'),
    path('criar-avaliacao/', criar_avaliacao, name='criar_avaliacao'),
    path('avaliacao/fechar/', fechar_avaliacao, name='fechar_avaliacao'),
    path('avaliacao/reabrir/', reabrir_avaliacao, name='reabrir_avaliacao'),
    path('adicionar-arquivos/', adicionar_arquivos, name='adicionar_arquivos'),
]