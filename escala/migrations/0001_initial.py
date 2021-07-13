# Generated by Django 3.2.5 on 2021-07-13 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Posto de Trabolho',
                'verbose_name_plural': 'Postos de Trabalho',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255, verbose_name='Nome')),
                ('lastname', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('admission_date', models.DateField(verbose_name='Data de Admissão')),
                ('active', models.BooleanField(default=True, verbose_name='Ativo')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
                'unique_together': {('firstname', 'lastname', 'admission_date')},
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='País')),
                ('state', models.CharField(max_length=255, verbose_name='Estado')),
                ('city', models.CharField(max_length=255, verbose_name='Cidade')),
                ('district', models.CharField(max_length=255, verbose_name='Bairro')),
                ('street', models.CharField(max_length=255, verbose_name='Rua')),
                ('number', models.CharField(max_length=255, verbose_name='Número')),
                ('Place', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='escala.place')),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
