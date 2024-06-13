from django import forms
from .models import Rifa


class RifaForms(forms.ModelForm):
    
    class Meta:
        model = Rifa
        fields = [
                
            'quantity',
            'value',
            'pix_key',
            'title',
            'description',
            'award',
            'date_start',
            'date_finish',
            
            ]

        widgets = {
            'quantity':   forms.NumberInput(attrs={'class': 'form-control'}),
            'value':      forms.NumberInput(attrs={'class': 'form-control'}),
            'pix_key':    forms.TextInput(attrs={'class': 'form-control'}),
            'title':      forms.TextInput(attrs={'class': 'form-control'}),
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'award':      forms.TextInput(attrs={'class': 'form-control'}),
            'date_start': forms.DateInput(attrs={'class': 'form-control'}),
            'date_finish':forms.DateInput(attrs={'class': 'form-control'}),
            
        }