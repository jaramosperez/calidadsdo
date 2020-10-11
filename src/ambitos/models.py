from django.db import models
from ckeditor.fields import RichTextField
from funcionarios.models import Funcionario


class Ambito(models.Model):
    nombre = models.CharField(verbose_name='Nombre de Ámbito', max_length=100)
    funcionario = models.ForeignKey(
        Funcionario, verbose_name="Encargado", on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='ambito_funcionario'
        )
    subrogante = models.ForeignKey(
        Funcionario, verbose_name="Subrogante", on_delete=models.CASCADE,
        blank=True, null=True,
        related_name='ambito_subrogante'
        )
    descripcion = RichTextField(verbose_name='Descripción')
    sigla = models.CharField(
        verbose_name="Sigla", max_length=3, null=True, blank=True
        )
    numero = models.PositiveSmallIntegerField(verbose_name='Número de Ámbito')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
        )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de edición'
        )

    class Meta:
        verbose_name = 'Ámbito'
        verbose_name_plural = 'Ámbitos'
        ordering = ['numero']

    def __str__(self):
        return self.nombre
