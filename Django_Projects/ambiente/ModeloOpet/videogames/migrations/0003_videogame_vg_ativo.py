# Generated by Django 3.0.5 on 2020-04-24 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videogames', '0002_auto_20200424_0936'),
    ]

    operations = [
        migrations.AddField(
            model_name='videogame',
            name='vg_ativo',
            field=models.BooleanField(default=False, verbose_name='Ainda e vendido:'),
        ),
    ]