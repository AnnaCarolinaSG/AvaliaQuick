from django.urls import path
from avaliaquick.views import index, avaliacao, perfil, lista, anteriores, login_redirect_view

urlpatterns = [
    path('', login_redirect_view, name="login_redirect"),
    path('inicio/', index),
    path('avaliacao/', avaliacao),
    path('perfil', perfil),
    path('lista-pesquisadores', lista),
    path('avaliacoes-anteriores', anteriores)
]