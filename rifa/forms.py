from django import forms
from .models import Rifa


class RifaForms(forms.ModelForm):
    
    class Meta:
        model = Rifa
        fields = [               
            'title',
            'value',   
            'description',
            'award',
            'date_finish',
            'cover',
            
            ]

        widgets = {
            'title':      forms.TextInput(attrs={'class': 'form-control'}),
            'value':      forms.NumberInput(attrs={'class': 'form-control'}), 
            'description':forms.TextInput(attrs={'class': 'form-control'}),
            'award':      forms.TextInput(attrs={'class': 'form-control'}),            
            'date_finish':forms.DateInput(attrs={'class': 'form-control','type': 'date'}),            
                                
        }

        labels = {
            'title': 'Título:',
            'value': 'Valor:',    
            'description': 'Descrição:',
            'award': 'Prêmio:',
            'date_finish': 'Sorteio:',
            'cover': 'Imagem:'
        }