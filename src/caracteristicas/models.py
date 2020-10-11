from django.db import models
from ambitos.models import Ambito
from funcionarios.models import Funcionario
from ckeditor.fields import RichTextField


class Caracteristica(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre de Caracteristica', max_length=100
        )
    funcionario = models.ForeignKey(
        Funcionario, verbose_name="Encargado", on_delete=models.CASCADE
        )
    ambito = models.ForeignKey(
        Ambito, verbose_name="Ámbito", on_delete=models.CASCADE
        )
    denominacion = RichTextField(
        verbose_name='Denomiación'
        )
    TIPO_CHOICES = (
        ('OBLIGATORIA', 'OBLIGATORIA'),
        ('NO OBLIGATORIA', 'NO OBLIGATORIA')
    )
    tipo = models.CharField(
        verbose_name="Tipo de caracteristica", choices=TIPO_CHOICES,
        max_length=15, null=True, blank=True
        )
    numero = models.FloatField(
        verbose_name='Número de Característica'
        )
    fecha_actualizacion = models.DateField(
        verbose_name='Fecha de última actualización', default='2018-11-13'
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
        )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de edición'
        )

    class Meta:
        verbose_name = 'Característica'
        verbose_name_plural = 'Características'
        ordering = ['ambito', 'numero']

    def __str__(self):
        return self.nombre
