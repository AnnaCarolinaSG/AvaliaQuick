import random

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario_A, Formulario_B, Formulario_C
from .forms import FormularioAForm, FormularioBForm, FormularioCForm
from avaliaquick.models import Pendentes

#--FORMS A--
def criarFormularioA(request, id):
    if request.method == 'POST':
        form = FormularioAForm(request.POST)
        avaliacao = get_object_or_404(Pendentes, id=id)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.avaliacao = avaliacao
            formulario.save() # Salva os campos do formulário


            print(form.cleaned_data)
            return redirect('criarFormularioB', id)
        else:
            print(form.errors)
    else:
        form = FormularioAForm()
    return render(request, 'formulario/formA.html', {'form': form, 'tipo': 'A'})

def editarFormularioA(request, id):
    obj = get_object_or_404(Formulario_A, id=id)
    form = FormularioAForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/listaFormularioA')
    else:
        print(form.errors)
    return  render(request, 'formulario/formA.html', {'form': form, 'tipo': 'A'})

#--FORMS B--
def criarFormularioB(request, id):
    if request.method == 'POST':
        form = FormularioBForm(request.POST)
        avaliacao = get_object_or_404(Pendentes, id=id)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.avaliacao = avaliacao
            formulario.save()

            return redirect('criarFormularioC', id)
        else:
            print(form.errors)
    else:
        form = FormularioBForm()
    return render(request, 'formulario/formB.html', {'form': form, 'tipo': 'B'})

def editarFormularioB(request, id):
    obj = get_object_or_404(Formulario_B, id=id)
    form = FormularioBForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/formB.html')
    else:
        print(form.errors)
    return  render(request, 'formulario/formB.html', {'form': form, 'tipo': 'B'})


#--FORMS C--
def criarFormularioC(request, id):
    if request.method == 'POST':
        form = FormularioCForm(request.POST)
        avaliacao = get_object_or_404(Pendentes, id=id)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.avaliacao = avaliacao
            formulario.save()
            messages.success(request,'Pesquisador avaliado com sucesso.')

            pendente = get_object_or_404(Pendentes, id=id)
            pendente.nota = random.randint(7, 10)
            pendente.status = 'FIN'
            pendente.save()

            return redirect('avaliacao')
        else:
            print(form.errors)
    else:
        form = FormularioCForm()
    return render(request, 'formulario/formC.html', {'form': form, 'tipo': 'C'})

def editarFormularioC(request, id):
    obj = get_object_or_404(Formulario_C, id=id)
    form = FormularioCForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/formC')
    else:
        print(form.errors)
    return  render(request, 'formulario/formC.html', {'form': form, 'tipo': 'C'})


# Create your views here.
