from django import forms

from .models import Detour

class DetourCreateForm(forms.ModelForm):
    class Meta:
        model = Detour
        fields = '__all__'
        
