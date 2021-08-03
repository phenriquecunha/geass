from django import forms
from django.db.models import fields

from .models import Detour

class DetourCreateForm(forms.ModelForm):
    class Meta:
        model = Detour
        fields =  [
            'date',
            'installations',
            'justification',
            'technical',
        ]

        
