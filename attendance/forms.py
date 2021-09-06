from django import forms
from .models import Register, Client

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

class ControlQualityCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'name',
            'city',
            'district',
            'street',
            'latitude',
            'longitude',
            'service'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cidade'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'street': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rua'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Latitude'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Longitude'
            }),
            'service': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Plano'
            }),
        }



        
