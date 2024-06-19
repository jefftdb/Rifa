from typing import Any
from django.db import models
from datetime import datetime
import os

   
class Rifa(models.Model):
    id = models.AutoField(primary_key=True,auto_created=True)
    user_id = models.IntegerField(default=0)
    quantity = models.IntegerField()
    value = models.FloatField()
    title = models.CharField(max_length=35)
    description = models.CharField(max_length=255)
    award = models.CharField(max_length=255)
    date_start = models.DateTimeField(null = True)
    date_finish = models.DateTimeField()
    active = models.BooleanField(default=False)

    def criaNome(instance, filename):
        t = datetime.now()
        base, ext = os.path.splitext(filename)
        nome = f"{'Imagem'}-{t.strftime('%d-%m-%Y-%H%M%S%f')}{ext}"
        return os.path.join('rifa/static/rifa/img', nome)

    cover = models.ImageField(upload_to=criaNome)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # Chama o __init__ da classe base
        self.quantity = 101  # Definindo valor padrão para quantity

    

    def make_rifa(self):
        rifa = []
        numeros = Number.objects.filter(rifa_id = self)
        for numero in numeros:        
            if not numero.status:
                rifa.append(f'<p class="number number-reserved number-name">{numero}</p>')
            else:
                rifa.append(f'''
                <a style="text-decoration: none;" href="#" data-rifa-id="{self.id}" data-numero-id="{numero.id}" data-bs-toggle="modal" data-bs-target="#myModal">
                    <p class="number number-name">{numero}</p>
                </a>
            ''')
        return ''.join(rifa)
    
    def make_number(self):
        # Garantir que a instância de Rifa está salva antes de criar os números
        if not self.pk:
            raise ValueError("A instância de Rifa deve ser salva antes de criar números.")
        for numero in range(1, self.quantity):  
            number_instance = Number(rifa_id=self, number=numero)  # Usar a instância do objeto
            number_instance.save()

    def __str__(self):
        return self.title
        

class Number(models.Model):
    id = models.AutoField(primary_key=True)
    rifa_id= models.ForeignKey(Rifa, on_delete=models.CASCADE, null=True)
    number =  models.IntegerField()
    status = models.BooleanField(default=True)
    date = models.DateTimeField(null = True)

    def __str__(self):
        return str(self.number)       



