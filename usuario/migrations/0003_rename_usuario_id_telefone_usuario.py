# Generated by Django 5.0.6 on 2024-06-19 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0002_usuario_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telefone',
            old_name='usuario_id',
            new_name='usuario',
        ),
    ]
