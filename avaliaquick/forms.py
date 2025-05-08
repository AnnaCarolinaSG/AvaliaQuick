from symtable import Class

from django import forms
from django.db import models

from .models import Pesquisador, Arquivo

class FormularioPesquisador(forms.ModelForm):
    class Meta:
        model = Pesquisador
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Digite o nome do Pesquisador'
            }),
            'matricula': forms.NumberInput(attrs={
                'placeholder': 'Digite a matrícula do Pesquisador'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Digite o email do Pesquisador'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'ativo' in self.fields:
            del self.fields['ativo']

    def clean_matricula(self):
        matricula = self.cleaned_data['matricula']
        if Pesquisador.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Já existe um pesquisador com essa matrícula.")
        return matricula


class EnvioArquivosForm(forms.Form):
    pass
