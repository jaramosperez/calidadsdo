from django import forms
from .models import Ambito


class AmbitoFormUpdate(forms.ModelForm):
    """
    Clase para el formulario de cambio de Encargado de ambito.
    """
    class Meta:
        model = Ambito
        fields = ['funcionario']
        widgets = {
            'funcionario': forms.Select(
                attrs={'class': 'ui small selection dropdown'}
                ),
        }
