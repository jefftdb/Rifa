from typing import Any
from django.db import models
from datetime import datetime
import os

class Endereco(models.Model):
    id = models.AutoField(primary_key = True)    
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.rua}, {self.numero}, {self.complemento}, {self.bairro}, {self.cidade}, {self.estado}, {self.cep}, {self.pais}'

    def formatar_endereco(self):
        partes = [
            f'Rua: {self.rua}',
            f'Número: {self.numero}',
            f'Complemento: {self.complemento}' if self.complemento else '',
            f'Bairro: {self.bairro}',
            f'Cidade: {self.cidade}',
            f'Estado: {self.estado}',
            f'CEP: {self.cep}',
            f'País: {self.pais}'
        ]
        return ', '.join(filter(None, partes))
    
    
class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=255)
    email=models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    
    def criaNome(instance, filename):
        t = datetime.now()
        base, ext = os.path.splitext(filename)
        nome = f"{'Foto'}-{t.strftime('%d-%m-%Y-%H%M%S%f')}{ext}"
        return os.path.join('usuario/static/usuario/img', nome)

    cover = models.ImageField(upload_to=criaNome,blank=True, null=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name='Endereco_Usuario')

class Telefone(models.Model):
    id = models.AutoField(primary_key = True)    
    pais = models.CharField(max_length=2)
    ddd = models.CharField(max_length =2)
    telefone = models.CharField(max_length=9)
    usuario_id = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='Telefone_Usuario')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.pais = '55'