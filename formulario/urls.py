from django.urls import path
from . import views

urlpatterns = [
    # FORM A
    path('formA/', views.criarFormularioA, name='criarFormularioA'),
    path('formA/<int:id>/editar/', views.editarFormularioA, name='editarFormularioA'),

    # FORM B
    path('formB/', views.criarFormularioB, name='criarFormularioB'),
    path('formB/<int:id>/editar/', views.editarFormularioB, name='editarFormularioB'),

    # FORM C
    path('formC/', views.criarFormularioC, name='criarFormularioC'),
    path('formC/<int:id>/editar/', views.editarFormularioC, name='editarFormularioC'),


]
