# Generated by Django 3.0.5 on 2020-04-24 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0003_videogame_vg_ativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videogame',
            name='vg_name',
            field=models.CharField(max_length=200, verbose_name='Nome do produto'),
        ),
    ]
