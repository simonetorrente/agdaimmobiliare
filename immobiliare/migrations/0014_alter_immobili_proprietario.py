# Generated by Django 5.1.3 on 2024-12-01 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobiliare', '0013_alter_immobili_agente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immobili',
            name='proprietario',
            field=models.ForeignKey(db_column='proprietario', null=True, on_delete=django.db.models.deletion.CASCADE, to='immobiliare.proprietari'),
        ),
    ]
