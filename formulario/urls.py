from django.urls import path
from . import views
from avaliaquick import views as av_vw

urlpatterns = [

    path('avaliacao/', av_vw.avaliacao, name='avaliacao'),
    # FORM A
    path('formA/<int:id>/', views.criarFormularioA, name='criarFormularioA'),
    path('formA/<int:id>/visualizar/', views.visualizarFormularioA, name='visualizarFormularioA'),

    # FORM B
    path('formB/<int:id>/', views.criarFormularioB, name='criarFormularioB'),
    path('formB/<int:id>/visualizar/', views.visualizarFormularioB, name='visualizarFormularioB'),

    # FORM C
    path('formC/<int:id>/', views.criarFormularioC, name='criarFormularioC'),
    path('formC/<int:id>/visualizar/', views.visualizarFormularioC, name='visualizarFormularioC'),


]
