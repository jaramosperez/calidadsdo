# Generated by Django 3.0.8 on 2020-10-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='version',
            field=models.FloatField(verbose_name='Versión del documento'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='vigencia',
            field=models.DateField(verbose_name='Fecha de realización'),
        ),
    ]