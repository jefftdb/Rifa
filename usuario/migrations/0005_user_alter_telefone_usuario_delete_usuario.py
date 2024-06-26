# Generated by Django 5.0.6 on 2024-06-20 13:28

import django.contrib.auth.models
import django.db.models.deletion
import usuario.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('usuario', '0004_alter_usuario_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(max_length=11)),
                ('cover', models.ImageField(upload_to=usuario.models.User.criaNome)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Endereco_Usuario', to='usuario.endereco')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='telefone',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Telefone_Usuario', to='usuario.user'),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
