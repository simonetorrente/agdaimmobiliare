# Generated by Django 5.1.3 on 2024-12-01 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('immobiliare', '0018_alter_immobili_fasce_visite_alter_immobili_tipo_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TodoItem',
        ),
        migrations.AlterField(
            model_name='agenti',
            name='trattative_concluse',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='immobili',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='immobili/'),
        ),
    ]