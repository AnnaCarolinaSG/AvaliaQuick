from django.urls import path
from avaliaquick.views import *

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
    path('buscar/', busca_global, name='busca_global'),
    path('pesquisador/<int:pk>/', detalhes_pesquisador, name='detalhes_pesquisador'),
    path('avaliacao/<int:pk>/', detalhes_avaliacao, name='detalhes_avaliacao'),
    path('pendente/<int:pk>/', detalhes_pendente, name='detalhes_pendente'),
    path('perfil/<int:id>/<str:tipo>/', perfil, name="perfil"),
    path('verificar-matricula/', verificar_matricula, name='verificar_matricula'),
    path('avaliacao/<int:id>/deletar/', deletar_avaliacao, name='deletar_avaliacao'),
    path('notificacoes/media-vista/', marcar_media_como_vista, name='media_vista'),

]