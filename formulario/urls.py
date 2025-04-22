from django.urls import path
from . import views

urlpatterns = [
    # FORM A
    path('formularioA/', views.listaFormularioA, name='listaFormularioA'),
    path('formularioA/novo/', views.criarFormularioA, name='criarFormularioA'),
    path('formularioA/<int:id>/editar/', views.editarFormularioA, name='editarFormularioA'),

    # FORM B
    path('formularioB/', views.listaFormularioB, name='listaFormularioB'),
    path('formularioB/novo/', views.criarFormularioB, name='criarFormularioB'),
    path('formularioB/<int:id>/editar/', views.editarFormularioB, name='editarFormularioB'),

    # FORM C
    path('formularioC/', views.listaFormularioC, name='listaFormularioC'),
    path('formularioC/novo/', views.criarFormularioC, name='criarFormularioC'),
    path('formularioC/<int:id>/editar/', views.editarFormularioC, name='editarFormularioC'),

    path('teste', views.teste, name='testes')
]
