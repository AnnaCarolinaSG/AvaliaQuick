from symtable import Class

from django import forms
from .models import Formulario_A

class FormularioAForm(forms.ModelForm):
    class Meta:
        model = Formulario_A
        fields = '__all__'

class FormularioBForm(forms.ModelForm):
    class Meta:
        model = Formulario_A
        fields = '__all__'

class FormularioCForm(forms.ModelForm):
    class Meta:
        model = Formulario_A
        fields = '__all__'
