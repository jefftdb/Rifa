# Generated by Django 5.0.6 on 2024-06-19 16:34

import rifa.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifa', '0009_alter_rifa_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_common',
            name='endereco',
        ),
        migrations.AlterField(
            model_name='rifa',
            name='cover',
            field=models.ImageField(upload_to=rifa.models.Rifa.criaNome),
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
        migrations.DeleteModel(
            name='User_common',
        ),
    ]
