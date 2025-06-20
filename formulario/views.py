import random

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Formulario_A, Formulario_B, Formulario_C
from .forms import FormularioAForm, FormularioBForm, FormularioCForm
from avaliaquick.models import Pendentes

#--FORMS A--
def criarFormularioA(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = Formulario_A.objects.filter(avaliacao=avaliacao).first()

    if request.method == 'POST':
        if formulario_existente:
            form = FormularioAForm(request.POST, instance=formulario_existente)
        else:
            form = FormularioAForm(request.POST)

        if form.is_valid():
            formulario = form.save(commit=False)
            updated = Formulario_A.objects.filter(avaliacao=avaliacao).update(
                visao_sistemica=formulario.visao_sistemica,
                visao_analitica=formulario.visao_analitica,
                foco_planejamento=formulario.foco_planejamento,
                orientacao_mudancas=formulario.orientacao_mudancas,
                relacoes_colaboracao=formulario.relacoes_colaboracao,
            )
            if updated == 0:
                formulario.avaliacao = avaliacao
                formulario.save() # Salva os campos do formulário
                formulario.total_A = formulario.calcular_media_A()
                formulario.save()
            else:
                formulario.total_A = formulario.calcular_media_A()
                updated = Formulario_A.objects.filter(avaliacao=avaliacao).update(total_A=formulario.calcular_media_A())

            return redirect('criarFormularioB', id)
        else:
            print(form.errors)
    else:
        if formulario_existente:
            form = FormularioAForm(instance=formulario_existente)
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

def visualizarFormularioA(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = get_object_or_404(Formulario_A, avaliacao=avaliacao)

    if request.method == 'POST':
        return redirect('visualizarFormularioB', id)

    form = FormularioAForm(instance=formulario_existente)

    # Desabilita todos os campos
    for field in form.fields.values():
        field.disabled = True

    return render(request, 'formulario/formA.html', {'form': form, 'tipo': 'A'})

#--FORMS B--
def criarFormularioB(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = Formulario_B.objects.filter(avaliacao=avaliacao).first()

    if request.method == 'POST':
        if formulario_existente:
            form = FormularioBForm(request.POST, instance=formulario_existente)
        else:
            form = FormularioBForm(request.POST)

        if form.is_valid():
            formulario = form.save(commit=False)
            updated = Formulario_B.objects.filter(avaliacao=avaliacao).update(
                presidente_comite=formulario.presidente_comite,
                membro_comite=formulario.membro_comite,
                presidente_portifolio=formulario.presidente_portifolio,
                membro_portifolio=formulario.membro_portifolio,
                divulgacao_midea=formulario.divulgacao_midea,
                formulacao_politicas=formulario.formulacao_politicas,
                palestrante_disciplina_pos=formulario.palestrante_disciplina_pos,
                parcerias_embrapa=formulario.parcerias_embrapa,
                parcerias_intituicoes=formulario.parcerias_intituicoes,
                responsavel_laboratorio=formulario.responsavel_laboratorio,
                acoes_gerenciais_locais=formulario.acoes_gerenciais_locais,
                treinamentos_capacitacoes=formulario.treinamentos_capacitacoes,
                total_B=formulario.total_B,
            )
            if updated == 0:
                formulario.avaliacao = avaliacao
                formulario.save()
                formulario.total_B = formulario.calcular_media_B()
                formulario.save()
            else:
                formulario.total_B = formulario.calcular_media_B()
                updated = Formulario_B.objects.filter(avaliacao=avaliacao).update(total_B=formulario.calcular_media_B())

            return redirect('criarFormularioC', id)
        else:
            print(form.errors)
    else:
        if formulario_existente:
            form = FormularioBForm(instance=formulario_existente)
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

def visualizarFormularioB(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = get_object_or_404(Formulario_B, avaliacao=avaliacao)

    if request.method == 'POST':
        return redirect('visualizarFormularioC', id)

    form = FormularioBForm(instance=formulario_existente)

    # Desabilita todos os campos
    for field in form.fields.values():
        field.disabled = True

    return render(request, 'formulario/formB.html', {'form': form, 'tipo': 'B'})

#--FORMS C--
def criarFormularioC(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = Formulario_C.objects.filter(avaliacao=avaliacao).first()

    if request.method == 'POST':
        if formulario_existente:
            form = FormularioCForm(request.POST, instance=formulario_existente)
        else:
            form = FormularioCForm(request.POST)
        if form.is_valid():
            formulario = form.save(commit=False)
            updated = Formulario_C.objects.filter(avaliacao=avaliacao).update(
                atuacao_editor=formulario.atuacao_editor,
                clareza_coesao=formulario.clareza_coesao,
                gestor_contratos=formulario.gestor_contratos,
                lideranca_projeto=formulario.lideranca_projeto,
                responsavel_solucao_contribuicao=formulario.responsavel_solucao_contribuicao,
                responsavel_atividade=formulario.responsavel_atividade,
                participacao_qualificacao=formulario.participacao_qualificacao,
                coordenacao_propostas_projetos=formulario.coordenacao_propostas_projetos,
                membro_propostas_projetos=formulario.membro_propostas_projetos,
                valor_recursos_financeiros_comprovados= formulario.valor_recursos_financeiros_comprovados,
                instrutor_eventos_tecnicos=formulario.instrutor_eventos_tecnicos,
                apresentacao_tecnologias_embrapa=formulario.apresentacao_tecnologias_embrapa,
                responsvel_capacitacao_ead=formulario.responsvel_capacitacao_ead,
                revisor_capacitacao_ead=formulario.revisor_capacitacao_ead,
                membro_capacitacao_ead=formulario.membro_capacitacao_ead,
                coordenador_novas_capacitacoes=formulario.coordenador_novas_capacitacoes,
                artigo_a1=formulario.artigo_a1,
                artigo_a2_a3_a4=formulario.artigo_a2_a3_a4,
                artigo_b1_b2=formulario.artigo_b1_b2,
                artigo_b3_inferior=formulario.artigo_b3_inferior,
                producoes_tecnicas_embrapa=formulario.producoes_tecnicas_embrapa,
                elaboracao_cap_livros=formulario.elaboracao_cap_livros,
                organizacao_edicao_livros=formulario.organizacao_edicao_livros,
                artigos_resumos_eventos=formulario.artigos_resumos_eventos,
                total_C=formulario.total_C,
            )
            if updated == 0 :
                formulario.avaliacao = avaliacao
                formulario.save()
                formulario.total_C = formulario.calcular_media_C()
                formulario.save()
                messages.success(request,'Pesquisador avaliado com sucesso.')
            else:
                formulario.total_C = formulario.calcular_media_C()
                updated = Formulario_C.objects.filter(avaliacao=avaliacao).update(total_C=formulario.calcular_media_C())

            pendente = get_object_or_404(Pendentes, id=id)
            formulario_A = Formulario_A.objects.get(avaliacao=avaliacao)
            formulario_B = Formulario_B.objects.get(avaliacao=avaliacao)

            total_A = formulario_A.total_A or 0
            total_B = formulario_B.total_B or 0
            total_C = formulario.total_C or 0

            nota_final = total_A * 0.1 + total_B * 0.2 + total_C * 0.7
            pendente.nota = round(nota_final, 3)
            pendente.status = 'FIN'
            pendente.save()

            return redirect('avaliacao')
        else:
            print(form.errors)
    else:
        if formulario_existente:
            form = FormularioCForm(instance=formulario_existente)
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

def visualizarFormularioC(request, id):
    avaliacao = get_object_or_404(Pendentes, id=id)
    formulario_existente = get_object_or_404(Formulario_C, avaliacao=avaliacao)

    if request.method == 'POST':
        return redirect('avaliacao')

    form = FormularioCForm(instance=formulario_existente)

    # Desabilita todos os campos
    for field in form.fields.values():
        field.disabled = True

    return render(request, 'formulario/formC.html', {'form': form, 'tipo': 'C'})
# Create your views here.
