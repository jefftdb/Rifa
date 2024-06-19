from django import forms
from .models import Usuario,Telefone,Endereco

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'pais']
        widgets = {
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'cidade': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'cep': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'rua': "Rua:",
            'numero': "Número:",
            'complemento': "Complemento:",
            'bairro': "Bairro:",
            'cidade': "Cidade:",
            'estado': "Estado:",
            'cep': "CEP:",
            'pais': "País"
        }

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [                
            "first_name",
            "last_name",
            "cpf",
            "email",
            "password",
            "cover"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': "Nome:",
            'last_name': "Sobrenome:", 
            'password': "Senha:",
            'email': "E-mail:",            
            'cpf': "CPF:", 
            'cover': "Foto:"            
        }

class TelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = [               
            "ddd",
            "telefone"
        ]
        widgets = {
            
            'ddd': forms.TextInput(attrs={'class': 'form-control'}), 
            'telefone': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            
            'ddd': "DDD:", 
            'telefone': "Telefone:"            
        }

class UsuarioEnderecoForm(forms.ModelForm):
    rua = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    complemento = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    estado = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pais = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    # Adding fields from Telefone to the combined form
    ddd = forms.CharField(max_length=2, widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Usuario
        fields = [                
            "first_name",
            "last_name",
            "cpf",
            "email",
            "password",
            "cover"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control'})
        }
        labels = {
            'first_name': "Nome:",
            'last_name': "Sobrenome:", 
            'password': "Senha:",
            'email': "E-mail:",            
            'cpf': "CPF:", 
            'cover': "Foto:"            
        }

