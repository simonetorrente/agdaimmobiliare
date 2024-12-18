# Generated by Django 5.1.3 on 2024-11-30 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobiliare', '0002_alter_todoitem_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cf', models.CharField(max_length=16)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('citta', models.CharField(max_length=255)),
                ('via', models.CharField(max_length=255)),
                ('civico', models.CharField(max_length=30)),
                ('data_nascita', models.DateField()),
                ('data_assunzione', models.DateField()),
                ('stipendio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('trattative_concluse', models.IntegerField(verbose_name=11)),
            ],
        ),
    ]
