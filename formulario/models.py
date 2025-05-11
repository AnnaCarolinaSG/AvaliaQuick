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

    avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE, null=False, default='')

    visao_sistemica = models.PositiveIntegerField(choices=SELECAO_CHOICES, null=False, blank=False)
    visao_analitica = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    foco_planejamento = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    orientacao_mudancas = models.PositiveIntegerField(choices=SELECAO_CHOICES,null=False, blank=False)
    relacoes_colaboracao = models.PositiveIntegerField(choices=SELECAO_CHOICES, null=False, blank=False)

    total_A = models.FloatField(null=True, blank=False, default=0)

    def calcular_media_A(self):
        total = (self.visao_sistemica +
                   self.visao_analitica +
                   self.foco_planejamento +
                   self.orientacao_mudancas +
                   self.relacoes_colaboracao
                   )/5
        total = round(total, 3)
        return total


class Formulario_B(models.Model):
    #Parte B1

    avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE, null=False, default='')

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

    total_B = models.FloatField(null=True, blank=False, default=0)

    def calcular_media_B(self):
        total_B1 = (self.presidente_comite * 4 +
                 self.membro_comite * 2 +
                 self.presidente_portifolio * 4 +
                 self.membro_portifolio * 2 +
                 self.divulgacao_midea * 2 +
                 self.formulacao_politicas * 2 +
                 self.palestrante_disciplina_pos * 1 +
                 self.parcerias_embrapa * 3 +
                 self.parcerias_intituicoes * 3 +
                 self.responsavel_laboratorio * 2 +
                 self.acoes_gerenciais_locais * 1
                )
        if total_B1 >= 13 :
            total = 4 * 0.75
        elif 12 >= total_B1 > 8:
            total = 3 * 0.75
        elif 8 >= total_B1 > 5 :
            total = 2 * 0.75
        elif 5 >= total_B1 > 0:
            total = 1 * 0.75
        else:
            total = 0

        total += self.treinamentos_capacitacoes * 0.25
        total = round(total, 3)

        return total

class Formulario_C(models.Model):

    avaliacao = models.ForeignKey(Pendentes, on_delete=models.CASCADE, null=False, default='')

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

    total_C = models.FloatField(null=True, blank=False, default=0)

    def calcular_media_C(self):
        total_C1 = (self.atuacao_editor + self.clareza_coesao) / 2 * 0.15
        total_C2 = self.gestor_contratos * 0.05
        total_C3 = 0
        total_C3_A = 0
        total_C3_B = 0
        total_C3_C = 0

        if self.lideranca_projeto:
            total_C3_A += 4
        if self.responsavel_solucao_contribuicao:
            total_C3_A += 3
        if self.responsavel_atividade:
            total_C3_A += 2
        if self.participacao_qualificacao:
            total_C3_A += 4
        if self.coordenacao_propostas_projetos:
            total_C3_A += 4
        if self.membro_propostas_projetos:
            total_C3_A += 2

        total_C3_A += self.valor_recursos_financeiros_comprovados

        if total_C3_A >= 13 :
            total_C3 += 4 * 0.5
        elif 12 >= total_C3_A > 8:
            total_C3 += 3 * 0.5
        elif 8 >= total_C3_A > 5 :
            total_C3 += 2 * 0.5
        elif 5 >= total_C3_A > 0:
            total_C3 += 1 * 0.5
        else:
            total_C3 += 0

        total_C3_B = (
            self.instrutor_eventos_tecnicos * 2 +
            self.apresentacao_tecnologias_embrapa +
            self.responsvel_capacitacao_ead * 2 +
            self.revisor_capacitacao_ead * 2 +
            self.membro_capacitacao_ead * 2 +
            self.coordenador_novas_capacitacoes * 2
        )
        if total_C3_B >= 6 :
            total_C3 += 4 * 0.25
        elif total_C3_B == 5 or total_C3_B == 4 :
            total_C3 += 3 * 0.25
        elif total_C3_B == 3 or total_C3_B == 2 :
            total_C3 += 2 * 0.25
        elif total_C3_B <= 1 :
            total_C3 += 1 * 0.25
        else:
            total_C3 += 0

        total_C3_C = (
            self.artigo_a1 * 4 +
            self.artigo_a2_a3_a4 * 3.5 +
            self.artigo_b1_b2 * 3 +
            self.artigo_b3_inferior * 2 +
            self.producoes_tecnicas_embrapa * 2 +
            self.elaboracao_cap_livros * 2 +
            self.organizacao_edicao_livros * 4 +
            self.artigos_resumos_eventos
        )
        if total_C3_C >= 7 :
            total_C3 += 4 * 0.25
        elif total_C3_C == 6 or total_C3_C == 5 :
            total_C3 += 3 * 0.25
        elif total_C3_C == 4 or total_C3_C == 3 :
            total_C3 += 2 * 0.25
        elif total_C3_C == 2 or total_C3_C == 1 :
            total_C3 += 1 * 0.25
        else:
            total_C3 += 0

        total = total_C1 + total_C2 + (total_C3 * 0.8)

        return total
