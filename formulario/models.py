from django.core.validators import integer_validator, MinValueValidator
from django.db import models

from avaliaquick.models import Pendentes

SELECAO_CHOICES = [(i, str(i)) for i in range(5)]
QUANTIDADE_CHOICES = [(i, str(i)) for i in range(5)]
SELECAO_UNICA_CHOICES = [
    (4, "Duas ou mais capacitações e ou treinamentos realizados pelo pesquisador"),
    (3, "Uma capacitação e ou treinamento realizada pelo pesquisador"),
    (0, "Capacitação não realizada"),
]
PORCENTAGEM_CHOICES = [
    (4, "100%" ),
    (3, "Acima de 60%"),
    (2, "Entre 40% e 59%"),
    (1, "Abaixo de 40%"),
    (0, "Nenhum"),
]
VALOR_CONTRATO_CONVENIO_CHOICES = [
    (4, "Acima de R$ 200 mil"),
    (3, "Entre R$ 80 e R$ 200 mil"),
    (2, "Até R$ 80 mil"),
    (1, "Sem ônus"),
    (0, "Sem contrato"),
]
VALOR_RECURSOS_FINANCEIROS_COMPROVADOS_CHOICES = [
    (4, "Acima de R$ 51 mil"),
    (3, "Entre R$ 21 mil e R$ 50 mil"),
    (2, "Entre R$ 11 mil e R$ 20 mil "),
    (1, "Até R$ 10 mil"),
    (0, "Sem captação"),
]

class Formulario_A(models.Model):
    #avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE, null=True)
    visao_sistemica = models.PositiveIntegerField(choices=SELECAO_CHOICES, null=False, blank=False)
    visao_analitica = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    foco_planejamento = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    orientacao_mudancas = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    relacoes_colaboracao = models.PositiveIntegerField(choices=SELECAO_CHOICES, null=False, blank=False)

    def __str__(self):
        return f"Formulário #{self.id}"



class Formulario_B(models.Model):
    #Parte B1
    #avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE, null=True)

    presidente_comite = models.PositiveIntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    membro_comite = models.PositiveIntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    presidente_portifolio = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    membro_portifolio = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    divulgacao_midea = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    formulacao_politicas = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    palestrante_disciplina_pos = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    parcerias_embrapa = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    parcerias_intituicoes = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    responsavel_laboratorio = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    acoes_gerenciais_locais = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)

    #Parte B2
    treinamentos_capacitacoes = models.IntegerField(choices=SELECAO_UNICA_CHOICES, null=False, blank=False)

class Formulario_C(models.Model):

    #avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE)
    #Parte C1
    atuacao_editor = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    clareza_coesao = models.IntegerField(choices=PORCENTAGEM_CHOICES, null=False, blank=False)

    #Parte C2
    gestor_contratos = models.IntegerField(choices=VALOR_CONTRATO_CONVENIO_CHOICES, null=False, blank=False)

    #Parte C3 - ITEM A
    #Participação em projetos SEG
    lideranca_projeto = models.BooleanField(default=False, null=False, blank=False)
    responsavel_solucao_contribuicao = models.BooleanField(default=False, null=False, blank=False)
    responsavel_atividade = models.BooleanField(default=False, null=False, blank=False)

    #Desenvolvimentos ativos tecnológicos
    participacao_qualificacao = models.BooleanField(default=False, null=False, blank=False)

    #Articulação e captação de recursos externos e internos
    coordenacao_propostas_projetos = models.BooleanField(default=False, null=False, blank=False)
    membro_propostas_projetos = models.BooleanField(default=False, null=False, blank=False)
    valor_recursos_financeiros_comprovados = models.IntegerField(choices=VALOR_RECURSOS_FINANCEIROS_COMPROVADOS_CHOICES, null=False, blank=False, default=0.00)

    #ITEM B
    #Participação em ações de tranferência de conheicmento, inovação e tecnologia
    instrutor_eventos_tecnicos = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    apresentacao_tecnologias_embrapa = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    responsvel_capacitacao_ead = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    revisor_capacitacao_ead = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    membro_capacitacao_ead = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    coordenador_novas_capacitacoes = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)

    #ITEM C
    #Publicações Técnicas e Técnico Científicas
    artigo_a1 = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    artigo_a2_a3_a4 = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    artigo_b1_b2 = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    artigo_b3_inferior = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    producoes_tecnicas_embrapa = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    elaboracao_cap_livros = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    organizacao_edicao_livros = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)
    artigos_resumos_eventos = models.IntegerField(choices=QUANTIDADE_CHOICES, null=False, blank=False)



