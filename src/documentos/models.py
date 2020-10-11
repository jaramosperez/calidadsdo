from django.db import models
from caracteristicas.models import Caracteristica
from funcionarios.models import Funcionario


class TipoDocumento(models.Model):
    """
    Clase para crear un tipo de documento para despues asignara al documento.
    """
    nombre = models.CharField(
        max_length=255, verbose_name="Nombre del tipo de documento"
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
        )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de edición'
        )

    def __str__(self):
        return self.nombre


class Documento(models.Model):
    """Clase dedicada para diversos documentos.
        Protocolos,
        Nombramientos,
        Indicadores"""
    nombre = models.CharField(
        max_length=255, verbose_name="Nombre del documento"
        )
    archivo = models.FileField(
        verbose_name='Archivo', null=True, blank=True, upload_to='documentos'
        )
    caracteristica = models.ForeignKey(
        Caracteristica, verbose_name="Característica", on_delete=models.CASCADE
        )
    funcionario = models.ForeignKey(
        Funcionario, verbose_name="Encargado", on_delete=models.CASCADE
        )
    tipo_documento = models.ForeignKey(
        TipoDocumento, verbose_name="Tipo de documento",
        on_delete=models.CASCADE
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
        )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de edición'
        )
    version = models.FloatField(
        verbose_name='Versión del documento'
        )
    vigencia = models.DateField(verbose_name="Fecha de realización")

    def __str__(self):
        return self.nombre
