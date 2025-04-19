from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario_A, Formulario_B, Formulario_C
from .forms import FormularioAForm, FormularioBForm, FormularioCForm

#--FORMS A--

def listaFormularioA(request):
    lista = Formulario_A.objects.all()
    return render(request, 'formulario/lista.html', {'formularios': lista, 'tipo': 'A'})

def criarFormularioA(request):
    if request.method == 'POST':
        form = FormularioAForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listaFormularioA')
    else:
        form = FormularioAForm()
    return render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'A'})

def editarFormularioA(request, id):
    obj = get_object_or_404(Formulario_A, id=id)
    form = FormularioAForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/listaFormularioA')
    return  render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'A'})

#--FORMS B--

def listaFormularioB(request):
    lista = Formulario_B.objects.all()
    return render(request, 'formulario/lista.html', {'formularios': lista, 'tipo': 'B'})

def criarFormularioB(request):
    if request.method == 'POST':
        form = FormularioBForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listaFormularioB')
    else:
        form = FormularioBForm()
    return render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'B'})

def editarFormularioB(request, id):
    obj = get_object_or_404(Formulario_B, id=id)
    form = FormularioBForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/listaFormularioB')
    return  render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'B'})


#--FORMS C--

def listaFormularioC(request):
    lista = Formulario_C.objects.all()
    return render(request, 'formulario/lista.html', {'formularios': lista, 'tipo': 'C'})

def criarFormularioC(request):
    if request.method == 'POST':
        form = FormularioCForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listaFormularioC')
    else:
        form = FormularioCForm()
    return render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'C'})

def editarFormularioC(request, id):
    obj = get_object_or_404(Formulario_C, id=id)
    form = FormularioCForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/listaFormularioC')
    return  render(request, 'formulario/formularioA.html', {'form': form, 'tipo': 'C'})


# Create your views here.
