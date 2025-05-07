from django.urls import path
from avaliaquick.views import (index, avaliacao, lista, anteriores, login_redirect_view, deletar_pesquisador,
                               criar_avaliacao, fechar_avaliacao, reabrir_avaliacao, adicionar_arquivos,
                               apresentar_anteriores, avaliar_pesquisador, solicitar_novamente, editar_pesquisador,
                               enviar_arquivos_view, sucesso_view)

urlpatterns = [
    path('', login_redirect_view, name="login_redirect"),
    path('inicio/', index, name="inicio"),
    path('avaliacao/', avaliacao, name="avaliacao"),
    path('lista-pesquisadores', lista, name='lista_pesquisadores'),
    path('avaliacoes-anteriores', anteriores, name='anteriores'),
    path('pesquisador/deletar/<int:id>/', deletar_pesquisador, name='deletar_pesquisador'),
    path('criar-avaliacao/', criar_avaliacao, name='criar_avaliacao'),
    path('avaliacao/fechar/', fechar_avaliacao, name='fechar_avaliacao'),
    path('avaliacao/reabrir/', reabrir_avaliacao, name='reabrir_avaliacao'),
    path('adicionar-arquivos/', adicionar_arquivos, name='adicionar_arquivos'),
    path('avaliacao/<int:id>/', apresentar_anteriores, name='apresentar_anteriores'),
    path('pendentes/avaliar/<int:id>/', avaliar_pesquisador, name='avaliar_pesquisador'),
    path('solicitar-novamente/<int:avaliacao_id>/', solicitar_novamente, name='solicitar_novamente'),
    path('pesquisador/<int:id>/editar/', editar_pesquisador, name='editar_pesquisador'),
    path('formulario-envio/<int:pendente_id>/<str:token>/', enviar_arquivos_view, name='enviar_arquivos'),
    path('envio/sucesso/', sucesso_view, name='sucesso_envio'),

]