from symtable import Class

from django import forms
from .models import Formulario_A, Formulario_B, Formulario_C

class FormularioAForm(forms.ModelForm):
    visao_sistemica = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(5)],
        widget=forms.RadioSelect(),
        required=True
    )
    class Meta:
        model = Formulario_A
        fields = '__all__'
        widgets = {
            'visao_sistemica': forms.RadioSelect(attrs={'class': 'radios-inline'})
        }

class FormularioBForm(forms.ModelForm):
    class Meta:
        model = Formulario_B
        fields = '__all__'

class FormularioCForm(forms.ModelForm):
    class Meta:
        model = Formulario_C
        fields = '__all__'
