# Generated by Django 5.0.6 on 2024-06-18 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rifa', '0006_alter_rifa_date_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rifa',
            name='cover',
            field=models.FileField(upload_to='static/rifa/img'),
        ),
    ]
