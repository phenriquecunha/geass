from django import forms
from .models import Register, Quiz

class RegisterCreateForm(forms.ModelForm):
    class Meta:
        model = Register
        fields =  [
            'protocol',
            'type_of_request',
            'sent_from',
            'sent_to',
        ]
        widgets = {
            'protocol': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Protocolo de atendimento'
            }),
            'type_of_request': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Tipo de solicitação'
            }),
            'sent_from': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Encaminhado de'
            }),
            'sent_to': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Encaminhada para'
            }),
        }

class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = [
            'client',
            'note',
        ]
        widgets = {
            'client': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Cliente'
            }),
            'note': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observação'
            }),
        }



        
