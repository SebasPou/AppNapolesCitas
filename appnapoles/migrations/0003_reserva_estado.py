# Generated by Django 5.0.2 on 2024-02-22 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnapoles', '0002_local_reserva_delete_elecciones_delete_preguntas'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='estado',
            field=models.CharField(default='PENDIENTE', max_length=10),
        ),
    ]
