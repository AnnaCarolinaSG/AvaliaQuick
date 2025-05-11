from symtable import Class

from django import forms
from .models import Formulario_A, Formulario_B, Formulario_C, QUANTIDADE_CHOICES, SELECAO_UNICA_CHOICES, SELECAO_CHOICES, PORCENTAGEM_CHOICES, VALOR_CONTRATO_CONVENIO_CHOICES, VALOR_RECURSOS_FINANCEIROS_COMPROVADOS_CHOICES

widget_config = forms.Select(attrs={'class': 'widget-quantidade', 'id': 'selecao_multipla'})
widget_checkbox_redondo = forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})


class FormularioAForm(forms.ModelForm):

    visao_sistemica = forms.ChoiceField(
        choices=SELECAO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radios-inline', 'id': 'selecao_multipla'})
    )
    visao_analitica = forms.ChoiceField(
        choices=SELECAO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radios-inline', 'id': 'selecao_multipla'})
    )
    foco_planejamento = forms.ChoiceField(
        choices=SELECAO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radios-inline', 'id': 'selecao_multipla'})
    )
    orientacao_mudancas = forms.ChoiceField(
        choices=SELECAO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radios-inline','id': 'selecao_multipla'})
    )
    relacoes_colaboracao = forms.ChoiceField(
        choices=SELECAO_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'radios-inline', 'id': 'selecao_multipla'})
    )

    class Meta:
        model = Formulario_A
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'avaliacao' in self.fields:
            del self.fields['avaliacao']
        if 'total_A' in self.fields:
            del self.fields['total_A']



class FormularioBForm(forms.ModelForm):

    presidente_comite = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    membro_comite = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    presidente_portifolio = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    membro_portifolio = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    divulgacao_midea = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    formulacao_politicas = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    palestrante_disciplina_pos = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    parcerias_embrapa = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    parcerias_intituicoes = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    responsavel_laboratorio = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    acoes_gerenciais_locais = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)

    treinamentos_capacitacoes = forms.ChoiceField(choices=SELECAO_UNICA_CHOICES,widget=forms.RadioSelect(attrs={'class': 'selecao-unica'}))

    class Meta:
        model = Formulario_B
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'avaliacao' in self.fields:
            del self.fields['avaliacao']
        if 'total_B' in self.fields:
            del self.fields['total_B']

class FormularioCForm(forms.ModelForm):
    # Parte C1
    atuacao_editor = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    clareza_coesao = forms.ChoiceField(choices=PORCENTAGEM_CHOICES, widget=widget_config)

    # Parte C2
    gestor_contratos = forms.TypedChoiceField(choices=VALOR_CONTRATO_CONVENIO_CHOICES,widget=forms.RadioSelect(attrs={'class': 'selecao-unica'}))

    # Parte C3 - ITEM A
    lideranca_projeto = forms.BooleanField(
        required=False,
        label="Liderança de Projetos",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )
    responsavel_solucao_contribuicao = forms.BooleanField(
        required=False,
        label="Responsável por Solução e/ou Contribuição para Inovação",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )
    responsavel_atividade = forms.BooleanField(
        required=False,
        label="Responsável por atividade",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )
    # =====
    participacao_qualificacao = forms.BooleanField(
        required=False,
        label="Participa do processo de qualificação dos ativos tecnológicos entregues como resultados em escalas TRLs 4,0 a 8,0 (comprovado pela CHTT)",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )
    coordenacao_propostas_projetos = forms.BooleanField(
        required=False,
        label="Coordena a articulação e elaboração de propostas de projetos, a serem submetidos em chamadas SEG, editais externos e contratos de parcerias (registradas no SEER e ou SEI)",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )
    membro_propostas_projetos = forms.BooleanField(
        required=False,
        label="Coordena a articulação e elaboração de propostas de projetos, a serem submetidos em chamadas SEG, editais externos e contratos de parcerias (registradas no SEER e ou SEI)",
        widget=forms.CheckboxInput(attrs={'class': 'checkbox-redondo'})
    )

    valor_recursos_financeiros_comprovados = forms.ChoiceField(
        choices=VALOR_RECURSOS_FINANCEIROS_COMPROVADOS_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'selecao-unica'})
    )

    #ITEM B

    instrutor_eventos_tecnicos = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    apresentacao_tecnologias_embrapa = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    responsvel_capacitacao_ead = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    revisor_capacitacao_ead = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    membro_capacitacao_ead = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    coordenador_novas_capacitacoes = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)

    #ITEM C

    artigo_a1 = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    artigo_a2_a3_a4 = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    artigo_b1_b2 = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    artigo_b3_inferior = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    producoes_tecnicas_embrapa = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    elaboracao_cap_livros = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    organizacao_edicao_livros = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)
    artigos_resumos_eventos = forms.ChoiceField(choices=QUANTIDADE_CHOICES, widget=widget_config)

    class Meta:
        model = Formulario_C
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'avaliacao' in self.fields:
            del self.fields['avaliacao']
        if 'total_C' in self.fields:
            del self.fields['total_C']
