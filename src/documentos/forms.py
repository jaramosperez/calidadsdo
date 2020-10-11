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
            'nombre': forms.TextInput(attrs={'class': 'ui input'}),
            'archivo': forms.FileInput(attrs={'class': 'inputfile', 'type': 'file'}),
            'caracteristica': forms.Select(
                attrs={'class': 'ui selection dropdown'}
                ),
            'funcionario': forms.Select(
                attrs={'class': 'ui selection dropdown'}
                ),
            'tipo_documento': forms.Select(
                attrs={'class': 'ui selection dropdown'}
                ),
            'version': forms.NumberInput(attrs={'class': 'ui input'}),
            'vigencia': forms.DateInput(format=('%d/%m/%Y'), attrs={'class': 'ui calendar', 'id': 'calendario', 'type': 'date'}),
        }
