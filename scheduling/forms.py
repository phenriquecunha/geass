from django import forms
from .models import Detour

class DetourCreateForm(forms.ModelForm):
    class Meta:
        model = Detour
        fields =  [
            'date',
            'installations',
            'calculation_basis',
            'justification',
            'cause',
            'technical',
        ]
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'Digite a data'
            }),
            'installations': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Quantas instalações foram feitas?'
            }),
            'calculation_basis': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'A base do calculo do desvio'
            }),
            'justification': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a justificava da equipe'
            }),
            'cause': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a causa principal'
            }),
            'technical': forms.SelectMultiple(attrs={
                'class': 'form-control select2',
                'placeholder': 'Técnicos envolvidos',
            }),
        }



        
