# Generated by Django 5.0.2 on 2024-02-22 15:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appnapoles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100)),
                ('cedula', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appnapoles.local')),
            ],
        ),
        migrations.DeleteModel(
            name='Elecciones',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
    ]
