from django.core.validators import integer_validator, MinValueValidator
from django.db import models

class Formulario_A(models.Model):
    visao_sistemica = models.IntegerField(choices=[(i, str(i)) for i in range(5)], null=False, blank=False)
    visao_analitica = models.IntegerField(null=False, blank=False)
    foco_planejamento = models.IntegerField(null=False, blank=False)
    orientacao_mudancas = models.IntegerField(null=False, blank=False)
    relacoes_colaboracao = models.IntegerField(null=False, blank=False)

class Formulario_B(models.Model):
    #Parte B1
    presidente_comite = models.IntegerField(null=False, blank=False)
    membro_comite = models.IntegerField(null=False, blank=False)
    presidente_portifolio = models.IntegerField(null=False, blank=False)
    membro_portifolio = models.IntegerField(null=False, blank=False)
    divulgacao_midea = models.IntegerField(null=False, blank=False)
    formulacao_politicas = models.IntegerField(null=False, blank=False)
    palestrante_disciplina_pos = models.IntegerField(null=False, blank=False)
    parcerias_embrapa = models.IntegerField(null=False, blank=False)
    parcerias_intituicoes = models.IntegerField(null=False, blank=False)
    responsavel_laboratorio = models.IntegerField(null=False, blank=False)
    acoes_gerenciais_locais = models.IntegerField(null=False, blank=False)
    #Parte B2
    treinamentos_capacitacoes = models.IntegerField(null=False, blank=False)

class Formulario_C(models.Model):
    #Parte C1
    atuacao_editor = models.IntegerField(null=False, blank=False)
    clareza_coesao = models.IntegerField(null=False, blank=False)

    #Parte C2
    gestor_contratos = models.BooleanField(max_length=10, null=False, blank=False)
    valor_gestor_contratos = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False, default=0.00)

    #Parte C3 - ITEM A
    #Participação em projetos SEG
    lideranca_projeto = models.IntegerField(null=False, blank=False)
    responsavel_solucao_contribuicao = models.IntegerField(null=False, blank=False)
    responsavel_atividade = models.IntegerField(null=False, blank=False)

    #Desenvolvimentos ativos tecnológicos
    participacao_qualificacao = models.BooleanField(default=False, null=False, blank=False)

    #Articulação e captação de recursos externos e internos
    coordenacao_propostas_projetos = models.BooleanField(default=False, null=False, blank=False)
    membro_propostas_projetos = models.BooleanField(default=False, null=False, blank=False)
    recursos_financeiros_comprovados = models.BooleanField(default=False, null=False, blank=False)
    valor_recursos_financeiros_comprovados = models.DecimalField(decimal_places=2, max_digits=10, null=False, blank=False, default=0.00)

    #ITEM B
    #Participação em ações de tranferência de conheicmento, inovação e tecnologia
    instrutor_eventos_tecnicos = models.IntegerField(null=False, blank=False)
    apresentacao_tecnologias_embrapa = models.IntegerField(null=False, blank=False)
    responsvel_capacitacao_ead = models.IntegerField(null=False, blank=False)
    revisor_capacitacao_ead = models.IntegerField(null=False, blank=False)
    membro_capacitacao_ead = models.IntegerField(null=False, blank=False)
    coordenador_novas_capacitacoes = models.IntegerField(null=False, blank=False)

    #ITEM C
    #Publicações Técnicas e Técnico Científicas
    artigo_a1 = models.IntegerField(null=False, blank=False)
    artigo_a2_a3_a4 = models.IntegerField(null=False, blank=False)
    artigo_b1_b2 = models.IntegerField(null=False, blank=False)
    artigo_b3_inferior = models.IntegerField(null=False, blank=False)
    producoes_tecnicas_embrapa = models.IntegerField(null=False, blank=False)
    elaboracao_cap_livros = models.IntegerField(null=False, blank=False)
    organizacao_edicao_livros = models.IntegerField(null=False, blank=False)
    artigos_resumos_eventos = models.IntegerField(null=False, blank=False)



