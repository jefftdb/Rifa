# Generated by Django 5.0.6 on 2024-06-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifa', '0004_endereco_remove_rifa_pix_key_rifa_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='cover',
            field=models.FileField(upload_to='rifa/static/rifa/img'),
        ),
    ]