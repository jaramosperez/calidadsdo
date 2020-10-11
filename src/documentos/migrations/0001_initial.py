# Generated by Django 3.0.8 on 2020-10-11 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '__first__'),
        ('caracteristicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del tipo de documento')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del documento')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='documentos', verbose_name='Archivo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('version', models.PositiveIntegerField(verbose_name='Versión del documento')),
                ('vigencia', models.DateField(verbose_name='Fecha de vigencia')),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='caracteristicas.Caracteristica', verbose_name='Característica')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='funcionarios.Funcionario', verbose_name='Encargado')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.TipoDocumento', verbose_name='Tipo de documento')),
            ],
        ),
    ]
