# Generated by Django 5.1.3 on 2024-12-01 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobiliare', '0015_alter_immobili_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='immobili',
            name='fasce_visite',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='immobili',
            name='spese_amministrazione',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='immobili',
            name='spese_riscaldamento',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='immobili',
            name='video',
            field=models.ImageField(null=True, upload_to='immobili/'),
        ),
    ]
