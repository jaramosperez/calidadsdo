from django.db import models


class Funcionario(models.Model):
    """
    Clase para crear Funcionarios con el objectivo de asignarlo en:
    Documentos, características o ámbitos
     """
    nombres = models.CharField(
        max_length=255, verbose_name="Nombres"
        )
    primer_apellido = models.CharField(
        max_length=50, verbose_name="Primer apellido"
        )
    segundo_apellido = models.CharField(
        max_length=50, verbose_name="Segundo apellido", blank=True
        )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Fecha de creación'
        )
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Fecha de edición'
        )

    def __str__(self):
        return f"{self.nombres} {self.primer_apellido}"
