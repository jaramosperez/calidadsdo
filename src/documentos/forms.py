from django import forms
from .models import Documento


class DocumentoForm(forms.ModelForm):
    """
    Clase del formulario para subir documentos al sistema.
    """
    class Meta:
        model = Documento
        fields = [
            'nombre',
            'archivo',
            'caracteristica',
            'funcionario',
            'tipo_documento',
            'version',
            'vigencia'
            ]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'ui small input'}),
            'archivo': forms.FileInput(attrs={'class': 'inputfile small', 'type': 'file'}),
            'caracteristica': forms.Select(
                attrs={'class': 'ui small selection dropdown'}
                ),
            'funcionario': forms.Select(
                attrs={'class': 'ui small selection dropdown'}
                ),
            'tipo_documento': forms.Select(
                attrs={'class': 'ui small selection dropdown'}
                ),
            'version': forms.NumberInput(attrs={'class': 'ui small input'}),
            'vigencia': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui small calendar', 'id': 'calendario', 'type': 'date'}),
        }
